BeCode real estate data analytics
==============================

use web scrapping, data analysis and machine learning to build and then deploy a real estate estimator

## Setup



## Objective
The real estate company "ImmoEliza" contacted us to create a Machine Learning model in order to come up with accurate and precise price predictions on real estate sales in Belgium. In order to do that, we had to built a dataset that contains information about at least 10,000 properties all over Belgium.

## Part 1: data scrapping analysis
Instead of scrapping individual html pages, we found that a wittier way was to scrap the xml sitemap. xml language is the basis knowledge representation and permits organizations to make sense of data. In  this case, the [immoweb sitemap](https://www.immoweb.be/sitemap.xml) contains around 30 [xml files](https://assets.immoweb.be/sitemap/classifieds-000.xml) consisting in ordered dictionary very easy to scrap.

### Code & Data
The code uses Selenium and the Chrome webdriver to navigate to a series of pages on immoweb and collect the URLs for each property listing on those pages. Data was collected through web scrapping (BeautifulSoup method) of Immoweb's real-estate website in various intervals from 02/01/2023 to 06/01/2023. The data collected in this repository is open-sourced and lies inside property_urls.txt. 

### Visualizing results


## Contributors
Maïté Rolin

Dimitri Marchand

Augustin Carbonnelle




## Part 2: Data Cleaning and analysis







## Part 3: regression with scikit learn

In this part I cleaned the data, built features and fitted a scikit-learn model. More detail here: 

[notebook]: (https://github.com/dimiphoton/BeCode-real-estate-ML-cookiecutter/blob/part3/src/ML_regression.md)



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- to do: Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- md reports
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    |
    ├── src                <- Source code for use in this project.
    │   ├── step_01_scrap_data          <- Scripts to download data from xml sitemap in a csv file
    │   │
    │   ├── step_02_load_data       <- Scripts to turn raw data into well-indexed dataframe
    │   │                               New features shall be added here
    │   ├── step_03_clean_data      <- Scripts to clean data. Feature eng & cleaning
    |   |                               No option yet 
    │   │                              
    │   ├── step_04_feature_engineering       <- add some engineered features: here a counter of specs
    │   │                               
    │   ├── step_05_compute_models       <- Different cripts to generate trained models ad their accuracies.
    │   │  
    ├── template    <- contains the html file for the online price predictor
    |   |
    ├──  app.py: Flask script that use trained and serialized model
    |   |
    ├── myimage.dockerfile: docker image

    


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>