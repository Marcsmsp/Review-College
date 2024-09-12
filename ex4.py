# Exercicio 4 - Um trabalhador recebeu seu salário depois depositou e emitiu dois cheques, agora ele quer saber o saldo atual.
# A cada retirada bancária tem que pagar CPMF de 0,38 e o saldo inicial é 0.

# Lê o salário informado pelo usuário.
sal = float(input('Informe seu salário: '))
# Faz um cálculo direto de tudo que é pedido.
print('O saldo na conta deste trabalhador equivale a:', sal-((sal*0.38)*2))