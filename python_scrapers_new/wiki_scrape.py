''' WHAT I WANNA DO
1) soup the page, grab all the years
2) make a dict for each year with 6 nomination categories
2) within each category, make a dict of the nominees + movie title + character name
3) mark true or false for a win 
4) spit out structured json like so:

	{ "year": 1930 
		"best actor":
			{"christian bale": 
				{
				"film": "American Hustle"
				"character": "Irving Rosenfeld"
				"win":false
				}
			"bob":
				{
				"film": "bobs party"
				"character": "jack roberts"
				"win":true
				}
			}
		"best director":
			{"martin scorcese": 
				{
				"film": "wolf of wall street"
				"win":false
			}
	}
'''

from bs4 import BeautifulSoup
import urllib
import urllib2
wiki = "http://en.wikipedia.org/wiki/86th_Academy_Awards"
header = {'User-Agent': 'Mozilla/5.0'} 			#Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
import requests
import pprint
import csv
import re


#go on this page, find the table classed "wikitable" and soup all the rows
#iterate over them all and soup the data
#print the text in the data

tables = soup.find_all("table", class_="wikitable")
table = tables[0] 
#print table									
for tr in table.find_all("tr"):					
    for td in tr.find_all("td"):
			print td.text










