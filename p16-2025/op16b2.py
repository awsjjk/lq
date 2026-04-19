
import sys
ans=0
ss=dict()
allBeautiful=set()
while True:
    #print('----')
    line = sys.stdin.readline().strip()
    if not line:
        break
    length = len(line)
    # compare letter;s count with previous word
    isBeautiful = False

    if length == 1:
        ans += 1

    wordstocompare = ss.get(length - 1)  # get[word,word]
    if wordstocompare:

        for i in wordstocompare:  # get 'word'
            #print(f'wdict:{wdict}   i={i}')
            dicttocompare = wdict.get(i, dict())
            #print(f'wordstocompare:{wordstocompare}')
            #print(f'dict:{dicttocompare}')
            if dicttocompare == linedict:
                isBeautiful = True


    #print('=======')


    #write word into ss :dict
    beauwords = ss.get(length) if ss.get(length) else list()
    beauwords.append(line)
    ss.update({length:beauwords})
    #print(f'ss:{ss}')           #ss : {lettersCountOfWord : word}
    #words in correct len
    words=ss.get(length) if ss.get(length) else list()
    #print(words)
    #calculate letter in word
    wdict=dict()
    for word in words:
        wdict.update({word:dict()})     #wdict: {word : {letter : count}}
        for l in word:
            ldict=dict()
            #ldict.update({l:ldict.get(l,0)+1})  #ldict: {letter : count}
            wdict.update({word: wdict.get(word, dict())})
            wdict[word][l]= wdict[word].get(l,0)+1
    #print(wdict)

   #get current ldict
    linedict=dict()
    for l in line:
        linedict.update({l:linedict.get(l,0)+1})    #current ldict
    #print(linedict)



    if isBeautiful:
        #print(f"is Btfl")
        ans += 1
        allBeautiful.add(line)
        continue
#print('-=-=-=--=-=-=--=-=-=--=-=-=-')
#print(f'allBeautiful{allBeautiful}')
longgest=''
for i in allBeautiful:
    if len(i) > len(longgest):
        longgest=i
print(longgest)










