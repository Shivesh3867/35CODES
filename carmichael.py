import time
import tracemalloc
import math

tracemalloc.start()
t1 = time.time()

def gcd(a , b):
 while b != 0:
  a , b = b , a % b
 return a

def carm(n):
 if n < 2:
  return False
 for a in range(2 , n):
  if gcd(a , n) == 1:
   if pow(a , n-1 , n) != 1:
    return False
 return True

x = int(input("enter number "))
print("carmichael =", carm(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
