# Exercicio 9 - Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o preço do litro da gasolina e o valor do pagamento, 
# e exibir quantos litros ele conseguiu colocar no tanque.

# Usuário irá determinar um preço imaginário para a gasolina já que a questão não oferece e também vai determianar a quantidade X de litros que quer adicionar.
preco_gasolina = float(input('Informe o preço da gasolina por litro: '))
dinheiro = float(input('Informe a quantidade de dinheiro que vai gastar na gasolina, em reais: '))

# A quantidade de litros foi calculada de forma direta na saída de dados. O cálculo seria a quantidade que quer colocar no tanque dividido pelo preço da gasolina.
print(f'A quantidade de litros que o motorista conseguiu colocar no tanque foi de: {dinheiro/preco_gasolina:.2f} litros')