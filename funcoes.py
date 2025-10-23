#Funçoes
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