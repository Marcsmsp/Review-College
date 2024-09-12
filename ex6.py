# Exercicio 6 - Uma padaria vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. Cada pão custa R$ 0,50 e a broa custa R$ 1,50. 
# Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). 
# Faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.

# Usuário informa a quantidade de pães e broas.
quant_paes = float(input('Informe a quantidade de pães que foram vendidos: '))
quant_broas = float(input('Informe a quantidade de broas que foram vendidas: '))

# Aqui vai mostrar a quantidade de dinheiro com a venda de pães e broas e também a soma entres esses valores. Ao final é mostrado o quanto vai ser depositado.
print(f'O valor total da venda de pães é: R$ {quant_paes*0.50:.2f}')
print(f'O valor total da venda de broas é: R$ {quant_broas*1.50:.2f}')
print(f'De acordo com esses dados o valor final foi de: R$ {(quant_paes*0.50) + (quant_broas*1.50):.2f}')
print(f'Logo, o total a ser guardado na conta poupança é: R$ {((quant_paes*0.50) + (quant_broas*1.50))*0.10:.2f}')