# Functions available in Python without any imports. Here are the most commonly used ones, grouped by category
def squared_number(num):
    print(num**2)
squared_number(3)  
    
def squared_number(number,power):
    c = number**power
    return c
num = squared_number(4,2)  
print(num)

def add(input1, input2):
    if type(input1) == type(input2):
        return input1 + input2
    else:
        return "Data types are different"
random = add(9, 5)
print(random)

def sum_x(num1, num2):
    print(num1 + num2)
sum_x(10, 30)

# Arbitury arguments
def number_args(*number):
    print(number[0]*number[1])                              # [0] = 5 in the list and [1] = 6
number_args(5,6,1,2,8)

# Arbitury arguments - calling on a tuple                    # * Accepts any number of values
args_tuple = (7,3,6,1,8)                                     # [0] = 7 in the list and [1] = 3
def number_args(*number):
    print(number[0]*number[1])                             
number_args(*args_tuple)                                     # Have to add a * to call on the tuple argument

# Keyword argument                                           # Uses two ** for key-value pairs
def greet(name,age):
    print(f"My name is {name} and I am {age}s old")
greet("Linda",30)  

# Question 1: Calculate Sum

#a. Define a function named 'calculate_sum' that takes two parameters 'a' and 'b'.
#b. Inside the function, calculate the sum of 'a' and 'b'.
#c. Use the 'return' statement to return the calculated sum.

def calculated_sum (a, b):
    return a + b
print(calculated_sum(5,3))

# Question 2: Calculate Product

#a. Define a function named 'calculate_product' that uses '*args' to accept any number of arguments.
#b. Inside the function, calculate the product of all the arguments.
#c. Use the 'return' statement to return the calculated product.

def calculate_product (*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result
print(calculate_product(2,3,4))

# Local variables - live inside the function
def clean_name(name):                       # name is a Parameter
    cleaned = name.strip().lower()          # cleaned is a local variable
    print(cleaned)
    print("Cleaned:", cleaned)
clean_name("Maria")
clean_name("Kuma")    
clean_name("")

# Global parameters - live outside the function
x = 10                                      # Global variable
y = 20                                      # Globval variable

def sum(num1, num2):
    print(num1 + num2)
sum(x,y)  

def sum(x, y):
    print(x)                                #Still a global variable as it is accessible
    print(y)
sum(x,y)  

def sum(x, y):
    z = 50                                  # Local variable
    print(x)
    print(y)
    print(z)                                # Accessible as it is in the function
sum(x,y)  
print("##############")
print(x)
print(y)
#print(z)                                    # Will give an error as z is not defined

print("------------------------")

# Making z a Global variable
def sum(x, y):
    global z                                #we are making z global within the function
    z = 50                                  
    print(x)
    print(y)
    print(z)                                
sum(x,y)  
print(x)
print(y)
print(z)