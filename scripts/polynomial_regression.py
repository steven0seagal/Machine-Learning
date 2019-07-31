import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# CREATING SOME DATA
np.random.seed(2)
X = np.random.normal(3.0, 1.0, 1000)
Y = np.random.normal(50.0, 10.0, 1000) / X

# DATA VISUALISATION
scatter(X, Y)

# X, Y TO ARRAY
x = np.array(X)
y = np.array(Y)

# FITTING WITH DEGREES "d"
d = 4
p4 = np.poly1d(np.polyfit(x, y, d))

# DATA VISUALIZATION
xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')
plt.show()
# CALCULATE CORRECTION OF FITTING
r2 = r2_score(y, p4(x))
print(r2)
"R^2 = 0.82937663963 , IT MEANS THAT THIS MODEL IS QUITE GOOD"