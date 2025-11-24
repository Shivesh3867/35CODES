import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def cd(n):
 c = 0
 for i in range(1 , n+1):
  if n % i == 0:
   c = c + 1
 return c

x = int(input("enter number "))
print("divisor count =", cd(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
