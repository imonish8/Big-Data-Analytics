def sgrade():
	
	n = int(input("How many Grades ?"))
	grades = []
	for i in range(0,n):
		element = input("Please enter the Grade : ")
		grades.append(element)
		
	print("Grades in String :",grades)
	print(type(grades[0]))
	try :
		grades_to_int = [int(num) for num in grades]
		print()
		print("Grades in INTEGER: ", grades_to_int)
		print(type(grades_to_int[0]))
		print()
	except Exception as e:
		print("Value entered cannot be converted ",e)
	
	

	
sgrade()
