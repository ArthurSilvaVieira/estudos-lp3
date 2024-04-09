# Função

# Quero somar uma lista de números
# usar a função sum()

# Quero calcular a média de notas dos alunos
# 1. tem no python?
# 2. alguém já programou (copiar ou adicionar dependencia)
# 3. declarar

# 1. Declaração

# def_nome_funcao(parâmetro1, parametro2):
#   return valor 

# 2. Chamada

print('Olá')
sum([1, 3, 5])

# nome_funcao('dad', 1)

# Função sem retorno e sem parâmetros

def imprimir_mensagem():
    print('Socorrro !')

imprimir_mensagem()
imprimir_mensagem()

# Função sem retorno com parâmetros
# parâmetros vs argumentos

def saudacoes(nome):
    print(f'Bom dia {nome}')

saudacoes('Maria')
saudacoes('José')

# argumento para parâmetro nome 'Maria'
saudacoes('Maria')

# argumento para parâmetro nome 'José da Silva'
nome_completo = 'José da Silva'
saudacoes(nome_completo)

# Função com retorno e sem parâmetros
def obter_mensagem():
    return 'Socorro!'

mensagem = obter_mensagem()
print(mensagem)

print(obter_mensagem())

# Função com retorno com parâmetros
def gerar_saudacao(nome):
    return f'Bom dia {nome}'

print(gerar_saudacao('Pedro'))
print(gerar_saudacao('João'))

# retorno   parâmetro
#  não         não
#  não         sim
#  sim         não
#  sim         sim  (adequado) (função pura)

# Imprimir saudação 
# Saudacao = frase (dinâmica) nome (dinâmico)
# "Bom dia Pedro"
# "Bom tarde Maria"
# "Bom noite Maria"


def saudacao(nome, frase):
    print(f'{frase} {nome}')

saudacao('João', 'Bom dia')

def saudacao(nome, frase):
    return(f'{frase} {nome}')

print(saudacao('João', 'Bom dia'))

# Enviar email saudacao
# Criar uma carta em pdf

# Entrada 
notas_alunos = [
    [9.0, 7.0, 3.0],
    [0.0, 1.0, 3.0],
    [10.0, 3.0, 3.0],
]

# Saída [5.5, 1.0, 6.6]

def calcular_media(notas):
    return sum(notas) / len(notas)


def calcular_media_alunos(notas_alunos):

    # medias = []
    # for notas in notas_alunos:
    #     media = calcular_media(notas)
    #     medias.append(media)

    #     return medias
    return [calcular_media(notas) for notas in notas_alunos]


def imprimir_medias(notas_alunos):
    medias = calcular_media_alunos(notas_alunos)
    print(medias)

def enviar_media_por_email(notas_alunos):
    medias = calcular_media_alunos(notas_alunos)
    # lógica de enviar por email as medias

imprimir_medias(notas_alunos)
enviar_media_por_email(notas_alunos)

#  Argumentos nomeados

def saudacao(nome, frase):
    return(f'{frase} {nome}')

print(saudacao('João', 'Bom dia'))
print(saudacao(name = 'João', frase = 'Bom dia'))
print(saudacao(frase = 'João', nome = 'Bom dia'))
print(saudacao('João', nome = 'Bom dia'))

# Parâmetro com valor padrão (default)
def saudacao(nome, frase = 'Bom dia'):
    return f'{frase} {nome}'

print(saudacao('João'))
print(saudacao('João', 'Bom tarde'))



