print("Welcome to the even and odd detector!")
x= int(input("Enter your first number"))
y= int(input("Enter your second number"))

if (x % 2 == 0 and y % 2 == 0):
  print("The product of both numbers are even")
elif(x % 2 == 1 and y % 2 == 1):
  print("The product of both numbers are odd")
elif(x % 2 == 1 and y % 2 ==0):
  print("The product of both numbers are even ")
else:
  print("The product of both numbers are even ")
