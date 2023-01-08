# Predicting Operating Margin for Retailers
 
# Project Description
Adidas United States Sales Team has asked me to provide a recommendation of how to grow sales in the United States market. 
 
# Project Goal
* Identify drivers of operating margin for retaileres 
* Develop and use machine learning model to accurately predict operating margin. 
* Deliver a report or presentation that can be understood by non-data scientists.
* Deliver a report that explains what steps were taken and why they were taken.

# Data Dictionary
| Feature | Definition |
|:--------|:-----------|
|Retailer| Specific store: Amazon, Foot Locker, Kohl's, Sports Direct, Walmart, West Gear|
|Region| Geographic Region in United States: Northeast, Midwest South, Southeast, West |
|Product| Products sold by retailer: men and women's footwear and apparel|
|Operating Margin| operating income/revenue|
|Sales Method | The method of sale: In Store, Online and Outlet |

# Executive Summary 
* Mean operating margin is 42%
* 3 Models were created, Best model performs 30% better than baseline model 
* drivers of target variable : region, product, retailer and sale method 
* Recommend shifting some inventory from walmart to better performing retailers

# Initial Thoughts
The retailer would be the most important driver of predicting operating margin 

# The Plan
* Acquire data from data.world at this specific url https://data.world/stellabigail/adidas-us-sales-datasets
 
* Prepare data
   * Deleted top row of excel sheet 
   * Dropped columns 
        * Invoice Date 
        * unnamed column
        * operating profit
        * retailer id 
        * total sales 
        * price per unit 
    * Performed get dummies on region, retailer, product and sales method columns 
    * replaced spaces with underscores and made all words lower case

* Explore data in search of drivers of operating margin
   * Answer the following initial questions
       * What are the median and mean operating margin
       * What is the mean home price?
       * Does region have a relationship with operating margin?
       * Does product have a relationship with operating margin?
       * Does retailer have a relationship with operarting margin?
       * Is there a relationship between operating margin and sales method?
      
* Develop a Model to predict an accurate value of the operating margin
   * Use drivers supported by statistical test results to build predictive models
   * Evaluate all models on train 
   * Evaluate top models on validate data 
   * Select the best model based on lowest Root Mean Squared Error
   * Evaluate the best model on test data
 
* Draw conclusions
   * Operating margin has a relationship with region,retailer,sale method and product 
   * Women's apparel and men's street footwear appear to have the highest profit margins
   * Online Sales appears to have the highest operating margin 
   * The retailer with the highest operating margin is sports direct
   * Walmart appears to be underperforming relative to its peers
   * South region has the highest operating margin 
   * Operating Margin has few outliers considering the difference median and mean are approximately 1% 

* Recommendations
   * Provide Walmart less inventory and shift inventory to better performing retailer
   * The sales department reach out to the retailer sports direct to find out if they are opening more locations

* Next Steps
   * Research if data supports decreasing the number of stores in certain cities or states based on how much of their operating margin comes from online sales  
 


# Steps to Reproduce
1) Clone this repo
2) Acquire the data from data.world
3) Delete rows 1 - 4 of the excel document
4) Put the data in the file containing the cloned repo
4) Run notebook
 
