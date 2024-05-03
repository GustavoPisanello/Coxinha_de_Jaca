variaveis = []
i = 0

while i < 20:
    num = int(input(f"Digite o {i + 1}° número: "))
    variaveis.append(num)
    i += 1

variaveis.sort()
print(variaveis[0], variaveis[i - 1])
