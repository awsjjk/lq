ans=0
words=["lqb","lbq","qlb","qbl","blq","bql"]
s=input()
index=[0]
while index:
    index=[]
    for w in words:
        index = []
        if w in s:
            index.append(words.index(w))
            print(index)
    if index:
        s=s[min(index)+3:]
    print(s)



print(ans)



