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

def get_xml(i):
    """get xml file given a number between 0 and 29

    Args:
        i (int): xml id

    Returns:
        xml file
    """
    return 'https://assets.immoweb.be/sitemap/classifieds-'+'{0:03}'.format(i)+'.xml'

def append_list_from_xml(propertieslist,obj):
    """appends properties to sale to propertieslist, given a xml file

    Args:
        propertieslist (list): list of properties url to append
        obj (dic): dic from xml
    """
    i = 2
    while i < len(obj['urlset']['url']):
        if "house/for-sale" in obj['urlset']['url'][i]['loc'] or "apartment/for-sale" in obj['urlset']['url'][i]['loc']:
            propertieslist.append(obj['urlset']['url'][i]['loc'])
        i += 3

def get_list(xml_url):
    """ edits the list of properties url given a xml url

    Args:
        xml_url (string): url of an xml file

    Returns:
        list of 5700 urls
    """
    propertieslist=[]
    r = requests.get(xml_url, allow_redirects=True)
    obj=xmltodict.parse(r.content)
    append_list_from_xml(propertieslist,obj)
    print(xml_url+' has been scrapped')
    return list(dict.fromkeys(propertieslist))
    

def collect_infos(url,df):
    """makes a bs4 request on one url and append dataframe

    Args:
        url (str): single url of a property
        df (dataframe): dataframe 
    """

    #with lock:
    if True:

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



            df.loc[immoweb_code]=[locality, type, subtype, price , sale_type, bedrooms,living_area,
            kitchen ,furnished , open_fire,terrace,area_terrace,garden,area_garden ,land_surface,
            facades ,swimming_pool,building_state]

        except:
            print("One property removed from the dataset due to errors.\n")
            pass

