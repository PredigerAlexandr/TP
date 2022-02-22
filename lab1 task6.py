N = int(input())
list = {}
for i in range(N):
    data = input().split(' ')
    if data[2] not in list:
        list[data[2]] = [[data[0], data[1]]]
    else:
        list[data[2]].append([data[0], data[1]])

N = int(input())
mounths = [input() for i in range(N)]

for mounth in mounths:
    if mounth in list:
        result = sorted(list[mounth], key=lambda x: (int(x[1]), x[0]))
        res = ''
        for i in result:
            res += ' '.join(i) + ' '
        print(res)
    if mounth not in list:
        print('')