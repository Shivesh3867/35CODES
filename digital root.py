import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def digroot(n):
 while n > 9:
  sm = 0
  for i in str(n):
   sm = sm + int(i)
  n = sm
 return n

x = int(input("enter number "))
print("digital root =", digroot(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()

