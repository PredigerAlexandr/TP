string = input()
per = int(string[0])
count = 1
for i in range(1, len(string)):
    if int(string[i])!=per:
        print(count, per)
        per = int(string[i])
        count = 1
    else:
        count +=1
    if i==len(string)-1:
        print(count, per)