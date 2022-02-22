a = 'аеиоуыэюя'
b = 'бвгджзйклмнпрстфхцчшщъь'
code = input()
list = []
word = 'begin'
while word != '':
    word = input()
    c = code
    flag = False
    if '*' in c and len(word) + 2 > len(c):
        c = c.replace('*','?'*(len(word) - len(c) + 1))
    if len(word) == len(c):
        N = len(word)
        for i in range(N):
            if ((c[i] == '?' or (word[i]) in a and c[i]=='0') or (word[i] in b and c[i]=='1')):
                flag = True
            else:
                flag = False
                break
    if flag:
        list.append(word)
if list:
    for i in list:
        print(i)
else :
    print('Нет результата')




# for w in iter(input, '') :
#     p = p1
#     k = 0
#     if '*' in p and len(w) + 2 > len(p):
#         p = p.replace('*','?'*(len(w) - len(p) + 1))
#     if  len(w) == len(p):
#         n = len(w)
#         for i in range(n):
#             if (p[i] == '?' or (w[i] in vow and p[i] == '0')
#             or (w[i] in cons and p[i] == '1')):
#                 k = 1
#             else :
#                 k = 0
#                 break
#     if k:
#         res.append(w)
# if res:
#     for i in res:
#         print(i)
# else :
#     print('Есть нечего, значить!')










# code = input()
# list = []
# per = '-1'
# a = 'аеиоуыэюя'
# b = 'бвгджзйклмнпрстфхцчшщъь'
#
# while per != '':
#     per = input()
#     list.append(per)
#
# for word in list:
#     iterator = 0
#     flag = True
#     for i in code:
#         if i == '0':
#             if a.find(word(iterator)) != -1:
#                 iterator += 1
#             else: flag = False
#         if i == '1':
#             if b.find(word(iterator)) != -1:
#                 iterator += 1
#             else: flag = False
#         if i == '?'
