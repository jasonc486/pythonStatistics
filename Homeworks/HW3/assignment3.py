import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats
import matplotlib.pyplot as plt

birth_data_raw = pd.read_csv('./pennbirthwgt0.csv')

# Checking if python is correctly reading the cvs file
# row, column = birth_data_raw.shape
# print(row, column)

# Education of Mother
Education_raw = birth_data_raw["dmeduc"]
Education = Education_raw.replace(99, '.')

# Age of Mother
Age = birth_data_raw["dmage"]
# Age variable is clean (there are no unreasonable values)

# Race of Mother
Race = birth_data_raw["mrace3"]
# Race variable is clean (there are no unreasonable values)
# 1 -> White; 2 -> Other; 3 -> Black

# Marital Status of Mother
Marital_status_raw = birth_data_raw["dmar"]
Marital_status_1 = Marital_status_raw.replace(1, 1)
Marital_status = Marital_status_1.replace(2, 0)
# Marital status variable is clean (there are no unreasonable values)
# 0 -> Unmarried; 1 -> Married

# Birth Injury Evaluation accoring to 1-10 Scale
Apgar_score_raw = birth_data_raw["fmaps"]
Apgar_score = Apgar_score_raw.replace(99, '.')

# The Month at which the Parents Started Taking Care
Parent_care_raw = birth_data_raw["monpre"]
Parent_care = Parent_care_raw.replace(99, '.')

# Number of Weeks Mother was Pregnant
Gestation_raw = birth_data_raw["dgestat"]
Gestation = Gestation_raw.replace(99, '.')

# Gender of the Baby
Gender_raw = birth_data_raw["csex"]
Gender_1 = Gender_raw.replace(1, 1)
Gender = Gender_1.replace(2, 0)
# Gender variable is clean (there are no unreasonable values)
# 0 -> Female; 1 -> Male

# Number of Live Births Given by Mother (Now Living)
Live_birth_raw = birth_data_raw["nlbnl"]
Live_birth = Live_birth_raw.replace(99, '.')

# Single Birth/ Twin Birth/ Triplet Birth/ Quadruplet Birth/ Quintuplet Birth
Plurality = birth_data_raw["dplural"]
# Plurality variable is clean (there are no unreasonable values)

# If Mother has Diabetes or not
Diabetes_raw = birth_data_raw["diabetes"]
Diabetes_1 = Diabetes_raw.replace(1, 1)
Diabetes_2 = Diabetes_1.replace(2, 0)
Diabetes = Diabetes_2.replace(9, '.')
# 0 -> No Diabetes; 1 -> Diabetes

# If Mother has Hypertension or not
Hypertension_raw = birth_data_raw["phyper"]
Hypertension_1 = Hypertension_raw.replace(1, 1)
Hypertension_2 = Hypertension_1.replace(2, 0)
Hypertension = Hypertension_2.replace(9, '.')
# 1 -> NO Hypertension; 1 -> Hypertension


# Number of Cigarettes Mother Smoked Per Week Before Giving Birth
Num_cigars_raw = birth_data_raw["cigar"]
Num_cigars = Num_cigars_raw.replace(99, '.')

# Number of Alcoholic Drinks Mother Drank Per Week Before Giving Birth
Num_drinks_raw = birth_data_raw["drink"]
Num_drinks = Num_drinks_raw.replace(99, '.')

# Weight of the Baby
Birth_weight_raw = birth_data_raw["dbrwt"]
Birth_weight = Birth_weight_raw.replace(9999, '.')

# Determine the indices of the missing observations of the variables I plan to use
index_Education = Education[(Education == '.')].index
index_Apgar_score = Apgar_score[(Apgar_score == '.')].index
index_Parent_Care = Parent_care[(Parent_care == '.')].index
index_Gestation = Gestation[(Gestation == '.')].index
index_Live_birth = Live_birth[(Live_birth == '.')].index
index_Diabetes = Diabetes[(Diabetes == '.')].index
index_Hypertension = Hypertension[(Hypertension == '.')].index
index_Num_cigars = Num_cigars[(Num_cigars == '.')].index
index_Num_drinks = Num_drinks[(Num_drinks == '.')].index
index_Birth_weight = Birth_weight[(Birth_weight == '.')].index

