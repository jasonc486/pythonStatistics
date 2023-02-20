import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats
import matplotlib.pyplot as plt

risk_data_raw = pd.read_csv('./brfss2018.csv')
# Checking if python is correctly reading the cvs file
row, column = risk_data_raw.shape
print(row, column)

# Label: Days in past 30 had alcoholic beverage
# Question: During the past 30 days, how many days per week or per month did you have at least one drink of any
# alcoholic beverage such as beer, wine, a malt beverage or liquor?

risk_data_raw["alcday5"][(100 < risk_data_raw["alcday5"]) & (risk_data_raw["alcday5"] < 108)] = round(4.2857*(risk_data_raw["alcday5"] - 100))
risk_data_raw["alcday5"][(200 < risk_data_raw["alcday5"]) & (risk_data_raw["alcday5"] < 231)] = risk_data_raw["alcday5"] - 200

#risk_data_raw["alcday5"].loc[((100 < risk_data_raw["alcday5"]) & (risk_data_raw["alcday5"] < 108)),"alcday5"] = risk_data_raw["alcday5"]-100
#risk_data_raw["alcday5"].loc[((200 < risk_data_raw["alcday5"]) & (risk_data_raw["alcday5"] < 231)),"alcday5"] = risk_data_raw["alcday5"]-200
Number_of_days_drinks_raw = risk_data_raw["alcday5"]
drink_1 = Number_of_days_drinks_raw.replace(777,11111111)
drink_2 = drink_1.replace(999,11111111)
drink_3 = drink_2.fillna(11111111)
Number_of_days_drinks = drink_3.replace(888,0)

# Number_of_days_drinks_raw = risk_data_raw["avedrnk3"]
# drink_1 = Number_of_days_drinks_raw.replace(77,11111111)
# drink_2 = drink_1.replace(99,11111111)
# drink_3 = drink_2.fillna(11111111)
# Number_of_days_drinks = drink_3.replace(88,0)

# Label: Computed income categories
Income_raw = risk_data_raw["x.incomg"]
Income_1 = Income_raw.replace(9,11111111)
Income_2 = Income_1.replace([1,2,3,4],0)
Income= Income_2.replace(5,1)
# 0 -> Low Income; 1 -> High Income

# Label: Reported Weight in Pounds
risk_data_raw["weight2"][risk_data_raw["weight2"] > 700] = 11111111
Weight_raw = risk_data_raw["weight2"]
Weight = Weight_raw.fillna(11111111)


# Label: Reported age in five-year age categories calculated variable
Age_cat_raw = risk_data_raw["x.ageg5yr"]
Age_cat = Age_cat_raw.replace(14,11111111)

# Label: Reported age in two categories calculated variable (greater than 65 year old or not)
Age_raw = risk_data_raw["x.age65yr"] #_AGE65YR
Age_1 = Age_raw.replace(3,11111111)
Age_2 = Age_1.replace(1,0)
Age = Age_2.replace(2,1)
# 0 -> Not OLD; 1 -> OLD


# Label: Calculated sex variable
Gender_raw = risk_data_raw["sex1"]
Gender = Gender_raw.replace(2, 0)
# 0 -> Female; 1 -> Male

# Label: Computed race groups used for internet prevalence tables
Race_raw = risk_data_raw["x.raceg21"]
Race_1 = Race_raw.replace(2, 0)
Race_2 = Race_1.fillna(11111111)
Race = Race_2.replace(9,11111111)

# Label: Lifetime Asthma Calculated Variable
Asthma_raw = risk_data_raw["x.ltasth1"]
temp_asthma = Asthma_raw.replace(9,11111111)
Asthma = temp_asthma.replace(2, 0)
# 0 -> Didn't have Asthma; 1 -> Had Asthma

# Label: Ever had CHD or MI
# Question: Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI)
CHD_or_MI_raw = risk_data_raw["x.michd"]
temp_CHD_or_MI= CHD_or_MI_raw.fillna(11111111)
CHD_or_MI = temp_CHD_or_MI.replace(2, 0)
# 0 -> Didn't have CHD or MI; 1 -> Had CHD or MI

