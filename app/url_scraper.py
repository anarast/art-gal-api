import requests
import random
import json

from bs4 import BeautifulSoup as bs

NUM_IMAGES = 6

with open('./genres.json') as genres:
  genres = json.load(genres)["genres"]
  
def scrape():
  genre_index = random.randint(0, len(genres))
  print(genre_index)
  print(genres[genre_index])
  url = f"https://www.shutterstock.com/search/{genres[genre_index]}?image_type=photo"
  print(url)
  try:
    r = requests.get(url, headers={"User-Agent": "Chrome/51.0.2704.64"})
  except Exception as e:
    print("Error occurred making request.")
    print(e)
    return []
  
  soup = bs(r.content, 'html.parser')
  img_elements = soup.find('div', {'data-automation': 'mosaic-grid'}).find_all('img')
  image_urls = []

  start_index = random.randint(0, 10)

  for index, image in zip(range(start_index, start_index + NUM_IMAGES), img_elements):
    image_urls.append(img_elements[index]['src'])
  
  print(image_urls)
  
  return image_urls

  