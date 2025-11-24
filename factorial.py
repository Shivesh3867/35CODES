import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def fact(n):
 f = 1
 if n == 0:
  return 1
 for i in range(1 , n+1):
  f = f * i
 return f

x = int(input("enter number "))
print("factorial =", fact(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()