# Label: Leisure Time Physical Activity Calculated Variable
# Question: Adults who reported doing physical activity or exercise during the past 30 days
Exercise_raw = risk_data_raw["x.totinda"]
temp_exercise = Exercise_raw.replace(9,11111111)
Exercise = temp_exercise.replace(2, 0)
# 0 -> No physical activity 1 -> Had physical activity

# Label: Number of Days Mental Health Not Good
Mental_health_raw = risk_data_raw["menthlth"]
ment_1 = Mental_health_raw.replace(77,11111111)
ment_2 = ment_1.replace(99,11111111)
ment_3 = ment_2.fillna(11111111)
Mental_health_bad = ment_3.replace(88,0)
# 0 -> 0 days mental heath not good (mental health good)

# Label: Number of Days Physical Health Not Good
Physical_health_raw = risk_data_raw["physhlth"]
phys_1 = Physical_health_raw.replace(77,11111111)
phys_2 = phys_1.replace(99,11111111)
phys_3 = phys_2.fillna(11111111)
Physical_health_bad = phys_3.replace(88,0)
# 0 -> 0 days physical heath not good (physical health good)

# Label: Smoked at Least 100 Cigarettes
Smoker_raw = risk_data_raw["smoke100"]
smoke_1 = Smoker_raw.replace(7,11111111)
smoke_2 = smoke_1.replace(9,11111111)
smoke_3 = smoke_2.fillna(11111111)
Smoker = smoke_3.replace(2,0)
# 0 -> Non-smoker ; 1 -> Smoker

# Label: (Ever told) you had any types of cancer?
Cancer_raw = risk_data_raw["chcocncr"]
cancer_1 = Cancer_raw.replace(7,11111111)
cancer_2 = cancer_1.replace(9,11111111)
cancer_3 = cancer_2.fillna(11111111)
Cancer = cancer_3.replace(2,0)
# 0 -> Didn't have cancer ; 1 -> Had cancer

# Label: (Ever told) you had diabetes?
Diabetes_raw = risk_data_raw["diabete3"]
dia_1 = Diabetes_raw.replace(7,11111111)
dia_2 = dia_1.replace(9,11111111)
dia_3 = dia_2.fillna(11111111)
dia_4 = dia_3.replace(3,0)
dia_5 = dia_4.replace(4,0)
Diabetes = dia_5.replace(2,1)
# 0 -> Didn't have diabetes ; 1 -> Had diabetes

# Label: Ever told you have kidney disease?
Kidney_raw = risk_data_raw["chckdny1"]
kid_1 = Kidney_raw.replace(7,11111111)
kid_2 = kid_1.replace(9,11111111)
kid_3 = kid_2.fillna(11111111)
Kidney = kid_3.replace(2,0)
# 0 -> Didn't have kidney disease ; 1 -> Had kidney disease

# Label: (Ever told) you had a depressive disorder?
Depressive_raw = risk_data_raw["addepev2"]
dep_1 = Depressive_raw.replace(7,11111111)
dep_2 = dep_1.replace(9,11111111)
dep_3 = dep_2.fillna(11111111)
Depressive = dep_3.replace(2,0)
# 0 -> Didn't have any depressive disorder ; 1 -> Had depressive disorder

# Label: Ever Diagnosed with a Stroke
Stroke_raw = risk_data_raw["cvdstrk3"]
str_1 = Stroke_raw.replace(7,11111111)
str_2 = str_1.replace(9,11111111)
str_3 = str_2.fillna(11111111)
Stroke = str_3.replace(2,0)
# 0 -> Didn't have stroke ; 1 -> Had stroke

# Label: How Much Time Do You Sleep
Sleep_raw = risk_data_raw["sleptim1"]
sleep_1 = Sleep_raw.replace(77,11111111)
sleep_2 = sleep_1.replace(99,11111111)
Sleep = sleep_2.fillna(11111111)

