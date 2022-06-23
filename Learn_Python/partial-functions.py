from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))

# Exercise
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function

edit = partial(func,5,4,3)
print(edit(6))

# Code introspection examples
# help()
# dir() 
# hasattr() 
# id() 
# type() 
# repr() 
# callable() 
# issubclass() 
# isinstance() 
# __doc__ 
# __name__