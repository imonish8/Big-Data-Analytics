#RETURN TYPE
def addTwoNum(x, y):
	return (x+y)

res = addTwoNum(1,55)
print()
print("sum of two nums is :",res)

# void function
def printMsg(msg):
                        """ Print MessageFunction """
                        print("Message is :"+msg)
                        return -1
print()
print(printMsg("Hello"))

#POSITIONAL ARGUMENTS

def printMsg(name, age):
	print("Name ",name)
	print("Age ",age)

print()
printMsg("Ayush", 22)
print("Krishna", 22)
print(33, "Ramesh")




#DEFAULT VALUES

print()
print("Default Values")
def multiply(a,b=50):
	return a*b

res1 = multiply(10)
print(res1)
res2 = multiply(20, 40)
print(res2)


# POISTIONAL ARGUMENTS

def printFullName(firstName, lastName):
	print("firstName", firstName, "lastName",lastName)

print()
printFullName(firstName ="Sunidhi", lastName = "DKDK")

# VARIABLE LENGTH ARGS *

def sumOfAll(*args):
	return sum(args)

print()
print("Sum of all Numbers ", sumOfAll(12,22,333,444,666,77))
print("Sum of All numbers ", sumOfAll(23,444,5678,88664455667575))


def myFun(**kwargs):
        """ hello world """
        for key, val in kwargs.items():
                	print("%s == %s" % (key, val))

myFun(first ="Python", second="Programming", third="Language", course ="Big Data Analytics")


def printm(msg):
        """ hello"""
        

print(printm.__doc__) # Message

print(myFun.__doc__) #Message


print(printMsg.__doc__) # None

# List Compreshsion

list_my = [x for x in range(1, 7)]
print(list_my)

for i in range(1, 7):
        if i%2==0:
                list_my.append(i)
                print(i)

print(list_my)


listCom = [ x for x in range(1, 7) if x%2==0]
print(listCom)

res5 = [x  for x in range(1, 10) for y in range(1, 10) if x>y]


print()
print()
print('LAMDA')

add = lambda x,y : x+y
print(add(4,5))

def evenNum(*args):
        evenNums = []
        for i in args:
                if i % 2 ==0:
                        evenNums.append(i)
        return evenNums

resEven = evenNum(1222,222,22222,45454646,6767676,676867,3435445,343434,2323)
print(resEven)
print()
# lambda
list1 = [22,343,2343,235674,2455,2234,2223562,5555,4444,654,4565423535]
res = list(filter(lambda x : x%2 ==0, list1))
print(res)
print()
# *args = list(int(input("Enter Numbers"
# resArgs = list(filter(lambda x : x%2 ==0, *args))


#print(resArgs)

list3 = [1, 2,3 ,4,88,22,922, 933]
sq_list = list(map(lambda x : x**2, list3))
print("Squared list", sq_list)
print()
def newFunction(num):
        if num % 2 ==0:
                return num * 2
 #       else:
       #         return num
        else:
                return False
        

# for i in range(1, 10) :
 #       res = list(map(newFunction, map(int, int(input("Enter a Number")))))
res = list(map(newFunction, list3))
print(res)
print()

# LAMBDA FUN IF ELSE
min1 = lambda x,y : x if(x<y) else y
print(min1(23,44))

print()
finding_min = lambda *args : [min(args)]
resFound = finding_min(1,3,4,53,3,45,3)
print(resFound)

print()
SQUARE_EACH = lambda *args : [x**2 for x in args]
resList = SQUARE_EACH(11,33,12,42,1,11)
print(resList)
#SCOPE IN FUNCTION / OUT-FUNCTION

print()
GLOBAL_VAR = 20

def fun1():
        return GLOBAL_VAR

def fun2():
        GLOBAL_VAR
        return GLOBAL_VAR

globalres = fun1()
globalres2 = fun2()
print(globalres)
print(globalres2)



#OUTER FUNCTION
x = 10
def outer_Fun():
        
        x = 19
        def inner_fn():
                nonlocal x
                x = 1900
                print("inner function :",x)

        inner_fn()
        print("Outer fn",x)

outer_Fun()

#REDUCE FUNCTION
from functools import reduce
list_fun = [123,444,623,578,335]
res = reduce(lambda x,y : x+y, list_fun)
print(res)




