import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def pp(n):
 for a in range(2 , n):
  p = a
  while p < n:
   p = p * a
   if p == n:
    return True
 return False

x = int(input("enter number "))
print("perfect power =", pp(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
