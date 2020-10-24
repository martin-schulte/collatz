#!/usr/bin/python3

import numpy as np

for n in range(5, 6):
#  print( n )
  for op in range(0, 2**n):
#    print( "  "+str(op) )
    a = np.zeros([n,n], dtype=int)
    b = np.zeros([n], dtype=int)
    opstr=""
    for r in range(0, n):
      if op >> r & 1 == 0:
#        print( "    np/2" )
        a[r][r]=1
        a[r][(r+1)%n]=-2
      else:
#        print( "    3n+1" )
        a[r][r]=-3
        a[r][(r+1)%n]=1
        b[r]=1
#    print( a, b)
    x=np.linalg.solve(a,b)
    print(x)
    is_int=True
    for pos in range(0, n):
      if not x[r].is_integer():
        is_int=False
        break
    if is_int:
      print( "Dimension:  "+str(n) )
      print( "Operations: " )
      print( "Solution:   "+str(x) )
