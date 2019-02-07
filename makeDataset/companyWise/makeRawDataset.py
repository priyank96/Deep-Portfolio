import glob
import json
import ciso8601
import time
import pickle

with open("C:\\Users\\Admin\\Documents\\Stuff\\makeDataset\\scrapify\\instruments") as f:
    instruments = f.readlines()
instruments = [x.split(",")[0] for x in instruments]

final_dict = dict()
for instrument_name in instruments:
    data = []
    files = glob.glob("../RAW/*" + instrument_name + "*")
    for fil in files:
        with open(fil, 'r') as f:
            parsed_json = json.loads(f.read())
            if parsed_json['status'] == 'success':
                for row in parsed_json['data']['candles']:
                    entry = [time.mktime(ciso8601.parse_datetime(row[0]).timetuple())]
                    entry.extend([float(x) for x in row[1:]])
                    data.append(entry)
    final_dict[instrument_name] = sorted(data, key=lambda x: x[0])

with open("CompanyWiseDict.pkl", 'wb') as f:
    pickle.dump(final_dict, f)
print("done")
