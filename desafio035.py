print('digite a medidas dos 3 lados para saber se é possviel formar um triangulo')
x = float(input('primeiro lado'))
y = float(input('segundo lado'))
z = float(input('terceiro lado'))
maior = x
if  z > x and z > y:
    maior = z
if y > x and y > z:
    maior = y
menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
meio = x
if x < z < y or y < z < x:
     meio   = z
if x < y < z or z < y < x:
    meio = y
if meio + menor > maior:
    print('O trinagulo é possivel')
else:print('O trinagulo é impossivel')
print(f'{maior,meio,menor}')