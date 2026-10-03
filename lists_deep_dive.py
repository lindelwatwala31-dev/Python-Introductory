# Lists
grocery_list = ["Spaghetti", "Sugar", "Salt", "Stock cubes"]
print(grocery_list[2])
print(len(grocery_list))


# Insert
camping_essentials = ["Camping chair", "Net", "Torch", "Tent"]
camping_essentials.insert(3, "Sunscreen")
print(camping_essentials)

odds = [1,3,5,7,9,11]
odds.insert(0, -1)
print(odds)

# Remove
colour_essentials = ["black", "beige", "blue", "brown"]
colour_essentials.remove("blue")
print(colour_essentials)

odds = [100,200,300,400,500,600,700]
odds.remove(500)
print(odds)

# Pop - removes an item from a list by its index position — and unlike remove(), it actually returns the removed item so you can use it
euro_summer = ["Croatia", "London", "Spain", "Moldova", "France"]
euro_summer.pop(3)
print(euro_summer)

odds = [10,20,30,40,50,60]                       
odds.pop()                                              # Removes the last item
print(odds)

# Delete - del
camping_essentials = ["Camping chair", "Net", "Torch", "Tent", "Fishing Rods"]
del camping_essentials[4]
print(camping_essentials)                               # Deletes the 4th position

odds = [-15,-13,-11,-9,-7,-5,-3,-1]                       
del(odds)                                               # Deletes the whole list

seafood = ["Fish", "Mussels", "Prawns", "Calamari", "Scallops"]
del seafood[1: 3]
print(seafood)                               # Deleted everything from index 1 up to but not including index 3!

seafood.clear()                              # Removes the lists' elements
print(seafood)

# Sort
south_asia = ["China", "Japan", "South Korea", "Thailand", "Singapore", "Bali"]
south_asia.sort()
print(south_asia)                           

odds = [8,73,15,7,25,-21, 3, 90, 40]                       
odds.sort() 
print(odds)

# Sorting in reverse order
shoes = ["boots", "sandals", "tekkies","loafers"]
shoes.sort(reverse=True)
print(shoes)

numbers = [6,3,9,11,46,2,8]
numbers.sort(reverse=True)
print(numbers)

# Append
summer_care = ["sun screen", "sandals", "hats"]
summer_care.append("umbrella")
print(summer_care)

dates = [1,2,3,4,5,6]
dates.append(7)
print(dates)