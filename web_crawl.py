from bs4 import BeautifulSoup
import os
import requests
import pandas as pd

url = "https://www.rottentomatoes.com/browse/tv_series_browse/?page=6"

for page in range(1, 10):
    response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed to load page {url}")
else:
    print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("div", attrs={'data-qa' : 'discovery-media-list-item'})
print(tags)

def get_name_of_shows(show_tags):

    show_name_list = []
    latest_ep_list = []
    critic_score_list = []
    audience_score_list = []
    show_cover_image_list = []
    synopsis_list = []
    network_list = []
    genre_list = []
    rating_list = []
    language_list = []
    release_date_list = []

    for show in show_tags:
        try:
            show_name_list.append(show.find("span", attrs={'data-qa' : 'discovery-media-list-item-title'}).text.strip())
            latest_ep_list.append(show.find("span", attrs={'data-qa' : 'discovery-media-list-item-start-date'}).text[29:].strip())
            critic_score_list.append(show.find("rt-text", attrs={'slot' : 'criticsScore'}).text.strip())
            audience_score_list.append(show.find("rt-text", attrs={'slot' : 'audienceScore'}).text.strip())
            show_cover_image_list.append(show.find("rt-img", {"slot" : "image"}.__getattribute__("src")))

            
            synopsis_list.append(show.find)
        except:
            show_name_list.append("Missing")
            latest_ep_list.append("Missing")
            critic_score_list.append("Missing")
            audience_score_list.append("Missing")
            show_cover_image_list.append("Missing")

    return show_name_list, latest_ep_list, critic_score_list, audience_score_list, show_cover_image_list,  len(show_name_list), len(latest_ep_list)

name_of_movies = get_name_of_shows(tags)
print(name_of_movies)
print("\n")
