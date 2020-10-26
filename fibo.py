#!/usr/bin/python3

fp=0
f=1
for i in range(2, 10):
  fn=f+fp
  fp=f
  f=fn
  print( i, f )
