n,m=map(int,input().split())
p=input().split()

members_max =[0 for i in range(n)]
for i in range(m):
    members = [0 for p in range(n)]
    leader_index=int(p[i])-1
    members[leader_index]=0
    current_member=1
    while leader_index+current_member<n:
        members[leader_index + current_member] = current_member
        current_member += 1
    current_member=1
    while leader_index-current_member>=0:
        members[leader_index-current_member]=current_member
        current_member += 1
    for index,member in enumerate(members):
        if member>members_max[index]:
            members_max[index]=member
for i in members_max:
    print(i,end=" ")
