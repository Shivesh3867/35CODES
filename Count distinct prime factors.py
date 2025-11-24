import time
import tracemalloc

tracemalloc.start( )
t1 = time.time( )

def cdp(n):
 u = []
 i = 2
 while i <= n:
  if n % i == 0:
   if i not in u:
    u.append(i)
   n = n // i
  else:
   i = i + 1
 return len(u)

x = int(input("enter number "))
print("count distinct prime factors =", cdp(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
