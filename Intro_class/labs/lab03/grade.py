num=float(input("Your Result here:"))
if num <=100 and num >=90:
    print("A+")
elif num <90 and num >=85:
    print("A")
elif num <85 and num >=80:
    print("A-")
elif num <80 and num >=75:
    print("B+")
elif num <75 and num >=70:
    print("B")
elif num <70 and num >=65:
    print("B-")
elif num <65 and num >=60:
    print("C+")
elif num <60 and num >=50:
    print("C")
elif num <50 and num >=45:
    print("C-")
elif num <45 and num >=40:
    print("D")
elif num <40 and num >=30:
    print("FX")
elif num <30 and num >=0:
    print("F")
else:
    print("Please enter correct Value")
