    # Lists exp

friends = ['Hoe', 'H', 'M', 'Lol']

for friend in friends:
    print('Hello', friend)

print('\n------------------------------\n')

    # Ok this is treaky so focus

names = [] # difine a list
try:
    numOfLists = int(input('\nplease input num of names in list\n')) # take input from the user "list size"
except:
    print('\nplese enter an int num\n')
    quit()
numOfNames = numOfLists # Make a variapleto work with if we ever needed the size 

while numOfNames > 0: # fill list
    name = input('\nplease inter a name\n')
    names.append(name) # append is a child of list responsable of filling list
    numOfNames -= 1

print(names) # normal print

print('\n------------------------------\n')

    # now we whant to make a list that has the age of every name in preavios list in the same ordar

ages = [] # define the list
count = -1 # variable we need in printing the two list try to understad the code 
numOfAges = numOfLists # see we needed the same variable of list size enterd pefore -we cannot make an age list begger than the name list-

try:
    for x in range (0, numOfAges): # fill list with for we can do it like before but i think this is a betterway
        print('\nplease inter a age of', names[x], ':') # print askingfor age of eatch name
        age = int(input()) # take the input
        ages.append(age) # append to list ages
        count += 1 # to count each name wit each age <-
except:
    print('\nplese enter an int num\n')
    quit() # we can import sys lip then use sys.exit(1) put i think tis better

while count >= 0: # again with a while loop to print the list
    print('\n', names[count], ages[count], '\n') # <-
    count -= 1 # decrimint the count

print('\n------------------------------\n')

    # len of list -how many iteam in the str-

print('lenght of names is', len(names))
print('lenght of ages is', len(ages)) # of course we enter that num and they poth equals but this is to unde stand the fun len

print('\n------------------------------\n')

    # create range list -we used tis before in filling a list above-

try:
    num = int(input('\nplease input num\n')) # take input from the user "to use in list size"
except:
    print('\nplese enter an int num\n')
    quit()

print(range(num)) # create a list with range to be used

print(range(len(names))) # take the length of names -you enter it before- then genrate a list with that range 'exp: if len = 3, the range = [0, 1, 2]'

print('\n------------------------------\n')

    # we can loop without knowing the postion and with knowing it

colors = ['red', 'green', 'blue']

for color in colors: # without knowing the postion
    print('color is:', color)

for i in range(len(colors)): # with knowing the postion
    color = colors[i]
    print('color is:', color)

print('\n------------------------------\n')

    # concatinating and slice

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

c = a + b

print(c) # output [1, 2, 3, 4, 5, 6, 7, 8]

print(c[2:5]) # output [3, 4, 5]

print('\n------------------------------\n')

    # list method oppend, count, extend, index, insert, pop, remove, reverse, sort

