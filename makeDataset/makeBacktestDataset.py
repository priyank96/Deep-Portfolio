import pickle

with open('./processedData/CompanyWiseDict.pkl', 'rb') as fil:
    company_wise_dict = pickle.load(fil)

# find the list of timestamps in all files
keys = company_wise_dict.keys()
values_set = None
for key in keys:
    if len(company_wise_dict[key]) > 0:
        timestamps = set(list([x[0] for x in company_wise_dict[key]]))
        if values_set is None:
            values_set = timestamps
        else:
            values_set = values_set.intersection(timestamps)

print(len(values_set))

# now make a dataframe with
