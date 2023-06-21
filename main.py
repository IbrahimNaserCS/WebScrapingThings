from bs4 import BeautifulSoup
import requests
import re
f = open('moviesdatesratings.txt', 'w')
url = f"https://www.imdb.com/chart/top/"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")
movie_links = doc.find_all('a', href=lambda href: href and href.startswith('/title/'))
movie_dates = doc.find_all(class_='secondaryInfo')
movie_ratings = doc.find_all(class_='ratingColumn imdbRating')
ratings_old = []
for rating in movie_ratings:
    ratings_old.append(rating.text)
ratings = [rating.strip() for rating in ratings_old]
names = []
dates = []
for name in movie_links:
    names.append(name.text)
for date in movie_dates:
    dates.append(date.text)
names = [name for name in names if " \n" not in name]
f.write("TOP 250 RATED MOVIES IMDB\n")
for name, date, rating in zip(names, dates, ratings):
    f.write(f"{name}, {date} Rating: {rating} \n")

