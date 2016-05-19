#################################################################
#																#
#	Este script é complementar a Aula 1 das Pyladies Floripa	#
#																#
#################################################################

# Isto é um comentário e não será processado

# Criando uma variável do tipo inteiro
minhaVariavel = 12 #comentários também podem ser feitos depois de um código

#Aqui estou pedindo para aparecer na tela o tipo da minha variavel
print(type(minhaVariavel))

#Criando uma variável do tipo decimal
valor = 1.0

#Aqui estou pedindo para aparecer na tela o tipo da minha variavel
print(type(valor))

#criando uma variável do tipo string
nome = 'pyladies'

#Aqui estou pedindo para aparecer na tela o tipo da minha variavel
print(type(nome))

#Aqui vamos testar se uma variável de string e uma variavel do tipo inteiro podem ser equiparadas
num1 = 10
num2 = '10'

print(num1==num2) #pedindo para mostrar uma comparação


#Criando uma lista
lista = [1, 2.0, '3', [4, 5, 6]]

#Acessando elementos de uma lista
lista[0] #primeiro valor
litsa[3] #ultimo valor
lista[-1] #também é o último valor!
lista[3][1] #Acessa o elemento 1 dentro da lista que esta contida na posicao 3 da lista inicial

#Funções que podem ajudar as listas

#tamanho da lista
tamanhoLista = len(lista)

#Adicionar novo elemento no final da lista
lista.append(99)

#É possível achar o mais valor dentro de uma lista numérica
lista2 = [2, 33, 142, 2, 32, 9, 15, 61]

#achando o valor maximo contido na lista
max(lista2)

#achando o valor mínimo contido na lista
min(lista2)

#Criando um dicionário
dic = {'pyladies': 999, 'floripa':'ilhadamagia', 2: [1, 2, 3]}

#Acessando valores de um dicionário
dic['pyladies']
dic['floripa']
dic[2]

#Exercicio 1: Faça parecer Oi, Pyladies
print('Oi, Pyladies!')

#Exercicio 2: Faça um programa que converta de centímetros para metros
valor_Cm = input('Digite seu valor em cm: ')
valor_Cm = int(valor_Cm)
print(valor_cm/100)

#Exercício 3: Faça um programa que peça um nome e um telefone e faça uma lista telefônica
listatel = {}
nome = raw_input('Digite o nome: ')
telefone = raw_input('Digite o telefone: ')
lista_telefonica[nome] = telefone




