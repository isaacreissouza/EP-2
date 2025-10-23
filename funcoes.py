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