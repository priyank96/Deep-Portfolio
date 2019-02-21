import pandas as pd

data_frame = pd.read_pickle("data_raw.pkl")
data_frame = (data_frame - data_frame.iloc[0]) /(data_frame.iloc[0])
# data_frame = data_frame.multiply(100)
print(data_frame.head())
pd.to_pickle(data_frame,"data.pkl")
