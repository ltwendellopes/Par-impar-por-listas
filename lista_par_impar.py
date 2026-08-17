numeros = []
pares = []
impares = []

for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Os números digitados foram: {sorted(numeros)}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')