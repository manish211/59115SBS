"""

# Examples of Unit tests  in Python

"""
import time
from ok import *

print time.strftime("%H:%M:%S\n")

@ok
def _ok1():
  assert 1==1

@ok
def _ok2():
  assert 2==1

@ok
def _ok3():
  assert 3==3

@ok
def _ok4():
  assert 1==1 

@ok
def _ok5():
  assert 420==1 

@ok
def _ok6():
  assert 421==1     

@ok
def _ok7():
  assert 450==1 

@ok
def _ok8():
  assert unittest.tries==8
  assert unittest.fails==4
  print unittest.score() 
  
