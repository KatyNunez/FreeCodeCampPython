import urllib.request, urllib.parse,urllib.error
File=urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #encode automatically
for line in File:
    print(line.decode().strip())

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())