import pandas as pd
from dtaidistance import dtw
import cProfile

data_frame = pd.read_pickle("../pandafy/data.pkl").head(60)
headings = list(data_frame)
query = data_frame[headings[0]].values
print(query.shape)


def test():
    results = data_frame.apply(lambda x: dtw.distance_fast(query, x.values))
    #print(results)
    return results.sort_values()


if __name__ == '__main__':
    print(test())
    # cProfile.run('test()')