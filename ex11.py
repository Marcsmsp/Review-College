# Exercicio 11 - Considere as variáveis abaixo declaradas: inteiro d, y, p, q,r; real a, b, c, s, z;
# Indique qual o resultado das expressões aritméticas, onde 
# a = 3.0; b = 2.0; c = 0.5; s = 9.0;  z =12.0; d= 16; y = 2; p = 4; q = 6; r = 24, x = 2;
# 1 - x + y – z * a
# 2 - d / y
# 3 - y % d
# 4 - p * (r % q) – q/2
# 5 - (a-b*y-d)
# 6 - ((z/a) + b * a) – d

# Primeiro, declaramos as variáveis:
a, b, c, s, z, d, y, p, q, r, x = 3.0, 2.0, 0.5, 9.0, 12.0, 16, 2, 4, 6, 24, 2
# Agora imprimimos para ver se está tudo correto:
print('a = ', a, '\nb = ', b, '\nc = ', c, '\ns = ', s, '\nz = ', z, '\nd = ', d, '\ny = ', y, '\np = ', p, '\nq = ', q, '\nr = ', r, '\nx = ', x)
print('Podemos perceber que há reais e inteiros entre eles, os quais: \nOs reais são: a, b, c, s, z. \nE os inteiros: d, y, p, q, r.')

# 1 - x + y – z * a
A = x+y-(z*a)
# A variável irá guardar o resultado e irá mostrar apenas a resposta. Aqui uma resolução: 
# z*a = 36.0, y-36 = 2-36 = -34, 2-36 = -34 
print(A)

# 2 - d / y
B = d/y
# A variável irá guardar o resultado e irá mostrar apenas a resposta. Aqui uma resolução: 
# vd/y = 16/2 = 8.0
print(B)

# 3 - y % d
C = y%d
# A variável irá guardar o resultado e irá mostrar apenas a resposta. Aqui uma resolução: 
# 2%16 = 2 
print(C)

# 4 - p * (r % q) – q/2
D = p*(r%q)-q/2
# A variável irá guardar o resultado e irá mostrar apenas a resposta. Aqui uma resolução:
# 24%6 = 0 _ 4*0 = 0 _ -q/2 = -6/2 = -3
print(D)
