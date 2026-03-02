import random

# Primeiro projeto - Máquina caça-níqueis

# costantes globais
MAXIMO_LINHAS = 3
MAXIMO_APOSTA = 100
MINIMO_APOSTA = 1

LINHAS = 3
COLUNAS = 3

contagem_de_simbolos = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

valores_de_simbolos = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def checar_vitorias(colunas, lines, aposta, valores):
    vitorias = 0
    linhas_vitoriosas = []
    for line in range(lines):
        simbolo = colunas[0][line]
        for coluna in colunas:
            simbolo_para_checar = coluna[line]
            if simbolo != simbolo_para_checar:
                break
        else:
            vitorias += valores[simbolo] * aposta
            linhas_vitoriosas.append(line + 1) 
            
    return vitorias, linhas_vitoriosas

def get_giro_caca_niqueis(linhas, cols, simbolos):
    todos_os_simbolos = []
    for simbolo, contagem_de_simbolos in simbolos.items():
        for _ in range(contagem_de_simbolos):
            todos_os_simbolos.append(simbolo)
            
    # lista de colunas      
    colunas = []
    for _ in range(cols):
        coluna = []
        simbolos_atuais = todos_os_simbolos[:] # ':' gera uma copia do vetor, que pode ser modificada sem afetar o original
        for _ in range(linhas):
            valor = random.choice(simbolos_atuais)
            simbolos_atuais.remove(valor)
            coluna.append(valor)
            
        colunas.append(coluna)
        
    return colunas

def print_caca_niqueis(colunas):
    for linha in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) - 1:
                print(coluna[linha], end=" | ")
            else:
                print(coluna[linha], end="")
                
        print()
        
def deposito(): 
    while True:
        quantidade = input("Quanto você gostaria de depositar? R$")
        if quantidade.isdigit():
            quantidade = int(quantidade)
            if quantidade > 0:

                break
            else:
                print("Quantidade depositada deve ser maior que 0.")
        else:
            print("Insira um número, por favor.")

    return  quantidade

def get_numero_de_linhas():
    while True:
        linhas = input("Insira o número de linhas para apostar (1-" + str(MAXIMO_LINHAS) + ") ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAXIMO_LINHAS:
                break
            else:
                print("Insira um valor válido de linhas.")
        else:
            print("Insira um número, por favor.")
            
    return  linhas

def get_aposta():
    while True:
        quantidade = input("Quanto você gostaria de apostar em cada linha? R$")
        if quantidade.isdigit():
            quantidade = int(quantidade)
            if MINIMO_APOSTA <= quantidade <= MAXIMO_APOSTA:
                break
            else:
                print(f"Quantidade apostada deve estar entre R${MINIMO_APOSTA} - R${MAXIMO_APOSTA}.")
        else:
            print("Insira um número, por favor.")

    return  quantidade

def giro(balanco):
    linhas = get_numero_de_linhas()
    while True:
        aposta = get_aposta()
        total_aposta = aposta * linhas
        
        if total_aposta > balanco:
            print(f"Você não tem fundos o suficientes para apostar essa quatidade, seu saldo atual é de R${balanco}.")
        else:
            break
        
    print(f"Você está apostando R${aposta} em {linhas} linhas. Aposta total é igual a: R${total_aposta}")
    
    vagas = get_giro_caca_niqueis(LINHAS, COLUNAS, contagem_de_simbolos)
    print_caca_niqueis(vagas)
    vitorias, linhas_vitoriosas = checar_vitorias(vagas, linhas, aposta, valores_de_simbolos)
    print(f"Você ganhou R${vitorias}.")
    print(f"Você ganhou nas linhas: ", *linhas_vitoriosas)
    return vitorias - total_aposta

def principal():
    balanco = deposito()
    while True:
        print(f"Saldo atual e R${balanco}")
        escolha = input("Pressione enter para jogar (q para sair).")
        if escolha == "q":
            break
        balanco =+ giro(balanco)
        
    print(f"Você saiu com R${balanco}")
            
principal()