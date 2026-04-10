from math import ceil

import time
start_time = time.perf_counter()

L = 120
ans = 0

Lhalf = ceil(L*0.5)+1
print(f'Lhalf is {Lhalf}')

for xa in range(1,Lhalf):
    for xb in range(1,Lhalf):
        X  = xa*xb
        if X>=L:
            continue
        for ya in range(1,Lhalf):
            for yb in range(1,Lhalf):
                Y=ya*yb
                if Y>=L:
                    continue

                if X + Y <= L:
                    print(xa,xb,ya,yb)
                    ans+=1

print(ans)


end_time = time.perf_counter()
print(end_time-start_time)