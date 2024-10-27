# SELF IS SAME AS THIS[ LIKE IN JAVA]

# OOPS

class Bird:
    species = 'WARM_BLOODED'
   
    def __init__(self, name="BirdName", age=00):
        self.name = name
        self.age = age

    def __str__(self):
        return f"somethiong"
        

    def printMethod(self):
        print(self.age)
        print(self.name)

   

a = Bird("Pikachu", 29)
b = Bird("Parrot", 22)
c = Bird()
print()
c.printMethod()
print()
print(a)
a.printMethod()
print(b)
print()
print("Species is : {Bird.__class__.species}")
print(f"Spexies is :{Bird.species}")
print("Species is : {}".format(a.__class__.species))
print("Species is : {}".format(a.species))
print("name",a.name)

#print(Bird.name) attributes  with class
# a.name arguements with objects 
# a.printMethod() methods with objects
# __str__ need of str when want to print readable object



