import pandas as pd
import numpy as np
from scipy import stats
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LassoCV, RidgeCV, Lasso, Ridge
from sklearn.model_selection import train_test_split
import pickle
from sklearn.pipeline import Pipeline


df_data = pd.read_csv('./data/df18to21_cleanedH.csv')

# df_data = df_data.drop(columns=['Unnamed: 0','Unnamed: 0.3','Unnamed: 0.2','Unnamed: 0.1',])

X = df_data.drop(columns=['sentence_length','guideline_range','guideline_var_pct','region','white'])
y = df_data['sentence_length']


numeric = ['count_convictons','age']
categorical = ['year_sentenced','dependents','race','disposition','citizen', 'state','criminal_hist', 'drug_type','weapon','gender','crime_type','case_type','presentence_stat','sentence_type','college','imprisoned']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42)

ctx = ColumnTransformer(
    [('ss',StandardScaler(),numeric),
     ('ohe',OneHotEncoder(handle_unknown='ignore'),\
     categorical)],
     verbose_feature_names_out=False,
     remainder = 'passthrough'
)

lasso_pipe = Pipeline(
    [
    ('ct',ctx),
    ('lasso',Lasso(alpha=.001,random_state=42,max_iter=10000))
    ]
)


lasso_pipe.fit(X_train,y_train)
print(lasso_pipe.score(X_train,y_train)), print(lasso_pipe.score(X_test,y_test))

print('works')

with open("./data/saved_lasso_sent_model.pkl", "wb") as file:
    pickle.dump(lasso_pipe, file)