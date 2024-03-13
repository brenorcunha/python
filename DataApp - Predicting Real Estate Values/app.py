import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.ensemble import RandomForestRegressor

#Charging the dataset
@st.cache_resource
def get_data():
    return pd.read_csv("housing.csv")

def train_model():
    data = get_data()
    x = data.drop("MEDV",axis=1)
    y = data["MEDV"]
    rf_regressor = RandomForestRegressor(n_estimators=200, max_depth=7, max_features=3)
    rf_regressor.fit(x, y)
    return rf_regressor

#Creating a dataframe
data = get_data()

#Training the model
model = train_model()

#Title
st.title("Data App - Predicting Real Estate Values")

#Subtitle
st.markdown("This is a Data App used to display the Machine Learning solution to Boston's real estate value prediction problem.")

# Checking the dataset
st.subheader("Selecionando apenas um pequeno conjunto de atributos")

#Standard attributes to be shown
defaultcols = ["RM","PTRATIO","LSTAT","MEDV"]

#Defining Attributes from MultiSelect
cols = st.multiselect("Atributos", data.columns.tolist(), default=defaultcols)

#Viewing the Top 10 Dataframe Record
st.dataframe(data[cols].head(10))


st.subheader("Distribution of properties by price")

#Defining the range of values
range_values = st.slider("Range of values: ", float(data.MEDV.min()), 150., (10.0, 100.0))

#Filtering the data
data_ = data[data['MEDV'].between(left=range_values[0],right=range_values[1])]

#Ploting the distribution data
f = px.histogram(data_, x="MEDV", nbins=100, title="Distribution of prices")
f.update_xaxes(title="MEDV")
f.update_yaxes(title="Total Real Estate (Imóveis)")
st.plotly_chart(f)


st.sidebar.subheader("Define property attributes for prediction")

#Mapping user data for each attribute
crim = st.sidebar.number_input("Crime Rate", value=data.CRIM.mean())
indus = st.sidebar.number_input("Proportion of Business Acres", value=data.CRIM.mean())
chas = st.sidebar.selectbox("Does it border the river?",("Yes","Not"))

#Turning Input Data into Binary Value
chas = 1 if chas == "Yes" else 0

nox = st.sidebar.number_input("Nitric oxide concentration", value=data.NOX.mean())

rm = st.sidebar.number_input("Number of rooms", value=1)

ptratio = st.sidebar.number_input("Student-to-Teacher Ratio",value=data.PTRATIO.mean())

b = st.sidebar.number_input("Proportion of black people",value=data.B.mean())

lstat = st.sidebar.number_input("Low Status Percentage (Poor)",value=data.LSTAT.mean())
medv = st.sidebar.number_input("MEDV ",value=data.MEDV.mean())
age = st.sidebar.number_input("AGE ",value=data.AGE.mean())
zn = st.sidebar.number_input("ZN ",value=data.ZN.mean())
dis = st.sidebar.number_input("MEDV ",value=data.DIS.mean())
#Inserting a button in the screen
btn_predict = st.sidebar.button("Perform prediction")

#Check if button was clicked
if btn_predict:
    result = model.predict([[crim,indus,chas,nox,rm,ptratio,b,lstat, medv, b, age, zn, dis]])
    st.subheader("The expected value for the property is:")
    result = "US $ "+str(round(result[0]*10,2))
    st.write(result)
