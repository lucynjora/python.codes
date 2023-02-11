#program to pay bonus to an employee
salary=int(input("enter the amount of salary"))
year_of_service=int(input("enyer the years of service"))
if(year_of_service>10):
    bonus_amount=salary+(0.1*salary)
    print("the bonus amout is",bonus_amount)
elif (year_of_service>=6 and year_of_service<=10):
    bonus_amount=salary+(0.08*salary)
    print("the bonus amount is",bonus_amount)
else:
    bonus_amount=salary+(0.05*salary)
    print("the bonus amount is",bonus_amount)
    