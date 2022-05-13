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
            
    def filling_missing(self,df):
        df_num = df.select_dtypes(include=["float","int"])
        normal_dist = []
        skewed = []
        for i in df_num.columns:
            if df_num[i].skew() < 0.5 and df_num[i].skew() > -0.5:
                normal_dist.append(i)
            else:
                skewed.append(i)
        for t in normal_dist:
            df[t].fillna(df[t].median(),inplace=True)
        for j in skewed:
            df[j].fillna(df[j].mean(),inplace=True)
        
        df_cat = df.select_dtypes(include=["object"])
        for n in df_cat.columns:
            df[n].fillna(df[n].mode()[0],inplace=True)
            
        df_date = df.select_dtypes(include=["datetime64[ns]"])
        for x in df_date.columns:
            df[x].ffill(axis=0,inplace=True)
            
    def check_outliers(self,df):
        numerical_columns = df.select_dtypes(include=["float","int"]).columns.tolist()
        for i in numerical_columns:
            sns.boxplot(data=df,x=df[i])
            plt.show()
            
    def fix_outliers(self,df,column):
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
    
        return df[column]