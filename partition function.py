import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def part(n):
 p = [0] * (n+1)
 p[0] = 1
 for k in range(1 , n+1):
  for i in range(k , n+1):
   p[i] = p[i] + p[i-k]
 return p[n]

n = int(input("enter number "))
print("partition =", part(n))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
