
import numpy as np
import pandas as pd

def central_tendency_measures(data_list, colname="House Price"):
    df = pd.DataFrame(data_list, columns=[colname])

    mean_ = df[colname].mean()
    median_ = df[colname].median()
    mode_ = df[colname].mode()

    print(f"\nHouse price average in the locality per sqft is: {mean_:.2f}")
    print(f"House price people are paying typically per sqft is: {median_:.2f}")

    
    if len(mode_) > 1:
        print(f"House price most people are paying is (multiple modes): {mode_.values}")
    else:
        print(f"House price most people are paying is: {mode_[0]:.2f}")


data = np.random.normal(loc=1000, scale=20, size=10000)
central_tendency_measures(data)

