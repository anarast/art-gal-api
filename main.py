from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import url_scraper

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/photo")
def read_photo():
  urls = url_scraper.scrape()
  return {"urls": urls}
