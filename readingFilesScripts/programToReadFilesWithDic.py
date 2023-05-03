try:
    name = input('\nenter a file\n')
    handle = open(name)
except:
    print('\nwrong file name or directory\n')
    quit()

counts = {}
bigword = None
bigcount = None

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1 # idiom for histogram, loop for word in words in line in file then if it there add 1 if ot make 0 and then add 1

for key,val in counts.items():
    if bigcount is None or val > bigcount:
        bigcount = val
        bigword = key

print('\nbiggest word counted:', bigword, '\nand the count is:', bigcount)

print('\n--------------------------------------------\n')
