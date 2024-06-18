import random
print('o professor diz:"Bom, agora irei sortear a ordem de apresentação dos trabalhos!"')
nome_1 = str('João')
nome_2 = str('Joaquina')
nome_3 = str('Mario')
nome_4 = str('Beatriz')
alunos =[nome_1 , nome_2, nome_3, nome_4]
random.shuffle(alunos)
print(f'a ordem será {alunos}')