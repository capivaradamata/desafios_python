import random
print('O professor diz:"Bom, irei pegar um de vocês para apagar o quadro!"')
print('alunos resmungam:"ah não prof!"')
nome_1 = str('João')
nome_2 = str('Joaquina')
nome_3 = str('Mario')
nome_4 = str('Beatriz')
alunos = nome_1 , nome_2, nome_3, nome_4
print(f'{nome_1}, {nome_2}, {nome_3} e {nome_4}, eu escolho {random.choice(alunos)}')