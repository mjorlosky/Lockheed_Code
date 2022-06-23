# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3] for all objects
mylist = [1,2,3]
print("A list: %s" % mylist)

# %s string and obj, %d ints %f floats, %.<#ofdigits>f
# %x/%X hex

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%.2f"

print(format_string % data)