"""

bell shaped, mean median mode all are at center of distribution shape has no skewness.
bell shaped equals unimodal with single mode in middle.

mean sensitive to outliners always unlike median mode.
this implies the z-score will negatice if lies before the mean
and z-score will be positive if it lies after the mean.

coefficient of skewness
= Sk = 3 (ų - md) / б

Sk > 0 posirice skew
Sk < 0 neg skew
Sk = 0 No Skeq

for skeness mean median and std
"""
import numpy as np
from scipy import stats
import numpy

data = np.array([1,2,3,4,5,6,8,9,100])

sk = round(stats.skew(data), 2)
print(sk)

