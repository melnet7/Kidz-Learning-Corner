import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

from statsmodels.graphics.tsaplots import plot_pacf

data = pd.read_csv('data/Quarter_Sales.csv')

# Your code starts after this line
salesC = data["Sales"]
shift = [1, 3, 4, 5, 6, 8, 11, 18]
s1 = salesC.shift(periods=1)
s3 = salesC.shift(periods=3)
s4 = salesC.shift(periods=4)
s5 = salesC.shift(periods=5)
s6 = salesC.shift(periods=6) 
s8 = salesC.shift(periods=8)
s11 = salesC.shift(periods=11)
s18 = salesC.shift(periods=18)
predictor = pd.DataFrame({'s4':s4, 's6':s6, 's18':s18})
Y=salesC[18:]
X=predictor[18:]
# X=sm.add_constant(X)
m=sm.OLS(Y,X)
print(m.fit().summary())
t=salesC.size
input=pd.DataFrame({'s4':[salesC[t-4]], 's6':[salesC[t-6]], 's18':[salesC[t-18]]})
predictInput=m.fit().predict(input)
print(round(predictInput, 2))
# Your code ends before this line