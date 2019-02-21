import requests
import datetime
from datetime import timedelta
from dateutil import relativedelta

startDate = datetime.date(2013, 10, 1)
print(startDate)

endDate = startDate + timedelta(days=29)
print(endDate)

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

with open("C:/Users/venka/source/repos/Deep-Portfolio/makeDataset/scrapify/instruments.txt") as f:
    content = f.readlines()
# content = ["256265,"]     NIFTY 50 symbol
while endDate < datetime.date.today():
    for i in content:
        la = i.split(",")
        instrument = la[0]
        print("Trying " + str(startDate) + " " + la[1][:-1])
        stra = "https://kitecharts.zerodha.com/api/chart/"+str(instrument)+"/day?public_token=" \
                                                                           "J1gWZ4LxjyUhjMGq0yFOz8zFRT6tNxBR" \
                                                                           "&user_id=DP4281" \
                                                                           "&api_key=kitefront&access_token=" \
                                                                           "u91oReV1lEwkEkMVpfOWMrKkvGkBGMvP&" \
                                                                           "from="+str(startDate) + \
               "&to="+str(endDate) + \
               "&ciqrandom=1548865012154"

        res = requests.get(stra)

        if len(res.text) > 50:
            with open("../RAWDAY/"+instrument+"-"+str(startDate), "w+") as fil:
                fil.write(res.text)
            print("Done")

    startDate = endDate + timedelta(days=1)
    endDate = startDate + timedelta(days=29)
