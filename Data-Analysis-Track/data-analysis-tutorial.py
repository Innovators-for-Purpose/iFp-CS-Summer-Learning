import pandas as pd
import matplotlib.pyplot as plt

#loading the dataset
df = pd.read_csv('social_media_impact.csv')

#run your program to see the 4500 answers dataframe
print(df)

# use df.head() to see the first 5 rows, which means first 5 answers
print(df.head())

# try to display the number of answers you want!
#print("first 10 rows of the dataset: ")
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

#data cleaning
#part 1: find the mean of the Perceived_Stress_Score column
average_stress = df["Perceived_Stress_Score"].mean()
print(average_stress)

#part 2: find the mean of the Academic_Performance_GPA column
average_gpa = df["Academic_Performance_GPA"].mean()
print(average_gpa)

#part 3: fill the missing values in Percieved_Stress_Column with the mean.
df["Perceived_Stress_Score"] = df["Perceived_Stress_Score"].fillna(average_stress)

#part 3.2: fill the missing values in Academic_Performance_GPA with the mean.
df["Academic_Performance_GPA"] = df["Academic_Performance_GPA"].fillna(average_gpa)

#part 4: check our data again!
#print("checking if we clean data correctly:")
print(df.isna().sum())

#Analyzing quantitative data per column. First example: `Age` column
age_column = df["Age"]
print(age_column)

#using describe()
print(age_column.describe())

#Analyzing qualitative date per column. First example: `Primary_Platform` column
primaty_platform_column = df["Primary_Platform"]
print(primaty_platform_column)

#using value_counts()
print(primaty_platform_column.value_counts())

#filtering data
# part 1: select column
daily_usage_hours_column = df["Daily_Usage_Hours"]
print(daily_usage_hours_column)

# create filter and save it in a variable
bigger_than_8 = df[daily_usage_hours_column > 8]

#see your filter data!
print(bigger_than_8)

#filter by text
#part 1: access `Primary_Platform` values
primary_platform_column = df["Primary_Platform"]
print(primary_platform_column)





