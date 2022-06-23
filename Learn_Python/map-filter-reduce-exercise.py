#### Map
from functools import reduce 

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

# Use map to print the square of each numbers rounded
# to three decimal places
map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
# Use filter to print only the names that are less than 
# or equal to seven letters
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
# Use reduce to print the product of these numbers
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)