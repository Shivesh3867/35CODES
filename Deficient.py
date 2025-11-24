import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def deficient(n):
 sm = 0
 for i in range(1 , n):
  if n % i == 0:
   sm = sm + i
 if sm < n:
  return True
 else:
  return False

x = int(input("enter number "))
print("deficient =", deficient(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
