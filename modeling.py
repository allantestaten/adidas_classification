import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.tree import DecisionTreeRegressor
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


def baseline_model(y_train):
    '''this function will create a baseline model'''
    # Predict property_value_pred_mean (not used in project)
    operating_margin_pred_mean = y_train['operating_margin'].mean()
    y_train['operating_margin_pred_mean'] = operating_margin_pred_mean

    # RMSE of prop_value_pred_mean
    rmse_baseline_train = mean_squared_error(y_train.operating_margin, y_train.operating_margin_pred_mean)**(1/2)
    print("RMSE for Baseline Model using Mean\nTrain/In-Sample: ", round(rmse_baseline_train, 4))

    return rmse_baseline_train

def linear_reg_model_train(X_train,y_train,rmse_baseline_train):
    '''this function will create and provide the results of the linear regression model'''
    # create the model object
    lm2 = LinearRegression(normalize=True)
    
    # fit train data to model 
    lm2.fit(X_train, y_train.operating_margin)

    # predict train
    y_train['operating_margin_lm2'] = lm2.predict(X_train)

    # evaluate: rmse
    rmse_polynomial_reg_train = mean_squared_error(y_train.operating_margin, y_train.operating_margin_lm2)**(1/2)

    # print results of model
    print("RMSE for Linear Regression Model\nTraining/In-Sample: ", rmse_polynomial_reg_train)
    
    #Improvement compared to baseline 
    print("Percent Improvement Compared to Baseline: ",((rmse_baseline_train-rmse_polynomial_reg_train)/(rmse_baseline_train)* 100))

def tree_reg_model_train(X_train,y_train,rmse_baseline_train):
    '''this function will create a decision tree regressor model and print results'''

    # create a regressor object
    reg = DecisionTreeRegressor(random_state = 100) 

    # fit the regressor with X and Y data
    reg.fit(X_train, y_train.operating_margin)

    # predict train
    y_train['operating_margin_reg'] = reg.predict(X_train)

    # evaluate: rmse
    rmse_tree_reg_train = mean_squared_error(y_train.operating_margin, y_train.operating_margin_reg)**(1/2)

    # print results of model
    print("RMSE for Decion Tree Regressor Model\nTraining/In-Sample: ", rmse_tree_reg_train)
    
    #Improvement compared to baseline 
    print("Percent Improvement Compared to Baseline: ",((rmse_baseline_train-rmse_tree_reg_train)/(rmse_baseline_train)* 100))

def tweedie_regressor_train(X_train,y_train,rmse_baseline_train):
      # create the model object
    glm = TweedieRegressor(power=1, alpha=0)

    # fitting model to training data
    glm.fit(X_train, y_train.operating_margin)

    # computing predictions on x train dataset
    y_train['operating_margin_pred_glm'] = glm.predict(X_train)

    # evaluate: train rmse
    rmse_tweedie_train = mean_squared_error(y_train.operating_margin, y_train.operating_margin_pred_glm)**(1/2)
    
    #printing results of model 
    print("RMSE for Tweedie Regressor Model\nTraining/In-Sample: ", rmse_tweedie_train)

    #Improvement compared to baseline 
    print("Percent Improvement Compared to Baseline: ",((rmse_baseline_train-rmse_tweedie_train)/(rmse_baseline_train)* 100))

def tree_reg_model_validate(X_train,y_train,X_validate,y_validate,rmse_baseline_train):
    '''this function will create a tweedie regressor model and print results'''
    # create a regressor object
    reg = DecisionTreeRegressor(random_state = 100) 

    # fit the regressor with X and Y data
    reg.fit(X_train, y_train.operating_margin)
    
    # predict train
    y_validate['operating_margin_reg_validate'] = reg.predict(X_validate)

    # evaluate: rmse
    rmse_tree_reg_validate = mean_squared_error(y_validate.operating_margin, y_validate.operating_margin_reg_validate)**(1/2)

    # print results of model
    print("RMSE for Tweedie Regressor Model\nValidate/Out-of-Sample: ", rmse_tree_reg_validate)
    
    #Improvement compared to baseline 
    print("Percent Improvement Compared to Baseline: ",((rmse_baseline_train-rmse_tree_reg_validate)/(rmse_baseline_train)* 100))

def linear_reg_model_validate(X_train,y_train,X_validate,y_validate,rmse_baseline_train):
    '''this function will create a linear regression model and print results'''

    # create the model object
    lm2 = LinearRegression(normalize=True)

    # fit train data to model 
    lm2.fit(X_train, y_train.operating_margin)

    # predict train
    y_validate['operating_margin_lm2'] = lm2.predict(X_validate)

    # evaluate: rmse
    rmse_linear_validate_reg_validate = mean_squared_error(y_validate.operating_margin, y_validate.operating_margin_lm2)**(1/2)

    # print results of model
    print("RMSE for Linear Regression Model\nValidate/Out-of-Sample: ", rmse_linear_validate_reg_validate)
    
    #Improvement compared to baseline 
    print("Percent Improvement Compared to Baseline: ",((rmse_baseline_train-rmse_linear_validate_reg_validate)/(rmse_baseline_train)* 100))

def tweedie_model_validate(X_train,y_train,X_validate,y_validate,rmse_baseline_train):
    '''this function will create a tweedie regressor model and print results'''
    # create a regressor object
    glm = TweedieRegressor(power=1, alpha=0)

    # fit the regressor with X and Y data
    glm.fit(X_train, y_train.operating_margin)
    
    # predict train
    y_validate['operating_margin_pred_glm_validate'] = glm.predict(X_validate)

    # evaluate: rmse
    rmse_tweedie_validate = mean_squared_error(y_validate.operating_margin, y_validate.operating_margin_pred_glm_validate)**(1/2)

    # print results of model
    print("RMSE for Tweedie Regressor Model\nValidate/Out-of-Sample: ", rmse_tweedie_validate)
    
    #Improvement compared to baseline 
    print("Percent Improvement Compared to Baseline: ",((rmse_baseline_train-rmse_tweedie_validate)/(rmse_baseline_train)* 100))

def test_model(X_train,y_train,X_test,y_test,rmse_baseline_train):
    '''this function will create the test model and results'''
    # create a regressor object
    reg = DecisionTreeRegressor(random_state = 100) 

    # fit the regressor with X and Y data
    reg.fit(X_train, y_train.operating_margin)

    # predict train
    y_test['operating_margin_reg'] = reg.predict(X_test)

    # evaluate: rmse
    rmse_tree_reg_test = mean_squared_error(y_test.operating_margin, y_test.operating_margin_reg)**(1/2)

    # print results of model
    print("RMSE for Decion Tree Regressor Model\nTest/Out-of-Sample: ", rmse_tree_reg_test)
    
    #Improvement compared to baseline 
    print("Percent Improvement Compared to Baseline: ",((rmse_baseline_train-rmse_tree_reg_test)/(rmse_baseline_train)* 100))