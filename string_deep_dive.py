# Escape characters

print("Go left\nGo right\nGo straight")                                       #\n adds a new line
print("Flower:\tRoses")                                                       # Adds a tab space
print("What\\Now")                                                            # Adds a \
print("I\'ve arrived at the station")                                         # \' adds a '(single quote)
print("She said: \"On Wednesday, we wear pink \"")                            #\" adds a " (double qoute)

# Methods
x = "lindelwa twala"
y = "HELLO LINDELWA"

# Capitalize works for the first letter only
print(x.capitalize())                                                           
print(y.capitalize())

# Title capitalizes all first letters
gender = "i am a female"
gender_2 = "HE IS A MALE"
print(gender.title())                                                          
print(gender_2.title())

# Upper converts all letters to uppercase
city = "cape town"
print(city.upper())

# Lower converts all letters to lowercase
town = "CLAREMONT"
print(town.lower())

# Indexing - accessing a specific item in a string or list using its position number (including spaces)
# Python starts counting from 0 not 1
town = "CLAREMONT"
print(town[3])
print(town[0])
print(town[-1])                                         # Minus can be used to staart from the end of the string

# Slicing - used to get a range of characters
town = "CLAREMONT"
print(town[0:3])                                        # From index 0 up to BUT not including 3                  
print(town[2:6])                                        
print(town[:6])                                         # From beginning to index 4
print(town[4:])                                         # From index 4 to the end

# Slicing can work on lists too
items = ["Hat", "Scarf", "Gloves", "Boots", "Glasses"]
print(items[0])
print(items[-2])
print(items[1:4])

# Strip - removes spaces
games = "                Playstation          "                
print(games.strip())
print(games.lstrip())                                     # Removes spaces from the left side only
print(games.rstrip())                                     # Removes spaces from the right side only

# Strip symbols
email = "###lindelwa@gmail.com######"
print(email.strip("#"))

# Can also check if strings are true
x = "hello world"
y = "HeLLO WORLD"
print(x.islower())
print(y.isupper())

# Replacing - Replaces all instances automatically
sentence = "I love matcha, I drink matcha and matcha tastes good."
print(sentence.replace("matcha", "water"))
print(sentence.replace("matcha", "water", 2))                       # Can replace a specific number of times
print(sentence.replace(" ", "-"))                                   # Can also replace spaces
print(sentence.replace("a", "o"))                                   # Can replace characters

# Split - takes a string and breaks it apart into a list based on a separator you specify
sentence = "I love to swim"
print(sentence.split())                                             
date = "2026-09-14"                                                  # Can split by hyphen
print(date.split("-"))
fruits = "Mango, Blueberries, Apples, Grapes"                        # Can split by comma
print(fruits.split(","))
rest = "I love to swim, dance and watch movies"
print(rest.split(" ", 2))                                                    # Can choose how many times to split                                                         