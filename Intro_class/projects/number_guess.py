import random as rd

secrate_no=rd.randint(1,99)
print("I am thinking of a number between 1 and 99...")
guess=int(input("Enter a guess:  "))
while (secrate_no != guess):
    if (guess > secrate_no):
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    guess=int(input("Please Enter a new guess:  "))
    
print(f"Congrats, the number was {secrate_no}")
        
        
