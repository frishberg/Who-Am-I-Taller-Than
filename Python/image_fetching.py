import os
from icrawler.builtin import GoogleImageCrawler
import time
import json

#param: name of celebrity
#this method downloads a picture of the desired celebrity to the image folder of the webpage
def fetch_image(celebrity_name) :
    filters = dict(type="face")
    google_Crawler = GoogleImageCrawler(storage = {'root_dir': 'Webpage/images'})
    google_Crawler.crawl(keyword = celebrity_name + " square", max_num = 1, filters=filters)
    try :
        os.rename('Webpage/images/000001.jpg', 'webpage/images/' + celebrity_name + '.jpg')
    except FileNotFoundError :
        os.rename('Webpage/images/000001.png', 'webpage/images/' + celebrity_name + '.jpg')

f = open("Webpage/data.json", "r")
data = json.load(f)
for entry in data :
    celeb_name = entry["name"]
    if (not os.path.exists("Webpage/images/" + celeb_name + ".jpg")) :
        fetch_image(celeb_name)
        print("Image fetched for " + celeb_name)
        time.sleep(1)
    else :
        print("Image already exists for " + celeb_name)