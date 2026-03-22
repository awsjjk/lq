
scores=[5,5,10,10,15,15,20,20,25,25]
possibilities=set()
possibilities.add(0)

for score in scores:
    now_score=set()
    for possibility in possibilities:
        now_score.add(possibility)
        now_score.add(possibility+score)
    possibilities=now_score


print(possibilities)
print(len(possibilities))

