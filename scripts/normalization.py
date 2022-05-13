from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler

class normalize_data():
    def __init__(self,df):
        self.df = df
        
    def normalizer(self,df):
        norm = Normalizer()
        normalized_data = norm.fit_transform(df)
        return normalized_data

    def standardizer(self,df):
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(df)
        return scaled_data
