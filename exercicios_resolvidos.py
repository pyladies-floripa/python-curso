######################
#
# Faça um Programa que mostre a mensagem "Alo mundo" na tela.
#
######################

# Forma 1

print("Alo mundo")

# Forma 2 (criando uma função)

def oi():
	print("Alo mundo") 

# Uso da função

oi()

######################
#
# Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]."
#
######################

#Forma 1
numero = input("Digite um numero: ")
print("O numero informado foi: ")

# Forma 2 (criando uma função)
def programa(numero):
	print("O numero informado foi" + numero)

# uso da função

programa(2)

######################
#
# Faça um Programa que peça dois números e imprima a soma.
#
######################

# Forma 1
numero1 = input("Digite um numero: ")
numero2 = input("Digite outro numero: ")
soma = int(numero1)+int(numero2)
print("A soma de ambos os numeros é: " + str(soma))

# Forma 2 (criando uma função)
def soma(numero1, numero2):
	soma=int(numero1)+int(numero2)
	print("A soma de ambos os numeros é: " + str(soma))
	return soma

# uso da função
soma(1,2)

######################
#
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
#
######################

# Forma 1 
numero1 = input("Digite um numero: ")
numero2 = input("Digite outro numero: ")
numero3 = input("Digite outro numero: ")
numero4 = input("Digite outro numero: ")
media = (numero1+numero2+numero3+numero4)/4
print("A media das notas é: " + str(media))

# Forma 2
def media(numero1, numero2, numero3, numero4):
	media = (numero1+numero2+numero3+numero4)/4
	print("A media das notas é: " + str(media))
	return media
