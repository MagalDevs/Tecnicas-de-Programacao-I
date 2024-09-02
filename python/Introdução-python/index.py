# Isso é um comentário
valor = 42 # Isso é um comentário após um comando
def soma(a, b):
 """
 Função para somar dois números.
 
 Args:
 a (float): O primeiro número.
 b (float): O segundo número.
 
 Returns:
 float: A soma dos dois números.
 """
 return a + b

import math
import random as rd
# imprime o valor de PI
print(math.pi)
# imprime o valor de RAIZ de 2
print(math.sqrt(2))
# gera um número aleatório entre 0 e 10
print(rd.randint(0,10))

# Variável inteira
idade = 25 
# Variável de ponto flutuante
altura = 1.75 
# Variável de caractere 
letra = 'A'

idade = 25
altura = 1.75 
letra = 'A'
print(type(idade))
print(type(altura))
print(type(letra))

idade = 25
print('Olá, mundo!')
print('idade:',idade)

altura = 1.76
print(f'A altura é {altura} e a idade é {idade}')

print('A altura é ',altura,' e a idade é',idade)
print('A altura é ',altura,' e a idade é',idade,sep='|')

# lê uma string
nome = input("Digite seu nome: ")
# lê e converte para inteiro
idade = int(input("Digite sua idade: "))
print(f'Seu nome é {nome} e sua idade é {idade}')

x = 10
y = 20
z = x * y
print("z = ",z)
z = y/10
print("z = ",z)
print("x+y = ",x+y)

x = 5
y = 3
print("Expressão 1: ",x > 4)
print("Expressão 2: ",x == 4)
print("Expressão 3: ",x != y)
print("Expressão 4: ",x != y+2)

x = 5
y = 3
r = (x > 2) and (y < x)
print("Resultado: ",r)
r = (x%2==0) and (y > 0)
print("Resultado: ",r)
r = (x > 2) or (y > x)
print("Resultado: ",r)
r = (x%2==0) or (y < 0)
print("Resultado: ",r)
r = not(x > 2)
print("Resultado: ",r)
r = not(x > 7) and (x > y)
print("Resultado: ",r)

#if
x = int(input("Digite um valor inteiro: "))
if x % 2 == 0:
 print("O valor de “,x,” é par")
print("Fim do programa")

x = int(input("Digite um valor inteiro: "))
if x % 2 == 0:
 print(" valor de “,x,” é par")
else:
 print("O valor de “,x,” é impar")
print("Fim do programa")

x = int(input("Digite um valor inteiro: "))
if x % 2 == 0:
 print("O valor de “,x,” é par")
else:
 print("O valor de “,x,” é impar")
print("Fim do programa")

x = int(input("Digite um valor inteiro: "))
if x == 0:
 print("O valor de “,x,” é igual a zero")
elif x > 0:
 print("O valor de “,x,” é positivo")
else:
 print("O valor de “,x,” é negativo")
print("Fim do programa")

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
while a <= b:
    print(a)
    a = a + 1
print("Fim do programa")