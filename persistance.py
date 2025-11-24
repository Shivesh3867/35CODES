import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def mp(n):
 ct = 0
 while n > 9:
  p = 1
  for i in str(n):
   p = p * int(i)
  n = p
  ct = ct + 1
 return ct

x = int(input("enter number "))
print("persistence =", mp(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
