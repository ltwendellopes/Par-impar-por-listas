numeros = []


for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))
    numeros.append(num)
    if i % 2 == 0:
        par = num
    else:
        impar = num
print(f'Os números digitados foram: {sorted(numeros)}')
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados foram: {impar}')