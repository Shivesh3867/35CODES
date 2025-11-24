import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def d(n):
 c = 0
 for i in range(1 , n+1):
  if n % i == 0:
   c = c + 1
 return c

def hc(n):
 for i in range(1 , n):
  if d(i) >= d(n):
   return False
 return True

x = int(input("enter number "))
print("highly composite =", hc(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
