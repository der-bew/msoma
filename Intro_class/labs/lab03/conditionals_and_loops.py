#python prime number
for x in range(1, 20+1):
    if x > 1:
        for i in range(2,x):
            if (x%i==0):
                break
        else:
            print(x)