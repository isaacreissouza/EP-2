#Exercicio 7

#Colocar as funçoes feitas do arquivo de funcoes.py
from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida, monta_tabuleiros
#O dicionario vazio da plataforma
frota = {
        "porta-aviões": [],
        "navio-tanque": [],
        "contratorpedeiro": [],
        "submarino": [],
    }

#Informaçoes do navio com tamanho e quantidade
navios_tam_qtd = [
    ("porta-aviões", 4, 1),
    ("navio-tanque", 3, 2),
    ("contratorpedeiro", 2, 3),
    ("submarino", 1, 4),
]

#Entrada de informaçoes paea o usuario e as informaçoes que ele irá digitar
for nome_navio, tamanho, quantidade in navios_tam_qtd:
    i=0
    while i< quantidade:
        print(f"Insira as informações referentes ao navio {nome_navio} que possui tamanho {tamanho}")
        linha = int(input())
        coluna = int(input())
        
        if nome_navio == "submarino": #A exceçao do submarino
            orientacao = "horizontal"
        
        else:
        
            orientacao= input() #Definiçao de escolha horizontal ou vertical
            if orientacao == '1':
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'


        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
            i+=1
                
        else:
                print("Esta posição não está válida!")

#imprime o dicionário frota
print(frota)

# Exercício 8

# Frota do oponente do enunciado:
frota_oponente = {
    'porta-aviões': [[[9,1],[9,2],[9,3],[9,4]]],
    'navio-tanque': [[[6,0],[6,1],[6,2]], [[4,3],[5,3],[6,3]]],
    'contratorpedeiro': [[[1,6],[1,7]], [[0,5],[1,5]], [[3,6],[3,7]]],
    'submarino': [[[2,7]], [[0,6]], [[9,7]], [[7,6]]]
}

tab_opp = posiciona_frota(frota_oponente)
tab_jog = posiciona_frota(frota)

# Verifica a quantia de tropas do inimigo:
total_navios = 0
for lista in frota_oponente.values():
    for navio in lista:
        total_navios = total_navios + 1

# Loop que faz o jogo rodar:
while True:
    monta_tabuleiros(tab_jog, tab_opp)

    linha = input('Qual linha deseja atacar? ')
    coluna = input('Qual coluna deseja atacar? ')

    # Vê se linha e coluna são números válidos:
    if linha == '' or coluna == '':
        print('Linha ou coluna inválida!')
        continue

    linha = int(linha)
    coluna = int(coluna)

    if linha < 0 or linha > 9:
        print('Linha inválida!')
        continue
    if coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        continue

    # Checa se já jogou na posição:
    if str(tab_opp[linha][coluna]) == 'X' or str(tab_opp[linha][coluna]) == '-':
        print('A posição linha', linha, 'e coluna', coluna, 'já foi informada anteriormente!')
        continue

    # Faz a jogada acontecer:
    if tab_opp[linha][coluna] == 1:
        print('Acertou!')
    else:
        print('Água!')

    faz_jogada(tab_opp, linha, coluna)

    # Vê se as condições pra vitória foram atingidas:
    if afundados(frota_oponente, tab_opp) == total_navios:
        monta_tabuleiros(tab_jog, tab_opp)
        print('Parabéns! Você derrubou seu oponente!')
        break