#Calculating salary increase

name = "Linda"
salary = int(input("Enter your salary: " ))
increase_current_year = float(input("Enter your increase percentag:" ))
increase_percentage = salary * increase_current_year
new_salary = salary + increase_percentage

print("Your salary increase is:", "R", increase_current_year, "%")
print("Your new salary is:" , "R", new_salary)

print(f"Hello:", name, "your new salary is:", new_salary)
