# encapsulation protected

class Company:
    def __init__(self):
        self.__project = "Cloud Project"

class Employee(Company):
    def __init__(self, ename):
        self.ename = ename
        Company.__init__(self)

    def Display(self):
        print("Employee name ",self.ename)
        print("Project name :", self.__project)


empCom = Employee("Shreya")
empCom.Display()
print(empCom.__project)
