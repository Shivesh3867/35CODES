import time
import tracemalloc
import random

tracemalloc.start()
t1 = time.time()

def mr(n , k):
 if n < 2:
  return False
 if n == 2 or n == 3:
  return True
 if n % 2 == 0:
  return False

 d = n - 1
 r = 0
 while d % 2 == 0:
  d = d // 2
  r = r + 1

 for i in range(0 , k):
  a = random.randrange(2 , n-1)
  x = pow(a , d , n)
  if x == 1 or x == n-1:
   continue
  ok = False
  for j in range(0 , r-1):
   x = pow(x , 2 , n)
   if x == n-1:
    ok = True
    break
  if not ok:
   return False
 return True

n = int(input("enter number "))
k = int(input("enter rounds "))
print("miller rabin =", mr(n , k))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
