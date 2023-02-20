# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats
import matplotlib.pyplot as plt
# Import all of our data, assumes the csv files are in same as execution directory
Q4_2020 = pd.read_csv('./fmli211.csv')
Q1_2021 = pd.read_csv('./fmli212.csv')
Q2_2021 = pd.read_csv('./fmli213.csv')
Q3_2021 = pd.read_csv('./fmli214.csv')
Q4_2021 = pd.read_csv('./fmli221.csv')

#Problem A
#Add up all our datasets for the year 2021
df = pd.concat(([Q1_2021, Q2_2021, Q3_2021, Q4_2021]), ignore_index = True)
#data = data1.copy()
#data.head()
#print(df.describe())

#Problem B
#We want to add up QC and QP and then multiply by 4 to anualize the expendature
anualExp = (df["TOTEXPPQ"] + df["TOTEXPCQ"]) * 4
anualInc = df["FINCBTXM"]
#Print the summary stats
print(anualExp.describe())
print(anualInc.describe())

#Problem C
#We want to drop values from data
thisdict = {"FAM_SIZE", "NUM_AUTO", "FINCBTXM", "TOTEXPPQ", "TOTEXPCQ", "ALCBEVCQ", "ALCBEVPQ", "FOODCQ", "FOODPQ", "FDHOMECQ", "FDHOMEPQ", "FDMAPCQ",  "FDMAPPQ", "FDAWAYCQ", "FDAWAYPQ", "MAJAPPCQ", "MAJAPPPQ", "TENTRMNC", "TENTRMNP", "EDUCACQ", "EDUCAPQ", "ELCTRCCQ", "ELCTRCPQ"}
#Drop all negatives for all the categories in the dictionary
for x in thisdict:
    df.drop(df[df[x] < 0].index, inplace = True)

anualExp = (df["TOTEXPPQ"] + df["TOTEXPCQ"]) * 4
anualInc = df["FINCBTXM"]
#Print the summary stats
print(anualExp.describe())
print(anualInc.describe())

#Problem E
m, Xcept, rVal, pVal, stdErr = stats.linregress(df['FINCBTXM'] ,((df["TOTEXPPQ"] + df["TOTEXPCQ"]) * 4))
#Generate best fit line
y_line = Xcept + m * df["FINCBTXM"]
#Report the values of slope, intercept, and R
print(f'The parameters of the line: m=',m, 'intercept=', Xcept, 'STD_ERR', stdErr, '\n')
#Create the plots
plt.figure()
plt.scatter(df['FINCBTXM'], ((df["TOTEXPPQ"] + df["TOTEXPCQ"]) * 4))
plt.plot(df['FINCBTXM'], y_line, 'r')
plt.title(f'Expendature vs. Income')
plt.xlabel('income ($)')
plt.ylabel('expendature ($)')

df["TOTEXPYEAR"] = (df["TOTEXPPQ"] + df["TOTEXPCQ"]) * 4
print(smf.ols(formula = "TOTEXPYEAR ~ FINCBTXM", data=df).fit(cov_type='HC1').summary())

#Problem F
#Separate the low income and high income into two parts
LowIncome = df.copy()
LowIncome.drop(LowIncome[LowIncome["FINCBTXM"] < 61338.8].index, inplace = True)
LowIncome["TOTEXPYEAR"] = (LowIncome["TOTEXPPQ"] + LowIncome["TOTEXPCQ"]) * 4
print(smf.ols(formula = "TOTEXPYEAR ~ FINCBTXM", data=LowIncome).fit(cov_type='HC1').summary())
#Then print the regression statistics for both low and high
HighIncome = df.copy()
HighIncome.drop(HighIncome[HighIncome["FINCBTXM"] > 61338.8].index, inplace = True)
HighIncome["TOTEXPYEAR"] = (HighIncome["TOTEXPPQ"] + HighIncome["TOTEXPCQ"]) * 4
print(smf.ols(formula = "TOTEXPYEAR ~ FINCBTXM", data=HighIncome).fit(cov_type='HC1').summary())

#Problem G 
#Separate the food from home and food from outside
#Print the summary statistics for the linear regression 
df["FDHOMEYEAR"] = (df["FDHOMECQ"] + df["FDHOMEPQ"]) * 4
df["FOODYEAR"] = (df["FOODCQ"] + df["FOODPQ"]) * 4
print(smf.ols(formula = "FDHOMEYEAR ~ FINCBTXM", data=df).fit(cov_type='HC1').summary())
print(smf.ols(formula = "FOODYEAR ~ FINCBTXM", data=df).fit(cov_type='HC1').summary())
plt.show()
