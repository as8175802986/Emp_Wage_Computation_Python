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
def totalWageandHrs():
    EMP_RATE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    MAX_HRS_IN_MONTH = 100
    totalEmpHrs = 0
    totalWorkingDays = 0
    totalEmpWage=0
    empWage = 0
    while totalEmpHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:
            totalWorkingDays+=1
            option = Check_attendence()
            totalEmpHrs=totalEmpHrs+option()
            empWage=option()*EMP_RATE_PER_HOUR
            #Incrementing and storing the values in total emp wage
            totalEmpWage += empWage
    print("Total Employee Hours : ",totalEmpHrs)
    print("Total Employee Wage : ",totalEmpWage)

if totalWageandHrs()=='totalWageandHrs()':
    print(totalWageandHrs())
