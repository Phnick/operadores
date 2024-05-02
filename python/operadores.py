#Uso do End 'e'
t1 = t2 = True
f1 = f2 = False


if t1 and t2:
    print('Expressão verdadeira')
else:
    print('Expressão falsa')



# Uso do Or 'ou'

if f1 or f2:
    print('Expressão verdadeira')
else:
    print('Expressão falsa')


#Uso do not

if not t1:
    print('Expressão veradeira')
else:
    print('Expressão falsa') 


#Uso do in

lista = 'José, Pedro, Mariana, Marcelo, Tiago, Lucas'
nome_1 = 'Gabi'
nome_2 = 'Ju'

if nome_1 and nome_2 in lista:
    print(f'{nome_1} e {nome_2} estão na lista')
else:
    print(f'{nome_1} e {nome_2} não estão na lista')    


#Desafio1

primeiro_numero = int(input('Digite um número: '))
segundo_numero = int(input('Digite um número: '))

if primeiro_numero > segundo_numero:
    print(f'{primeiro_numero} é maior que {segundo_numero}')
else:
    print(f'{segundo_numero} é maior que {primeiro_numero}')



#desafio2

crescimento = float(input('Digite o percentual de crescimento'))
if crescimento > 0:
    print('Houve crescimento')
elif crescimento < 0:
    print('Houve um decrescimento')
else:
    print('Não houve alteração')       


#Desafio3
digite_letra = (input('Digite uma letra: '))
vogal = 'A,E,I,O,U'

if digite_letra in vogal:
    print(f'{digite_letra} é uma vogal')
else:
    print(f'{digite_letra} é uma consoante')    


#Desafio 4

preco_ano1 = float(input('Informe o valor médio de preço: '))
preco_ano2 = float(input('Informe o valor médio de preço: '))
preco_ano3 = float(input('Informe o valor médio de preço: '))


maior = preco_ano1
if preco_ano2 > maior:
    maior = preco_ano2
if preco_ano3 > maior:
    maior = preco_ano3


menor = preco_ano1
if preco_ano2 < menor:
    menor = preco_ano2
if preco_ano3 < menor:
    menor = preco_ano3


print(f'O preço mais alto foi de R$ {maior}')
print(f'O menos valor foi de R$ {menor}')

#Desafio 5
produto1 = float(input('Qual o valor do produto 1?: '))
produto2 = float(input('Qual o valor do produto 2?: '))
produto3 = float(input('Qual o valor do produto 3?: '))


if produto1 < produto2 and produto1 < produto3:
    print('O produto 1 é o mais barato')
if produto2 < produto1 and produto2 < produto3:
    print('O produto 2 é o mais barato')
if produto3 < produto1 and produto3 <produto2:
    print('O produto 3 é o mais barato')
if produto1 == produto2 == produto3:
    print(' Os produtos tem o mesmo preço')   

#Desafio 6 colocar os números em ordem decrescente 

numero1 = 10
numero2 = 30
numero3 = 55

if numero1 > numero2 and numero1 > numero3:
    print(numero1)
    if numero2 > numero3:
        print(numero2)
        print(numero3)
    else:
        print(numero3)
        print(numero2)    

elif numero2 > numero1 and numero2 > numero3:
    print(numero2)
    if numero1 > numero3:
        print(numero1)
        print(numero3)
    else:
        print(numero3)
        print(numero1) 

else:
    print(numero3)
    if numero1 > numero2:
        print(numero1)
        print(numero2)
    else:
        print(numero2)
        print(numero1)    

#Desafio 7

pessoa = (input('Qual turno você estuda?: '))
if pessoa == 'Manhã':
    print('Bom dia')
elif pessoa == 'Tarde':
    print('Boa tarde')
else:
    print('Boa Noite') 


#Desafio 8

num = int(input('Escreva um número inteiro: '))
if num % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')    











