import pandas as pd
import numpy as np

data = pd.read_csv("C:\\Users\\ENET29\\Downloads\\car_data.csv")
print(data.info)
print(data.isnull().sum())
print(data.describe())
print(data.head())
import datetime
date_time = datetime.datetime.now()
print(date_time)
data['age']=date_time.year - data ['Year']
print(data.head(40))
data.drop('Year',axis=1,inplace=True)
print(data.head(40))
import  seaborn as sns
print(sns.boxplot(data['Selling_Price']))
data=data[~(data['Selling_Price']>=35.0)&(data['Selling_Price']<=33.0)]
data.shape
data['Fuel_Type'].unique()
print(data['Selling_type'].unique())
data['Transmission'] = data['Transmission'].map({'Manual':0,'Automatic':1})
data['Selling_type'] = data['Selling_type'].map({'Individual':0,'Dealer':1,'Trustmark Dealer':2})
data['Fuel_Type'] = data['Fuel_Type'].map({'Petrol':0,'Diesel':1,'CNG':2,'LPG':3})
x = data.drop(['Car_Name','Selling_Price'],axis=1)
y=data['Selling_Price']
print(y)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=9)
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred1 = lr.predict(x_test)
print(lr.score(x_test,y_test))
lr=LinearRegression()
lr_final =lr.fit(x,y)
import joblib
model=joblib.load('car_price_predictior')
import pandas as pd
data_new=pd.DataFrame({
    'Present_Price':5.58,
    'Driven_kms':27000,
    'Fuel_Type':0,
    'Selling_type':0,
    'Transmission':0,
    'Owner':1,
    'age':8
},index=[0])
print(model.predict(data_new))