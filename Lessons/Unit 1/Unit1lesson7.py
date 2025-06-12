# Predict
# A) I preditct that the statement would say ("Yes!", y, "is a factor of", x)
# B) I predict that the statement would say ("No", y, "is not a factor of", x)


import math

x = input("Please input a whole number: ")
x = int(x)
if (x < 1) or (x > 20):
  print("Error: the number must be between 1 and 20.")
  exit()
y = input("Please input another nonzero whole number")
y = int(y)
if y==0:
  print("y cant be 0")
  exit()
if (y < 1) or (y > 20):
  print("Error: the number must be between 1 and 20.")
  exit()
print("Now deciding if", y, "is a factor of", x, "...")
rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)
else: 
  print("no", y,"is not a factor of", x )
exit()
