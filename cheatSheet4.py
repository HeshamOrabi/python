    # Make a Dicrionarie

purse = dict() # defing a dic or purce = {}

purse ['money'] = 1 # put things into dic purse with key -refirce on how many of something in the dic-
purse ['candy'] = 2
purse ['tissues'] = 3

print('\n', purse)

print('\n------------------------------\n')

    # program to make a dic fill it then print it

nameOfDic = {}
try:
    numoFoThingsInDic = int(input('\nplease inter num of things in the dic\n'))
except:
    print('\nenter num\n')
    quit()

for iteam in range(0, numoFoThingsInDic):
    thingInDic = input('\nthing in dic\n')
    try:
        keyOfTheThing = int(input('\nkey is\n')) 
    except:
        print('\nenter num\n')
        quit()
    nameOfDic [thingInDic] = keyOfTheThing

print('\n', nameOfDic, '\n')

print('\n------------------------------\n')

    # search in dic -we can use the in operatour to search in loops-

searshInDic = input('search word in dic\n')

if searshInDic in nameOfDic:
    print('\nvaloue in', searshInDic, 'is', nameOfDic[searshInDic], '\n')
else:
    print('\nnot found\n')

print('\n------------------------------\n')

    # simplified counting with get() how many keies of a list put count in a dic

nameOfDicTwo = {}
lisOfWords = []
try:
    numoFoThingsInList = int(input('\nplease inter num of twords you whant to count in dic\n'))
except:
    print('\nenter num\n')
    quit()

for word in range(0, numoFoThingsInList):
    lisOfWords.append(input('enter the word'))

for word in lisOfWords:
    nameOfDicTwo[word] = nameOfDicTwo.get(word, 0) + 1

print(nameOfDicTwo)

print('\n------------------------------\n')

    # two iteration variables

for key,value in nameOfDic.items(): # iteams convert dic into tuple
    print(key, value)

print('\n------------------------------\n')
