# Exercicio 3 - Determinar a medida em pés e converter para polegadas, jardas e milhas

# Usuário irá informar uma quantidade em pés para ser convertida
pes = float(input('Informe uma quantidade em pés: '))   # Valor inicial
# Na saída de dados os dados em pés serão convertidos para Polegadas e Jardas.
print('Convertendo para polegadas:', pes*12, '\nConvertendo para jardas:', pes/3) # Conversão para polegadas e jardas
# Na segunda saída de dados os dados são transformados em Milhas.
print('Convertendo para milhas:', (pes/3)/1760) # Conversão para milhas