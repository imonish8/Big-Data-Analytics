try:
    if(salary > 9999):
        print(salary)
except NameError as e:
    print(f"NameError message : {e}")
    

print()
print()
print()
print()

try:
    x=int(input("Enter a Numerator"))
    y=int(input("Enter Denominator"))
    z = x / y
    print(z)
except TypeError as e:
    print(f"Type Error occured message : {e}")
except NameError as e:
    print(f"NameError occured go back to src code : {e}")
except ZeroDivisionError as e:
    print(f"Message for Division : {e}")
except ValueError as e:
    print(f"Message for data type : {e}")
else:
    print(f"value of division : {z}")
finally:
    print("hello this block is finaly only executes when run success")

