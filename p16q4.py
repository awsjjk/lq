
s=input()
ans=0

length= len(s)
index=[0]
while min(index)<length:
    #find first possible word in str

    words=['lqb','lbq','qlb','qbl','blq','bql']
    index =[length for i in range(6)]
    for word,num in zip(words,range(6)):
        if word in s:
            index[num]=s.find(word)

    #cut first word
    if min(index)!=length:
        s=s[min(index)+3:]
        ans+=1
    # print(f'{s}:{ans}:{min(index)}')
print(ans)


