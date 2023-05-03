import sys

try:
    iHand = input('\ninput name File.txt you want to read\n') # Taking input from the user
    fHand = open(iHand,'r') # open() fun makes you read the file fir atr is the file name s is to r "read"
except:
    print('\nwrong file name or directory\n')
    sys.exit(1) # or we can use quit() fun

count = 0

for line in fHand: # Loops until found \n
    print(line) #  Print lines in file
    count += 1 #  number of lines in file

print('\nNumber of lines in file is:', count)

print('\n------------------------------\n')

try:
    fIHand = input('\ninput name File.txt you want to read\n') # Taking input from the user
    sfHand = open(fIHand,'r') # open() fun makes you read the file first atr is the file name secont is to r "read"
except:
    print('\nwrong file name or directory\n')
    sys.exit(1)

inpFToStr = sfHand.read() #read the Hole file and but it into a str 

print('\n')
print(inpFToStr) # Print Str
print('\n', len(inpFToStr)) # Print num of char in string

print('\n------------------------------\n')

try:
    supStrFinal = int(input('\ninput sup string num from 0 to x\n')) # Taking input from the user final of sup string
except:
    print('enter num')
    sys.exit(1)
print('\n')
print(inpFToStr [:supStrFinal])

print('\n------------------------------\n')

try:
    fSeInHand = input('\ninput name File.txt you want to serch in:\n') # Taking input from the user
    seFHand = open(fSeInHand,'r') # open() fun makes you read the file, first atr is the file name. secont is to r "read".
except:
    print('\nwrong file name or directory\n') # if the name or dirictory is wrong "file not found"
    sys.exit(1) # exit

seWord = input('\nenter sersh word\n') # serch word
sCount = 0 # number of words we sershed in file

for line in seFHand: # normal serch by line
    for word in line.split(): # split() will splitt line to words and serch each word
        if word == seWord: # serching process by eatch word
            print('\n', line, '\n')
            sCount += 1

print('\n', sCount, '\n')

print('\n------------------------------\n')

try:
    speFHand = open(input('\ninput name File.txt you want to serch in:\n'), 'r') # Taking input and read file in one line
except:
    print('\nwrong file name or directory\n') # if the name or dirictory is wrong "file not found"
    sys.exit(1) # exit

stWith = input('\ninput start of a line:\n')

for line in speFHand:
    line = line.rstrip() # delete new line
    if line.startswith(stWith):
        print(line)

print('\n------------------------------\n')
