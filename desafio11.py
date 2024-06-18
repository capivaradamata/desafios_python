print('olá, para saber quantos litros de tinta serão necessario, infome o que for pedido')
altura = float(input('Por favor informe a altura da porta me metros:'))
largura = float(input('agora, informe a largura da porta em metros:'))
tinta = 2
area_porta = (altura*largura)
print(f'A quantidade de tinta necessarios será de {area_porta/tinta} litros.')