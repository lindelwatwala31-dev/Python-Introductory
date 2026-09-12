# While loop
x = 0
while x < 6:
    print("Current value of x", x)
    x = x + 1
else:
    print("Loop is complete")   
    
# No.2   
num = 1
sum = 0

print("Enter num for sum, Press '0' to exit.")
while num != 0:
    num = int(input("Enter number: "))
    sum = sum + num
    print("Current Sum:", sum)
else:
    print("Loop is complete")    

# Break statement
number = 1
while number < 5:
    print(number)
    if number == 3:
        break
    number = number + 1
    
# No.2
a = [0,1,2,3,4,5]    
for x in a:
    print(x)
print("-------------------------------------------------------")
i = 0
while i < 5:
    print(i)
    i += 1
    
           
# Else statement
number = 1
while number < 5:
    print(number)
    if number == 3:
        break
    number = number + 1
else:
    print("No longer < 5")     
print("Done")

# Continue statement
number = 1
while number < 5:
    number = number + 1
    if number == 3:
        continue                                    # It will run until if number == 3: and repeat the loop
    print(number)
else:
    print("No longer < 5")  
             
# In loops
A = [0, 1, 2, 3, 4, 5]                              # list
B = (0, 1, 2, 3, 4, 5)                              # tuple
C = {0, 1, 2, 3, 4, 5}                              # set
D = 'Linda'                                         # string
E = {"name": 'Linda', "age": 22}                    # dictionary

print("D" in D)
print("--------------------------------------------------")

# For loops
integers = [1,2,3,4,5]
for number in integers:                             # Numbers is a given variable to the numbers in the list
    print(number)

for number in integers:                           
    print("Take 5")
    
integers = [1,2,3,4,5]
for Jelly in integers:                             # Numbers is a given variable to the numbers in the list
    print(Jelly + Jelly)    

# Dictionary loop example
ice_cream_dict = {"Store name": "Paul's ice cream", "Weekly intake": 3, "Favorite flavours": ["Pistachio", "Butterscotch", "Malva pudding", ]} 
for cream in ice_cream_dict.values():                               # We are calling on the values not keys
    print(cream)
# Calling the key and values
for key, values in ice_cream_dict.items():
    print(key, ':' ,values)    
       
# No.2
A = [0, 1, 2, 3, 4, 5]                              # list
B = (0, 1, 2, 3, 4, 5)                              # tuple
C = {0, 1, 2, 3, 4, 5}                              # set
D = 'Linda'                                         # string
E = {"name": 'Linda', "age": 22}                    # dictionary

for i in E.values():
    print(i)
for x, y in E.items():
    print(x, " ", y)    
    
print("D" in D)

# Nested For loop4
pizza_base = ["Thick", "Thin", "Cheese crust", "Gluten free"]
pizza_toppings = ["Pepperoni", "Onions", "Cheese", "Chicken"]
for one in pizza_base:
    for two in pizza_toppings:
        print(one,"topped with", two)

# Range in loops
for x in range(1, 5):
    print(x)  
else:
    print("----------------------------------------------")        
    