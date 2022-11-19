from faker import Faker
import random
import matplotlib.pyplot as plt
from num2words import num2words
from wordcloud import WordCloud

a = Faker('pt-BR')
with open('notas.txt', 'w') as arquivo:
  for i in range(10):
    notas=a.name()+', '+str(a.random_int(1,10))+' \n'
    arquivo.write(notas)

with open('notas.txt', 'r') as arquivo:
  lista_notas = []
  for line in range(10):
    lista = arquivo.readline()
    sep = lista.split(' ')
    lista_notas.append(int(sep[-2]))

plt.title('Histograma das Pontuações')
plt.xlabel('Pontuações')
plt.ylabel('Probabilidade')
plt.hist(lista_notas, density=True, rwidth=0.9)
plt.show()

nums = []
for i in lista_notas:
  notas = num2words(i, lang='pt-BR')
  nums.append(notas)
notas = (',').join(nums)
print(notas)

nuvem = WordCloud().generate(notas)
plt.imshow(nuvem, interpolation='bilinear')
plt.axis('off')
plt.show()
nuvem.to_file('nuvem_notas.png')

