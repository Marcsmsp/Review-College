# Exercicio 9 - Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit. Faça um algoritmo para ler uma temperatura Celsius e imprimi-la em Fahrenheit 
# (pesquise como fazer este tipo de conversão).

# Usuário irá informar a temperatura em graus Celsius, 'c' representando Graus Celsius e 'f' representando Fahrenheits
c = float(input('Informe a temperatura (em Graus Celsius): '))

# Conversão feita na saída de dados
print(f'Convertendo essa quantidade em graus para fahrenheits obtemos: {(c*(9/5))+32:.2f}°F')