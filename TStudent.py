import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


# IMPLEMENTANDO TESTE DE T STUDENT



def tstudent(amostra, u0, alfa, tipo_teste, cauda="D"):

    

    tamanho_amostra = len(amostra) # Tamanho da amostra
    graus_liberdade = tamanho_amostra - 1 # Graus de liberdade da amostra

    media_amostra = sum(i for i in amostra) / tamanho_amostra # Média da amostra

    variancia_amostra = sum((i-media_amostra) ** 2 for i in amostra) / (graus_liberdade) # Variância da amostra
    desvio_padrao_amostra = math.sqrt(variancia_amostra) # Desvio padrão da amostra]



    tabela = pd.read_csv('tstudenttable.csv') # Lendo Tabela CSV
    tabela_tstudent = tabela[tabela['Graus de Liberdade'] == graus_liberdade] # Filtrando a tabela T student a partir dos graus de liberdade
    valor_critico = tabela_tstudent[f'{alfa} ({tipo_teste})'].values[0] # Valor crítico de T

    print(tabela_tstudent)
    print(valor_critico)


    estatistica_t = t_teste(media_amostra, u0, desvio_padrao_amostra, tamanho_amostra)
    print("==============================================")
    print(f"Estatistica de T: {estatistica_t}")
    print(f"Valor Critico: {valor_critico}")
    print(f"Média da Amostra: {media_amostra}")

    if (tipo_teste == "Unilateral") and (cauda == "D"):
        if estatistica_t > valor_critico:
            print("Rejeitamos a H0(Hipotese Nula)\n")
            print(f"H1: u > u0 | A media da amostra eh significativamente maior que a media hipotetica: {u0}")
        else:
            print("Nao rejeitamos a H0(Hipotese Nula)\n")
            print(f"H0: u = u0 | A media da amostra nao eh significativamente maior que a media hipotetica: {u0}")

    elif(tipo_teste == "Unilateral") and (cauda == "E"):
        if estatistica_t < valor_critico:
            print("Rejeitamos a H0(Hipotese Nula)\n")
            print(f"H1: u < u0 | A media da amostra eh significativamente menor que a media hipotetica: {u0}")
        else:
            print("Nao rejeitamos a H0(Hipotese Nula)\n")
            print(f"H0: u = u0 | A media da amostra nao eh significativamente menor que a media hipotetica: {u0}")
    else:
        if abs(estatistica_t) > valor_critico:
            print("Rejeitamos a H0(Hipotese Nula)\n")
            print(f"H1: u != u0 | A media da amostra eh significativamente diferente que a media hipotetica: {u0}")
        else:
            print("Nao rejeitamos a H0(Hipotese Nula)\n")
            print(f"H0: u = u0 | A media da amostra nao eh significativamente diferente que a media hipotetica: {u0}")



    plot_t_distribution(graus_liberdade, estatistica_t, tipo_teste, cauda, valor_critico)

    return -1


# Função T_teste para calcular a estatística de t.
def t_teste(media_amostra, u0, desvio_padrao_amostra, tamanho_amostra):
    estatistica = (media_amostra - u0) / (desvio_padrao_amostra / math.sqrt(tamanho_amostra))
    return estatistica



# Função para plotar a distribuição t e a região crítica
def plot_t_distribution(graus_liberdade, estatistica_t, tipo_teste, cauda, valor_critico):
    # Valores de x para a distribuição t
    x = np.linspace(-4, 4, 1000)
    
    # Calcula a distribuição t
    y = stats.t.pdf(x, graus_liberdade)
    
    # Plotando a curva da distribuição t
    plt.plot(x, y, label='Distribuição t')

    # Definindo as regiões críticas
    if tipo_teste == "Unilateral":
        if cauda == "D":
            x_critico = np.linspace(valor_critico, 4, 100)
            plt.fill_between(x_critico, 0, stats.t.pdf(x_critico, graus_liberdade), color='red', alpha=0.5, label='Região Crítica Direita')
            plt.text(valor_critico, 0.02, 'RC', color='black', fontsize=12)
            
        elif cauda == "E":
            x_critico = np.linspace(-valor_critico, -4, 100)
            plt.fill_between(x_critico, 0, stats.t.pdf(x_critico, graus_liberdade), color='red', alpha=0.5, label='Região Crítica Esquerda')
            plt.text(-valor_critico - 0.12, 0.02, 'RC', color='black', fontsize=12)
    else:
        # Região crítica para teste bicaudal
        x_critico_esq = np.linspace(-valor_critico, -4, 100)
        x_critico_dir = np.linspace(valor_critico, 4, 100)
        plt.fill_between(x_critico_esq, 0, stats.t.pdf(x_critico_esq, graus_liberdade), color='red', alpha=0.5, label='Região Crítica Esquerda')
        plt.fill_between(x_critico_dir, 0, stats.t.pdf(x_critico_dir, graus_liberdade), color='red', alpha=0.5, label='Região Crítica Direita')
        plt.text(valor_critico, 0.02, 'RC', color='black', fontsize=12)
        plt.text(-valor_critico - 0.12, 0.02, 'RC', color='black', fontsize=12)
    
    # Plotando a estatística t encontrada
    plt.axvline(estatistica_t, color='blue', linestyle='--', label=f'Estatística t: {estatistica_t:.2f}')

    # Ajustes do gráfico
    plt.title('Distribuição t e Região Crítica')
    plt.xlabel('Valores de t')
    plt.ylabel('Densidade de Probabilidade')
    plt.legend()
    plt.grid(True)
    plt.show()




