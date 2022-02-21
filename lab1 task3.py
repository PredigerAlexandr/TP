N = int(input())
searchList = []
wordList = []
res = []
for i in range(N):
    searchList.append(input())
N = int(input())
for i in range(N):
    wordList.append(input())

for i in searchList:
    flag = True
    for j in wordList:
        if j not in i:
           flag = False
    if flag:
        res.append(i)

for i in res:
    print(i)
