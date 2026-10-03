# String sequence

city = "Rivonia"
print(city[0])                                                  # Also known as indexing
print(city[1])
print(city[2])
print(city[-1])

# List sequence
numbers = [90, 40, 67, 32, 467, 10]
print(numbers)

twos = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(twos[7])                                                  # Will rerun the 7th position

# Range sequence
range_type = range(10, 50, 5)                                   # Will count from 10 to 50 in 5s
print(list(range_type))

# Tuple sequence                                                # Tuples cannot be changed/ appended
directions = ("North", "South", "East", "West")
print(directions[3])
print(directions[0], "and", directions[3])
print("I am", directions[0], directions[-1])

print("My name is", directions[0], directions[-1],"and I live in", city, "and I am", twos[7], "years old.")
                               
# Sets - removes duplicates and orders numbers
unique_numbers = {2,6,4,9,0,3,6,8,9}
print(unique_numbers)
favorite_fruits = {"mango", "blackberry", "watermelon", "mulberries", "grapes"}
print(favorite_fruits)

# Creating a dictionary {}
vacation_dream = {
    "destination": "Maldives",
    "budget": 10000,
    "duration": 14,
    "activities": ["snorkeling", "scuba diving", "sunbathing", "sailing"]
}
print("My dream dream vacation is to go to", vacation_dream["destination"])
print("I want to go for", vacation_dream["duration"], "days and my budget is", vacation_dream["budget"],"$")
print("I want to eat", favorite_fruits)
print(vacation_dream["duration"])                                           #Calling on the item in the dictionary
vacation_dream["destination"] = "South Asia"                                # Replacing the item in the dictionary
print(vacation_dream)

# Literals
tone_colours =("Brown\nArmy green\nDusty pink\nCream\nBaby blue")
print("These are earth tone colours:\n",tone_colours)