# Determine the union of the indices of the missing observations
index_unknown = index_Education.union(index_Apgar_score)
index_unknown = index_Parent_Care.union(index_unknown)
index_unknown = index_Gestation.union(index_unknown)
index_unknown = index_Live_birth.union(index_unknown)
index_unknown = index_Diabetes.union(index_unknown)
index_unknown = index_Hypertension.union(index_unknown)
index_unknown = index_Num_cigars.union(index_unknown)
index_unknown = index_Num_drinks.union(index_unknown)
index_unknown = index_Birth_weight.union(index_unknown)

# Drop the missing observations of the variables using the above indices
Education.drop(index_unknown, inplace=True)
Age.drop(index_unknown, inplace=True)
Race.drop(index_unknown, inplace=True)
Marital_status.drop(index_unknown, inplace=True)
Apgar_score.drop(index_unknown, inplace=True)
Parent_care.drop(index_unknown, inplace=True)
Gestation.drop(index_unknown, inplace=True)
Gender.drop(index_unknown, inplace=True)
Live_birth.drop(index_unknown, inplace=True)
Plurality.drop(index_unknown, inplace=True)
Diabetes.drop(index_unknown, inplace=True)
Hypertension.drop(index_unknown, inplace=True)
Num_cigars.drop(index_unknown, inplace=True)
Num_drinks.drop(index_unknown, inplace=True)
Birth_weight.drop(index_unknown, inplace=True)

Database = pd.DataFrame({"Education": pd.to_numeric(Education), "Age": Age, "Race": Race, "Marital_Status": Marital_status,
                         "Apgar_Score": pd.to_numeric(Apgar_score), "Parental_Care_Month": pd.to_numeric(Parent_care),
                        "Gestation": pd.to_numeric(Gestation), "Gender": Gender, "Number_Live_Birth": pd.to_numeric(Live_birth),
                         "Plurality": Plurality, "Diabetes": pd.to_numeric(Diabetes), "Hypertension": pd.to_numeric(Hypertension),
                         "Number_of_Cigarettes": pd.to_numeric(Num_cigars), "Number_of_Drinks": pd.to_numeric(Num_drinks),
                         "Birth_Weight": pd.to_numeric(Birth_weight)})
