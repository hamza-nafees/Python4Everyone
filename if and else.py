#1  Operators
# x=int (input("Enter a number of your choice : "))
# if x>=10:
#     if x>10:
#         print('Number is greater than 10')
#     elif x==10:
#          print('Number equals to 10')
# else:
#     print("Number is smaler than 10")

#2 Take two numbers from users and compare them
# x=int(input('Enter a number N1 : '))
# y=int(input('Enter a number N2 : '))
#
# if x>y:
#     print('N1 is greater than N2')
# elif x==y:
#     print('N1 is equals to N2')
# else:
#     print('N1 is less than N2')

#3 Calculating Bonus of employees

# x=int(input('Enter the number of service years : '))
#
# if x>=5:
#     print('You are ELIGIBLE for bonus!')
#     y=int(input('Enter your Salary : '))
#     z=y*(5/100)
#     t=y+z
#     print(f'Your Bonus Salary is {t}, Congratulations!')
#
#
# else :
#     print('You are NOT Eligible for bonus')


# Give employes 1.5 times more salary when hrs > 40
try:

    work_hour=int(input('Enter the number of hours of work : '))
    hour_rate=int(input('Enter wage rate per hour : '))
except:
     print('Enetr Correct Numeric Value!')
     quit()

if work_hour > 40:

   bonus_hour = work_hour-40
   bonus_hour_rate = bonus_hour*(hour_rate*1.5)
   salary = bonus_hour_rate+(40*hour_rate)
   print(f'Congratulations! Your salary is {salary}')

elif work_hour < 40:
    sal2 = work_hour*hour_rate
    print(f'Sorry you are INELIGIBLE for bonus, your pay is {sal2}')
