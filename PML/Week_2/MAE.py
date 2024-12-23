actual = [2,3,5,5,9]

calculated = [3,3,8,7,6]

n = 5
sum = 0

for i in range(n):
    sum += abs(actual[i] - calculated[i])
    error = sum / n
    print("Mean absolute error  : "+str(error))
