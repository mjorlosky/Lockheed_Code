x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

# checks objects
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True # by value
print(x is y) # Prints out False # compares instances

print(not False) # Prints out True
print((not False) == (False)) # Prints out False