# Slicing & indexing
x = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]

print(x[0:3:1])                     #Start: End: Count by
print(x[4: ])                       # Leave a space after the colon to run until the last value
print(x[ : 5])                      # Leave space before the colon to run the first values until your sliced value index
print(x[ : ])                       # This returns all the values (start to end)

print(x[ : : 2])                    # This calculates all values but returns the second values

# Negative indexing
y = (00, 10, 20, 30, 40, 50, 60, 70, 80, 90)
print(y[ : :-1])                    # Reverses all values and returns them
print(y[-3: : ])                    # Returns last 3 values


z = "Numbers"
print("Numbers"[-3:1:-1])  
 