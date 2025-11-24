import time
import tracemalloc

tracemalloc.start( )
t1 = time.time( )

def prime(n):
 if n < 2:
  return False
 for i in range(2 , int(n**0.5)+1):
  if n % i == 0:
   return False
 return True

def mers(p):
 if prime(p):
  m = 2**p - 1
  if prime(m):
   return True
 return False

x = int(input("enter p "))
print("mersenne prime =", mers(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
