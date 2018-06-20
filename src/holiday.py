import spss.pyspark.runtime
from spss.pyspark.exceptions import ASContextException

from pyspark.sql.types import *
from pyspark.sql import SQLContext
from datetime import datetime

import requests
import json

cxt = spss.pyspark.runtime.getContext() 
sc = SQLContext(cxt.getSparkContext())

url = "https://holidayapi.com/v1/holidays"

key ="%%item_key%%".strip()
year = "%%item_year%%".strip()
country = "%%item_country%%".strip()
public = "%%item_public%%".strip()
month = "%%item_month%%".strip()
day = "%%item_day%%".strip()
behaviour = "%%item_bodb%%".strip()

payload = {'country':country, 'year':year, 'key':key, 'public':public}

if month:
	payload['month'] = month
	if day:
		payload['day'] = day
		if not behaviour == "empty":
			payload[behaviour] = "TRUE"

print(payload)
print("")

dateField = StructField("Date", StringType(), nullable = False)
nameField = StructField("Name", StringType(), nullable = False)
publicField = StructField("PublicHoliday", StringType(), nullable = False)
_schema = StructType([dateField, nameField, publicField])

if  cxt.isComputeDataModelOnly():   
	cxt.setSparkOutputSchema(_schema)
else:
	myResponse = requests.get(url, payload, verify=True)
	data = list()
	#print (myResponse.status_code)

	# For successful API call, response code will be 200 (OK)
	if(myResponse.ok):
		# Loading the response data into a dict variable
		# json.loads takes in only binary or string variables so using content to fetch binary content
		# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
		jData = json.loads(myResponse.content)	
		print("")
		print("The response contains {0} properties".format(len(jData)))
		for key in jData:
			if key == "holidays":
				dict = jData[key]
				if type(dict) == type({}):
					for info in dict:
						#print(str(info) + " : " + str(type(dict[info])))
						if type(dict[info]) == type([]):
							line = dict[info][0]
							data.append((line['date'], line['name'], str(line['public'])))
				if type(dict) == type([]):
					print("dict is list.")
					print(dict)
					for line in dict:
						if type(line) == type({}):
								data.append((line['date'], line['name'], str(line['public'])))

	else:
		# If response code is not ok (200), print the resulting http error code with description
		data.append(("Statuscode",myResponse.status_code,"given"))
		print(myResponse.text)
	if len(data) == 0:
		data.append(("No","response","given"))
	_newDF = sc.createDataFrame(data, _schema)
	cxt.setSparkOutputData(_newDF)