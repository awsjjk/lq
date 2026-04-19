##P10387训练士兵
import sys
input_data=list(map(int,sys.stdin.read().strip().split()))

idx = 0
n=input_data[idx]
idx+=1
S=input_data[idx]
idx+=1

soldiers=[]
total_p=0
for _ in range(n):
    pi=input_data[idx]
    idx+=1
    total_p+=pi
    ci=input_data[idx]
    idx+=1

    soldiers.append([pi,ci])    #soldiers:[ [价钱，次数] , [..，..] ， ...]
    
##print(soldiers)
    
soldiers.sort(key=lambda x : x[1])  #按需要次数从小到大排序,
##print(soldiers)

need_p=total_p
now_soldier=-1

while now_soldier < n - 1 and need_p>S:
    now_soldier+=1
    need_p-=soldiers[now_soldier][0]
##    print(f'while::now:{now_soldier},{soldiers[now_soldier]},need_p={need_p}')
#在now_soldier前的通过集体训练结束训练，训练次数为soldiers[now_soldier][1]

#如果没有集体训练
if now_soldier==-1:
    train_times=0
    ans=0
else:  
    train_times=soldiers[now_soldier][1]
    ans=train_times*S
##print(f'times:{train_times},ans:{ans},now:{now_soldier}')

for i in range(now_soldier + 1, n):
    _p, _c = soldiers[i]
    # 超过了团购次数，才需要补钱
    if _c > train_times:
        ans += _p * (_c - train_times)

print(ans)
