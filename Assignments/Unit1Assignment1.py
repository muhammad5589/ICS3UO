print("Welcome to the even and odd detector!") 
print("This program determines if the product of two whole positive numbers will be even or odd!")
x = input("Enter your first number:")
y = input("Enter your second number:") 
if (x % 2==0) and (y % 2==0):
  print("the product of both numbers are even")
elif (x % 2==1) and (y % 2==1):
  print("the product of both numbers is odd")
else 
  print("the product of both numbers are even")
- 2
import math

print ("I will find the cube's inner diagonal for any edge length!")
j= int(input("Please enter the edge length of your cube:"))
s=math.sqrt(3)*j
d= j*s
print("your inner diagonal is: %.2f" % d)

- 3
change=int(input("Please enter the amount of change in cents:"))
if change >= 100:
  change= change % 100

qamnt= change//25
qrem= change % 25 
  
damnt= qrem//10
drem= qrem % 10
  
namnt= drem//5
nrem= drem % 5
  
pamnt=nrem
  
if qamnt==0 and damnt==0 and namnt==0 and pamnt==0:
  print("You have a dollar")
  
else:
  print("cents are:")
  
  if qamnt>0:
    print(qamnt,"quarters")
  
  if damnt>0:
    print(damnt,"dimes")
    
  if namnt>0:
    print(namnt,"nickles")
    
  if pamnt>0:
    print(pamnt, "pennies") 
