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
import requests
import pprint
import csv
import re

# made URL a global variable so that i can use this bad boy again

url = "http://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor"

# STEP 1: okay first up: a function that will get me the years

def get_years(url):
    years = () 														#should i do this here because i want a dict?
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    table = soup.find_all('table', class_='wikitable') 										
        for years in tr.find_all('th')tag.has_key('scope'):                    
            if not isinstance(data, unicode):              
                years.append(data.text)                
    return years




 def get_keywords(url):
    keywords = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    tables = soup.find_all('table', class_='dataTable') #ok so there were two tables on the page, the one we want a BS amazon table so we had to be specific here
    table = tables[0]                                          # [0] gets the first element of the list "tables" 
    for tr in table.find_all('tr'):                     # beautifulsoup always returns a list when calling find_all
        for td in tr.find_all('td'):                    # even if there is only one element
            if not isinstance(td, unicode):             # "isinstance" just checks the type of the variable, wanted to make sure we dont get those blank table rows 
                keywords.append(td.text)                #here we appended the keywords to the empty list we created in line 45
    return keywords



