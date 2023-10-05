respaldo=[
0,0,0,0,0
]

lista = [
    [0,2,5,6,7],
    [0,0,0,3,8],
    [2,9,6,3,4],
    [1,5,6,1,4],
    [0,9,2,5,0]
]

for i in range (len(lista)):
    for j in range(len(lista[i])):
        if lista[i][j] == 0:
            respaldo[i]+=1

print (respaldo)
