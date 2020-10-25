#!/usr/bin/python3

import numpy as np

printit=False

for n in range(5, 6):
#  print( n )
  for op in range(0, 2**n):
    if not printit:
      printit=True
    else:
      print()
#    print( "  "+str(op) )
    a = np.zeros([n,n], dtype=int)
    b = np.zeros([n], dtype=int)
    ops=[]
    for r in range(0, n):
      if op >> r & 1 == 0:
        ops.append( "np/2" )
        a[r][r]=1
        a[r][(r+1)%n]=-2
      else:
        ops.append( "3n+1" )
        a[r][r]=-3
        a[r][(r+1)%n]=1
        b[r]=1
#    print( a, b)
    x=np.linalg.solve(a,b)
    is_int=True
    for pos in range(0, n):
      x[pos]=round(x[pos], 5)
      if not x[pos].is_integer():
#        print( "No int: "+("{:.20f}".format(x[pos])) )
        is_int=False
        break
    if is_int:
      print( "Working:" )
    print( "Dimension:  "+str(n) )
    print( "Operations: "+str(ops) )
    print( "Solution:   "+str(x) )
