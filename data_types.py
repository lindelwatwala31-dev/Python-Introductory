# Variables

x = "Dancing shoes"
print(x)

r, s, t = "Option 1", "Option 2", "Option 3"                   # Every value must be in qoutation marks
print(r)
print(s)
print(t)

c=d=e = "Itsy Bitsy Spider"
print(c)
print(d)
print(e)

winter_essentials = ['Gloves', 'Beanie', 'Boots', 'Leg warmers']            # List type
do = re = me = fa = winter_essentials

print(do)
print(re)
print(me)
print(fa)

# Concatenation
name_surname = "Lindelwa " + "Twala"
print(name_surname)
age = 10 + 16
print(age)

print(f"I am {name_surname} and I am {age}s years old")
q = "I am "
z = "learning "
l = "python."
print(q+z+l)

# Data types - String
name = "Linda"                                      
print(name)
print(type(name))

# Integers
age = 26                                            
print(age)
print(type(age))

# Float - returns decimals
weight = 63.5                                       
print(weight)
print(type(weight))

# List
likes = ["food", "exercise", "netflix"]            
print(likes)
print(type(likes))

heat_wave = [f"100 Degrees Celcius", "Very Hot", 10 > 7]
print(heat_wave)

# Adding append
random = [ "Monkey", 70, ["Power Valley"], 7 >9]            # [Power Valley is a nested lis]
random.append("Is the Earth flat?")                         # Append adds to the end of the list, cannot append a tuple()
print(random)

# Changing a list
random[1] = 90                                              # Substituted 70 with 90
print(random)

# Sets
colours = {"Red", "Brown", "Black", "Pink"}
print(colours)
all_numbers = {3,5,7,9,11,3,9,0,7}                         # Will remove duplicates
print(all_numbers)

# Boolean - true or false
b = 10 > 5                                         
print(b)
print(type(b))

# Triple qoute
poem = """
I am now undertsnading
python basics and YouTube
has been very helpful.
"""
print(poem*2)                                   # Will return the poem twice





