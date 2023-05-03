import urllib.request, urllib.parse, urllib.error

inp = input('\nplease enter a full url\n') # you can enter http://data.pr4e.org/romeo.txt to retreave a data and heshamorabi.comto retreve the html for my portofolio

fHand = urllib.request.urlopen(inp) # here we requst the html page we can also requst a page content

for line in fHand:
    print(line.decode().strip())

