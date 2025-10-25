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
        linha = int(input("Linha: "))
        coluna = int(input("Coluna: "))
        
        if nome_navio == "submarino": #A exceçao do submarino
            orientacao = "horizontal"
        
        else:
        
            orientacao= input('Orientação: [1] Vertical [2] Horizontal ')
            if orientacao == '1':
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'


        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho)
            i+=1
                
        else:
                print("Esta posição não está válida!")

# Exercício 8

# Frota do oponente:
frota_oponente = {
    'porta-aviões': [[[9,1],[9,2],[9,3],[9,4]]],
    'navio-tanque': [[[6,0],[6,1],[6,2]], [[4,3],[5,3],[6,3]]],
    'contratorpedeiro': [[[1,6],[1,7]], [[0,5],[1,5]], [[3,6],[3,7]]],
    'submarino': [[[2,7]], [[0,6]], [[9,7]], [[7,6]]]
}

tab_opp = posiciona_frota(frota_oponente)
tab_jog = posiciona_frota(frota)

# Roda o jogo:
while True:
    # Imprime os tabuleiros:
    monta_tabuleiros(tab_jog, tab_opp)
    # Pergunta e valida a linha:
    linha = int(input("Jogador, qual linha deseja atacar? "))
    while linha > 9 or linha < 0:
        print('Linha inválida!')
        linha = int(input("Jogador, qual linha deseja atacar? "))
    # Pergunta e valida a coluna:
    coluna = int(input("Jogador, qual coluna deseja atacar? "))
    while coluna > 9 or coluna < 0:
        print('Coluna inválida!')
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
    # Vê se é inédito:
    while tab_opp[linha][coluna] == 'X' or tab_opp[linha][coluna] == '-':
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        # Pergunta e valida a linha:
        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha > 9 or linha < 0:
            print('Linha inválida!')
            linha = int(input("Jogador, qual linha deseja atacar? "))
        # Pergunta e valida a coluna:
        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna > 9 or coluna < 0:
            print('Coluna inválida!')
            coluna = int(input("Jogador, qual coluna deseja atacar? "))
    # Aplica a jogada:
    faz_jogada(tab_opp, linha, coluna)
     # Verifica vitória:
    if afundados(frota_oponente, tab_opp) == 10:
        # Imprime o tabuleiro final e mensagem de vitória:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        break