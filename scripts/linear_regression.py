# IMPORT ALL IMPORTANT LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
from scipy import stats
sns.set()

# DATA TO WORK WITH
data = pd.read_csv('C:\\Users\\bartek\\PycharmProjects\\machine_learning\\data\\1.01. Simple linear regression.csv')

# SUMMARY OF FIELDS
data.describe()

# DEFINING AXES
"dependent variable, checking what interfere with GPA"
y = data['GPA']
"independent variable"
x = data['SAT']

# DATA VIEW IN SCATTER PLOT
plt.scatter(x,y)
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()

#STATISTICS
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
"R square  = 0.4060039147967981, it means that this is not good fit"
r_value ** 2

# CREATE FIT LINE

def predict(x):
    return slope * x + intercept
fitLine = predict(x)

# PLOTTING
"scatter plot"

plt.scatter(x,y)
plt.plot(x,fitLine, c='r')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()