# driver script for the project
from autoEncoder.autoEncoder import AutoEncoder
import pickle

# get the most recent data for all the instruments
with open('./makeDataset/processedData/CompanyWiseDict.pkl','rb') as fil:
	company_wise_dict = pickle.load(fil)
# vectorize the data
to_cluster = dict()

for instrument in company_wise_dict.keys():
	to_cluster[instrument] = AutoEncoder.get_vectors(company_wise_dict[instrument][-20:])

# get the clusters

# get the instrument with the best Sharpe ratio for each cluster  

# save the portfolio