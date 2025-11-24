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

def twin(limit):
 t = []
 for i in range(2 , limit):
  if prime(i) and prime(i + 2):
   t.append((i , i + 2))
 return t

x = int(input("enter limit "))
print("twin primes =", twin(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
