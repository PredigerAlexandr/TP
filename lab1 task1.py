import copy

N = int(input())
string = input()
res=''
alf = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ALF = copy.deepcopy(alf.upper())

for i in string:
    if i.isupper():
        res += ALF[(ALF.index(i) + N) % len(ALF)]
    elif i.islower():
        res += alf[(alf.index(i) + N) % len(alf)]
    else:
        res+= i
print(res)