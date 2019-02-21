import glob
import pandas as pd
import json
files = glob.glob("../RAWDAY/*")
data_frame = pd.DataFrame()
count = 0

fail_count = 0
for fil_name in files:
    with open(fil_name) as fil:
        unparsed_json = fil.read()
        parsed_json = json.loads(unparsed_json)
        if parsed_json['status'] == 'success':
            data_frame_column = []
            for row in parsed_json['data']['candles']:
                print(row[1])
                data_frame_column.append(row[1]) 
        try:
            series = pd.Series(data_frame_column)
            print(len(data_frame_column))
            data_frame[fil_name[7:]+"_"+str(count)] = series.values
        except:
            print("Incomplete series: "+fil_name, data_frame_column)
            fail_count += 1
        count += 1
        
print(data_frame.shape)
print("Incomplete Series:  ", fail_count)
data_frame.to_pickle("data_raw.pkl")
