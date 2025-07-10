def divide(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("division by zero is not possible")
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
divide(a,b)