print("\n=============================================================")
print(Database.iloc[: , 0:4].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n==================================================================")
print(Database.iloc[: ,4:8].describe().applymap('{:,.3f}'.format))
print("==================================================================\n")

print("\n================================================================")
print(Database.iloc[: ,8:12].describe().applymap('{:,.3f}'.format))
print("================================================================\n")

print("\n==========================================================")
print(Database.iloc[: ,12:15].describe().applymap('{:,.3f}'.format))
print("==========================================================\n")

# Separate the data set into two parts (Nonsmoking Mothers and Smoking Mothers)
Nonsmoker = Database.copy()
Nonsmoker.drop(Nonsmoker[Nonsmoker["Number_of_Cigarettes"] != 0].index, inplace = True)

Smoker = Database.copy()
Smoker.drop(Smoker[Smoker["Number_of_Cigarettes"] == 0].index, inplace = True)

print("\n=============================================================")
print(Nonsmoker.iloc[: , 0:4].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n==================================================================")
print(Nonsmoker.iloc[: ,4:8].describe().applymap('{:,.3f}'.format))
print("==================================================================\n")

print("\n================================================================")
print(Nonsmoker.iloc[: ,8:12].describe().applymap('{:,.3f}'.format))
print("================================================================\n")

print("\n==========================================================")
print(Nonsmoker.iloc[: ,12:15].describe().applymap('{:,.3f}'.format))
print("==========================================================\n")

print("\n=============================================================")
print(Smoker.iloc[: , 0:4].describe().applymap('{:,.3f}'.format))
print("=============================================================\n")

print("\n==================================================================")
print(Smoker.iloc[: ,4:8].describe().applymap('{:,.3f}'.format))
print("==================================================================\n")

print("\n================================================================")
print(Smoker.iloc[: ,8:12].describe().applymap('{:,.3f}'.format))
print("================================================================\n")

print("\n==========================================================")
print(Smoker.iloc[: ,12:15].describe().applymap('{:,.3f}'.format))
print("==========================================================\n")


variables = {"Education", "Age", "Race", "Marital_Status", "Apgar_Score", "Parental_Care_Month", "Gestation", "Gender",
             "Number_Live_Birth", "Plurality", "Diabetes", "Hypertension",  "Number_of_Cigarettes", "Number_of_Drinks",
             "Birth_Weight"}

print("\n==============================================================================")
for i in variables:
    res = stats.ttest_ind(Nonsmoker[i], Smoker[i], equal_var=True)
    print("Two-Sample T-test for variable " + i + ":")
    print(res)
    print("-----------------------------------------------------------------------------")
print("\n===============================================================================")

print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Database).fit(cov_type='HC1').summary())
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes + Number_of_Drinks + Education + Age "
                        "+ Race + Marital_Status + Apgar_Score + Parental_Care_Month + Gender "
                        "+ Number_Live_Birth + Plurality + Diabetes + Hypertension ", data=Database).fit(cov_type='HC1').summary())


Female = Database.copy()
Female.drop(Female[Female["Gender"] == 1].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Female).fit(cov_type='HC1').summary())

Male = Database.copy()
Male.drop(Male[Male["Gender"] == 0].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Male).fit(cov_type='HC1').summary())

Married = Database.copy()
Married.drop(Married[Married["Marital_Status"] == 0].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Married).fit(cov_type='HC1').summary())

Unmarried = Database.copy()
Unmarried.drop(Unmarried[Unmarried["Marital_Status"] == 1].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Unmarried).fit(cov_type='HC1').summary())

Yes_Diabetes = Database.copy()
Yes_Diabetes.drop(Yes_Diabetes[Yes_Diabetes["Diabetes"] == 0].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Yes_Diabetes).fit(cov_type='HC1').summary())

No_Diabetes = Database.copy()
No_Diabetes.drop(No_Diabetes[No_Diabetes["Diabetes"] == 1].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=No_Diabetes).fit(cov_type='HC1').summary())

Care = Database.copy()
Care.drop(Care[Care["Parental_Care_Month"] < 5.0].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Care).fit(cov_type='HC1').summary())

No_Care = Database.copy()
No_Care.drop(No_Care[No_Care["Parental_Care_Month"] > 4.0].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=No_Care).fit(cov_type='HC1').summary())

Yes_Gestation = Database.copy()
Yes_Gestation.drop(Yes_Gestation[Yes_Gestation["Gestation"] < 24.0].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Yes_Gestation).fit(cov_type='HC1').summary())

No_Gestation = Database.copy()
No_Gestation.drop(No_Gestation[No_Gestation["Gestation"] > 23.0].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=No_Gestation).fit(cov_type='HC1').summary())

Alcoholic = Database.copy()
Alcoholic.drop(Alcoholic[Alcoholic["Number_of_Drinks"] == 0].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Alcoholic).fit(cov_type='HC1').summary())

Nonalcoholic = Database.copy()
Nonalcoholic.drop(Nonalcoholic[Nonalcoholic["Number_of_Drinks"] != 0].index, inplace = True)
print(smf.ols(formula = "Birth_Weight ~ Number_of_Cigarettes", data=Nonalcoholic).fit(cov_type='HC1').summary())
