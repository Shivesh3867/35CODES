import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def sdiv(n):
 sm = 0
 for i in range(1 , n):
  if n % i == 0:
   sm = sm + i
 return sm

def ami(a , b):
 if sdiv(a) == b and sdiv(b) == a:
  return True
 else:
  return False

a = int(input("enter a number : "))
b = int(input("enter b number : "))

ans = ami(a , b)
print("amicable =", ans)

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)

tracemalloc.stop()

