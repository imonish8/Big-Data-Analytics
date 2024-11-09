# yields info about relativenes of two variables/ columns
#corr_matrix

"""mdx

r = summation( (x - mean(x))(y - mean(y)) /
                    sqrt(summation((x - x)^2 summation((y - mean(y)^2))

r > 0 or tends to == positive relation
r < 0 or tends to == neg relation

corr is measure of degree if reltives variables.
it can help a buisness researcher determine eg., weather stock of airline rise and fall in any related manner.

several measures of corr :
1. Pearson product moment corr.
2.

term `r` is a measure of linear correlation of two variables.
$ its a number ranges -1,0,1
+1 --> perfect positive corr
-1 --> perfect negative corr between two.
0 --> no corr

# positive corr.
 both moves in same directions.
 both increase or both decrease.

# neg corr
 both move in diff bidirections
 one decrease other increase.

# zero corr = no corr
 skip no comments.

"""
import pandas as pd

data = {'Hours' :[1,2,3,4,5,6,7], 'Score' :[50,50,60,60,70,80,90]}

df = pd.DataFrame(data)
print(df)

correlation = df['Hours'].corr(df['Score'])
print(round(correlation, 2))
if correlation > 0:
    print("Positive corr both moves in same direction")
elif correlation < 0:
    print("Neg")
else:
    print("No Comments")


