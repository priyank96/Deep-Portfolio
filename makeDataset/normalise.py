# Don't know how to normalize volume data so leaving it as it is for now
# 0th position is time stamp leaving that untouched
import pickle
    
symbols = []


# todo doing this to remove timestamp and volume, remove this function if you want it back later
def remove_volume_and_time(series):
    for entry in series:
        del (entry[0])  # time
        del (entry[-1])  # volume


def normalize(series):
    for i in range(len(series) - 2, -1, -1):
        for j in range(1, len(series[i]) - 1):  # not changing time stamp and volume
            series[i + 1][j] = float("{0:.4f}".format((series[i + 1][j] - series[i][j]) / series[i][j]))*100
    for j in range(1, 5):
        series[0][j] = float(0)


with open("./processedData/CompanyWiseDict.pkl", 'rb') as f:
    companyDict = pickle.load(f)

for symbol in companyDict.keys():
    if len(companyDict[symbol]) > 0:
        normalize(companyDict[symbol])
        remove_volume_and_time(companyDict[symbol])

with open("./processedData/NormalisedCompanyWiseDict.pkl", 'wb') as f:
    pickle.dump(companyDict, f)

print("done")
