import matplotlib.pyplot as plt
# import pandas as pd

# Funções do modelo Lotka-Volterra
def lotka_volterra_predador(x, y, a, b, c, d):
    return x * (a - b * y)

def lotka_volterra_presa(x, y, a, b, c, d):
    return y * (-c + d * x)

# Método de Heun
def metodo_heun(x0, y0, a, b, c, d, T, dt):
    time = [0]
    x_values = [x0]
    y_values = [y0]
    k1x_values = [0]
    k1y_values = [0]
    k2x_values = [0]
    k2y_values = [0]

    for _ in range(int(T / dt)):
        x_current = x_values[-1]
        y_current = y_values[-1]

        # Cálculo de k1
        k1_x = dt * lotka_volterra_predador(x_current, y_current, a, b, c, d)
        k1_y = dt * lotka_volterra_presa(x_current, y_current, a, b, c, d)

        # Previsão com Euler
        x_euler = x_current + k1_x
        y_euler = y_current + k1_y

        # Cálculo de k2
        k2_x = dt * lotka_volterra_predador(x_euler, y_euler, a, b, c, d)
        k2_y = dt * lotka_volterra_presa(x_euler, y_euler, a, b, c, d)

        # Correção com Heun
        x_next = x_current + 0.5 * (k1_x + k2_x)
        y_next = y_current + 0.5 * (k1_y + k2_y)

        time.append(time[-1] + dt)
        x_values.append(x_next)
        y_values.append(y_next)
        k1x_values.append(k1_x)
        k1y_values.append(k1_y)
        k2x_values.append(k2_x)
        k2y_values.append(k2_y)

    return time, x_values, y_values, k1x_values, k1y_values, k2x_values, k2y_values

# Parâmetros e condições iniciais
a = 0.20 # Taxa de crescimento de presas (coelhos) por ano
b = 0.001 # Taxa de predação por lince
c = 0.08 # Taxa de declinio dos predadores (lince) por ano
d = 0.001 # Taxa de crescimento dos predadores (lince) em relaçao á predação por (coelho * lince)/ano
x0 = 2 * 69.7 # População inicial de coelhos (milhares de coelhos por hectare)
y0 = 209 # População inicial de linces
T = 100 # Tempo total de simulação (anos)
dt = 1 # Passo de tempo (ano)

# Execução da simulação
tempo, coelhos, linces, k1x_values, k1y_values, k2x_values, k2y_values = metodo_heun(x0, y0, a, b, c, d, T, dt)

# Analises de resultados e uso de librarias externas

'''

# Criação de um DataFrame para armazenar os resultados da simulação
data = {
    'Tempo (anos)': tempo,
    'População de Coelhos (em milhares)': coelhos,
    'População de Linces': linces,
    'k1x': k1x_values,
    'k1y': k1y_values,
    'k2x': k2x_values,
    'k2y': k2y_values
}
df = pd.DataFrame(data)

# Grava a tabela num arquivo CSV
df.to_csv('populacoes.csv', index=False)

# Plots dos Gráficos

# Gráfico Dinamica Populacional Predador-Presa
plt.figure(figsize=(12, 6))
plt.plot(tempo, coelhos, label='Presas (Coelhos)')
plt.plot(tempo, linces, label='Predadores (Linces)')
plt.title('Dinâmica Populacional Predador-Presa')
plt.xlabel('Tempo (anos)')
plt.ylabel('População (em milhares para coelhos, unidades para linces)')
plt.legend()
plt.grid(alpha=0.1, linestyle='-')
plt.show(interactive=True)

# Gráfico das taxas de variação
plt.figure(figsize=(12, 6))
plt.plot(tempo, k1x_values, label='Taxa de Variação de Coelhos (k1x)')
plt.plot(tempo, k2x_values, label='Taxa de Variação de Coelhos (k2x)')
plt.plot(tempo, k1y_values, label='Taxa de Variação de Linces (k1y)')
plt.plot(tempo, k2y_values, label='Taxa de Variação de Linces (k2y)')
plt.title('Taxas de Variação das Populações')
plt.xlabel('Tempo (anos)')
plt.ylabel('Taxa de Variação')
plt.legend()
plt.grid(alpha=0.1, linestyle='-')
plt.show(interactive=True)

'''
