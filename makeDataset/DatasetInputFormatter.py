import pickle
import os

with open(os.path.join(os.getcwd(), 'processedData', 'NormalisedCompanyWiseDict.pkl'), 'rb') as f:
    vals = pickle.load(f)  # dict

final_dataset = []  # will finally be n * 20 * 4 list

for i in vals.keys():
    for j in range(len(vals[i]) - 20):  # 20 because the CAE paper also used 20
        final_dataset.append(vals[i][j:j + 20])

print("n: ", len(final_dataset))
print("20: ", len(final_dataset[0]))
print("4: ", len(final_dataset[0][0]))

with open(os.path.join(os.getcwd(), 'FinalDataset.pkl'), 'wb') as f:
    pickle.dump(final_dataset, f)

print("done")
