# Book Review Rating Estimator: Project Overview 
* Created a tool that estimates book review rating (MAE ~ 0.19) to help writers understand response of readers when they write a book.
* Obtained over 10K book review rating from Kaggle source(mentioned below), later extracted books written only in english or english derived languages(>95%-of-data).
* Engineered features from list of authors to quantify the value readers put to main author/co-author(s) and number of authors.
* Engineered features from title of book to quantify the value readers put to length of title. 
* Optimized Linear, Lasso, and Random Forest Regressors using GridsearchCV to reach the best model. 
* Built a client facing API using flask 

## Code and Resources Used 
**Python Version:** 3.7  
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, flask, json, pickle  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```  
**Data Source:** https://www.kaggle.com/jealousleopard/goodreadsbooks  
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## Understanding Data
After obtaining data from Kaggle.com. With each book, we got the following:
*  Book ID
*  Book title
*  Authors
*  Average Rating
*  ISBN
*  ISBN13
*  Language Code
*  Number of pages
*  Rating Count
*  Text Review Count
*  Publication Date
*  Publisher

## Data Cleaning
After obtaining the data, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

*	Extracted books that have been written in English or English related language(more than 95% of raw-data), i.e., formed of english alphabets(a-z or A-Z), ignoring languages like Japanese, Chinese, etc. It was done in MS Excel itself, right after obtaining data.
*  Parsed list of author to get number of authors, main authors and 2 co-authors, if any, considering main author being first one in list and rest similarly in order.
*  Added a column for age of book from current year and publication year.
*  Dropped rows with zero average rating
*  Dropped rows with non-zero average rating and zero rating count(which was min)
*  Splitted title to get actual title and removing words after keyword: "by" representing auhtor's name in title itself.
*  Column for title length( number of words).

## EDA
I looked at the distributions of the data and the value counts for the various categorical variables. Below are a few highlights from the pivot tables. 

![alt text](https://github.com/miteshmadaan/BookReview/blob/documentation/language%20wise%20distribution%20of%20books.png)
![alt text](https://github.com/miteshmadaan/BookReview/blob/documentation/main%20author%20wise%20distribution%20of%20books.png)
![alt text](https://github.com/miteshmadaan/BookReview/blob/documentation/publisher%20wise%20distribution%20of%20books.png)
![alt text](https://github.com/miteshmadaan/BookReview/blob/documentation/corr%20matrix%20image.png)

## Model Building 

First, I transformed thhttps://github.com/miteshmadaan/BookReview/blob/documentation/language%20wise%20distribution%20of%20books.pnge categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.   

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.   

I tried three different models:
*	**Multiple Linear Regression** – Baseline for the model
*	**Lasso Regression** – Because of the sparse data from the many categorical variables, I thought a normalized regression like lasso would be effective.
*	**Random Forest** – Again, with the sparsity associated with the data, I thought that this would be a good fit. 

## Model performance
The Random Forest model far outperformed the other approaches on the test and validation sets. 
*	**Random Forest** : MAE = 0.19
*	**Linear Regression**: MAE = 0.19
*	**Lasso Regression**: MAE = 0.22

## Productionization 
In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The API endpoint takes in a request with a list of values from a book listing and returns an estimated rating. 



