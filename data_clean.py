import pandas as pd 
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt 


class clean_data():
    def __init__(self,df):
        self.df = df
        
    def drop_high_nan_column(self,df):
        column_30percent = [i for i in df.columns if df[i].isnull().sum()*100/len(df) >= 30 ]
        df.drop(column_30percent,axis=1,inplace=True)
        
        return df 
    
    def percentage_missing(self,df):
        missings = df.isnull().sum()*100/len(df)
        
        return missings
    
    def normality_test (self,df):
        numerical_columns = df.select_dtypes(include=["float","int"]).columns.tolist()
        df_cols = df[numerical_columns]
        nan_columns = [i for i in df_cols.columns if df_cols[i].isna().sum() > 0]
        for i in nan_columns:
            sns.histplot(data=df_cols,x=df_cols[i],bins=25)
            plt.show()