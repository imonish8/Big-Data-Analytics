
def factorial(n):
    if(n == 1):
        return 1
    else:
        return n*factorial(n-1)

def main():
    print("Printing the Factorial from one to 10")

    for i in range(1,10):
        temp = factorial(i)
        print(i," ",temp)

    
if __name__ == "__main__":
    main()
