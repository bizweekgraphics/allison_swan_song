from bs4 import BeautifulSoup
import urllib2
 
wiki = "http://en.wikipedia.org/wiki/Academy_Award_for_Best_Actor"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
tables = soup.findChildren("table", class_="wikitable")

# This will get the first (and only) table. Your page may have more.
my_table = tables[1]

# You can find children with multiple tags by passing a list of strings
rows = my_table.findChildren(['th', 'tr'])

for row in rows:
    cells = row.findChildren('td')
    for cell in cells:
        text = cell.string
        print text
        