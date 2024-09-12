# Aluno Marcos - 1° Semestre do Curso - Algoritmos

# Atividade Exemplo
# Entrada de Dados
x = 10+(20*30)     # Valor 1
y = (4**2)/30      # Valor 2
z = ((9**4)+2)*6-1 # Valor 3
# Saída de Valores
print('A resposta de X:', x, '\nA resposta de Y:', y, '\nA resposta de Z:', z) # Aqui eu estava apenas testando a quebra de linha.

# Exercicio 1 - Determinar o salário de um funcionário com gratificação (+) e imposto (-)

# Usuário irá informar o salário do funcionário.
sal = float(input('Informe o salário do respectivo funcionário:\n'))
# Na saída de dados o código já irá calcular automaticamente e mostrar o resultado.
print('A soma do salário com a gratificação, equivale:\n', sal+(sal*(5/100))) # Salário + Gratificação = SalG
print('O imposto equivale a:\n', sal*(7/100)) # Imposto
print('O total, considerando o imposto é:\n', (sal+(sal*(5/100)))-sal*(7/100)) # SalG - Imposto = Total