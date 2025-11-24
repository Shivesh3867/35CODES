import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def luc(n):
 a = 2
 b = 1
 if n == 1:
  return [2]
 if n == 2:
  return [2 , 1]
 s = [2 , 1]
 for i in range(3 , n+1):
  c = a + b
  s.append(c)
  a = b
  b = c
 return s

x = int(input("enter n "))
print("lucas sequence =", luc(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
