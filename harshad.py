import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def harshad(n):
 sm = 0
 for i in str(n):
  sm = sm + int(i)
 if n % sm == 0:
  return True
 else:
  return False

x = int(input("enter number "))
print("harshad =", harshad(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
