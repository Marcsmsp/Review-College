# Exercicio 2 - Determinar um depósito, incluiondo os juros(rendimento) e o rendimento anual.

# Usuário vai informar o valor depositado.
dep = float(input('Informe o valor do depósito:\n'))
# Na saída de dados o valor informado é calculado e mostrado no resultado final.
print(f'O rendimento mensal seria R$', f'{dep*(2/100):.2f}', 'ao mês') # O rendimento do depósito ao mês
print(f'Já o rendimento anual seria R$', f'{(dep*(2/100))*12:.2f}', 'por ano.') # O rendimento por ano
print(f'Fazendo assim, o rendimento total ser R$', f'{dep+((dep*(2/100))*12):.2f}') # depósito + rend. anual