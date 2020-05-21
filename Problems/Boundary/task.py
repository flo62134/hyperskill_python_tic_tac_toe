# work with a list from this variable
numbers = [int(n) for n in input()]
THRESHOLD = 5


# change the next two lines
less_than_5 = [number for number in numbers if number < THRESHOLD]
greater_than_5 = [number for number in numbers if number > THRESHOLD]

# printing your results
print(less_than_5)
print(greater_than_5)
