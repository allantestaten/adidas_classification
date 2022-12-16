import pandas as pd
from sklearn.model_selection import train_test_split



#------------------GET DATA-------------------------------
def get_clean_data():
    '''this function will retrieve and clean data '''
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

    return df

def split_data(df):
    '''this function will split the data '''
    # split data/ train, validate, test 
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123) 

    return train, validate, test

#------------------PREPARE DATA-------------------------------

def dataframe_prep(train,validate,test):
    '''this function will prepare the dependent variable for modeling '''
    # creating target variables in train, validate and test datasets
    y_train = train['operating_margin']
    y_validate = validate['operating_margin']
    y_test = test['operating_margin']

    # changing y train, validate and test into a dataframe to append the new column with predicted values 
    y_train = pd.DataFrame(y_train)
    y_validate= pd.DataFrame(y_validate)
    y_test= pd.DataFrame(y_test)    

    #preparing dataframes for modeling 
    X_train = train.drop(columns=['retailer','region','state','city','product','operating_margin','sales_method'])
    X_validate = validate.drop(columns=['retailer','region','state','city','product','operating_margin','sales_method'])
    X_test = test.drop(columns=['retailer','region','state','city','product','operating_margin','sales_method'])

    return X_train, X_validate, X_test, y_train, y_validate, y_test

def region_data_frames(train):
    '''this function will create dataframes'''
    # create dataframes of regions with their operating margin 
    n_east = train[train.region == 'Northeast'].operating_margin
    midwest = train[train.region == 'Midwest'].operating_margin
    south = train[train.region == 'South'].operating_margin
    west = train[train.region == 'West'].operating_margin
    s_east= train[train.region == 'Southeast'].operating_margin

    return n_east,midwest,south,west,s_east

def retailer_data_frames(train):
    '''this functin will create dataframes'''
    # create dataframes of retailers with their operating margin 
    sports_direct = train[train.retailer == 'Sports Direct'].operating_margin
    walmart = train[train.retailer == 'Walmart'].operating_margin
    foot_locker = train[train.retailer == 'Foot Locker'].operating_margin
    amazon = train[train.retailer == 'Amazon'].operating_margin
    west_gear= train[train.retailer == 'West Gear'].operating_margin
    kohls= train[train['retailer'] == "Kohl's"].operating_margin    

    return sports_direct,walmart,foot_locker,amazon,west_gear,kohls



