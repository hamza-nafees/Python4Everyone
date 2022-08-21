#Syntax for Increment

# x=0
# while x < 10 :
#     print(x)
#     x = x + 1    #while loop require increment to reached desire value
# print('Blastoff!')
# print(x)

#Find the largest number
# largest = None
#
# for num in  [12, 13, 96, 74, 25, 17, 28, 104]:
#    if largest is None:
#       largest = num
#       print(f'Largest so far {largest}')
#    elif num>largest:
#        largest=num
#        print(f'Largest so far {largest}')

#Smallest number
# smallest = None
#
# for number in [23,16,82,42,13,15,2]:
#     if smallest is None:
#         smallest=number
#     elif number<smallest:
#         smallest=number
#
# print(f'Smallest so far is {smallest}')

#Counting in loop
# count=0
# for thing in [50,100,175,250,300,225]:
#     count = count+1
#     print(count,thing)

#Counting in loop with average
# count=0
# sum = 0
# for number in [10, 20, 30, 40, 50, 60]:
#     sum = sum + number
#     count=count+1
#     print(count, sum)
# print(sum, sum/number)


#filtering in loop
# found = False
# print('Before', found)
# for things in [1, 2, 3, 4, 5, 6]:
#     if things%2==0:
#         found = True
#         print(found, things)
# print('After', found)

#Ex_05_01
# count = 0
# total = 0.0
# while True:
#
#     ival = input('Enter a value: ')
#     if ival == "done":
#         break
#     try:
#         fval = float(ival)
#     except:
#         print('Invalid number')
#         continue
#     count = count+1
#     total = total+fval
#
# print(count, total, total/count)

#Ex_05_02

# count=0
# while True:
#     val=input('Enter Value: ')
#     if val=='done':
#         break
#     try:
#        fval=float(val)
#     except:
#        print('Invalid input')
#     if count == 0:
#         min = fval
#         max = fval
#     elif fval < min:
#         min=fval
#     elif fval > max:
#         max=fval
#
#     count=count+1
#
# print('Maximum is',int(max))
# print('Minimum is',int(min))





