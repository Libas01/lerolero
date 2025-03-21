#!/usr/bin/python3
'''GERADOR DE LERO LOUR GERA FRASES DE EFEITO''' 
from random import choice

parte1 = ["O sistema em desenvolvimento",
"O novo protocolo de comunicacao",
"O algoritmo de otimizacao"]
parte2 = ["possui excelente desempenho",
"oferece garantias de precisao acima da media",
"preenche uma lacuna significativa"]
parte3 = ["nas aplicacoes a que se destina",
"em relacao as opcoes disponiveis no mercado",
", provendo ampla vantagem competitiva a seus usuarios"]

lingua = int(input("escolha o linguini: 1 - portugues, 2 - ingles")

if lingua == 2:
    parte1 = []
    parte2 = []
    parte3 = []

print(choice(parte1),choice(parte2),choice(parte3))
