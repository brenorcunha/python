# Project: Model Evaluation & Validation
This well-known project aims to obtain standards on old data of real estate in Boston, according to the user's preferences and some pre-established parameters.
## Predicting Boston Housing Prices
In this project, you will evaluate the performance and estimation power of a model that has been trained and tested on data collected from real estate in the suburbs of Boston, Massachusetts. A model prepared for this data and seen as *well-adjusted* can then be used for certain estimates about a property – in particular, its monetary value. This model would be of great value to someone like a securities agent, who could make use of this information on a daily basis.

The dataset for this project originates from the UCI Machine Learning repository (https://archive.ics.uci.edu/ml/datasets/Housing). Boston real estate data was collected in 1978 and each of the 489 entries represents aggregate data on 14 attributes for real estate from various suburbs of Boston. For the purpose of this project, the following preprocessing steps were done for this dataset:
- 16 data observations have a ''MEDV'' value of 50.0. These notes likely contain **missing or censored values** and have been removed.
- The attributes ''RM'', ''LSTAT'', ''PTRATIO'', and ''MEDV'' are essential. The rest of the attributes are not very relevant.

As a reminder, we're using three attributes from the Boston real estate dataset: 'RM'', ''LSTAT'' and ''PTRATIO''. For each data observation (neighborhood):
- The ''RM'' is the average number of bedrooms among properties in the neighborhood.
- The ''LSTAT'' is the percentage of property owners in the neighborhood considered to be "lower class" (proletariat).
- The ''PTRATIO'' is the ratio of students to teachers in the middle and high schools in the neighborhood.
- The ''MEDV'' attribute has been **multiplicatively scaled** to account for 35 years of market inflation.
### Install

This project requires the following Python libraries installed:

- [Pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/python)
- [scikit-learn](http://scikit-learn.org/stable/)

Udacity recommends our students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 

### Code

The `housing.csv` dataset file is necessary to complete your work. While some code has already been implemented to get you started.

### Run

Just run in your favorite editor.

### Data

The dataset used in this project is included with the scikit-learn library ([`sklearn.datasets.load_boston`](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html#sklearn.datasets.load_boston)). You do not have to download it separately. You can find more information on this dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Housing) page.

#This project was made during the "Data Science Week" made in 2020 by MinerandoDados.