import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

data = pd.read_csv('./SleepNoIndex.csv')
# Checking if python is correctly reading the cvs file
row, column = data.shape
print(row, column)

variables = {"Number_of_days_drinks", "Income", "Weight", "Age", "Gender", "Race", "Asthma", "CHD_or_MI", "Exercise",
             "Mental_health_bad", "Physical_health_bad", "Smoker", "Cancer", "Diabetes", "Kidney", "Depressive",
             "Stroke", "Sleep", "Bronchitis","Married"}


df = data.copy()

print(df.columns)

cols = ['Number_of_days_drinks', 'Weight', 'Gender', 'Asthma', 'CHD_or_MI','Exercise','Smoker', 'Cancer', 'Diabetes',
 'Kidney', 'Depressive', 'Stroke' ,'Sleep' ,'Bronchitis','Income', 'Race', 'Age']


X_Sleep = df['Sleep']
X_Sleep = sm.add_constant(X_Sleep)

X = df[cols]
X = sm.add_constant(X)

Y_Physical = df['Physical_health_bad']
Y_Mental = df['Mental_health_bad']

print(sm.OLS(Y_Physical, X_Sleep).fit(cov_type='HC3').summary())
print(sm.OLS(Y_Mental, X_Sleep).fit(cov_type='HC3').summary())

print(sm.OLS(Y_Physical, X).fit(cov_type='HC3').summary())
print(sm.OLS(Y_Mental, X).fit(cov_type='HC3').summary())

import seaborn as sb
from matplotlib import pyplot as plt
plt.xlim([-2, 30])
plt.ylim([-2, 35])
sb.regplot(x = "Sleep", y = "Physical_health_bad", data = df, truncate=False, x_jitter=0.15, y_jitter=0.15, scatter_kws={"color": "green", "s": 10, "marker": ".", 'alpha':1/25}, line_kws={"color": "red"})
plt.xlabel('Hours of Sleep')
plt.ylabel('Number of Days Physical Health Bad')
plt.title('Number of Days Physical Health Bad vs Hours of Sleep')
plt.show()

plt.xlim([-2, 30])
plt.ylim([-2, 35])
sb.regplot(x = "Sleep", y = "Mental_health_bad", data = df, truncate=False, x_jitter=0.15, y_jitter=0.15, scatter_kws={"color": "orange", "s": 10, "marker": ".",'alpha':1/25}, line_kws={"color": "blue"})
plt.xlabel('Hours of Sleep')
plt.ylabel('Number of Days Mental Health Bad')
plt.title('Number of Days Mental Health Bad vs Hours of Sleep')
plt.show()

ax = df.hist(column='Sleep', bins=24, grid=False, color='#86bf91', zorder=2, rwidth=0.9)

ax = ax[0]
for x in ax:

    # Despine
    x.spines['right'].set_visible(False)
    x.spines['top'].set_visible(False)
    x.spines['left'].set_visible(False)

    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    # Remove title
    x.set_title("Hours of Sleep from Brfss 2018 Survey Data")

    # Set x-axis label
    x.set_xlabel("Hours of Sleep", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    x.set_ylabel("Counts", labelpad=20, weight='bold', size=12)

    # Format y-axis label
    x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

plt.xlim([-1, 25])
plt.show()


ax = df.hist(column='Physical_health_bad', bins=30, grid=False, color='gold', zorder=2, rwidth=0.9)

ax = ax[0]
for x in ax:

    # Despine
    x.spines['right'].set_visible(False)
    x.spines['top'].set_visible(False)
    x.spines['left'].set_visible(False)

    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    # Remove title
    x.set_title("Number of days Physical Health Bad from Brfss 2018 Survey Data")

    # Set x-axis label
    x.set_xlabel("Number of days Physical Health Bad", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    x.set_ylabel("Counts", labelpad=20, weight='bold', size=12)

    # Format y-axis label
    x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

plt.xlim([-1, 31])
plt.show()


ax = df.hist(column='Mental_health_bad', bins=30, grid=False, color='#FFA07A', zorder=2, rwidth=0.9)

ax = ax[0]
for x in ax:

    # Despine
    x.spines['right'].set_visible(False)
    x.spines['top'].set_visible(False)
    x.spines['left'].set_visible(False)

    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    # Remove title
    x.set_title("Number of days Mental Health Bad from Brfss 2018 Survey Data")

    # Set x-axis label
    x.set_xlabel("Number of days Mental Health Bad", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    x.set_ylabel("Counts", labelpad=20, weight='bold', size=12)

    # Format y-axis label
    x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

plt.xlim([-1, 31])
plt.show()


ax = df.hist(column='Age_cat', bins=13, grid=False, color='lightblue', zorder=2, rwidth=0.9)

ax = ax[0]
for x in ax:

    # Despine
    x.spines['right'].set_visible(False)
    x.spines['top'].set_visible(False)
    x.spines['left'].set_visible(False)

    # Switch off ticks
    x.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

    # Draw horizontal axis lines
    vals = x.get_yticks()
    for tick in vals:
        x.axhline(y=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    # Remove title
    x.set_title("Categorical Age of People from Brfss 2018 Survey Data")

    # Set x-axis label
    x.set_xlabel("Categorical Age", labelpad=20, weight='bold', size=12)

    # Set y-axis label
    x.set_ylabel("Counts", labelpad=20, weight='bold', size=12)

    # Format y-axis label
    x.yaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

plt.xlim([1, 13])
plt.show()