astring = "Hello world!"
astring2 = 'Hello world!'
print("single quotes are ' '")

print(len(astring))
print(astring.index("o"))
print(astring.count("l"))
print(astring[3:7])
print(astring[3:7:2])
#same
print(astring[3:7])
print(astring[3:7:1])
#reverse
print(astring[::-1])

print(astring.upper())
print(astring.lower())

print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")