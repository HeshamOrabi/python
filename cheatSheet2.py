import sys # Lip to force exit

    # def is a reserved word to gen a Fun

def grt():
    name = input('\nPlease, enter your name\n')
    print('\nHi', name)

# calling the fun

grt()

print('\n------------------------------\n')

    # max fun

big = max('Hello world')
print(big)

print('\n', type(big)) # type fun

print('\n------------------------------\n')

    # same grt fun but with return

def grt():
    name = input('\nPlease, enter your name\n')
    return name

# calling the fun

print('\nHello,', grt())

print('\n------------------------------\n')

    # cal fun with arg and return

try:
    fNum = int(input('\nFirst num\n'))
    sNum = int(input('\nSecond num\n'))
except:
    print('\nplease enter a num\n')
    sys.exit(1)

op = input('\nplease, enter operation\n')

if op == '*' or op == '/' or op == '+' or op == '-':
    def cal(f, s, op):
        if op == '*':
            res = int(f) * int(s)
        elif op == '-':
            res = int(f) - int(s)
        elif op == '/':
            res = int(f) / int(s)
        elif op == '+':
            res = int(f) + int(s)
        return res

    # calling the fun

    print('\nresult is,', cal(fNum, sNum, op))

else:
    print('\nworng op')
    print('\n------------------------------\n')
    sys.exit(1)

print('\n------------------------------\n')

    # while loop

try:
    i = int(input('\nnum of iteration\n'))
except:
    print('\nplease enter a num\n')
    sys.exit(1)

if i > 0:
    while i > 0:
        print('\n', i)
        i -= 1 # decrimint i by 1
    print('\nnum is 0 now') 
else:
    print('\nnum is negative\n')


print('\n------------------------------\n')

    # break out of loop

while True:
    line = input('> ')
    if line == 'done':
        break
    else:
        print(line)
print('\nDone!\n')

print('\n------------------------------\n')

    # contuniue

while True: # <-
    line = input('> ')
    if line[0] == '#': #line [0] means the first char in str line
        continue # return to stat of the loop <-
    elif line == 'done':
        break
    else:
        print(line)
print('\nDone!\n')

print('\n------------------------------\n')

    # for loop

for i in [4, 2, 1, 3, 5]: # Define loop, for i equal 4, next iteration i equal 2 and so on
    print(i)
print('\nBlastoff!\n')

print('\n------------------------------\n')

    # for loop str

friends = ['joe', 'hesham', 'lily']

for friend in friends:
    print('\nHappy new year', friend)

print('\nDone!')

print('\n------------------------------\n')

    # loop ldioms

    # loop throught a set

friends = ['joe', 'hesham', 'lily']

for friend in friends:
    print('\nHappy new year', friend)

print('\nDone!')

print('\n------------------------------\n')

    # largest Number we can use None as we used it in smallest below

setOfNum = [3, 41, 12, 9, 74, 15]
largestSoFar = 0

print('\nbefore', largestSoFar)

for theNum in setOfNum: 
    if theNum > largestSoFar:
        largestSoFar = theNum
    print(largestSoFar, theNum)

print('\nafter', largestSoFar)

print('\n------------------------------\n')

    # number of things in a list

con = 0

print('\nbefore', con)

for thing in setOfNum:
    con += 1
    print(con, thing)

print('\nafter', con)

print('\n------------------------------\n')

    # sum of list

sum = 0

print('\nbefore', sum)

for thing in setOfNum:
    sum = sum + thing
    print(sum, thing)

print('\nafter', sum)

print('\n------------------------------\n')

    # avr of list

cont = 0
sumM = 0

print('\nbefore', cont, sumM)

for thing in setOfNum:
    cont += 1
    sumM = sumM + thing
    print(cont, sumM, thing)

avr = sumM / cont

print('\nafter', cont, sumM, avr)

print('\n------------------------------\n')

   # smallest Number with first list iteam

smallestSoFar = setOfNum[0]

print('\nbefore', smallestSoFar)

for theNum in setOfNum: 
    if theNum < smallestSoFar:
        smallestSoFar = theNum
    print(smallestSoFar, theNum)

print('\nafter', smallestSoFar)

print('\n------------------------------\n')

    # smallest Number with None 

smallest = None

print('\nbefore', smallest)

for theNum in setOfNum: 
    if smallest is None: # is is stronger than == it ask is this equals this in type and value
        smallest = theNum
    if theNum < smallest:
        smallest = theNum
    print(smallestSoFar, theNum)

print('\nafter', smallestSoFar)

print('\n------------------------------\n')

    # string length

Strgg = 'banana'
print(len(Strgg))

print('\n------------------------------\n')

    # loop throw str entered by the user while loop

someStr = input('\nenter str so i can loop throw\n')
i = 0

while i < len(someStr):
    print(i, someStr[i])
    i += 1

print('\n------------------------------\n')

    # loop throw str entered by the user while loop

i = -1

for iteam in someStr:
    i += 1
    print(i, iteam)

print('\n------------------------------\n')

    # count the number og chr you choose in string enterd before

lettr = input('\nplease enter a charcter you wont to serch for\n')
count = 0

if len(lettr) == 1:
    for iteam in someStr:
        if iteam == lettr:
            count += 1
else:
    print('more than 1 char')
    print('\n------------------------------\n')
    sys.exit(1)
    
print(count)

print('\n------------------------------\n')

    # slicing

try:
    sSlic = int(input('enter a start num to slice\n'))
    eSlic = int(input('enter a end num to slice\n'))
except:
    print('please enter a num')
    print('\n------------------------------\n')
    sys.exit(1)

if sSlic < eSlic:
    print(someStr[sSlic:eSlic])
else:
    print('enter a  start num and end num')
    print('\n------------------------------\n')
    sys.exit(1)

print('\n------------------------------\n')

    # string library

zap = someStr.lower() # convert str to lowercase
print(zap)

gre = input('\ninput string\n')
print(gre.lower())

print('\n------------------------------\n')

    # important, dir is to know the method in obj str

print(dir(someStr))

print('\n------------------------------\n')

    # 