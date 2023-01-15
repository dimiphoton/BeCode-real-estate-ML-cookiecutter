from bs4 import BeautifulSoup
import json
import numpy as np
import os
import pandas as pd
import random
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import RLock
from threading import Thread
from time import perf_counter
import xmltodict

start_urlscollection = perf_counter()
print("Starting now to collect the urls...")

# Creating a list of all listings for houses and apartments for sale in Belgium  !! 130.000+ listings
main_url=['https://assets.immoweb.be/sitemap/classifieds-'+'{0:03}'.format(i)+'.xml' for i in range(2)]

def append_list(propertieslist,obj):
    i = 2
    while i < len(obj['urlset']['url']):
        if "house/for-sale" in obj['urlset']['url'][i]['loc'] or "apartment/for-sale" in obj['urlset']['url'][i]['loc']:
            propertieslist.append(obj['urlset']['url'][i]['loc'])
        i += 3

def get_list():
    propertieslist=[]
    for xml_url in main_url:
        r = requests.get(xml_url, allow_redirects=True)
        obj=xmltodict.parse(r.content)
        append_list(propertieslist,obj)
        print(xml_url+' has been scrapped')
    return list(dict.fromkeys(propertieslist))

# Saving the urls in a separate .txt file for future use and check
if __name__ == "__main__":
    propertieslist=get_list()
    with open('Property_urls.txt', 'w') as fp:
        for item in propertieslist:
        # write each item on a new line
            fp.write("%s\n" % item)

print("Collection of urls finished.")

print("Number of urls collected: " + str(len(propertieslist))) # Checking the amount of results returned - must be >10.000 as per requierement in the project

end_urlscollection  = perf_counter()
print("Urls collection process time: " + str(end_urlscollection  - start_urlscollection))

# Moving on to the scraping part
start_scraping = perf_counter()
print("Starting now to scrape the pages...")

# Creating a dictionnary to store the informations collected
data = list()

lock = RLock()

def collect_infos(url):

    with lock:

        #print(url) # To be removed once program is up and running

        # Getting all the property specific page content as a workable json format (with help from Beautifulsoup)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "lxml")               # "lxml" fast than "html.parser" - pip install lxml
        content = soup.find('div', class_="container-main-content")
        try:
            content_string = content.script.string
            content_span = re.search(' = ', content_string).span()[1]
            content_sliced = content_string[content_span:-10]
            info = json.loads(content_sliced)
            if info["transaction"]["sale"]["price"] is not None:
            # Collecting the different informations on the property
                immoweb_code = info["id"]
                locality = info["property"]["location"]["locality"]
                type = info["property"]["type"]
                subtype = info["property"]["subtype"]
                price = info["transaction"]["sale"]["price"]
                sale_type = info["transaction"]["subtype"]
                bedrooms = info["property"]["bedroomCount"]
                living_area = info["property"]["netHabitableSurface"]
                if info["property"]["kitchen"] is None:
                    kitchen = "None"
                else:
                    kitchen = "1" if info["property"]["kitchen"]["type"] == "HYPER_EQUIPPED" else "0"
                if info["transaction"]["sale"] is not None and info["transaction"]["sale"]["isFurnished"] == "true":
                    furnished = "1"
                else:
                    furnished = "None"
                open_fire = "None" if info["property"]["fireplaceExists"] is None else int(info["property"]["fireplaceExists"])
                terrace = "None" if info["property"]["hasTerrace"] is None else int(info["property"]["hasTerrace"])
                area_terrace = "None" if info["property"]["terraceSurface"] is None else info["property"]["terraceSurface"]
                garden = "None" if info["property"]["hasGarden"] is None else int(info["property"]["hasGarden"])
                area_garden = "None" if info["property"]["gardenSurface"] is None else info["property"]["gardenSurface"]
                land_surface = "None" if info["property"]["land"] is None else info["property"]["land"]["surface"]
                facades = "None" if info["property"]["building"] is None else info["property"]["building"]["facadeCount"]
                swimming_pool = "None" if info["property"]["hasSwimmingPool"] is None else int(info["property"]["hasSwimmingPool"])
                building_state = "None" if info["property"]["building"] is None else info["property"]["building"]["condition"] 

            # Adding the informations collected to the dictionnary
                infos = {
                    "Id": immoweb_code, "Locality": locality, "House or appartment?": type, "Subtype": subtype, 
                    "Price": price , "Type of sale": sale_type, "Number of rooms": bedrooms, "Living area": living_area, 
                    "Fully equipped kitchen": kitchen , "Furnished": furnished , "Open fire": open_fire, "Terrace": terrace, 
                    "Area of terrace": area_terrace, "Garden": garden, "Area of garden": area_garden , "Land surface": land_surface ,
                    "Number of facades": facades , "Swimming pool": swimming_pool, "State of building": building_state
                    }

                data.append(infos)

        except:
            print("One property removed from the dataset due to errors.\n")
            pass

# Creating a list of sublists for the propertieslist of the size of the CPU count on the computer to optimize their use
properties_array = np.array(random.sample(propertieslist, 15000))       # Limiting list to 15.000 entries randomly picked as list has >130.000 entries
properties_split = np.array_split(properties_array, os.cpu_count())
propertieslistofsublists = [list(subarray) for subarray in properties_split]

def collect_infos_sublist(sublist):
    for link in sublist:
        collect_infos(link)

# Using a thread to collect simultaneously the urls on all pages
threads = list()

for sublist in propertieslistofsublists:
    thread = Thread(target=collect_infos_sublist, args=(sublist,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Scraping of pages finished.")

print("Number of pages scraped: " + str(len(data)))

end_scraping = perf_counter()
print("Scraping process time: " + str(end_scraping - start_scraping))

# Copying the data collected into a .csv file
df = pd.DataFrame(data)
df.to_csv('Immoweb_data.csv', index=False, header=True)

print("Full program finished. Data can be found in Immoweb_data.csv file.")
