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

## 

### Visualizing results
Typical vizualizations include price and area distribution, as well as basic geographic data, for example the mean price/m2 for each region. This can be achieved with the use of postgresql.

## Contributors
Maïté Rolin

Dimitri Marchand

Augustin Carbonnelle




## Part 2: Data Cleaning and analysis

### Step 1 : Data Cleaning

Data cleaning consists in:

1. remove duplicate
2. fix naming problems: no blank space
3. fix erroneous data
4. fix ex empty values

### Step 2 : Data Analysis



##### How many rows and columns?

##### What is the correlation between the variables and the price? (Why might that be?)

##### How are variables correlated to each other? (Why?)

##### Which variables have the greatest influence on the price?

##### Which variables have the least influence on the price?

##### How many qualitative and quantitative variables are there? How would you transform these values into numerical values?

##### What is the percentage of missing values per column?



### Step 3 : Data Interpretation



##### Plot the outliers

##### Which variables would you delete and why ?

##### Represent the number of properties according to their surface using a histogram.

##### In your opinion, which 5 variables are the most important and why?

##### What are the **most** expensive municipalities in Belgium? (Average price, median price, price per square meter)

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>