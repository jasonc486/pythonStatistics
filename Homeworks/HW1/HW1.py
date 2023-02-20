import numpy as np
import pandas as pd
import math as math
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sn
import scipy.stats as stats

def main():
    #Question 1 part A
    #I am on a Unix-like system hence importing with ./
    df = pd.read_csv('./layoffs.csv')
    #We want to only look at the statistics for variable layoffs
    layoffs = df["layoffs"]
    
    #Lists and prints all the statistics for layoffs
    print(layoffs.describe())
    
    #Question 1 part B
    #Do a T-test to check if null hypothesis for
    #the mean will be rejected or not rejected
    hypothetical_mean = 240

    #This is a one sample T-Test, takes input of the layoffs and guess mean
    #nan_policy omit is required because dataset has several blanks
    t_stat, p_val = stats.ttest_1samp(layoffs, popmean=hypothetical_mean, 
                                    nan_policy='omit', alternative='two-sided')
    print("t-stat: ", t_stat,"p value: ", p_val)

    #Question 1 part C
    #Split Dataframe into the three years
    df_list = [d for _, d in df.groupby(['notice_year'])]

    #Print the statistics for each year
    for i in range (0,3):
        print("202{0}: \n".format(i), df_list[i]['layoffs'].describe(), '\n')

    #Question 2 part A
    #Import the other Dataset
    peopleData = pd.read_csv('Wooldrridge smoking data.csv')
    
    #Print out the relevant Statistics
    #educ, age, income, cigs, cigpric
    print(peopleData[['educ','age', 'income', 'cigs', 'cigpric']].describe())

    #Question 2 part B
    #Count number of smokers
    numSmokers = len(peopleData[peopleData['cigs'] > 0])
    #Count number of total people
    totalPeople = len(peopleData.index)
    #Divide smokers by total people to find ratio smokers
    percentSmokers = numSmokers / totalPeople * 100
    print("\nPercent Smokers: ", percentSmokers, '%\n')

    #Question 2 part C
    #Create dataframes of smokers and nonsmokers
    smokerList = peopleData[peopleData['cigs'] > 0]
    nonSmokerList = peopleData[peopleData['cigs'] == 0]
    #Summarize Data of both
    print("Smokers' Data: \n", smokerList[['educ','age', 'income', 
        'cigs', 'cigpric']].describe())
    print("Non-Smokers' Data: \n", nonSmokerList[['educ','age', 'income', 
        'cigs', 'cigpric']].describe())
    #Question 2 part D
    #Manually calculate ttest 2 samples
    meanEduSmoker = smokerList['educ'].mean()
    meanEduNonSmoker = nonSmokerList['educ'].mean()
    nSmoker = len(smokerList)
    nNonSmoker = len(nonSmokerList)
    stdevEduSmoker = smokerList['educ'].std()
    stdevEduNonSmoker = nonSmokerList['educ'].std()
    tSmoke = (meanEduSmoker - meanEduNonSmoker) / np.sqrt(stdevEduSmoker ** 2 / nSmoker + 
            stdevEduNonSmoker ** 2 / nNonSmoker)
    print("T-stat value:", tSmoke)
    #We want to verify with the scipy 2 sample TStat
    tstat, pval = stats.ttest_ind(smokerList['educ'], nonSmokerList['educ'],
            axis=0, equal_var=True, nan_policy='omit', alternative='two-sided')
    print("Scipy Tstat 2 sample:", tstat, "Pval:", pval)
    
    #Question 2 part E
    #Count the number of white/nonwhite smokers
    whiteSmokerList = smokerList[smokerList['white'] == 1]
    nonWhiteSmokerList = smokerList[smokerList['white'] == 0]
    #Pun intended
    whiteList = peopleData[peopleData['white'] == 1]
    nonWhiteList = peopleData[peopleData['white'] == 0] 
    #Calculate ratio smokers for white and non white
    whiteRatioSmoke = len(whiteSmokerList) / len(whiteList) * 100
    nonWhiteRatioSmoke = len(nonWhiteSmokerList) / len(nonWhiteList) * 100
    #Print the ratios
    print('\n')
    print('Percent white smoking: ', whiteRatioSmoke, '%\n',
            'Percent non-white smoking: ', nonWhiteRatioSmoke, '%', sep='')
    
    #Question 2 part F
    #Do a linear regression on the income vs cigs
    m, Xcept, rVal, pVal, stdErr = stats.linregress(peopleData['income'],
            peopleData['cigs'])
    #Generate best fit line
    y_line = Xcept + m * peopleData['income']
    #Report the values of slope, intercept, and R
    print(f'The parameters of the line: m=',m,
    'intercept=', Xcept, 'R Value=', rVal, '\n')
    #Create the plots
    plt.figure()
    plt.scatter(peopleData['income'], peopleData['cigs'])
    plt.plot(peopleData['income'], y_line, 'r')
    plt.title(f'Cigs Smoked vs. Income')
    plt.xlabel('income')
    plt.ylabel('cigs smoked')

    #Question 2 part G
    #Create new plot
    plt.figure()
    #Do a linear regression on the cigprice vs cigs
    plt.scatter(peopleData['cigpric'], peopleData['cigs'])
    m, Xcept, rVal, pVal, stdErr = stats.linregress(peopleData['cigpric'],
            peopleData['cigs'])
    #Generate best fit line
    y_line = Xcept + m * peopleData['cigpric']
    print(f'The parameters of the line: m=',m,
            'intercept=', Xcept, 'R Value=', rVal, '\n')
    #Create the plots
    plt.plot(peopleData['cigpric'], y_line, 'r')
    plt.title(f'Cigs Smoked vs. Cig Price')
    plt.xlabel('cig price')
    plt.ylabel('cigs smoked')
    plt.show()

if __name__=="__main__":
    main()
