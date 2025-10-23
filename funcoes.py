#Funçoes
#Exercício 1
def define_posicoes(linha, coluna, orientacao, tamanho):

    lista_final=[]
    
    
    #definir se vai se estabilizar em coluna
    if orientacao == 'horizontal':
        d_linha=0
        d_coluna=1
    else:            #definir se vai se estabilizar em linha
        d_linha=1
        d_coluna=0  

    i=0 #definir as posicoes pelo tamanho da embarcação
    while i< tamanho:
        
        nova_linha= linha+ i * d_linha
        nova_coluna= coluna + i * d_coluna
        lista_final.append([nova_linha, nova_coluna])
        i+=1
       


    return lista_final


#Exercicio 2
def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):

       
            posicao_final=define_posicoes(linha, coluna, orientacao, tamanho)
            if nome_navio not in frota:
                frota[ nome_navio]= [posicao_final]

            else:
               
                frota[ nome_navio].append(posicao_final)             

            return frota

#Exercicio 3
def faz_jogada (tabuleiro, linha, coluna):
     
    if tabuleiro[linha][coluna] == 1:
         tabuleiro[linha][coluna] = 'X'

    else:
          tabuleiro[linha][coluna] = '-'

    return tabuleiro

# Exercicio 4    
def posiciona_frota(frota):
    # cria um tabuleiro 10x10 só com 0
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]

    # percorre cada tipo de navio
    for lista_embarcacoes in frota.values():
        # percorre cada embarcação desse tipo
        for embarcacao in lista_embarcacoes:
            # percorre cada posição da embarcação
            for linha, coluna in embarcacao:
                tabuleiro[linha][coluna] = 1
    return tabuleiro

# Exercicio 5
def afundados(frota, tabuleiro):
    navios_afundados = 0
    # percorre cada tipo de navio
    for lista_embarcacoes in frota.values():
        # percorre cada embarcação desse tipo
        for embarcacao in lista_embarcacoes:
            # verifica se todas as posições dessa embarcação foram atingidas
            afundado = True
            for linha, coluna in embarcacao:
                if tabuleiro[linha][coluna] != 'X':
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1
    return navios_afundados

# Exercicio 6
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    # Usa a função para gerar as posições do novo navio
    posicoes_novo_navio = define_posicoes(linha, coluna, orientacao, tamanho)

    # Verifica se o navio cabe dentro do tabuleiro
    for l, c in posicoes_novo_navio:
        if l < 0 or l > 9 or c < 0 or c > 9:
            return False

    # Cria uma lista com todas as posições já ocupadas da frota existente
    posicoes_ocupadas = []
    for lista_embarcacoes in frota.values():
        for embarcacao in lista_embarcacoes:
            for pos in embarcacao:
                posicoes_ocupadas.append(pos)

    # Verifica se alguma posição do novo navio já está ocupada
    for pos in posicoes_novo_navio:
        if pos in posicoes_ocupadas:
            return False
    return True