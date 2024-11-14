import numpy as np
import pandas as pd


def classMeasures(data_list, colname="Class Scores"):
    df = pd.DataFrame(data_list, columns=[colname])

    mean_ = df[colname].mean()
    median_ = df[colname].median()
    mode_ = df[colname].mode()

    print(f"\nStudent' score  average in the Class is: {mean_:.2f}")
    print(f"Typically Student get this score: {median_:.2f}")

    if len(mode_) > 1:
        print(f"Most student scored this much: {mode_.values}")
    else:
        print(f"This is common score among student: {mode_[0]:.2f}")


dataGen = np.random.normal(loc=99, scale=5, size=10000)
classMeasures(dataGen)
