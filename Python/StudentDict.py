def studentData(var, delRrd, modifyN):
	
	print(var)

	
	var[44] = "Monish"

	print("After adding a Name roll in dict", var)
	print()
	
	del var[delRrd]
	print("After deleting a record", var)
	print()
	
	var[modifyN] = "Akash"
	print()
	print("After modifying the Record", var)

	

print("Please enter  Names of the students")
n = int(input("Enter the number of students "))
sdata = {}

for i in range(1,n+1):
	name = input("Enter Student name")
	sdata[i] = name

print("Entered Dictionary is ")
print(sdata)

delRecord = int(input("Enter roll number to delete student record"))

modifyName = int(input("Enter Student no to modify name"))

studentData(sdata, delRecord, modifyName)
	
	
	
