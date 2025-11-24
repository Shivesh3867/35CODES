import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def pf(n):
 f = []
 i = 2
 while i <= n:
  if n % i == 0:
   f.append(i)
   n = n // i
  else:
   i = i + 1
 return f

x = int(input("enter number "))
print("prime factors =", pf(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
