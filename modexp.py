import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def me(b , e , m):
 r = 1
 for i in range(e):
  r = (r * b) % m
 return r

b = int(input("enter base "))
e = int(input("enter exp "))
m = int(input("enter mod "))

print("mod exp =", me(b , e , m))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
