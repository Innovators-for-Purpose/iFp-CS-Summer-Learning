# iFp Python Coding Practice: Data Analysis with Python

Welcome to iFp's Python coding practice 3! In this session you will practice Python by analyzing and visualizing the dataset of "Social Media Impact of Life."

## What you'll do
- Build your own version of `my-data-analysis.ipynb`
- Load and explore a CSV dataset with information of 4,500 students
- Filter, sort, count, and group data to answer questions
- Investigate patterns in the data
- Create your own data analysis!

## What you'll learn

Work on this project will help you to:
- Improve your Python programming skills
- Understand how Python can be used for data analysis
- Work with CSV files using `pandas` library
- Create visualizations using `matplotlib` library
- Learn what data can show us and what it can't

This tutorial is part of the **Data Analysis and AI with Python** iFp curriculum.

## Before start coding

We need to make sure we have the following install in our computer:

### Step 1: Install Python

Download and install [Python](https://www.python.org/downloads/) on your computer. 

After installing Python, open your VS Code terminal and check that it works:

`python3 --version`

You should see a Python version number in the terminal.

### Step 2: Install pandas

Pandas is the Python library we will use for data manipulation.

In the same VS Code terminal:

`python3 -m pip install pandas`

### Step 3: Install matplotlib

Matplotlib is the Python library we will use to turn our data into graphs and visualizations.

In the same VS Code terminal:

`python3 -m pip install matplotlib`

### Step 4: Install Jupyter Notebook extension

Go to VS Code and click on the extensions tab. Search the **Jupyter** extension and install it. This extension allows you to create a Jupyter Notebook file where you can write python code that manages big amounts of data and run it in one single file.


### **OPTIONAL** Step 5: Install Rainbow CSV in Visual Studio Code

Go to VS Code and click on the extensions tab. Install the Rainbow CSV extension. This extension give different colors to the colums in our CSV file.


## Start coding!

Navigate to Visual Studio Code in your applications and clone the `iFp Summer Coding Practice folder` from the iFp Github repository. Open the the `Data-Analysis-Tutorial` folder. You should be able to see the following files:

- `my-jupyter-data-analysis.ipynb`:  The provided reference sample. This file will contain the structure and behavior of your data analysis.

- `PyREADMEDataAnalysis.md` : You are reading the file right now! This file contains the tutorial instructions. 

- `social_media_impact.csv` : The Dataset we will work with!

- `DataLifeCycle.png`: This is an image of the data analysis cycle, and it will be explained on the following tutorial.

Open `data-analysis-tutorial.py` in VS Code and look through the example. Then create a new file in the same folder named:

```python
my-data-analysis.ipynb
```

### `my-data-analysis.ipynb`

Your `my-data-analysis.ipynb` file will contain the code you write throughout this tutorial.

You will organize your program into:

1. Imports
2. Loading the dataset
3. Exploring the dataset
4. Cleaning/checking the data
5. Filtering and sorting
6. Counting and grouping
7. Data visualization
8. Your own analysis

### `social_media_impact.csv`

This is the dataset we will work with during the whole tutorial. This dataset was obtained from [Kaggle](https://www.kaggle.com/), a platform where anyone around the world can upload and download datasets from diverse topics. I recommend you to explore tons of datasets available there!

The dataset we are using is called [**Impact of Social Media on Life**](https://www.kaggle.com/datasets/harishyadav0506/impact-of-social-media-on-life) 

**Here is the description of the dataset:** In recent years, the intersection of digital platform consumption, sleep hygiene, and stress has become a critical focus of behavioral and educational research. This dataset provides granular survey metrics across 4,500 students ranging from high school to postgraduate programs to analyze how digital engagement shapes daily life and well-being.

In the following steps we will explore more and more the dataset.

## Imports

In our new file `my-data-analysis.ipynb` write the following code at the top:

```python
import pandas as pd
import matplotlib.pyplot as plt
```
Run it!

`import` allows us to use code from a Python library in our program. We are assigning `pandas` the shorter name `pd` and `matplotlib` the shorter name `plt`. In the world of programming, this shorter names are called aliases.

Later, when we want to use something from pandas, we can write:

`pd.NAME_OF_PANDAS_FUNCTION`

For example: `pd.read_csv()`

And when we want to use something from matplotlib, we can write:

`plt.NAME_OF_MATPLOTLIB_FUNCTION`

For example: `plt.show()`

We will show you how to work with this in the following steps!

## Exploratory Data Analysis (EDA)

Exploratory data analysis (EDA) is used by data scientists to analyze and investigate datasets and summarize their main characteristics, often employing data visualization methods. - IBM

In the following image you can see the steps for EDA based on Harvard Business School:

![DataLifeCycle](DataLifeCycle.png)

Since our dataset `social_media_impact.csv` was download from the web the following steps were already done:

1. Generation: Created a form with questions about the social media impact in students life
2. Collection: Send the form to 4,500 students
3. Processing: Get 4,500 answers
4. Storage: Save the answers in a CSV file

In this tutorial we are going to work on the following steps:

5. Management: Load the dataset and play with it!
6. Analyzing: We are going to understand what the collected data is telling us
7. Visualization: We are going display the data with graphs 
8. Interpretation: We assign meaning to our data, and explain findings!

## Data Management: Loading our dataset

Before we can manage and analyze data, we need to load it into Python.

### What is a CSV?

CSV stans for **Comma-Separated Values**

A CSV file is a common way to store data in a table. For example, a very small CSV can look like this:

```text
Name,Age,Favorite Color
Alex,19,Yellow
Adina,19,Blue
Andres,16,Orange
```

Each row represents one student, and each column represents a piece of information about that student. Our dataset is much larger. It contains information of **4,500 students**.

### Read our CSV file

Make sure `social_media_impact.csv` is in the same folder as `my-data-analysis.ipynb`.

In our `my-data-analysis.ipynb` add the following code:

```python
df = pd.read_csv("social_media_impact.csv")
```
Run it!

We are using `pd.read_csv()` to read the CSV file. We are storing the dataset in a variable called `df`.

`df` is a common abbreviation for **DataFrame**. A pandas DataFrame organizes the information of our CSV in a table that Python can work with.

### Print the DataFrame

Let's see what our DataFrame looks like. Add the following line of code:

```python
print(df)
```

Now run your program! 
**IMPORTANT:** Everytime you add a piece of code in your `my-data-analysis.ipynb` file, you should run your code to see the new functions working!

Another thing to **remember**: Since you have 4,500 rows, pandas will usually shorten the output instead of printing every row.

### Display the DataFrame

We can use `display()` function to see our  Jupyter notebook DataFrames in a clean and interactive HTML version. 

```python
display(df)
```
Try using this function along side `print()` in the next steps!

## Data Management: Explore and handle the data

Now that we have access to the 4,500 answers, let's start learning what is the information they provide. Let's print the first 5 rows to see the information of the first 5 students.

In your `my-data-analysis.ipynb` file add the following:

```python
print(df.head())
display(df.head())
```
`head()` shows the first five rows of the DataFrame.

We can also ask for a specific number of rows:

```python
print(df.head(10))
display(df.head(10))
```
This shows the first 10 rows! Now it is **your turn**. Try changing `10` to another number. What happens?

**GOOD PRACTICE TIP:** At this point, you may have notice we are going to be using `print()` a LOT! Everytime you add a new `print()` line, make sure you also print a small line describing what are you doing.

**For example:**
```python
print("First ten rows of data set: ") #this printing line describing what you will see in the terminal.
print(df.head(10))
```
**This is a good practice tip, you decide if you want to add it to your code!**

### Looking at the last rows

We can also look at the end of the dataset. Add:

```python
print(df.tail())
display(df.tail())
```
`tail()` shows the last five rows.

Try:

```python
print(df.tail(10))
display(df.tail(10))
```

How many rows can you see?

### What is the size of our dataset?

We know our dataset contains 4,500 answers from high school to undergraduate students, but let's ask Python!

Add:

```python
print(df.shape)
```
Now run again your program.

You should see something similar to:

```python
(4500, 16)
```
The first number is the number of **rows**. The second number is the number of **columns**. So our dataset has:
- 4,500 rows
- 16 columns

## Data Analysis: What is the data telling us?

Now that we have access to the dataset, let's analyze it! The columns tell us what information is available for each student.

### Printing the column names

Add: 
```python
print(df.columns)
```
You should see the following columns names:
- 'Student_ID'
- 'Age'
- 'Gender'
- 'Academic_Level'
- 'Primary_Platform'
- 'Daily_Usage_Hours'
- 'Weekend_Extra_Hours'
- 'Device_Type'
- 'Sleep_Duration_Hours'
- 'Sleep_Quality_Score'
- 'Late_Night_Usage'
- 'Social_Comparison_Frequency'
- 'Perceived_Stress_Score'
- 'Mental_Health_Index'
- 'Academic_Performance_GPA'
- 'Overall_Impact'

### Analyze the columns

Look at the column names. What questions could we ask using this dataset?

For example:

- Which social media platforms appear in the dataset?
- How many hours do students spend on social media each day?
- Do students who use social media late at night report different sleep durations?
- Which academic level appears most often?
- How does social media use vary by platform?

There are many questions we could investigate. Add yours to the list!

Pandas can give us more information about our DataFrame. Add the following line:

```python
print(df.info())
```

`info()` gives us information such as:

- RangeIndex: Number of Rows
- Data Columns: Number and Name of columns
- Non-Null Count: Number of non-empty values each column has
- Dtype: The type of data stored in each column. For example:
    - `str`: the data type is text
    - `int64`: the data type is a number
    - `bool`: the data type is `True` or `False`
    - `float64`: the data type is a decimal number

Also in the end it mentions the amount of times one data types are repeated. We have 1 `bool`, 5 `float64`, 3 `int64`, 7 `str`.

This is important because different kinds of data can be analyzed in different ways.

### Check if there is any missing data

Real-world datasets are not always perfect. Sometimes, when you work with big datasets information is missing. Our dataset contains some missing values, so we should check for them before making certain calculations.

Add:
```python
print(df.isna().sum())
```
`isna()` checks whether a value is missing.
`sum()` counts how many missing values there are in each column.

In your terminal you should be able see that we have:
- 46 missing values in `Perceived_Stress_Score`
- 85 missing values in `Academic_Performance_GPA`

### Why is this important in Data Analysis?

Imagine we want to calculate the average GPA. If some students do not have a GPA recorded, we need to know that before interpreting our results. 
**Missing data does not mean that the dataset is bad.** It means we need to pay attention to what information is available. 

## Data Cleaning: What do we do when there is missing values in our dataset?

In data analysis, data cleaning means preparing our data so that we can analyze it more reliably. Before starting playing and analyzing numerica data let's make sure we clean the missing data we found in `Perceived_Stress_Score` and `Academic_Performance_GPA`.

There are different ways to handle missing data. For example:

- Remove rows that contain missing values
- Replace missing values with another value
- Use a statistical method to estimate the missing value

For this tutorial, we will use the technique called Mean Substitution.

### Mean Substitution Technique

Mean substitution replaces a missing numerical value with the mean (average) of the available values in that column.

For example, let's imagine we have a column in our dataframe called "test scores":
```python
test scores,
80,
90,
70,
missing,
100,
```
First, we calculate the mean of the values that we **do** have:

`(80 + 90 + 70 + 100) / 4 = 85`

The missing value would then be replaced with 85. Our data would become:

```python
test scores,
80,
90,
70,
85,
100,
```
We are using information from the other values in the same column to fill in the missing value.

For this project, we will use mean substitution so we can practice an important data cleaning technique with pandas.

### Cleaning `Perceived_Stress_Score`

Pandas can calculate the mean for us using `.mean()`.

In your `my-data-analysis.ipynb` file add:

```python
average_stress = df["Perceived_Stress_Score"].mean()

print(average_stress)
```

`df["Perceived_Stress_Score"]` selects the `Perceived_Stress_Score` column of our dataframe.

`.mean()` calculates the average of all the values in the column.

After we got the mean we save the result in the variable called `average_stress`. When we `print(average_stress)` it will show the mean result in the terminal.

### YOUR TURN: Cleaning `Academic_Performance_GPA`

As we find out before, we have missing data in the `Perceived_Stress_Score` and `Academic_Performance_GPA` columns. Now it is your turn to find the mean for the `Academic_Performance_GPA` column.

Create a variable called `average_gpa` and called a pandas function that helps you get the mean of the `Academic_Performance_GPA`. HINT: review what we did to get the mean of `Perceived_Stress_Score`!!!

```python
average_gpa = ______________________________ 

print(average_gpa)

```

### Replacing the missing values with the mean

Next, we can use the mean to replace the missing values in our dataset. 

`fillna()` is a pandas function that fills in the missing values.

Add the following code:

```python
df["Perceived_Stress_Score"] = df["Perceived_Stress_Score"].fillna(average_stress)
```

That looks like a huge code sentence! Let's break it little by little.

`df["Perceived_Stress_Score"]` selects the column we want to clean.

`.fillna(average_stress)` tells pandas that wherever there is a missing value, replace it with the value stored in `average_stress`.

Finally: 
```python
df["Perceived_Stress_Score"] = ...
```
stores the cleaned column back in our DataFrame.

### YOUR TURN: Fill the missing values in `Academic_Performance_GPA`!

Two steps ago you created a variable called: `average_gpa` where you store the mean of the `Academic_Performance_GPA` column. It should look like this:

```python
average_gpa = df["Academic_Performance_GPA"].mean()

print(average_gpa)
```

Now use that mean to fill the missing values:
HINT: review what we did to replace the missing values of `Perceived_Stress_Score`!!!

```python
df["Academic_Performance_GPA"] = ___
```

Now both columns have been cleaned!

### Check our data again

Whenever we change our data, it is a good idea to check whether our change worked. Remember how we checked for missing values earlier?
We used:
```python
print(df.isna().sum())
```

Now add it again to your file and run it! Check the data display in your terminal. `Perceived_Stress_Score` & `Academic_Performance_GPA` should now be at 0.

**GOOD PRACTICE TIP:** In data analysis, we should not assume that our code worked just because Python did not show an error. We should check our data before and after cleaning to make sure the change happened.

## Data Analysis: Working with quantitative data

Our dataset has 8 columns with numerical values. The columns have information that can be measured or counted. That is what we call **quantitative data**. 

In this dataset the numerical values that we found are 2 types:

- `int`: Short for integer. An integer is a whole number(with no decimal point!) It can be positive, negative, or zero. Examples: 10, -3, 0, 42

- `float`: Short for floating-point number. A float is a number that has a decimal point. Examples: 3.14, -2.5, 0.0, 10.75

The `describe()` pandas method can help us get the following statistics information:

- `count`: Number of values of the column
- `mean`: Average of the column
- `standard deviation`: Number that explains how "spread out" the values are
- `minimum` and `maximum`: lowest and highest value of the column
- `quartiles`: 25%, 50%, 75% (50% represents the median)
 
We can use `describe()` to get an overview of the columns that we want to explore!

### Analyzing stadistics of `Age` column

Let's start use `describe()` to explore our the information that `Age` column is giving us.

First let's select our column:
```python
age_column = df["Age"]
print(age_column)
```

Now let's use `describe()`
```python
print(age_column.describe())
```
Now you can see the statistic information of the `Age` column!

**IMPORTANT:** We can only use `describe()` with columns that have numerical values. 

### YOUR TURN: Get the statistics of the following columns!

In this dataset the columns that have integer and float values are:
- `Age` **(We already got the information of this one)**
- `Daily_Usage_Hours`
- `Weekend_Extra_Hours`
- `Sleep_Duration_Hours`
- `Sleep_Quality_Score`
- `Perceived_Stress_Score`
- `Mental_Health_Index`
- `Academic_Performance_GPA`

Now it is your turn to:
- Create one variable per each column where you can save and select the column information
- Use the `describe()` method on each variable
- Print and analyze the statistics!

**HINT**: Check the code that we used for `Age` column!

## Data Analysis: Working with qualitative data

There are 16 columns in our dataset, 8 of them contained numerical values and the rest have non-numerical values that describe qualities, characteristics, categories, opinions, and experiences. This is what we called **qualitative data**. 

In this dataset the non-numerical values that we found are 2 types:

- `str`: Short for string. A string is text, such as words, sentences, or even one single character. In Python, strings are written inside quotation marks. Examples: "Hello!", "Bela", "123"

- `bool`: Short for boolean. A boolean is a value that can only be one of two things: True or False. Example: whether a player has won a game.

We can use multiple panda methods to analyze qualitative data. Some columns contain categories, we can count how often each category appears with the `value_counts()` pandas method.

### Counting categories of `Primary_Platform` column

First, just like we did with our numeric columns, let's select our column:

```python
primaty_platform_column = df["Primary_Platform"]
print(primaty_platform_column)
```
Now let's use `value_counts()`:

```python
print(primaty_platform_column.value_counts())
```
Now you can see the what was the primary platform that most of the students use!

### YOUR TURN: Use `value_counts()` method with other categorical columns!

In this dataset the 8 columns that have string and boolean values are:
- `Student_ID`
- `Gender`
- `Academic_Level` 
- `Primary_Platform` **(We already got the information of this one)**
- `Device_Type`
- `Late_Night_Usage`
- `Social_Comparison_Frequency`
- `Overall_Impact`

Check the CSV file, which are the other columns that have categorical values? how many do we have?

Once you identified the other columns, it is your turn to:
- Create one variable per each column where you can save and select the column information
- Use the `value_counts()` method on each variable
- Print and analyze the results!

**HINT**: Check the code that we used for the `Primary_Platform` column!

### Reflect on results

Before we continue playing with qualitative and quantitative data, it is always great to reflect on what the data is telling us. 

## Data Analysis: Filtering data

One of the most useful things we can do with pandas is **filter** data. **Filtering** means selecting only the rows that match a condition.

### Filter numerical values 

Let's start with a question:

***How many students spend more than 8 hours a day on social media?***

To answer this question, we'll work with the `Daily_Usage_Hours` column.

#### Select the column

If you already created a variable for this column, you can skip this step and reuse it. Otherwise, add the following:

```python
daily_usage_hours_column = df["Daily_Usage_Hours"]
print(daily_usage_hours_column)
```
Now that we created the `daily_usage_hours_column` variable we have access to all the values in the column. The **next step** is to define a condition for the filtering.

#### Create a filter condition

We want to filter **students whose daily social media usage is greater than 8 hours**.

This is the general structure of a filter in pandas:

```python
df[condition]
```

Let's break it down:

- `df`: the DataFrame containing our dataset
- `[condition]`: a rule that determines which rows to keep. Pandas checks each row against the condition and returns `True` or `False`. Only rows where the condition is `True` are included in the filtered DataFrame.

This is how our condition would look like:

```python
df[daily_usage_hours_column > 8]
```

The `>` operator means greater than. This filter keeps only the rows where students' daily social media usage is greater than 8 hours.

#### Filter the rows

We can use the condition inside `df[...]` to keep only the rows that meet it.

```python
more_than_8h_online = df[daily_usage_hours_column > 8]
print(more_than_8h_online)
```

Congrats!!! You've created your first filter! The variable `more_than_8h_online` now contains only the students who spend more than 8 hours a day on social media.

#### Count the filter rows

How many students meet our condition?

We can use `.shape` to find the dimensions of a DataFrame. It returns a **tuple** containing the number of rows and columns. The first value of the tuple, `shape[0]`, tells us how many rows there are.

Add the following code:

```python
print(more_than_8h_online.shape[0])
```
Now we know that out of the 4,500 students, ***632 students spend more than 8 hours*** in social media everyday.

### Filter with text values

We can also filter data using text values, for example social media platform names. 

Let's answer a new question:

***How many students use TikTok as their primary social media platform?***

Just like we did in the past example, the first step is to select the column we want to work with. If you created a variable for `Primary_Platform` before, you can **jump to the next step** and **use your own variable**. Otherwise, add:
```python
primary_platform_column = df["Primary_Platform"]
#if you would like to see the values of this column you can print it!
print(primary_platform_column)
```

Now that we created the `primary_platform_column` variable we have access to all the values in that column. The **next step** is to define a condition for the filtering.

This time, we want to find rows where the primary platform is TikTok.
```python
primary_platform_column == "TikTok"
```

The `==` operator checks whether a value is equal to another value. Just like our numerical filter, this condition returns `True` or `False` for each row.

Let's apply the condition to our DataFrame:
```python
tiktok_users = df[primary_platform_column == "TikTok"]
print(tiktok_users)
```

This displays only the rows where `Primary_Platform` is `"TikTok"`. To count these students, we can use:
```python
print(tiktok_users.shape[0])
```

### When comparing a column's text values, we need to remember...

1) **Use quotation marks** around text, for example `"TikTok"`, so Python recognizes it as a string.
2) **Match the text in your dataset exactly** including spaces and capitalization.
    Our code:
    ```python
    primary_platform_column == "TikTok"
    ```
    checks for the exact text `"TikTok"`. Writing `primary_platform_column == TikTok` without quotation marks makes Python interpret `TikTok` as a variable name which can cause a `NameError` if that variable hasn't been defined.

    If you write `"Tik Tok"` with a space instead, Python treats it as a string, but it won't match rows containing `"TikTok"`. The filter will simply return no matching rows if that exact value doesn't exist in the column.

### Filtering with multiple conditions

We learn how to filter data with numerical and text values, now let's combine conditions!

For example, maybe we are curious to know:
***How many students use social media for more than 8 hours per day `AND` sleep less than 6 hours per night***

Remember: when combining conditions in pandas, put each condition inside parentheses.

```python
#feel free to change the names of the variables
two_conditions = df[(df["Daily_Usage_Hours"] > 8) & 
    (df["Sleep_Duration_Hours"] < 6)]

print(two_conditions)
#you can also display it! 
display(two_conditions)
```
In this condition, the `&` operator means `AND`.

Let's count how many students accomplished our conditions. **how many students use social media more than 8 hours per day `AND` sleep less than 6 hours per night.**

```python
print(two_conditions.shape[0])
```
Now we know **518 students** use social media *more than 8 hours per day* `AND` *sleep less than 6 hours per night.*

### YOUR TURN: Create 5 multiple condition filters!!!

Let's practice our filter skills! Create a filter condition that answers the following questions. Remember:

- Create a new variable to store your filtered DataFrame
- Use `&` when you want **both conditions** to be true
- Put each conditions inside parentheses
- Use `df[condition]` to filter the rows
- Use `print()` and `display()` to show the filtered results
- Use `.shape[0]` to count how many students meet your conditions
- For each challenge:

#### Filter 1: Social media AND Sleep duration

Create a multiple condition filter that can answer this question: ***How many students use social media for more than 6 hours per day AND sleep for less than 7 hours per night?***

#### Filter 2: Social media AND Mental health

Create a multiple condition filter that can answer this question: ***How many students use social media for more than 5 hours per day AND have a mental health score greater than 7?***

#### Filter 3: Prefered platform AND Daily usage

Create a multiple condition filter that can answer this question: ***How many students use social media for more than 6 hours per day AND use Instagram as their primary social media platform?***

#### Filter 4: Social media AND Academic performance

Create a multiple condition filter that can answer this question: ***How many students use social media for less than 3 hours per day AND have an academic performance score greater than 7?***

#### Filter 5: 4 conditions challenge
Create a multiple condition filter that can answer this question: ***How many students use social media for more than 5 hours per day, sleep for less than 7 hours per night, have a mental health score greater than 5, AND have Youtube as their primary social media platform?***

🚧This part of the tutorial is under construction!!!🚧
## Data Analysis: Sorting data



## Data Analysis: Grouping data



## Data Visualization!

## References:

To create this tutorial I used the following references:

- Tim Stobierski, Harvard Business School [Why Exploratory Data Analysis (EDA) Is Essential to Machine Learning](https://online.hbs.edu/blog/post/exploratory-data-analysis), May 28, 2026

- MIT IBM, [What is exploratory data analysis (EDA)?](https://www.ibm.com/think/topics/exploratory-data-analysis)

- MIT CSAIL, [6.S079 Data Cleaning – Part 2](https://dsg.csail.mit.edu/6.S079-2022/lectures/6.S079_Lec08.pdf), Fall 2022












