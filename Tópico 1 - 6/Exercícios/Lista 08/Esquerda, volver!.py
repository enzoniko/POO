direcao = 'NLSO'
while True:
    x = 0
    n = int(input())
    if (n == 0):
        break
    comando = input()
    comando[:n]
    for i in range(n):
        if comando[i] == 'D':
            x += 1


        if comando[i] == 'E':
            x -= 1

    print(direcao[x])
            
            
            