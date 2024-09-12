# Exercicio 8 - Um restaurante a quilo cobra R$45,00 o Kg de refeição. Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
# Lembre-se que deve ser informado o peso do prato (tara), para que seja descontado do peso total.

# Usuário irá colocar o peso total do prato (comida+prato).
peso_total = float(input('Informe o peso total do prato (em kg): '))
# Usuário irá informar o peso do prato/tara (somente o prato).
peso_prato = float(input('Informe o peso do prato (em kg): '))

# O cáculo foi feito diretamente na saída de dados, mostrando o peso do prato excluindo a tara.
print(f'O peso do prato, excluindo a tara, equivale a: {peso_total - peso_prato:.2f}')
# Valor total a se pagar considerando que a tara foi excluída. 45: valor do prato informando pela questão.
print(f'Logo, o valor a pagar equivale a: {(peso_total - peso_prato)*45:.2f}')
