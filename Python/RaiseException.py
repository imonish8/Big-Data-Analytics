try:
    a = int(input("Enter a positive number : "))

    if( a < 0):
            raise ValueError("Negative numbers are not allowed")
    result = 10 / a
    print(f"Result : {result}")
except ValueError as e :
    print(f"Error message  prints here :  {e}")
    
