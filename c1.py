class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    #This function is used to add two numbers
    def addition(self,num1,num2):
        return num1 + num2
    # This function is used to subtract two numbers
    def subtraction(self,num1,num2):
        return num1 - num2
    # This function is used to multiply two numbers
    def multiplication(self,num1,num2):
        return num1 * num2
    # This function is used to divide two numbers
    def division(self,num1,num2):
        try:
            return num1/num2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
print("Addition","(",num1,"+",num2,"):" ,calculator(num1, num2).addition(num1,num2))
print("Subtraction","(",num1,"-",num2,"):",calculator(num1, num2).subtraction(num1,num2))
print("Multiplication","(",num1,"*",num2,"):",calculator(num1, num2).multiplication(num1,num2))
print("Division","(",num1,"/",num2,"):",calculator(num1, num2).division(num1,num2))