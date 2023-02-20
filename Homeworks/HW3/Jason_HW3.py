# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats
import matplotlib.pyplot as plt
# Import all of our data, assumes the csv files are in same as execution directory
df = pd.read_csv('./pennbirthwgt0.csv')

#Problem 1: Clean up our data and replace missing values with '.'

#Variable of interest
"""
Average Cigarettes Smoked Per Day:  CIGAR       Bad: 99     Normal
Birth Weight of Baby:               DBRWT       Bad: 9999   Normal
"""
#Good Control Variables List:
"""
Age of Mother:                      DMAGE       Clean       Normal
Month of Prenatal Care Began:       MONPRE      Bad:    99  Normal
Race of Mother:                     MRACE3      Clean       Dummy
Education of Mother:                DMEDUC      Bad:    99  Normal
Adequacy of Care Record:            ADEQUACY    Bad:    4   Dummy
Average Number of Drinks Per Week:  DRINK       Bad:    99  Normal
Marital Status of Mother:           DMAR        Clean       Dummy
Pop Size of County of Occurrence:   CNTOCPOP    Clean       Dummy
HERPES:                             HERPES      Bad:    8,9 Dummy
Education of Father Detail:         DFEDUC      Bad:    99  Normal
"""
#Bad Controls List:
"""
Gestation Period Weeks              DGESTAT     Bad:    99  Normal
"""
#Useless Controls List:
"""
Sex                                 CSEX        Clean       Dummy
Birth Month                         BIRMON      Clean       Normal 
"""

setNames = np.array(['cigar', 'dbrwt', 'dmage', 'monpre', 'mrace3', 'dmeduc', 'adequacy', 'drink', 'dmar', 'cntocpop', 'herpes', 'dfeduc', 'dgestat', 'csex', 'birmon'])

#Clean data by replacing all bad values
#First make a dictionary
CtrlClean = np.array([['cigar', 99], ['dbrwt', 9999], ['monpre', 99], ['dmeduc', 99], ['adequacy', 4], ['drink', 99], ['herpes', 8], ['herpes', 9], ['dfeduc', 99], ['dgestat', 99]])

#Do operation for all values which must be cleaned
for i in range(0, np.shape(CtrlClean)[0]):
    df.drop(df[df[CtrlClean[i][0]] >= int(CtrlClean[i][1])].index, inplace = True)
#Create our analysis dataset
dummies = np.array([['mrace3', 1], ['dmar', 1], ['cntocpop', 0], ['csex', 1], ['herpes', 2]])
#Convert dummies to 0 and 1
for i in range(0, np.shape(dummies)[0]):
    df.loc[df[dummies[i][0]] == int(dummies[i][1]), dummies[i][0]] = 0
    df.loc[df[dummies[i][0]] > 0, dummies[i][0]] = 1
df.loc[df['adequacy'] < 3, 'adequacy'] = 0
df.loc[df['adequacy'] == 3, 'adequacy'] = 1
#Print out the summary statistics for our dataset
aSet = df[setNames]
print(aSet.mean(axis = 0, skipna = True))


#Problem 2 Part a
#First divide our Dataset into smokers and nonsmokers
noSmoke = aSet.copy()
Smoke = aSet.copy()

noSmoke.drop(noSmoke[noSmoke['cigar'] != 0].index, inplace = True)
Smoke.drop(Smoke[Smoke['cigar'] == 0].index, inplace = True)

#Print out the means of the smoker and non smoker groups
print("Mean Birth Weight nonSmokers:")
print(noSmoke.mean(axis = 0, skipna = True))
print("Mean Birth Weight Smokers:")
print(Smoke.mean(axis = 0, skipna = True))

#Problem 2 Part b
#Do a simple linear regression without any controls
print(smf.ols(formula = "dbrwt ~ cigar", data=aSet).fit(cov_type='HC3').summary())

#Problem 2 Part c
#Analyze several variables we want to test if they are significant
dummies = np.array(['mrace3', 'adequacy', 'dmar', 'cntocpop', 'herpes', 'csex'])
setNames = np.array(['cigar', 'dbrwt', 'dmage', 'monpre', 'mrace3', 'dmeduc', 'adequacy', 'drink', 'dmar', 'cntocpop', 'herpes', 'dfeduc'])
def createString(a, b):
    form = "dbrwt ~ cigar"
    for i in range(2, a.size):
        form = form + " + " + a[i]
    print(form)
    return form
stringInst = createString(setNames, dummies)
print(smf.ols(formula = stringInst, data=aSet).fit(cov_type='HC3').summary())

#Problem 2 part e
#Add in only good controls into our regression
setNames = np.array(['cigar', 'dbrwt', 'dmage', 'monpre', 'mrace3', 'dmeduc', 'adequacy', 'drink', 'dmar', 'cntocpop', 'dfeduc'])
dummies = np.array(['mrace3', 'adequacy', 'dmar', 'cntocpop']) 

stringInst = createString(setNames, dummies)
print(smf.ols(formula = stringInst, data=aSet).fit(cov_type='HC3').summary())

#Problem 2 part g
#Add in useless controls sex and birth month into regression
dummies = np.array(['mrace3', 'adequacy', 'dmar', 'cntocpop', 'csex'])
setNames = np.array(['cigar', 'dbrwt', 'dmage', 'monpre', 'mrace3', 'dmeduc', 'adequacy', 'drink', 'dmar', 'cntocpop', 'dfeduc', 'csex', 'birmon'])

stringInst = createString(setNames, dummies)
print(smf.ols(formula = stringInst, data=aSet).fit(cov_type='HC3').summary())

#Problem 2 part h
#Add in the bad control of gestation
dummies = np.array(['mrace3', 'adequacy', 'dmar', 'cntocpop', 'csex'])
setNames = np.array(['cigar', 'dbrwt', 'dmage', 'monpre', 'mrace3', 'dmeduc', 'adequacy', 'drink', 'dmar', 'cntocpop', 'dfeduc', 'csex', 'birmon', 'dgestat'])

stringInst = createString(setNames, dummies)
print(smf.ols(formula = stringInst, data=aSet).fit(cov_type='HC3').summary())
