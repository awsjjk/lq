counts=0
for red in range(256):
    for green in range(256):
        for blue in range(256):
            if blue>red and blue>green:
                counts+=1
print(counts)


