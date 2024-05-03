import math

seq = int(input("Digite o número o qual deseja a sequência ir até: "))
i = 0
fibonacci = [1]

while i < seq:
    num = fibonacci[i] + fibonacci[i - 1]
    fibonacci.append(num)
    i += 1

fibonacci.sort(reverse=True)
fibonacci.append(1)
fibonacci.sort()

print(f"{fibonacci}")
