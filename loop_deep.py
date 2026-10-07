x = range(0,100,10)
for num in x:
    print(num)

print("........................")

#No.2 - we are printing from highest to lowest
x = range(0,100,10)
for num in reversed(x):
    print(num)

print("==================")

#No 3
max=100
for element in range(1,max+1):
    if element == 63:
        print("Loop complete") 
        continue
    print(element)

print("----------------------------------")

# No 4 Print 1 to 10 and another print 10 to 20, then compare the elements that share within both codes == common element  
max=10
for element in range(1,max+1):
    print(element) 
num = 20
for count in range(1, num+1):
    print(count)  