import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def inv(a , m):
 a = a % m
 for x in range(1 , m):
  if (a * x) % m == 1:
   return x
 return None

def crt2(r1 , m1 , r2 , m2):
 M = m1 * m2
 M1 = M // m1
 M2 = M // m2
 x = r1 * M1 * inv(M1 , m1)  +  r2 * M2 * inv(M2 , m2)
 return x % M

def crt_multi(rs , ms):
 M = 1
 for i in ms:
  M = M * i
 x = 0
 for i in range(len(ms)):
  Mi = M // ms[i]
  x = x + rs[i] * inv(Mi , ms[i]) * Mi
 return x % M

print("1 for 2 equations    2 for many equations")
ch = int(input("enter choice "))

if ch == 1:
 r1 = int(input("r1 "))
 m1 = int(input("m1 "))
 r2 = int(input("r2 "))
 m2 = int(input("m2 "))
 print("CRT =", crt2(r1 , m1 , r2 , m2))
else:
 n = int(input("how many eq "))
 rs = []
 ms = []
 for i in range(n):
  r = int(input("r "))
  m = int(input("m "))
  rs.append(r)
  ms.append(m)
 print("CRT =", crt_multi(rs , ms))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
