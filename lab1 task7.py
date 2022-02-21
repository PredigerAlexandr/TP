def func (str):
    import re
    list = re.split('matrix = |], ', str)
    del list[0]
    matrix = []
    for i in range(len(list)):
        matrix.append([])
        for j in range(len(list[i])):
            if list[i][j].isnumeric():
                 matrix[i].append(int(list[i][j]))
    return matrix



string = input()
Matrix = []
Matrix = func(string)
trans_matrix = [[0 for j in range(len(Matrix))] for i in range(len(Matrix[0]))]
for i in range(len(Matrix)):
    for j in range(len(Matrix[0])):
        trans_matrix[j][i] = Matrix[i][j]

for i in range(len(trans_matrix)):
    res = ''
    for j in range(len(trans_matrix[0])):
        res+= str(trans_matrix[i][j]) + ' '
    print(res)


