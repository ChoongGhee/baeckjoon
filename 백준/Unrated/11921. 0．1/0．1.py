import sys
import time

total = 0
cnt = 0
N = int(sys.stdin.readline())
end_time = time.perf_counter() + 0.2

try:
   while cnt < N and time.perf_counter() < end_time:
       total += int(sys.stdin.readline())
       cnt += 1
except:
   pass

print(cnt)
print(total)