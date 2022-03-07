def FullTime():
    return 8

def PartTime():
    return 4

def Absent():
    return 0

def Check_attendence():
    import random
    number = random.randint(0, 2)
    switcher = {
        0: Absent,
        1: FullTime,
        2: PartTime,
    }
    return switcher.get(number)

def TotalMonthWage():
    EMP_RATE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    empHrs = 0
    empWage = 0
    totalEmpWage = 0
    day = 0
    while day<NUM_OF_WORKING_DAYS:
    # Get the option from switcher dictionary
        option = Check_attendence()
        empWage=option()*EMP_RATE_PER_HOUR
        totalEmpWage += empWage
        day+=1
    #print employee wage
    print("Total Employee Wage : ",totalEmpWage)

#Calling function to print result
if TotalMonthWage()=='TotalMonthWage()':
    print(TotalMonthWage())
