
S=input()
Q=int(input())

prefix_sum=[[0] * (len(S) + 1) for _ in range(26)]
#prefix_sum[char_id][pos]
print(prefix_sum)


for i,char in enumerate(S):
    for j in range(26):
        prefix_sum[j][i+1]=prefix_sum[j][i]
    if 'a'<=char<='z':
        prefix_sum[ord(char)-ord('a')][i+1]+=1
print(prefix_sum)

counts_per_char=[[] for i in range(26)]

stack=[]
for i,char in enumerate(S):
    if char=='(':
        stack.append(i)
    if char==')':
        left=stack.pop()
        right=i
        for j in range(26):
            count=prefix_sum[j][right+1]-prefix_sum[j][left]
            counts_per_char[j].append(count)

print(counts_per_char)
