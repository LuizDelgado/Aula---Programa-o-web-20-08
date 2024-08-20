################### ESTRUTURAR DE CONDIÇÃO ###################
'''
=  -> Instanciando uma variavel ou objeto
== -> Comparação de valor
!= -> Diferente de
AND E OR
'''

# x = 10.7 #Variavel inteira com o valor de 10

# if x == 10:
#     print("O valor de x é igual a 10")

# elif x < 10: ##PRECISA DO IF
#     print("O seu número é menor que 10")

# else: ##PRECISA DO IF
#     print("O seu número é maior que 10")

################### ESTRUTURAR DE REPETIÇÃO DE UM LOOP CONTROLADO ###################
# for _ in range(1,11): ## partida -- chegada
#                       ##    1    --   10
#     print(_)
#     print("Luiz Henrique é mineiro")

# x = 20
# while True:
#     ### CRIAR UM LOOOP INFINITO ###
#     print("Luizinho é o melhor professor")
#     x += 1
#     print(x)
#     if x == 30:
#         break

'''
Desafio de hoje
Adivinhador de numeros
O jogo consiste em você tentar acertar um número aleatorio de 1 a 10
'''

#Importou as bibliotecas
import random 

#Gerou o número aleatório
numero_secreto = random.randint(1, 10)

#Lógica do Palpite
palpite = None

while palpite != numero_secreto:
    palpite = int(input("Tente adivinhar o número entre 1 e 10: "))
    if palpite < numero_secreto:
        print("Mais alto!")
    elif palpite > numero_secreto:
        print("Mais baixo")
    else:
        print("Você acertou o número!")
    




