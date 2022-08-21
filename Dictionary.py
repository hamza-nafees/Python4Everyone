                                       #01 Name frequency
count = dict()
names = ['hamza', 'haseeb', 'hassan', 'sarmad', 'hamza', 'hamza']
for name in names:
    count[name] = count.get(name, 0) + 1  #Idiom for counting names with get() method
print(count)


                                            # 02 Task
count=dict()
print('Enter your phrase for word count: ')
line=input('')
words=line.split()
# print('Words:',words)
for word in words:
    count[word]=count.get(word, 0) +1
print(count)

                                    #03 Reading file and count word frequency

counts=dict()
fname=open('romeo.txt')

for lines in fname:
    words=lines.split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
                                 #(contn.)countion most word out of text with frequency#
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)


                                             #04 Autograder Task 9.4

dictionary_addresses = dict()  # Initialize variables
maximum = 0
maximum_address = ''

fname = input('Enter file name: ')
try:
     fhand = open(fname)
except FileNotFoundError:
        print('File cannot be opened:', fname)
        quit()

for line in fhand:
    words = line.split()
    if len(words) < 2 or words[0] != 'From':
        continue

    if words[1] not in dictionary_addresses:
            dictionary_addresses[words[1]] = 1  # First entry
    else:
            dictionary_addresses[words[1]] += 1  # Additional counts

    for address in dictionary_addresses:
        if dictionary_addresses[address] > maximum:  # Checks if new maximum
            # Update the maximum if needed
            maximum = dictionary_addresses[address]
            # Stors the address of maximum
            maximum_address = address

print(maximum_address, maximum)

                                    #Word Counter and most occur word


fname= input('Open File: ')
fhandle=open(fname)
data=dict()

for lines in fhandle:
    lines.rstrip()
    nlines=lines.split()

    for word in nlines:
        #print(word)
        data[word]=data.get(word,0)+1

nullcount=-1
word_at_null=None

for k,v in data.items():
    if v>nullcount:
        nullcount=v
        word_at_null=k

print(f'Most repeated word: {word_at_null}, occurs {nullcount} times')


