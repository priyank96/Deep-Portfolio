import pickle
import pprint
import os
with open(os.path.join(os.getcwd(),'processedData','NormalisedCompanyWiseDict.pkl'), 'rb') as f:
    vals = pickle.load(f)

for i in vals.keys():
    pprint.pprint(vals[i][:10])
