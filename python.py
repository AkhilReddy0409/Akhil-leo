import json from logpy import Relation, facts, run, conde, var, eq
# Check if 'x' is the parent of 'y' 
def parent(x, y):  
  return conde([father(x, y)], [mother(x, y)])
# Check if 'x' is the grandparent of 'y' 
def grandparent(x, y):
  temp = var()
  return conde((parent(x, temp), parent(temp, y)))
# Check for sibling relationship between 'a' and 'b'   
def sibling(x, y):
  temp = var()
  return conde((parent(temp, x), parent(temp, y)))
# Check if x is y's uncle
def uncle(x, y):
  temp = var()
   return conde((father(temp, x), grandparent(temp, y)))
  
