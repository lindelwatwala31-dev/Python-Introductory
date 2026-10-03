# Tuples
fives = (10,15,20,25,30)
print(fives[3])

hundreds = (100, 200, 300, 400, 500, 300, 900, 200, 600, 700)
print(hundreds.count(200))
print(len(hundreds))

new_numbers = fives + hundreds
print(new_numbers)

# Max function
odds = (1,3,5,7,9,11,13,15,17,19,21)
print(max(odds))
print(min(odds))
print(sum(odds))
del(odds)

# Comma - A trailing comma ensures that it is a tuple, otherwise it will be a string
x = ("Hello")
print(type(x))
y = ("Hello",)
print(type(y))
