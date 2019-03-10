"""keeps price history for timestamps which occur in all time series,
assumes the input dict is already sorted by time """
import pickle
from itertools import filterfalse

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

print("data points: ", len(values_set))


# keep only these timestamp values in each list now


def filter(element):
    return element[0] in values_set


for key in keys:
    print(key)
    if len(company_wise_dict[key]) > 0:
        company_wise_dict[key] = filterfalse(filter, company_wise_dict[key])

with open('./processedData/BackTestDict.pkl', 'wb') as fil:
    pickle.dump(company_wise_dict, fil)

print('done')
