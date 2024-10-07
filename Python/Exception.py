try:
    num = int(input("Enter numerator"))
    denom = int(input("Enter Denominator"))

    result = num / denom
    
    #result = 10 / 0
    #result = 10 / 5
    print(result)

except ZeroDivisionError as e :
    print(f"Error message  : {e}")

