print("Informe o valor do produtos e o a forma de pagamento para saber o valor final")
valor = float(input("Valor:"))
meio_pagamento = float(input("escolha o meio de pagamento \nÀ vista dinheiro ou cheque(1) \nÀ vista cartão(2) \n2x no cartão(3) \n3x no cartão(4) \n:"))
if meio_pagamento == 1:
    print(f"O valor final de sua compra é R${float(valor*0.9)}")
elif meio_pagamento == 2:
    print(f"O valor final de sua compra é R${float(valor*0.95)}")
elif meio_pagamento == 3:
    print(f"O valor final de sua compra é R${float(valor)}")
elif meio_pagamento == 4:
    print(f"O valor final de sua compra é R${float(valor*1.2)}")