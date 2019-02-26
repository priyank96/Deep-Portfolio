# class to calculate sharpe ratio of a given time series of arbitrary length
import numpy as np
import math
class SharpeRatio:
    # note that to calculate sharpe ratio from t0 to tn, pass t-1 to tn
    def __init__(self):
        self.trading_days = 252 # no of trading days in a year
        self.risk_free_return_rate = 0.07 # 5 year india govt bond yield

    def ratio(self, series):
        # calculate daily returns
        daily_returns = []
        prev = series[0] # t-1
        for x in series[1:]:
            daily_returns.append(float(x/prev)-1)
            prev = x
        annualised_mean_returns = np.mean(daily_returns) * self.trading_days
        annualised_stddev = (np.std(daily_returns) * self.trading_days) ** 0.5
        if(annualised_stddev == 0):
            return math.inf * -1
        sharpe_ratio = (annualised_mean_returns - self.risk_free_return_rate) / annualised_stddev
        return sharpe_ratio


if __name__== "__main__":
    print("sharpe.py")
    print("Running Test#1 ")
    sharpe = SharpeRatio()
    a = [1,2,3,4,5]
    print(a, sharpe.ratio(a))

    a = [1,1,1,1,1,1]
    print(a, sharpe.ratio(a))

    a = [100, 105, 100, 110, 115, 112,116,120]
    print(a, sharpe.ratio(a))

    a = [100, 105, 108, 110, 115, 112,116,120]
    print(a, sharpe.ratio(a))