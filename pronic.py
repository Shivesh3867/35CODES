import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def pronic(n):
 for i in range(1 , n+1):
  if i * (i + 1) == n:
   return True
 return False

x = int(input("enter number "))
print("pronic =", pronic(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()

