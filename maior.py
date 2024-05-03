list = [5, 4, 3, 7, 6, 34, 2, 76, 8, 45, 98, 17]

maiores = []
menores = []

def verifica():
    i = 0
    y = i + 1

    while i < len(list):
        if list[y] < list[i]:
            maiores.append(list[i])
        else:
            menores.append(list[i])
        i += 1

    print(maiores)
    print(menores)

verifica()