#Addition is lists

number=list()
while True:
    int=input('Enter number: ')
    if int=='done':
        break
    ninp=float(int)
    number.append(ninp)

avg=sum(number)/len(number)
print(f'Your average is: {avg}')

#EX_06_05
# text = "X-DSPAM-Confidence:  0.8475"
# appos=text.find(':')
# flpos=text[appos+2:]
# print(float(flpos))

#print day from mbox-short.txt
# fname=input('Enter file name: ')
# fopen=open(fname)
# for line in fopen:
#     if not line.startswith("From "):
#         continue
#     nline=line.split()
#     print(nline[2])

#Autograder 8.4
# my_list = []
# fhand = open('romeo.txt')
# for line in fhand:
#     words = line.split()                # Splits line into array of words
#     for word in words:
#         if word in my_list:
#             continue                    # Discards duplicates
#         my_list.append(word)            # Updates the list
# print(sorted(my_list))                  # Alphabetical order

#Autograder 8.5
# fhand = open('mbox-short.txt')
# count = 0
# for line in fhand:
#     words = line.split()
#     if len(words) < 3 or words[0] != 'From':
#         continue
#     print(words[1])
#     count =count+ 1
# print(f'There were {count} lines in the file with From as the first word')



