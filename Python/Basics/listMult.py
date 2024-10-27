m = int(input("please enter m for m x n of matrix 1     "))
n = int(input("Please enter n of m x n for matrix 1     "))
p = int(input("Please enter p of p x q for matrix 2     "))
q = int(input("please enter q of p x q for matrix 2     "))

print(m, " X  ",n," ","Dimensions of the first matrix")
print(p, " X ",q," ","Dimensions of the Second matrix")

print()
print()

matrix1  = []
matrix2 = []

print("Proceeding with Matrix 1")

for i  in range(0, m):
    temp = []
    for j in range(n):
        usr= int(input("Enter Input for Matrix 1        "))
        temp.append(usr)
    matrix1.append(temp)

        
print(matrix1)
print()
print("Proceed with Second Matrix")
for i in range(p):
    temp = []
    for j in range(q):
        usr = int(input("enter next value for matrix 2      "))
        temp.append(usr)
    matrix2.append(temp)
print()
print(matrix2)



result = []

for i in range(m):
    row = []
    for j in range(q):
        row.append(matrix1[i][j] * matrix2[i][j])
    result.append(row)

print(result)
