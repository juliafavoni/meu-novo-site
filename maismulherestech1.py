### Aqui eu vou anotar todos os conteúdosdo curso para auxiliar no desafio
'''
Essa é outra forma de fazer comentários + longos
'''

# Para fazer comentários
print('Olá mundo!')

# Variáveis
'''
int = 1
float = 1.5
string = 'Julia'
bool = True, False
'''

# input - entrada
numero = int(input("Digite um número: "))
print(numero)

# Divisão inteira
print(9//2)

# incremento
valor1 = 5
valor1 += 1
print(valor1)

# decremento
valor2 = 5
valor2 -= 1
print(valor2)

# resto %
print(10%2)

## Operadores relacionais
# == igual
# != diferentes

# Definir o numero de casas após a vírgula
valor3 = 4.123456789
print(f"{valor3:.9f}")

print('Olá {}, você tem {} anos'.format("Júlia", 21))

# Estruturas condicionais = if, else, elif
idade = int(input("Qual sua idade? "))
if idade > 17:
    print("Maior de idade")
else:
    print("Você é menor de idade")

# while - laço de repetição
while idade < 17:
    idade = int(input("Digite outra idade: "))

# for - para cada - loop infinito
frutas = ['maca', 'banana', 'uva'] # declarando uma lista
for fruta in frutas:
    print(fruta)

### Listas, tuplas, dicionários

# Lista
lista_frutas = ['morango']

# adicionar + um item na lista:
fruta_adicionada = input('Digite uma fruta: ')
lista_frutas.append('Maçã')
lista_frutas.append('Uva')
lista_frutas.append(fruta_adicionada)

print(lista_frutas)

# Tuplas = os valores não podem ser alterados

tupla_compras = ("Café", "ovo", "macarrão")
print(tupla_compras)

# Dicionários = consegue adicionar valores a significados, tem algumas funções prontas dentro dos dicionários

dicionario = {'Chave': 'Valor'}
dicionario['maca'] = 'é uma fruta'
dicionario['carro'] = 'é um veículo'
print(dicionario)



### Funções: grupo de instruções relacionadas que executa uma tarefa

# declaração
def soma():
    calculo = 10 + 2
    print(f"O resultado da soma é: {calculo}")

def subtração():
    sub = 10 - 2 # a variável não pode ter o mesmo nome da função
    print(f"O resultado da subtração é {sub}")


# chamada da função
soma() 

### Manipulação de arquivos

# Abertura para escrita
arquivo_escrita = open(file, "w")
arquivo_escrita.write("Texto a ser escrito")
arquivo_escrita.close()

# Abertura de arquivos binários
arquivo_binario = open(file, "wb")


# Leitura
# Abertura somente para leitura
arquivo_leitura = open(file, "r")
leitura = arquivo_leitura.read()
print(leitura)
arquivo_leitura.close()

### Tratamento de exceções

def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
    except ZeroDivisionError:
        print("Erro: Impossível dividir valor por zero")
    except TypeError as e:
        print(f"Erro: O tipo do dado informado está incorreto. \n Detalhes: {e}")

divisao(10,0)
