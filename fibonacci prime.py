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

def isfib(n):
 a = 0
 b = 1
 while b < n:
  c = a + b
  a = b
  b = c
 if n == a or n == b:
  return True
 return False

def fp(n):
 if prime(n) and isfib(n):
  return True
 else:
  return False

x = int(input("enter number "))
print("fibonacci prime =", fp(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
