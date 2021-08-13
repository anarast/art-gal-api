import requests
import random
import json

from bs4 import BeautifulSoup as bs

NUM_IMAGES = 6
  
def scrape():
  with open('./genres.json') as genres:
    genres = json.load(genres)["genres"]
    
  genre_index = random.randint(0, len(genres) - 1)
  print(genre_index)
  print(genres[genre_index])
  
  headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
  }
  url = f"https://www.shutterstock.com/search/{genres[genre_index]}?image_type=photo"
  print(url)
  image_urls = []
  
  try:
    r = requests.get(url, headers=headers, timeout=10)
    
    if r.status_code == 200:
      soup = bs(r.content, 'html.parser')
      img_elements = soup.find('div', {'data-automation': 'mosaic-grid'}).find_all('img')


      start_index = random.randint(0, 10)

      for index, image in zip(range(start_index, start_index + NUM_IMAGES), img_elements):
        image_urls.append(img_elements[index]['src'])
    
      print(image_urls)
      
  except Exception as e:
    print("Error occurred making request." + str(e))

  finally:
    return image_urls
    


  