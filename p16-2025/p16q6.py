import math

n=input()
h=input().split(' ')

left=0
right=0
distance=0
flag=True

for distance in range(1, len(h)):
    while flag:
        if distance==len(h)-1:
            ans=math.ceil(n/2)
        right = left+distance
        if h[left]<=h[right]:
            flag=False
            continue
        left=right

#TODO