# Label: (Ever told) (you had) chronic obstructive pulmonary disease, C.O.P.D., emphysema or chronic bronchitis? CHCCOPD2
Bronchitis_raw = risk_data_raw["chccopd1"]
bro_1 = Bronchitis_raw.replace(7,11111111)
bro_2 = bro_1.replace(9,11111111)
bro_3 = bro_2.fillna(11111111)
Bronchitis = bro_3.replace(2,0)
# 0 -> Didn't have bronchitis ; 1 -> Had bronchitis

# Label: Marital Status
Married_raw = risk_data_raw["marital"]
mar_1 = Married_raw.replace([2,3,4,5,6,9],0)
Married = mar_1.fillna(11111111)
# 0 -> Not married ; 1 -> Married

# Determine the indices of the missing observations of the variables we plan to use
index_Number_of_days_drinks = Number_of_days_drinks[(Number_of_days_drinks == 11111111)].index
index_Income = Income[(Income == 11111111)].index
index_Weight = Weight[(Weight == 11111111)].index
index_Age = Age[(Age == 11111111)].index
index_Age_cat = Age_cat[(Age_cat == 11111111)].index
index_Gender = Gender[(Gender == 11111111)].index
index_Race = Race[(Race == 11111111)].index
index_Asthma = Asthma[(Asthma == 11111111)].index
index_CHD_or_MI = CHD_or_MI[(CHD_or_MI == 11111111)].index
index_Exercise = Exercise[(Exercise == 11111111)].index
index_Mental_health_bad = Mental_health_bad[(Mental_health_bad == 11111111)].index
index_Physical_health_bad = Physical_health_bad[(Physical_health_bad == 11111111)].index
index_Smoker = Smoker[(Smoker == 11111111)].index
index_Cancer = Cancer[(Cancer == 11111111)].index
index_Diabetes = Diabetes[(Diabetes == 11111111)].index
index_Kidney = Kidney[(Kidney == 11111111)].index
index_Depressive = Depressive[(Depressive == 11111111)].index
index_Stroke = Stroke [(Stroke == 11111111)].index
index_Sleep = Sleep[(Sleep == 11111111)].index
index_Bronchitis = Bronchitis[(Bronchitis == 11111111)].index
index_Married = Married[(Married == 11111111)].index

# Determine the union of the indices of the missing observations
index_unknown = index_Number_of_days_drinks.union(index_Income)
index_unknown = index_Weight.union(index_unknown)
index_unknown = index_Age.union(index_unknown)
index_unknown = index_Age_cat.union(index_unknown)
index_unknown = index_Gender.union(index_unknown)
index_unknown = index_Race.union(index_unknown)
index_unknown = index_Asthma.union(index_unknown)
index_unknown = index_CHD_or_MI.union(index_unknown)
index_unknown = index_Exercise.union(index_unknown)
index_unknown = index_Mental_health_bad.union(index_unknown)
index_unknown = index_Physical_health_bad.union(index_unknown)
index_unknown = index_Smoker.union(index_unknown)
index_unknown = index_Cancer.union(index_unknown)
index_unknown = index_Diabetes.union(index_unknown)
index_unknown = index_Kidney.union(index_unknown)
index_unknown = index_Depressive.union(index_unknown)
index_unknown = index_Stroke.union(index_unknown)
index_unknown = index_Sleep.union(index_unknown)
index_unknown = index_Bronchitis.union(index_unknown)
index_unknown = index_Married.union(index_unknown)


# Drop the missing observations of the variables using the above indexes
Number_of_days_drinks.drop(index_unknown, inplace=True)
Income.drop(index_unknown, inplace=True)
Weight.drop(index_unknown, inplace=True)
Age.drop(index_unknown, inplace=True)
Age_cat.drop(index_unknown, inplace=True)
Gender.drop(index_unknown, inplace=True)
Race.drop(index_unknown, inplace=True)
Asthma.drop(index_unknown, inplace=True)
CHD_or_MI.drop(index_unknown, inplace=True)
Exercise.drop(index_unknown, inplace=True)
Mental_health_bad.drop(index_unknown, inplace=True)
Physical_health_bad.drop(index_unknown, inplace=True)
Smoker.drop(index_unknown, inplace=True)
Cancer.drop(index_unknown, inplace=True)
Diabetes.drop(index_unknown, inplace=True)
Kidney.drop(index_unknown, inplace=True)
Depressive.drop(index_unknown, inplace=True)
Stroke.drop(index_unknown, inplace=True)
Sleep.drop(index_unknown, inplace=True)
Bronchitis.drop(index_unknown, inplace=True)
Married.drop(index_unknown, inplace=True)

