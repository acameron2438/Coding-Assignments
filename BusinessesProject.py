#-----Business DataCamp Project
#A practice assignment from DataCamp where I execute several data manipulations to practice my skills
#Downloaded the data from Datacamp and saved it to my computer

#-----Install packages
#run the following in the command line in the virtual environment:
#pip install pandas
#pip install matplotlib.pyplot
#pip install kaggle

#-----Import packages
import pandas as pd
import matplotlib.pyplot as plt

#-----Problem 1
# Load the business.csv file as a DataFrame called businesses
businesses = pd.read_csv('C:/Users/Andrew/WS/.venv/businesses.csv')
# Sort businesses from oldest businesses to youngest
sorted_businesses = businesses.sort_values('year_founded')
# Display the first few lines of sorted_businesses
print(sorted_businesses.head())

#-----Problem 2
# Load countries.csv to a DataFrame
countries = pd.read_csv('C:/Users/Andrew/WS/.venv/countries.csv')
# Merge sorted_businesses with countries
businesses_countries = sorted_businesses.merge(countries,on='country_code')
# Filter businesses_countries to include countries in North America only
north_america = businesses_countries[businesses_countries['continent']=='North America']
print(north_america.head())

#-----Problem 3
# Create continent, which lists only the continent and oldest year_founded
continent = businesses_countries[['continent','year_founded']]
# Merge continent with businesses_countries
merged_continent = continent.merge(businesses_countries,on=['continent','year_founded'])
print(merged_continent.head())
# Subset continent so that only the four columns of interest are included
subset_merged_continent = merged_continent[['continent','country','business','year_founded']]
print(subset_merged_continent)

#-----Problem 4
# Use .merge() to create a DataFrame, all_countries
all_countries = countries.merge(businesses,how='left',on='country_code')
print(all_countries.head())
# Filter to include only countries without oldest businesses
missing_countries = all_countries[all_countries['business'].isna()]
print(missing_countries.head(100))
# Create a series of the country names with missing oldest business data
missing_countries_series = missing_countries['country']
# Display the series
print(missing_countries_series)

#-----Problem 5
# Import new_businesses.csv
new_businesses = pd.read_csv('C:/Users/Andrew/WS/.venv/new_businesses.csv')
# Add the data in new_businesses to the existing businesses
all_businesses = pd.concat([businesses,new_businesses])
# Merge and filter to find countries with missing business data
new_all_countries = all_businesses.merge(countries,on='country_code',how='right')
new_missing_countries = new_all_countries[new_all_countries['business'].isna()]
print(new_missing_countries.head(5))
# Group by continent and create a "count_missing" column
count_missing = new_missing_countries.groupby('continent')['country_code'].count()
count_missing.columns = ['continent','count_missing']
print(count_missing.head(10))

#-----Problem 6
# Import categories.csv and merge to businesses
categories = pd.read_csv('C:/Users/Andrew/WS/.venv/categories.csv')
businesses_categories = businesses.merge(categories,on='category_code')
# Create a DataFrame which lists the number of oldest businesses in each category
count_business_cats = businesses_categories.groupby('category').agg({"business":"count"})
count_business_cats2 = businesses_categories.groupby('category')["business"].count()
# Rename column and display the first five rows of the DataFrame
count_business_cats.columns = ['count']
count_business_cats2.columns = ['count']
print(count_business_cats.head())
print(count_business_cats2.head())

#-----Problem 7
# Filter using .query() for CAT4 businesses founded before 1800; sort results
old_restaurants = businesses_categories.query('category_code=="CAT4" and year_founded<1800')
# Sort the DataFrame
old_restaurants = old_restaurants.sort_values('year_founded')
print(old_restaurants.head(30))

#-----Problem 8
# Merge all businesses, countries, and categories together
businesses_categories_countries = businesses.merge(countries,on='country_code') \
    .merge(categories,on='category_code')
# Sort businesses_categories_countries from oldest to most recent
businesses_categories_countries = businesses_categories_countries.sort_values('year_founded')
# Create the oldest by continent and category DataFrame
print('aaaaaaaaaaaaaaa')
oldest_by_continent_category = businesses_categories_countries[['continent','category','year_founded']].groupby(by=['continent','category'],as_index=True)['year_founded'].min()
print(oldest_by_continent_category.head(10))