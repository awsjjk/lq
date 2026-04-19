count=0
for p in range(1,2025):
    bina :str =str(bin(p))
    bina=bina[2:]
    sum_b :int =0

    for char in bina:
        sum_b+=int(char)

    sum_f: int = 0
    for char1,char2 in zip(bina[-1::-2],bina[-2::-2]):
        char=int(char1)+int(char2)*2
        sum_f+=char
    if len(bina)%2!=0:
        sum_f+=int(bina[0])

    if sum_f==sum_b:
        count+=1
        print(p,sum_f,sum_b)
print(count)