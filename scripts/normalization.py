from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MinMaxScaler

class normalize_data():
    
    def normalizer(df):
        norm = Normalizer()
        normalized_data = norm.fit_transform(df)
        return normalized_data

    def standardizer(df):
        scaler = MinMaxScaler()
        scaled_data = scaler.fit_transform(df)
        return scaled_data
