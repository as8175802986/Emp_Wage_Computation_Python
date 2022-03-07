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
def total1():
    EMP_RATE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    MAX_HRS_IN_MONTH = 100
    totalEmpHrs = 0
    totalWorkingDays = 0
    totalEmpWage = 0
    empWage = []
    while totalEmpHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:

        option = Check_attendence()
        totalEmpHrs = totalEmpHrs + option()
        empWage.append(option() * EMP_RATE_PER_HOUR )
        #print("Daily wage : ", empWage[totalWorkingDays])
        totalWorkingDays += 1

    print(empWage)
    print("Total Employee Hours : ", totalEmpHrs)
    print("Total Employee Wage : ", sum(empWage))

def total2():
    EMP_RATE_PER_HOUR = 20
    NUM_OF_WORKING_DAYS = 20
    MAX_HRS_IN_MONTH = 100
    totalEmpHrs = 0
    totalWorkingDays = 0
    totalEmpWage = 0
    empWage = []
    while totalEmpHrs <= MAX_HRS_IN_MONTH and totalWorkingDays < NUM_OF_WORKING_DAYS:

        option = Check_attendence()
        totalEmpHrs = totalEmpHrs + option()
        empWage.append(option() * EMP_RATE_PER_HOUR )
        #print("Daily wage : ", empWage[totalWorkingDays])
        totalWorkingDays += 1

    print(empWage)
    print("Total Employee Hours : ", totalEmpHrs)
    print("Total Employee Wage : ", sum(empWage))

def Check_Company():
    import random
    number = random.randint(0, 1)
    if number == 1 :
     print("Bridgelabz")
     print(total1())

    else:
     print("Wtvision")
     print(total2())


if Check_Company()== 'Check_Company()':
    Check_Company()



