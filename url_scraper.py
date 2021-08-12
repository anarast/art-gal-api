import requests
import random
import json

from bs4 import BeautifulSoup as bs

NUM_IMAGES = 6

with open('./genres.json') as genres:
  genres = json.load(genres)["genres"]
  
genre_index = random.randint(0, len(genres))

def scrape():
  url = f"https://www.shutterstock.com/search/{genres[genre_index]}?image_type=photo&page=2"
  print(url)
  r = requests.get(url, headers={"User-Agent": "Chrome/51.0.2704.64"})
  soup = bs(r.content, 'html.parser')
  img_elements = soup.find('div', {'data-automation': 'mosaic-grid'}).find_all('img')
  image_urls = []

  start_index = random.randint(0, 10)

  for index, image in zip(range(start_index, start_index + NUM_IMAGES), img_elements):
    print(index)
    image_urls.append(img_elements[index]['src'])
  
  return image_urls

  