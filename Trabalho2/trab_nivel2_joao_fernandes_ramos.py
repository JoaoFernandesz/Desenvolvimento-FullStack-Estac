# -*- coding: utf-8 -*-
"""trab_nivel2_joao_fernandes_ramos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w2ew5ei2b4rSKvfGgGqM1PU4nK2Z4hq6
"""

def conversor(num):
    """função que dado um número decimal retorna o valor dele em formato binário
       int -> int"""
     
    if num>= 1:
        conversor(num // 2)
    print(num % 2, end ='')
    return ""

num=int(input("Digite um numero decimal: "))
print(f"{conversor(num)} é a conversão do numero em Binario.")

