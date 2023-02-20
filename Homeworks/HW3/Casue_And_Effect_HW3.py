# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv()



# part 1 of the problem set is showcased below. 
# For 1a, we need to clean up the data like removing values that have 999 to them, or no values given. 
print(np.round(data["dbrwt"].describe(), 2).T[['count','mean', 'std', 'min', 'max', '50%']])

data.drop(data[data["dbrwt"] > 9998].index, inplace = True)
data.drop(data[data["cigar"] > 1].index, inplace = True)
data.dropna(subset = ['cigar' , 'dbrwt' ], inplace = True)

print(np.round(data["dbrwt"].describe(), 2).T[['count','mean', 'std', 'min', 'max', '50%']])




# FOR ALL ThE COVARIATES (10 total for this study)
data.drop(data[data["cigar"] > 98].index, inplace = True)

data.drop(data[data["drink"] > 98].index, inplace = True)

data.drop(data[data["dbrwt"] > 9998].index, inplace = True)

data.drop(data[data["pldel3"] > 8].index, inplace = True)

data.drop(data[data["adequacy"] > 3].index, inplace = True)

data.drop(data[data["nlbnl"] > 98].index, inplace = True)

data.drop(data[data["dgestat"] > 98].index, inplace = True)

data.drop(data[data["anemia"] > 7].index, inplace = True)

data.drop(data[data["cardiac"] > 7].index, inplace = True)

data.drop(data[data["lung"] > 7].index, inplace = True)

data.drop(data[data["diabetes"] > 7].index, inplace = True)

data.drop(data[data["herpes"] > 7].index, inplace = True)







data.dropna(subset = ['cigar' , 'drink' , 'dbrwt' , 'pldel3' , 'dmage' , 'adequacy' , 'nlbnl', 'csex' , 'dgestat'], inplace = True)
data.dropna(subset = ['anemia' , 'cardiac' , 'lung' , 'diabetes' , 'herpes'], inplace = True)


print(np.round(data["dbrwt"].describe(), 2).T[['count','mean', 'std', 'min', 'max', '50%']])

X = data[['cigar' , 'drink' , 'pldel3' , 'dmage' , 'adequacy' , 'nlbnl', 'dgestat' , 'anemia' , 'cardiac' , 'lung' , 'diabetes' , 'herpes']]
Y = data['dbrwt']
X = sm.add_constant(X)
model = sm.OLS(Y, X).fit(cov_type = 'HC1')
print(model.summary())

