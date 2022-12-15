import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats


def table(train):
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

def barplot(data,x,y,title):
    '''this function will create a barplot'''
    # barplot of region and operating margin 
    sns.barplot(data=data, x=x, y=y).set(title= title)


#----------STATISTICAL TESTS--------------------
def anova_test(a,b,c,d,e):

    # statistical test /#pearsonr test 
    results, p = stats.kruskal(a,b,c,d,e)

    # print results of statistical test 
    print(f'Kruska Result = {results:.4f}')
    print(f'p = {p}')

def anova_test_six(a,b,c,d,e,f):
    """this function will run ANOVA test"""
    # statistical test 
    results, p = stats.kruskal(a,b,c,d,e,f)
    # print results of statistical test 
    print(f'Kruska Result = {results:.4f}')
    print(f'p = {p}')

def anova_test_sales(train):
    """this function will run ANOVA test"""   
    # create dataframes of sales-method with their operating margin 
    in_store = train[train.sales_method == 'In-store'].operating_margin
    online = train[train.sales_method == 'Online'].operating_margin
    outlet = train[train.sales_method == 'Outlet'].operating_margin
    # statistical test 
    results, p = stats.kruskal(in_store,online,outlet)
    # print results of statistical test 
    print(f'Kruska Result = {results:.4f}')
    print(f'p = {p}')

def anova_test_products(train):
    """this function will run ANOVA test"""
    # create dataframes of products with their operating margin 
    men_athletic_footwear = train[train['product'] == "Men's Athletic Footwear"].operating_margin
    men_apparel = train[train['product'] == "Men's Apparel"].operating_margin
    women_street_footwear = train[train['product'] == "Women's Street Footwear"].operating_margin
    women_athletic_footwear = train[train['product'] == "Women's Athletic Footwear"].operating_margin
    men_street_footwear= train[train['product'] == "Men's Street Footwear"].operating_margin
    women_apparel= train[train['product'] == "Women's Apparel"].operating_margin
    # statistical test 
    results, p = stats.kruskal(men_athletic_footwear,men_apparel,women_street_footwear,women_athletic_footwear,men_street_footwear,women_apparel)
    # print results of statistical test 
    print(f'Kruska Result = {results:.4f}')
    print(f'p = {p}')

