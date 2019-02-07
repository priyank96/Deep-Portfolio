import pickle
import pprint
with open("NormalisedCompanyWiseDict.pkl", 'rb') as f:
    vals = pickle.load(f)

for i in vals.keys():
    pprint.pprint(vals[i][:10])
