import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def poly(s , n):
 return ((s - 2) * n * n - (s - 4) * n) // 2

s = int(input("enter s "))
n = int(input("enter n "))

print("polygonal number =", poly(s , n))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
