# Dictionary - Has keys and values and keys must be unique
me = {
    ("Start", "End"): (2026, 2027),
    "Course": "Data Science",
    "Year": 2026,
    "Certificates":["Data fundamentals", "Microsoft", "Data Fabrics"],
    "Complete": False
}

print(me["Year"])                                   # Can access by key, not index position
print(me["Start", "End"])

#Adding a new key-value pair:
me["Hair colour"]= "Black"
print(me)

#Updating an exiting value:
me["Course"] = "ZAIO - Data Science"
print(me)

#Deleting an item
del me["Hair colour"]
print(me)

# Common methods
brunch = {
    "Location": "Rosebank",
    "Time": 3,
    "Restaurant": "Akti"
}
print(brunch.keys())     					            # all keys
print(brunch.values())   				                # all values
print(brunch.items())    				                # all key-value pairs
print(len(brunch))       					            # number of items
print(brunch.update({"Time": 2}))                       # Updating key even values
print("New brunch:", brunch)

# More methods
emp = {
    "Occupation": "Data scientist",
    "Year": 2035,
    "Company": "Data Inc",
    "perm": True
}

print(emp.get("Year"))
print(emp.pop("Occupation"))                            # Removes a specific key-value pair based on the specified key
print(emp)
print(emp.clear())
print(emp)