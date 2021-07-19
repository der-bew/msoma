print ("please enter -1 to stop the loop")
res=float(input("Enter Numbers: "))
count=0
sum=0
while res !=1:
    sum +=res
    count +=1
    res=float(input("Enter Numbers: ")) 
    if res==-1:
        break
print(f"The sum of the numbers: {sum}")
avr=sum/count
print (f"Avarage: {avr}")
