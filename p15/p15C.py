n,m=map(int,input().split())
ps=list(map(int,input().split()))

# members_max =[0 for i in range(n)]
# for i in range(m):
#     members = [0 for p in range(n)]
#     leader_index=int(ps[i])-1
#     members[leader_index]=0
#     current_member=1
#     while leader_index+current_member<n:
#         members[leader_index + current_member] = current_member
#         current_member += 1
#     current_member=1
#     while leader_index-current_member>=0:
#         members[leader_index-current_member]=current_member
#         current_member += 1
#     for index,member in enumerate(members):
#         if member>members_max[index]:
#             members_max[index]=member
# for i in members_max:
#     print(i,end=" ")

left_leader=min(ps)
right_leader=max(ps)

members=[0 for _ in range(n)]
for member_index in range(n):
    members[member_index]=max(right_leader-member_index,member_index-left_leader)

print(*members)



