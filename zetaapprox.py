import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def za(s , t):
 sm = 0.0
 for n in range(1 , t+1):
  sm = sm + 1.0 / (n ** s)
 return sm

s = float(input("enter s "))
t = int(input("enter terms "))
print("zeta approximation =", za(s , t))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
