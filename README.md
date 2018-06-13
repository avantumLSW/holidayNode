# holidayNode
A node to use the information from [holidayAPI.com](https://holidayapi.com/) within the SPSS Modeler natively.

## The Node
![The holiday node when opened](https://raw.githubusercontent.com/avantumLSW/holidayNode/master/Node.JPG "The holiday node when opened")

As you can see in the screenshot provided, there are not that many options required to use the node. The node itself is just some kind of wrapper function to communicate with the RESTAPI provided by holidayapi.
Therefore the options are mostly the same as they are on the website.
### Required Parameters
| Parameter  | Explanation |
| ---------- | ----------- |
| key        | your API key |
| country    | ISO 3166-2 format |
| year       | ISO 8601 format |
### Optional Parameters
| Parameter  | Explanation |
| ---------- | ----------- |
| month | 1 or 2 digit month (1-12) |
| day | 1 or 2 digit day (1-31 depending on the month) |
| previous | boolean, return previous holidays based on the date |
| upcoming | boolean, return upcoming holidays based on the date |
| public | boolean, return only public holidays |

## Installation
Here is a quick guide for an easy start:
1. Create an account at [holidayAPI.com](https://holidayapi.com/)
    * Keep in mind you need a payed account for commercial use.
2. Install the dependencies for your SPSS Modeler Installation of python
3. Install the holidayAPI.mpe from your SPSS Modeler
4. Enter your API-key, a year (e.g. 2017) and a country from the list of countries.
    * You could check 2017 for "DE" which should give you a list of german holidays to check whether something is hindering your device from communicating with the service.
5. You are free to go.

## Dependencies
For usage please assure to have the dependencies (json and requests) installed for the python version located within your Modeler installation.

## avantum
[![avantum](https://www.avantum.de/typo3conf/ext/website_avantum/Resources/Public/Media/layout/avantum-logo-2018-9.png "avantum consult AG")](https://www.avantum.de/)
This node is created by [avantum](https://www.avantum.de/).
