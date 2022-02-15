import requests
import random
import json

NUM_IMAGES = 6
  
def fetch():
  with open('./genres.json') as genres:
    genres = json.load(genres)["genres"]
    
  genre_index = random.randint(0, len(genres) - 1)
  print(genre_index)
  print(genres[genre_index])
  
  headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
  }
  url = f"https://www.shutterstock.com/studioapi/search?q={genres[genre_index]}"
  print(url)
  image_data = {}
  
  try:
    r = requests.get(url, headers=headers, timeout=10)
    
    if r.status_code == 200:
      data = json.loads(r.content)['data']
      start_index = random.randint(0, 10)
      count_index = 0;

      for index, image in zip(range(start_index, start_index + NUM_IMAGES), data):
        print(index)
        print(data[index])
        image_data[count_index] = {
          'url': data[index]['attributes']['preview_image_url'],
          'description': data[index]['attributes']['description']
        }
        count_index += 1
      print(image_data)
      
  except Exception as e:
    print("Error occurred making request." + str(e))

  finally:
    return image_data
    


  