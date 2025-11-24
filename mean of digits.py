import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def mean(n):
 sm = 0
 c = 0
 for i in str(n):
  sm = sm + int(i)
  c = c + 1
 return sm / c

x = int(input("enter number "))
print("mean of digits =", mean(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
