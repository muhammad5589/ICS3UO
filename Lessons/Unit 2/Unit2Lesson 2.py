"""
I think the code will run a loop that prints the value of "count",
and every time it prints it will decrease the value by 1 from the total value. This will trigger the != in the second line and it will
not run anymore.
"""

count = 9
while (count != 0):
    print(count)
    count -= 1

# Modify 1

count = 9
while (count != 0):
    count -= 1
    print(count)

# The output was different, because it subtracted one before printing the count, so nine is never printed

# Modify 2

tnumcount = 1 # Which triangular number the program is on (1st, 2nd, 3rd...)
trinumnum = 1 # Actual triangular number. (1, 3, 6, 10, 15...)
addnum = 2 # Number to be added to the triangular number each time
toaddnum = 1 # Value to be added to the value of the number being added
while tnumcount <= 6: # Which stage of the triangular number the program will count to (If 3 is put instead of 6, for example, the output will be 1, 3, 6.)
  if tnumcount == 1: # Since the first, second, and third
    print("The %dst triangluar number is %d" %  (trinumcount, trinum))
    trinum += addnum
    addnum += toaddnum
    tnumcount += 1
  if tnumcount == 2:
    print("The %dnd triangular number is %d" % (trinumcount, trinum))
    trinum += addnum
    addnum += toaddnum
    tnumcount += 1
  if tnumcount == 3:
    print("The %drd triangular number is %d" % (trinumcount, trinum))
    trinum += addnum
    addnum += toaddnum
    tnumcount += 1
  if tnumcount > 3 or trinumcount == 5:
    print("The %dth triangular number is %d" % (trinumcount, trinum))
    trinum += addnum
    addnum += toaddnum
    tnumcount += 1
