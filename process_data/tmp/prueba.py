matrix = [
        [1,1,1,1,1,1,1,1],
        [2,2,2,2,2],
        [3,3,3,3,3,3,3,3,3,3],
        ]


rot = []

for i in range(len(matrix[0])):
    tmp_fila = []
    for l in matrix:
        if i >= len(l):
            l.append('')
        tmp_fila.append(l[i])
        #print(l[i],end=' ')
    rot.append(tmp_fila)
print(rot)
#print(max(list(map(len,matrix))))
