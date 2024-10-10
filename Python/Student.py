class Student:
	marks = {}
	def __init__(self,rollno, sname, coursename):
		self.rollno = rollno
		self.sname = sname
		self.coursename = coursename
		#self.maths.marks = maths.marks
		#self.chem.marks = chem.marks
		#self.phy.marks = phy.marks

	def __str__(self):
		#return f"Student INFO , RollNo : {self.rollno}, Name : {self.sname}, Course Name : "{self.coursename}, Maths : {self.maths.marks}, Chemistry : {self.chem.marks}, Physics : {self.phy.marks}"
		return f"Student Name : {self.sname}, Student Roll : {self.rollno}, Student Course : {self.coursename}"
	
	
	def inputMarks(self):
		print("Enter the number of Subjects ")
		n = int(input("Enter number")
		for mark in range(n):
			key = input("Enter subject name")
			value = int(input("



s1 = Student(22, "Raj", "DBDA")

		
	
