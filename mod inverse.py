import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def inv(a , m):
 a = a % m
 for x in range(1 , m):
  if (a * x) % m == 1:
   return x
 return None

a = int(input("enter a "))
m = int(input("enter m "))

print("mod inverse =", inv(a , m))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
