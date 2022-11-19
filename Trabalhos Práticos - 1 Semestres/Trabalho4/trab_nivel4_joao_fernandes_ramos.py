

from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


class Grafico:  
  def __init__(self, lista_despesas):
    self.lista_despesas=lista_despesas
    self.imprimir_graf()

  def padrao_do_grafico(self):
    plt.title('Gráficos de Despesas')    
    plt.ylabel('Despesas')
    plt.xlabel('Dias')

  def imprimir_graf(self):
    self.padrao_do_grafico()
    for gastos in self.lista_despesas:
      mLista = gastos.dicionario.items()
      cor = gastos.cor
      nome = gastos.nome
      x, y = zip(*mLista)
      plt.plot(x, y, label = nome, marker='o', markerfacecolor='black', markersize=12, color=cor, linewidth=4)
    plt.legend()
    plt.show()

  def regressao_linear(self, id_grafico):
    gastos = self.lista_despesas[id_grafico]
    mLista = gastos.dicionario.items()    
    cor = gastos.cor
    nome = gastos.nome
    dias, valores = zip(*mLista)
    dias = np.array(dias)
    valores = np.array(valores)
    dias = dias.reshape(-1, 1)
    valores = valores.reshape(-1, 1)
    regressao = LinearRegression()
    regressao.fit(X=dias, y=valores)
    plt.plot(dias, regressao.predict(dias), color='black', label = "Regressão Linear")

    x, y = zip(*mLista)
    plt.plot(x, y, label = nome+str(" - original"), marker='o', markerfacecolor='black', markersize=12, color=cor, linewidth=4)
    plt.legend()
    plt.show()



class Dicionario:

    def __init__(self, dicionario, cor, nome):
        self.dicionario = dicionario
        self.cor=cor
        self.nome = nome

qntd_dias = int(input("Escolha quantos dias deseja registrar: "))
qntd_despesas = int(input("Escolha quantos tipos de despesas deseja registrar: "))


lista_despesas = []
lista_despesas_str = []


for despesa in range(1,qntd_despesas+1):

  tipo_gasto = input(f"Qual o nome da despesa{despesa} a ser registrada: ")

  cor_gasto = input(f"Qual a cor da despesa{despesa} a ser representada: ")

  gasto_dia = {}


  for dia in range(1,qntd_dias+1):

    gasto = int(input(f"Coloque o valor de {tipo_gasto} que foi gasto no dia {dia}: "))

    gasto_dia[dia] = gasto


  lista_despesas_str.append(f"despesa{despesa}, " + tipo_gasto)

  globals()["despesa" + str(despesa)] = Dicionario(gasto_dia, cor_gasto, tipo_gasto)
  lista_despesas.append(globals()["despesa" + str(despesa)])

grafico = Grafico(lista_despesas)


print("Selecione o index da despesa que deseja ser representada com a regressão linear")
for despesa in range(qntd_despesas):
  print(f"{lista_despesas_str[despesa]} o index é {despesa}")

id_despesa = int(input())
grafico.regressao_linear(id_despesa)