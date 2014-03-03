"""Scrape data about academy award winners from wikipedia."""
import requests
import pprint
from bs4 import BeautifulSoup

URL = "http://en.wikipedia.org/wiki/{award_year}{number_suffix}_Academy_Awards"

def get_movies(url):
    """Return a list of lists of movies extracted from the url."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    movie_titles = []
    tables = soup.find_all("table", class_="wikitable")
    table = tables[0] 
    
    for tr in table.find_all("tr"):                 
        category = []
        for td in tr.find_all("td"):
            for title in td.text.split('\n'):
                if title:
                    category.append(title.replace(u'\u2013', ''))
            movie_titles.append(category)
    return movie_titles


def get_categories(url):
    """Return a list of categories extracted from the url."""
    categories = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    tables = soup.find_all('table', class_='wikitable') 
    table = tables[0]                                          
    for th in table.find_all('th'):                  
        categories.append(th.text)
    return categories

def get_url_for_year(year):
    """Return the url for the academy awards page on wikipedia for the given
    year."""
    #response = requests.get(URL.format(award_year=year, suffix='th'))
    #if 'does not have an article' in response.text:
    #    response = requests.get(URL.format(award_year=year, suffix='st'))
    #    if 'does not have an article' in response.text:
    #        response = requests.get(URL.format(award_year=year, suffix='nd'))
    #        if 'does not have an article' in response.text:
    #            response = requests.get(URL.format(award_year=year, suffix='rd'))
    suffixes = ['th', 'st', 'nd', 'rd']
    for suffix in suffixes:
        response = requests.get(URL.format(award_year=year, number_suffix=suffix))
        if 'does not have an article' not in response.text:
            break
    return response.url

def main():
    """Main entry point for script."""
    movie_data = {}
    for year in range(1, 86):
        print year
        url = get_url_for_year(year)
        categories = get_categories(url)
        movies = get_movies(url)
        category_data = {}
        for index, movie in enumerate(movies):
            current_category = categories[index]
            category_data[current_category] = movie
        movie_data[year] = category_data
    print movie_data[1]

if __name__ == '__main__':
    main()