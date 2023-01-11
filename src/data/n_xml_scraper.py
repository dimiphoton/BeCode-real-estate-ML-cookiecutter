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

import scraper_utils

#start_urlscollection = perf_counter()
#print("Starting now to collect the urls...")

# Creating a list of all listings for houses and apartments for sale in Belgium  !! 130.000+ listings






# Saving the urls in a separate .txt file for future use and check
#if __name__ == "__main__":
#    propertieslist=get_list()
#    with open('Property_urls.txt', 'w') as fp:
#        for item in propertieslist:
#        # write each item on a new line
#            fp.write("%s\n" % item)

#print("Collection of urls finished.")

#print("Number of urls collected: " + str(len(propertieslist))) # Checking the amount of results returned - must be >10.000 as per requierement in the project

#end_urlscollection  = perf_counter()
#print("Urls collection process time: " + str(end_urlscollection  - start_urlscollection))



# Creating a dataframe to store the informations collected
def collect_infos_sublist(sublist,df):
    for link in sublist:
        scraper_utils.collect_infos(link,df)

def run(n):
    columns_names=["Region","Province","District","Postcode","House or appartment?", "Subtype","Price", "Type of sale", "Number of rooms",
    "Living area","Fully equipped kitchen","Furnished", "Open fire", "Terrace","Area of terrace",
    "Garden", "Area of garden", "Land surface","Number of facades", "Swimming pool", "State of building","EPC score"]

    df = pd.DataFrame(columns=columns_names)
    df.index.names=["Id"]

    propertieslist=scraper_utils.get_list(scraper_utils.get_xml(n))

    properties_split = np.array_split(propertieslist, os.cpu_count())
    propertieslistofsublists = [list(subarray) for subarray in properties_split]
    lock = RLock()
    

    # Using a thread to collect simultaneously the urls on all pages
    threads = list()

    for sublist in propertieslistofsublists:
        thread = Thread(target=collect_infos_sublist, args=(sublist,df))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Scraping of pages finished.")


    #end_scraping = perf_counter()
    #print("Scraping process time: " + str(end_scraping - start_scraping))

# Copying the data collected into a .csv file
    df.to_csv('Immoweb_data'+'{0:03}'.format(n)+'.csv', index=True, header=True)

    print('Full program finished. Data can be found in Immoweb_data'+'{0:03}'.format(n)+'.csv file.')


if __name__ == '__main__':
    run(0)
