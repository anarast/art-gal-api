from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import image_data_fetcher

app = FastAPI()

origins = [
  "https://artgal.saratan.me",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/photos")
def get_photos():
  image_data = image_data_fetcher.fetch()
  return {"image_data": image_data}
