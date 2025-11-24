import time
import tracemalloc

tracemalloc.start()
t1 = time.time()

def pal(n):
 s = str(n)
 if s == s[::-1]:
  return True
 else:
  return False

x = int(input("enter number "))
print("palindrome =", pal(x))

t2 = time.time()
print("time =", t2 - t1)

cur , pk = tracemalloc.get_traced_memory()
print("memory =", cur)
tracemalloc.stop()
