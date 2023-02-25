    # change type from str to num

sval = '123'
type = (sval) #this print <class 'str'>

ival = int(sval)
type = (sval) #this print <class 'int'>

print('\n',ival + 1)

print('\n------------------------------\n')

    # take input from the user

name = input('who are you?\n')

print('\nwelcome,', name)

print('\n------------------------------\n')

    # small elevator program

oneOr_zero = input('Floor in Us, are in Europe press 1\n')
floor = input('Europe Floor is\n')

if oneOr_zero == '1' :
    print('\nUS Floor is', int(floor) + 1)
else :
    print('\nUS Floor is', int(floor))

print('\n------------------------------\n')

    # Try and Except

astr = 'Hello'
try:
    istr = int(astr)
except:
    istr = -1
print('\nFirst', istr)

astr = '123'
try:
    istr = int(astr)
except:
    ister = -1
print('\nSecond', istr)

print('\n------------------------------\n')

    # Try and except number chacher

snumber = input('Enter a number\n')

try:
    inumber = int(snumber)
except:
    print('\nNot a number')

print('\nYou enterd', snumber)

print('\n------------------------------\n')

    #