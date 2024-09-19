import math
import pandas as pd


# IMPLEMENTANDO TESTE DE T STUDENT





def main():
    # Parâmetros de exemplo

    amostra = [68, 70, 72, 65, 74, 73, 69, 71, 66, 68]
    
    u0 = 85 # H0 (Hipotese Nula)
    alfa = 0.05 # Nível de Significância
    media_amostra = sum(i for i in amostra) / len(amostra) # Média da amostra
   
    variancia_amostra = sum((i-media_amostra) ** 2 for i in amostra) / len(amostra) # Variância da amostra
    desvio_padrao_amostra = math.sqrt(variancia_amostra) # Desvio padrão da amostra
    tamanho_amostra = len(amostra) # Tamanho da amostra
    graus_liberdade = len(amostra) - 1 # Graus de liberdade da amostra


    tabela = pd.read_csv('tstudenttable.csv') # Lendo Tabela CSV
    tabela_tstudent = tabela[tabela['Graus de Liberdade'] <= graus_liberdade] # Filtrando a tabela T student a partir dos graus de liberdade
    valor_critico = tabela_tstudent[f'{alfa} (Bicaudal)'].values[graus_liberdade-1] # Valor crítico de 

    print(tabela_tstudent)
    print(valor_critico)


    estatistica_t = t_teste(media_amostra, u0, desvio_padrao_amostra, tamanho_amostra)
    print("==============================================")
    print(f"Estatistica de T: {estatistica_t}")
    print(f"Valor Critico: {valor_critico}")

    if abs(estatistica_t) <= valor_critico:
        print("Nao rejeitamos a H0(Hipotese Nula)\n")
        print(f"H0: u = u0 | {u0} nao eh significativamente diferente da media da amostra")
    else:
        print("Rejeitamos a H0(Hipotese Nula)\n")
        print(f"H1: u != u0 | {u0} eh significativamente diferente da media da amostra")

    return -1


# Função T_teste para calcular a estatística de t.
def t_teste(media_amostra, u0, desvio_padrao_amostra, tamanho_amostra):
    estatistica = (media_amostra - u0) / (desvio_padrao_amostra / math.sqrt(tamanho_amostra))
    return estatistica




if __name__ == '__main__':
    main()