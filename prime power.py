import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def prime(n):
 if n < 2:
  return False
 for i in range(2 , int(n**0.5)+1):
  if n % i == 0:
   return False
 return True

def pp(n):
 for p in range(2 , n+1):
  if prime(p):
   k = p
   while k <= n:
    if k == n:
     return True
    k = k * p
 return False

x = int(input("enter number "))
print("prime power =", pp(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