Database = pd.DataFrame({"Number_of_days_drinks": Number_of_days_drinks,
                         "Income": Income,
                         "Weight": Weight,
                         "Age": Age,
                         "Age_cat": Age_cat,
                         "Gender": Gender,
                         "Race": Race,
                         "Asthma": Asthma,
                         "CHD_or_MI": CHD_or_MI,
                         "Exercise":  Exercise,
                         "Mental_health_bad":  Mental_health_bad,
                         "Physical_health_bad": Physical_health_bad,
                         "Smoker": Smoker,
                         "Cancer":  Cancer,
                         "Diabetes": Diabetes,
                         "Kidney":  Kidney,
                         "Depressive": Depressive,
                         "Stroke":  Stroke,
                         "Sleep":   Sleep,
                         "Bronchitis": Bronchitis,
                         "Married": Married
                         })

# Checking if the cleaned data set is correctly created
row1, column1 = Database.shape
print(row1, column1)

Database.to_csv('Sleep.csv')
Database.to_csv('SleepNoIndex.csv', index=False)

print("\n=============================================================")
print(Database.iloc[: , 0:4].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n=============================================================")
print(Database.iloc[: , 4:8].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n==========================================================================")
print(Database.iloc[: , 8:12].describe().applymap('{:,.3f}'.format))
print("============================================================================\n")

print("\n=============================================================")
print(Database.iloc[: , 12:16].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n=================================================================")
print(Database.iloc[: , 16:22].describe().applymap('{:,.3f}'.format))
print("===================================================================\n")

Not_enough_sleep = Database.copy()
Not_enough_sleep.drop(Not_enough_sleep[Not_enough_sleep["Sleep"] > 7.022].index, inplace = True)

Enough_sleep = Database.copy()
Enough_sleep.drop(Enough_sleep[Enough_sleep["Sleep"] < 7.022].index, inplace = True)

print("\n=============================================================")
print("Summary Statistics for Not enough sleep")
print("=============================================================\n")

print("\n=============================================================")
print(Not_enough_sleep.iloc[: , 0:4].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n=============================================================")
print(Not_enough_sleep.iloc[: , 4:8].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n==========================================================================")
print(Not_enough_sleep.iloc[: , 8:12].describe().applymap('{:,.3f}'.format))
print("============================================================================\n")

print("\n=============================================================")
print(Not_enough_sleep.iloc[: , 12:16].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n=============================================================")
print(Not_enough_sleep.iloc[: , 16:20].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n=============================================================")
print("Summary Statistics for Enough sleep")
print("=============================================================\n")

print("\n=============================================================")
print(Enough_sleep.iloc[: , 0:4].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n=============================================================")
print(Enough_sleep.iloc[: , 4:8].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n==========================================================================")
print(Enough_sleep.iloc[: , 8:12].describe().applymap('{:,.3f}'.format))
print("==========================================================================\n")

print("\n=============================================================")
print(Enough_sleep.iloc[: , 12:16].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n=============================================================")
print(Enough_sleep.iloc[: , 16:20].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")


variables = {"Number_of_days_drinks", "Income", "Weight", "Age", "Gender", "Race", "Asthma", "CHD_or_MI", "Exercise",
             "Mental_health_bad", "Physical_health_bad", "Smoker", "Cancer", "Diabetes", "Kidney", "Depressive",
             "Stroke", "Bronchitis","Married"}

print("\n==============================================================================")
for i in variables:
    res = stats.ttest_ind(Not_enough_sleep[i], Enough_sleep[i], equal_var=True)
    print("Two-Sample T-test for variable " + i + ":")
    print(res)
    print("-----------------------------------------------------------------------------")
print("\n===============================================================================")

















