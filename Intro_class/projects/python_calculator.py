def main():
    try:
        num1 =float(input("Please enter first number: "))
        num2 =float(input("Please enter second number: "))
        print("INSTRACTIONS".center(50, "="))
        print(""" Please=> 
              Enter 'a' for addition  
              Enter 's' for substraction 
              Enter 'm' for multiplication 
              Enter 'd' for division 
              Enter 'o' to stop the loop""")

        ch=input ("Please Enter char: ")
        while ch != 'o':
            if ch.lower() == 'a':
                addition(num1, num2)
            elif ch.lower() == 's':
                substraction(num1, num2)
            elif ch.lower() == 'm':
                multipilication(num1, num2)
            elif ch.lower() == 'd':
                division(num1, num2)
            elif ch.lower()=='o':
                break
            else:
                print ("please enter only the char mentioned")
            ch=input ("Please Enter char if u want to do another calculations: ") 
            ch=ch.lower()
            if ch == 'a' or ch == 's' or ch =='m' or ch=='d':
                num1 =float(input("Please enter first number: "))
                num2 =float(input("Please enter second number: "))
            elif ch=='o':
                break
            else:
               print ("please enter only the char mentioned") 
    except Exception as e:
        print ("Unknown Error",e)
def addition(x, y):
    result=x+y
    print (f"The sum of the numbers is: {result}")
def substraction(x,y):
    result=x-y
    print (f"The substraction of the numbers is: {result}")
def multipilication(x,y):
    result= x*y
    print (f"The Result of the numbers is: {result}")
def division(x,y):
    result= x/y
    print (f"The Result of the numbers is: {result}")
main()