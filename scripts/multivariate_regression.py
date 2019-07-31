# IMPORT ALL IMPORTANT LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn
seaborn.set()

# DATA TO WORK WITH
data = pd.read_csv('C:\\Users\\bartek\\PycharmProjects\\machine_learning\\data\\1.02. Multiple linear regression.csv')

# SUMMARY OF FIELDS
data.describe()

# DEFINING AXES
"dependent variable, checking what interfere with GPA"
y = data ['GPA']
"independent variable, as dataframe but we need const"

x1 = data [['SAT','Rand 1,2,3']]
x = sm.add_constant(x1)


est = sm.OLS(y, x).fit()
est.summary()
"base on the results it is clear that SAT is more important than RAND 13"