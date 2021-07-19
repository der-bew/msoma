import random as rd

#dice1=rd.randint(1,6) print(f"your dice is {dice1}")

while True:
    x=[1,2,3,4,5,6]
    print(rd.choice(x))
    
    res=input("please enter 0 to stop: \n")
    res=res.lower()
    if (res==0):
        break
    
