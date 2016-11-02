#!/usr/bin/encv python
f = open('test.txt')
content = f.read()
print (content)

if content.isdigit(): 
    print ("true")
else:
    print ("False")

lines = content.splitlines()
for line in lines:
    test = line.replace(".", "")
#    test = test.replace(",", "")
    if test.isdigit():
        print line
    else:
        print ("false")

print ("done")
