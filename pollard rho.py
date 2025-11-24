import time
import tracemalloc
import random
import math

tracemalloc.start()
t1 = time.time()

def prho(n):
 if n % 2 == 0:
  return 2
 if n == 1:
  return 1
 x = random.randint(2 , n-1)
 y = x
 c = random.randint(1 , n-1)
 d = 1
 while d == 1:
  x = (x*x + c) % n
  y = (y*y + c) % n
  y = (y*y + c) % n
  d = math.gcd(abs(x - y) , n)
  if d == n:
   return None
 return d

n = int(input("enter number "))
print("pollard rho factor =", prho(n))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =" , cur)
tracemalloc.stop()
