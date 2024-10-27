try:
    a = int(input("enter denominator : "))
    result = 10 / a
    print(result)

except ValueError as e:
    print(f"ValueError : {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError : {e}")

