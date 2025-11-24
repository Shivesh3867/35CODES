import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def om(a , n):
 a = a % n
 if a == 0:
  return None
 v = 1
 for k in range(1 , n+1):
  v = (v * a) % n
  if v == 1:
   return k
 return None

a = int(input("enter a "))
n = int(input("enter n "))

print("order mod =", om(a , n))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
