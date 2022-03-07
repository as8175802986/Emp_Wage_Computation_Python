def Attendence():
    import random
    number = random.randint(0,1)
    if number == 1:
        print("Employee is present")
    else:
        print("Employee is absent")
#Calling function to print result
Attendence()