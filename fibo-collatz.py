#!/usr/bin/python3

fp=0
f=1
collatzT=27
step=0
while collatzT != 1:
  step=step+1
  if collatzT % 2 == 1:
    collatzT = (3*collatzT+1)//2
    fn=f-fp
  else:
    collatzT = collatzT//2
    fn=f+fp
  fp=f
  f=fn
  print( step, f )
