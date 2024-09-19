import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Dados da amostra (pesos em kg)
amostra = [68, 70, 72, 65, 74, 73, 69, 71, 66, 68]

# Definir a média hipotética (H0: a média é 70 kg)
media_hipotetica = 150

# Passo 1: Calcular a média e o desvio padrão da amostra
media_amostra = np.mean(amostra)
desvio_padrao_amostra = np.std(amostra, ddof=1)

# Passo 2: Realizar o teste t para uma amostra
t_stat, p_valor = stats.ttest_1samp(amostra, media_hipotetica)

# Resultados
print(f"Média da amostra: {media_amostra:.2f}")
print(f"Desvio padrão da amostra: {desvio_padrao_amostra:.2f}")
print(f"Estatística t: {t_stat:.4f}")
print(f"P-valor: {p_valor:.4f}")

# Decisão com base em α = 0.05
alpha = 0.05
if p_valor < alpha:
    print("Rejeitamos a hipótese nula. A média é significativamente diferente de 68.")
else:
    print("Não rejeitamos a hipótese nula. A média não é significativamente diferente de 68.")

# Gráfico visualizando a distribuição t
x = np.linspace(-4, 4, 1000)
t_dist = stats.t.pdf(x, df=len(amostra)-1)
plt.plot(x, t_dist, label='Distribuição t')
plt.axvline(t_stat, color='red', linestyle='--', label='t observado')
plt.legend()
plt.title('Distribuição t com t observado')
plt.show()
