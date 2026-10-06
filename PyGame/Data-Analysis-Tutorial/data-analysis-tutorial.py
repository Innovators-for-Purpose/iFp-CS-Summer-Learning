import pandas as pd
import matplotlib.pyplot as plt

#loading the dataset
df = pd.read_csv('social_media_impact.csv')

#run your program to see the 4500 answers dataframe
print(df)

# use df.head() to see the first 5 rows, which means first 5 answers
print(df.head())

# try to display the number of answers you want!
print(df.head(10))

# last 5 rows
print(df.tail())

#what is the size of our dataset?
print(df.shape)

# printing the column names
print(df.columns)

#more info about our DataFrame
print(df.info())

#looking for missing values
print(df.isna().sum())
