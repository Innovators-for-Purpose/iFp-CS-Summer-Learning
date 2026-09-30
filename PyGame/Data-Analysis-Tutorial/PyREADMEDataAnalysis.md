# iFp Python Coding Practice: Data Analysis with Python

Welcome to iFp's Python coding practice 3! In this session you will practice Python by analyzing and visualizing the dataset of "Social Media Impact of Life."

## What you'll do
- Build your own version of `my-data-analysis.py`
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

**Step 1: Install Python**

Download and install [Python](https://www.python.org/downloads/) on your computer. 

After installing Python, open your VS Code terminal and check that it works:

`python3 --version`

You should see a Python version number.

**Step 2: Install pandas**

Pandas is the Python library we will use to work with tables.

In the same VS Code terminal:

`python3 -m pip install pandas`


**Step 3: Install matplotlib**

Matplotlib is the Python library we will use to turn our data into graphs and visualizations.

In the same VS Code terminal:

`python3 -m pip install matplotlib`

## Start coding!

Navigate to Visual Studio Code in your applications and clone the `iFp Summer Coding Practice folder` from the iFp Github repository. Open the `PyGame` folder and then the`Data-Analysis-Tutorial` folder. You should be able to see the following files:

- `data-analysis-tutorial.py`: The provided reference sample. This file will contain the structure and behavior of your data analysis.

- `PyREADMEDataAnalysis.md` : You are reading the file right now! This file contains the tutorial instructions. 

- `Social_media_impact_on_life.csv` : The Dataset we will work with!

### Imports

1. Open `data-analysis-tutorial.py` in VS Code and look through the example.
3. Create a file in the same folder named `my-data-analysis.py`.
4. Open `my-data-analysis.py` in VS Code.
5. Add the following imports at the top of `my-data-analysis.py`:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

`import` allows us to use code from a Python library in our program. We are assigning `pandas` the shorter name `pd` and `matplotlib` the shorter name `plt`. These shorter names are called aliases.

Later, when we want to use something from pandas, we can write:

`pd.NAME_OF_PANDAS_FUNCTION`

For example:

`pd.read_csv()`

And when we want to use something from matplotlib, we can write:

`plt.NAME_OF_MATPLOTLIB_FUNCTION`

For example:

`plt.show()`

We will show you how to work with this in the following steps!


