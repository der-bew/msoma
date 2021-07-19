num=int(input("enter Second Number:"))
def factorial(x):
    factor = 1
    for i in range(1, x+1):
       factor = factor * i
    print (f"The factorial of the number is: {factor}") 
factorial(num)