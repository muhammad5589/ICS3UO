print("Welcome to the even and odd detector!") 
x = input("Enter your first number")
y = input("Enter your second number") 
if (x % 2==0) and (y % 2==0):
  print("the product of both numbers are even")
elif (x % 2==1) and (y % 2==1):
  print("the bproduct of both numbers is odd")

- 2
import math

print ("I will find the cube's inner diagonal for any edge length!")
j= int(input("Please enter the edge length of your cube:"))
s=math.sqrt(3)*j
print(s)
