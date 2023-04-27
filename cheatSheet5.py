    # Make a Tuple

myTuple = () # defing an empty Tup or myTuple = (x, y, z, ...)

mySecTuple = ('x', 'y', 'z', 'T') # we cannot add things into tuples, things not to do in tuples(.sort, .append, .reverse), we can only use (.count, .index) files

print('\n', myTuple)
print('\n', mySecTuple)

print('\n------------------------------\n')

    # put tuple that can use var and assin val to that var

(x, y) = (4, 'fred')

print('\n', x, y)

print('\n------------------------------\n')

    # return tup from a dic

purse = dict() # defing a dic or purce = {}

purse ['money'] = 1 # put things into dic purse with key -refirce on how many of something in the dic-
purse ['candy'] = 2
purse ['tissues'] = 3

for k,v in purse.items():
    print('\n', k, v)

print('\n------------------------------\n')

    # show the tup output

tups = purse.items()
print(tups)

print('\n------------------------------\n')

    # Tuples are immutable; you can't change which variables they contain after construction. However, you can concatenate or slice them to form new tuples

a = (1, 2, 3)
b = a + (4, 5, 6)  
c = b[1:]  

print('\n', a, b, c)

print('\n------------------------------\n')

    # Ok how to sort a tup hmmmmm you can do a list of tup then sort them by key

nameOfDic = {} # same code to make a dic then fillit you can find it in cheetSheet4
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

tupOfNameOfDic = nameOfDic.items()

sortByKeyTupOfNameOfDic = sorted(tupOfNameOfDic)

print('\n', sortByKeyTupOfNameOfDic)

print('\n------------------------------\n')

    # ok how to sort by value. use data structure -list of tup where the value is first-

tmp = list()

for k,v in nameOfDic.items():
    tmp.append( (v, k) )

sortByValTupOfNameOfDic = sorted(tmp, reverse = True) # reverse is descending sort hight val first

print('\n', tmp)

print('\n------------------------------\n')

    # some short version of shorter

print( sorted( [ (v,k) for (k,v) in nameOfDic.items() ] ) ) # list comprehension creates a dynamis list, basically

print('\n------------------------------\n')

