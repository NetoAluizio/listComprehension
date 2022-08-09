# -*- coding: utf-8 -*-
"""listComprehensionExercicio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ae_D0kxWHF1RHHBdQBoMhpgjAVbcYmnN
"""

"""exemplo de utilização de list comprehension 
para criar listas a partir de uma string"""
# utilizando laço for 
str = '012345678901234567890123456789012345678901234567890123456789'
lista = []
for i in range(0, len(str), 10):
  lista.append(str[i:i+10])

print(lista)

nova_lista = '.'.join(lista)
print(nova_lista)

# usando list comprehension
str = '012345678901234567890123456789012345678901234567890123456789'
lista2 = [(str[i:i+10]) for i in range(0, len(str), 10)]
nova_lista2 = '.'.join(lista) 
print(lista2)
print(nova_lista2)

