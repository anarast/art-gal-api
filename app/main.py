from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import url_scraper

app = FastAPI()

origins = ["https://artgal.saratan.me/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/photos")
def get_photos():
  urls = url_scraper.scrape()
  return {"urls": urls}
