# 56) Crie um programa que leia vários números pelo teclado e mostre no final o
# somatório entre eles.
# Obs: O programa será interrompido quando o número 1111 for digitado

soma = 0

while True:
    numero = int(input("Digite um número (1111 para sair): "))
    if numero == 1111:
        break
    soma += numero

print(f"A soma dos números digitados é: {soma}")

# 57) Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários.
# No final, mostre o total de salários pagos aos homens e o total pago às
# mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não
# sempre que ler os dados de um funcionário.

soma_mulheres = 0
soma_homens = 0

while True:
    salario = int(input("Qual o salário? "))
    sexo = input("Qual o sexo (F/M)? ")
    if sexo == "F":
        soma_mulheres += salario
    else:
        soma_homens += salario
    continuar = input("Você deseja continuar (S/N)? ").lower
    if "N":
        break


# 58) Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa
# vai parar quando for digitada a idade 999. No final, mostre quantos alunos
# existem na turma e qual é a média de idade do grupo.
# - - - - -

# 59) Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai
# perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
# a) qual é a maior idade lida
# b) quantos homens foram cadastrados
# c) qual é a idade da mulher mais jovem
# d) qual é a média de idade entre os homens
# - - - - -

# 60) Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas.
# O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A média de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos
# - - - - -
