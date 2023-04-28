import re

    # Regular Expressions

txt = "The rain in Spain" # Search the string to see if it starts with "The" and ends with "Spain"

x = re.search("^The.*Spain$", txt) 

if x:
  print('\n', "YES! We have a match!")
else:
  print('\n', "No match")

print('\n------------------------------\n')

    # Print a list of all matches

txt = "The rain in Spain"

x = re.findall("ai", txt)

print(x) 

print('\n------------------------------\n')

    # Return an empty list if no match was found

txt = "The rain in Spain"

x = re.findall("Portugal", txt)

print(x) 

print('\n------------------------------\n')

    # Search for the first white-space character in the string

txt = "The rain in Spain"

x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

print('\n------------------------------\n')

    # Split at each white-space character

txt = "The rain in Spain"

x = re.split("\s", txt)

print(x) 

print('\n------------------------------\n')

    # Do a search that will return a Match Object

txt = "The rain in Spain"

x = re.search("ai", txt)

print(x) #this will print an object

print('\n------------------------------\n')

