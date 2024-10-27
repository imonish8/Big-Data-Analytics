def simpleCalc(num1,num2):
    def adding(num1,num2):
        return num1+num2
    def minus(num1,num2):
        return num1-num2
    def multiply(num1,num2):
        return num1*num2
    def divide(num1,num2):
        return num1/num2

    return adding(num1,num2), minus(num1,num2), multiply(num1,num2), divide(num1,num2)

res = simpleCalc(22,34)

print("Simple calc operation on ")
print(res)
