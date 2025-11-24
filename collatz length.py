import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def cl(n):
 c = 0
 while n != 1:
  if n % 2 == 0:
   n = n // 2
  else:
   n = 3*n + 1
  c = c + 1
 return c

x = int(input("enter number "))
print("collatz length =", cl(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
