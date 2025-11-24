import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def qr(a , p):
 a = a % p
 for x in range(0 , p):
  if (x * x) % p == a:
   return True
 return False

a = int(input("enter a "))
p = int(input("enter p "))

print("quadratic residue =", qr(a , p))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
