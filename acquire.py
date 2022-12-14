import os
import requests
import pandas as pd
from env import get_db_url


#------------------ACQUIRE DATA-------------------------------
def get_split_data():
    '''this function will retrieve, clean and split the data'''
    # reading data into python from excel 
    df = pd.read_excel('Adidas_US_Sales_Datasets.xlsx')

    #replace spaces with underscore
    df.columns = [column.replace(' ','_').lower() for column in df]
    # dropping columns 
    df = df.drop(columns= ['unnamed:_0','invoice_date','operating_profit','price_per_unit','units_sold','retailer_id','total_sales'])
    # have to get dummys for categorical variables 

    # Uses one-hot encoding to create dummies of string columns for future modeling 
    dummy_df = pd.get_dummies(df[['region','retailer','product','sales_method']], dummy_na=False, drop_first=[False])
    df = pd.concat([df, dummy_df], axis=1)

    #replace spaces with underscore
    df.columns = [column.replace(' ','_').lower() for column in df]
    
    # split data/ train, validate, test 
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123) 
