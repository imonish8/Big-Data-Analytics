import scipy.stats as stat
import numpy as np
import  pandas as pd

running_time = [12.5, 11.8, 13.0, 12.3, 14.1, 12.9, 11.5, 13.3, 12.2, 11.9,
14.5, 15.0, 13.8, 12.8, 11.7, 12.6, 13.1, 12.4, 14.0, 15.2,
11.6, 13.5, 12.1, 14.2, 15.5, 12.0, 13.9, 12.7, 11.4, 14.3,
11.3, 15.3, 12.5, 14.6, 13.6, 11.2, 11.8, 14.7, 13.4, 15.1
]

def quartileMeasures(list):
    times_series = pd.Series(list)
    Q1 = times_series.quantile(0.25)
    Q2 = times_series.quantile(0.50)
    Q3 = times_series.quantile(0.70)

    ranges = {
        "Q1 range (<= Q1)": times_series[times_series <= Q1],
        "Q1-Q2 range (> Q1 and <= Q2)": times_series[(times_series > Q1) & (times_series <= Q2)],
        "Q2-Q3 range (> Q2 and <= Q3)": times_series[(times_series > Q2) & (times_series <= Q3)],
        "Above Q3 (> Q3)": times_series[times_series > Q3]
    }

    for range_key, range_data in ranges.items():
        num_athelets = range_data.count()
        avg_ = range_data.mean()
        print(f"{range_key}")
        print(f"{num_athelets}")
        print(f"{avg_}")

quartileMeasures(running_time)


