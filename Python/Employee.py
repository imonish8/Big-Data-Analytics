# Encapsulation
#private 
class Employee:
    def __init__(self, ename, eage, esalary):
        self.ename = ename
        self.eage = eage
        self.__esalary = esalary

    def diwaliDhamaka(self):
        print("DiwaliDhamaka",self. __esalary+1000000)

    def Display(self):
        print(f"Name :{self.ename}, Age : {self.eage}, Salary : {self.__esalary}")


eobj = Employee("Novak", 34,3000000)
eobj.Display()
eobj.diwaliDhamaka()
print(eobj.ename)
print(eobj.eage)
eobj.__esalary


