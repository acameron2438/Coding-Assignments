#-----Netflix DataCamp Project
#A practice assignment from DataCamp where I execute several data manipulations to practice my skills

#-----Install packages
#run the following in the command line:
#pip install pandas
#pip install matplotlib.pyplot
#pip install kaggle

#-----Import packages
import pandas as pd
import matplotlib.pyplot as plt
import kaggle as kg

#-------Save the Kaggle dataset to the computer
#URL: https://www.kaggle.com/datasets/shivamb/netflix-shows
#Kaggle documentation: https://technowhisp.com/kaggle-api-python-documentation/
kg.api.authenticate()
kg.api.dataset_download_files(dataset='shivamb/netflix-shows',path='C:/Users/Andrew/WS/.venv/', unzip=True,)

#-----Problem 1: Create a dictionary
#Create the years and durations lists
#Problem assignment provides the following lists of years and durations to use (doesn't come from csv file)
years=[2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations=[103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

#Create the dictionary with the two lists
movie_dict={'years':years,'durations':durations}
#Print the dictionary
print(movie_dict)

#-----Problem 2: Create a dataframe
#Creating a dataframe from a dictionary
#Create the dataframe
durations_df=pd.DataFrame(movie_dict)
#Print the dataframe
print(durations_df)

#-----Problem 3: Import matplotlib.pyplot under its usual alias and create a figure
fig = plt.figure()
# Draw a line plot of release_years and durations
plt.plot(durations_df['years'], durations_df['durations'])
# Create a title
plt.title('Netflix Movie Durations 2011-2020')
# Show the plot
plt.show()

#-----Problem 4: Loading the rest of the data from a CSV
netflix_df=pd.read_csv("C:/Users/Andrew/WS/.venv/netflix_titles.csv")
#Print the first 5 rows of the dataframe
print(netflix_df.head(5))

#-----Problem 5: Filtering for movies
# Subset the DataFrame for type "Movie"
netflix_df_movies_only=netflix_df[netflix_df['type']=='Movie']
print(netflix_df_movies_only.head(10))
# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['listed_in','title','country','release_year','duration']]
# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset.head(50))
#print(netflix_df_movies_only.head(20))
#We need to split the duratio column into a integer and a unit column
netflix_movies_col_subset[['duration', 'd_unit']] = netflix_movies_col_subset['duration'].str.split(pat=' ',n=1, expand=True)
#Check Output
print(netflix_movies_col_subset.head(50))
#Change column datatype
netflix_movies_col_subset['duration'] = pd.to_numeric(netflix_movies_col_subset['duration'])

#-----Problem 6: Creating a Scatter Plot
# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))
# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset['release_year'],netflix_movies_col_subset['duration'])
# Create a title
plt.title("Movie Duration by Year of Release")
# Show the plot
plt.show()

#-----Problem 7: Digging Deaper
# Filter for durations shorter than 60 minutes
short_movies=netflix_movies_col_subset[netflix_movies_col_subset['duration']<60]
# Print the first 20 rows of short_movies
print(short_movies.head(20))

#-----Problem 8: Marking non-feature films
# Define an empty list
colors = []
# Iterate over rows of netflix_movies_col_subset
for index, a in enumerate(netflix_movies_col_subset['listed_in']) :
    if a == 'Children & Family Movies' :
        colors.append('red')
    elif a == 'Documentaries' :
        colors.append('blue')
    elif a == 'Stand-Up Comedy' :
        colors.append('green')
    else:
        colors.append('black')
# Inspect the first 10 values in your list        
print(colors[0:10])

#-----Problem 9: Plotting with color
# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))
# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset['duration'],netflix_movies_col_subset['release_year'],c=colors)
# Create a title and axis labels
plt.title('Movie duration by year of release')
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
# Show the plot
plt.show()