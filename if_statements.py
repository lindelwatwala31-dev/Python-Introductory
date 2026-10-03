# IF statements
age = 25
if age >= 25:
    print("You are in your mid twenties and above")
elif age >= 20 and age <=25:
    print("You are in your early twenties")
else:
    print("You are in your teen years")        

# No.2
speed_limit = 60
if speed_limit > 60:
    print("Traffic violation! You are speeding!!!")
elif speed_limit == 60:
    print("Lower your speed!")
else:
    print("You are driving safely")
    
# No.3
robot_light = "Green"
if robot_light == "Green":
    print("You may go")
elif robot_light =="Yellow":
    print("You need to slow down")
else:  
    print("You need to slow down")      
    
# No.4
age = int(input("Enter your age:"))
if age <= 18:
    print("Access Denied")
elif age >= 18 and age <= 30:
    print("Access granted")
else:
    print("No entry for now")

# Nested IF statements
i = int(input("Enter your number :"))
if i >= 0:
    print("Positive")
    if i%2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative")
    
# Elif statements
std = input("Enter students grade: ")  
if std == "Grade 8":
    print("Go to Room 1")
elif std == "Grade 9":
    print("Go to Room 2")
elif std == "Grade 10":
    print("Go to Room 3")
elif std == "Grade 11":
    print("Go to Room 4")    
else:
    print("Go to Room 5")
        
# Operators in If statements
colour = input("Enter your colour: ")
if colour == "Red":
    print("It's a primary colour")  
elif colour == "Yellow":
    print("It's a primary colour")  
elif colour == "Blue":
    print("It's a primary colour")    
elif colour == "Orange":
    print("It's a secondary colour") 
elif colour == "Green":
    print("It's a secondary colour")
elif colour == "Purple":
    print("It's a scondary colour")
else:
    print("Not a primary or secondary colour")                 