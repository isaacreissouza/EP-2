#Exercicio 7

#Colocar as funçoes feitas do arquivo de funcoes.py
from funcoes import define_posicoes, preenche_frota, faz_jogada, posiciona_frota, afundados, posicao_valida
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