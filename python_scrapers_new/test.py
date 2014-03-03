''' WHAT I WANNA DO
1) soup the page with all the top grossing films
2) grab the link for each titles
3) write those to a list
4) iterate through that list 
5) go to keyword page for each title
6) write keywords to a csv, add new column with movie name
7) do that for every movie 
8) download csv
'''

from bs4 import BeautifulSoup
import urllib
import urllib2
import requests
import pprint
import csv
import re


url = "http://www.imdb.com/search/title?at=0&sort=boxoffice_gross_us,desc&start=101&year=2013,2013"

url_list = []                                      

#why does this give me empty url_list?

def get_urls(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)                  									
	url_list = soup.select('.title a[href*="title"]')
print url_list

#but this gives me working url_list? 

page = urllib2.urlopen(url)
soup = BeautifulSoup(page)                  									
url_list = soup.select('.title a[href*="title"]')
print url_list