#!/usr/bin/python3

import numpy as np

def show( c, s ):
  print( "Step "+str(s)+": "+str(c) )

collatz=31
step=0
show( collatz, step )

while collatz != 1:
  if collatz % 2 == 1:
    collatz=(3*collatz+1)//2
  else:
    collatz=collatz//2
  step=step+1
  show( collatz, step )
