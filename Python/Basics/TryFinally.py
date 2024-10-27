def tryFinally(*args):
	
	try:

		listSQ = [num*num for num in args]
		print("Original List of number eneterd")
		for num in args:
			print(num," ")
		
		print(type(listSQ[0]))
		print(listSQ)

	finally :
		
		print("THis is Finally clause which will run only when program is excuted successfully ")
	

tryFinally(1,2,3,4,5,6,7,8,9)
	
		
