times = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco da Gama", "EC Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude", "Bragantino", "Athletico-PR", "Criciúma", "Atlético-GO", "Cuiabá")
print(f"Times do Brasileirão: {times}")
print(f"Os 5 primeiros são: {times[:5]}")
print(f"Os últimos 4 são {times[-4:]}")
print(f"Os times em ordem alfabética são {sorted(times)}")
posição_corinthians = times.index("Corinthians")
print(f"O Corithians está em {posição_corinthians+1}")