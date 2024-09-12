# Exercicio 10 - Escreva as expressões algébricas em forma computacional. a = 4, b = 2, c = 12, d = 5
# a) a + bc + d
# b) (a+b) c + d (a-2b)
# c)[2a + (c-d)2] 2
# d)(x+y) (x-y)

# Atribuição de valores as variáveis
a, b, c, d, x, y = 4, 2, 12, 5, 6, 8
print('a = ', a, '\nb = ', b, '\nc = ', c, '\nd = ', d, '\nx = ', x, '\ny = ', y) # Para testar se os valores foram atribuídos de forma correta.

# a)
A = (a+(b*c)+d)
# Primeiro calculamos b*c, que é igual a 24. Em seguida podemos somar a e d, que equivale a 9. Somando 24 e 9
# obtemos 33.
print('a) (a+(b*c)+d) = ', A)

# b)
B = (a+b)*c+d*(a-(2*b))
# Primeiro calculamos a+b e (a-(2*b)), os quais os resultados são 6 e 0, nessa ordem. Como o resultado de (a-(2*b)) é 0 eliminamos o d pois seu 
# resultado também seria 0. Logo, 6*12 = 72.
print('b) (a+b)*c+d*(a-(2*b)) = ', B)

# c) 
C = [(2*a) + ((c-d)*2)]*2
# Primeiro calculamos c-d = 7. Em seguida, 2*a = 8 e 7*2 = 14. Logo, 8+14 = 22 e finalmente [22]*2 equivale a [22]+[22], que seria [22,22]
print('c) [(2*a) + ((c-d)*2)]*2 = ', C)

# d)
D = (x+y)*(x-y)
# Como podemos ver isso é um produto da soma pela diferença. Logo, x^2 - y^2. Substituindo tudo temos 6^2 - 8^2 = 36 - 64 = -28.
print('d) (x+y)*(x-y) =', D)