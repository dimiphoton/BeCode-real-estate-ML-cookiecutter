# my proposition for a regression model

## building the features

### 1: geospatial data (work in progress)



When buying/renting, the location is often a prime parameter. The dataset only contains zip code. I could map it to the median household wealth. If I enhance the scrapping, I could get an address and try pg routing and find distance to nearest school, university, train station, technocentre.

###  2. Living Area and number of rooms



These features were used without prior transformation. Missing data policy was drop()

### 

### 3. Garden, Open Fire, Land Area...



Instead of dummy variable, I wanted to shrink the number of variables by creating counter variables names 'basic counter' and 'advanced counter' which are incremented by 1 if a condition is met (big garden, big land area)



### 4. State of the building



I mapped the state from -10 to 10 and I implemented a feature called 'malus' which consists in the product of state and living area values.

There are also possible transformations on the Price dataset (for example log-transformation) but I chose to keep the price untouched.



## Preprocessing



After splitting the data ,I fitted a standard scaler on the training set and applied it to the test set. 



## Running the regression algorithm





I chose the random forest algorithm because it is robust

[a relative link]: BeCode-real-estate-ML-cookiecutter/src/MLexperiments.ipynb	"notebook"

The metric is R² and its value is 0.51 when applied to the rent dataset and this is a porr value. I should compare with a one hot encoding feature engineering.



