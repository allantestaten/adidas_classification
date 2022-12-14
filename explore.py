import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


def table():
    ''' This function will create a table of information '''
    #calculating median of property values 
    median = train.operating_margin.median() 

    #calculating mean of property values 
    mean = train.operating_margin.mean()

    # difference between mean and median 
    difference = mean - median

    #provides data for table
    df = [["Median", median], 
        ["Mean", mean],
        ["Difference", difference]]
        
    #define header names
    col_names = ["Metric", "Value"]
  
    #display table
    print(tabulate(df, headers=col_names))   

#---------------VISUALS------------

def barplot(dats,x,y,title):
    '''this function will create a barplot'''
    # barplot of region and operating margin 
    sns.barplot(data=train, x=x, y=y).set(title= "title")



#----------STATISTICAL TESTS--------------------
def anova_test(a,b,c,d,e):
    '''this function will provide the results of the ANOVA test'''
    # create dataframes of regions with their operating margin 
    n_east = train[train.region == 'Northeast'].operating_margin
    midwest = train[train.region == 'Midwest'].operating_margin
    south = train[train.region == 'South'].operating_margin
    west = train[train.region == 'West'].operating_margin
    s_east= train[train.region == 'Southeast'].operating_margin 

    # statistical test /#pearsonr test 
    results, p = stats.kruskal(a,b,c,d,e)

    # print results of statistical test 
    print(f'Kruska Result = {results:.4f}')
    print(f'p = {p}')

def anova_test_retailer(a,b,c,d,e,f):

    # create dataframes of retailers with their operating margin 
    sports_direct = train[train.retailer == 'Sports Direct'].operating_margin
    walmart = train[train.retailer == 'Walmart'].operating_margin
    foot_locker = train[train.retailer == 'Foot Locker'].operating_margin
    amazon = train[train.retailer == 'Amazon'].operating_margin
    west_gear= train[train.retailer == 'West Gear'].operating_margin
    kohls= train[train['retailer'] == "Kohl's"].operating_margin

    """this function will run ANOVA test"""
    # statistical test 
    results, p = stats.kruskal(a,b,c,d,e,f)
    # print results of statistical test 
    print(f'Kruska Result = {results:.4f}')
    print(f'p = {p}')

def anova_test_retailer(a,b,c):
    """this function will run ANOVA test"""   
    # statistical test 
    results, p = stats.kruskal(a,b,c)
    # print results of statistical test 
    print(f'Kruska Result = {results:.4f}')
    print(f'p = {p}')

