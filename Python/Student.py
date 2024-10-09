class Student:
	
	#subs = { "Maths" : "{maths.marks}", "Chemistry" : "{chem.marks}", "Physic" : "{phy.marks}"}

	#def __init__(self, rollno, sname, coursename, maths.marks, chem.marks, phy.marks):
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


s1 = Student(22, "Raj", "DBDA")
print(s1)
		
	
