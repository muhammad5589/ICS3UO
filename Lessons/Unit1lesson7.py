# Predict
# A) I preditct that the statement would say ("Yes!", y, "is a factor of", x)
# B) 


# Modify
import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)
    
    #Modify 2 
import math
#modify
x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)
else: 
  print("you can't enter zero. enter a non zero number")
    
  #Modify3
x=input("only accept numbers between 1 and 20:")
if (x < 1) and (x > 20):
  print("Error: the number must be between 1 and 20.")
else:
y=input("only accept numbers between 1 and 20:")
