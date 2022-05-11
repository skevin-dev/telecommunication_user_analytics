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