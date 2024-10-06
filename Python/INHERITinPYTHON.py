#inheriantce in python

# PARENT
class StudentDB:
    def __init__(self, PRN, DOB):
        self.PRN = PRN
        self.DOB = DOB

    def DB(self):
        print("PR Number is : {self.PRN}, Date of Birth : {self.DOB}")
        

 # CHILD       
class Student(StudentDB):
    def __init__ (self, PRN, DOB, sname, sid):
        self.sid = sid
        self.sname = sname
        StudentDB.__init__(self, PRN, DOB)

    def Display(self):
        print(self.name, " ",self.sid)

    def StudentDetails(self):
        print(f"Name is :{self.name}")
        print(f"ID is :{self.sid}")

    def __str__(self):
        return f"Name is :{self.sname}, Student ID : {self.sid}, Date of Birth :{self.DOB}, PR Number :{self.PRN} "

# GRAND CHILD
class Player(Student):
    def __init__(self,PRN, DOB, sname, sid, sports):
        self.sports = sports
        StudentDB.__init__(self, PRN, DOB)
        Student.__init__(self,PRN, DOB, sid, sname)

    def PlayerDetails(self):
         print(f"Player ID is :{self.sid},  Name is :{self.sname}, Sport playing :{self.sports}, Date of Birth : {self.DOB}, PR number : {self.PRN}")

    def __str__(self):
         return f"Player ID is :{self.sid},  Name is :{self.sname}, Sport playing :{self.sports}, PR Number : {self.PRN}, DOB : {self.DOB}"
"""
print()
object1 = Student("Snape", 2)
print(object1)
print()
"""
objectChild = Player(10008,"2002/04/11","Tirth", 22, "Cricket")
print(objectChild)
print()
objectChild.PlayerDetails()
print()

