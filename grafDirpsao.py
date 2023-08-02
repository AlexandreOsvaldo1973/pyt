# importando a biblioteca
import matplotlib.pyplot as plt

# definido a função
def func_ter_grau(x, a=1, b=1, c=1, d=1): # função que recebe 5 parâmetros de entrada, sendo os 4 último opcionais com default = 1
    y = a*x**3 + b*x**2 + c*x + d
    return y

def func_sec_grau(x, a=1, b=1, c=1):
    y = a*x**2 + b*x + c
    return y

lista_x = range(-50, 50)
lista_y_3 = []
lista_y_2 = []

for i in lista_x:
    lista_y_3.append(func_ter_grau(i))
    lista_y_2.append(func_sec_grau(i))

# criando o gráfico
plt.plot(lista_x, lista_y_3, label='3Grau', color='green') # imprime linha
plt.plot(lista_x, lista_y_2, label='2Grau', color='blue') # imprime linha
#plt.scatter(lista_x, lista_y, color='red', marker='*') # imprime os pontos
plt.legend()

# criando legendas
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")

# criando título

plt.title("Gráfico de f(x)")

# impressão do gráfico

plt.show()