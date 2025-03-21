#!/usr/bin/python3
'''GERADOR DE LERO LOUR GERA FRASES DE EFEITO''' 
from random import choice

parte1 = ["O sistema em desenvolvimento",
"O novo protocolo de comunicacao",
"O algoritmo otimizado"]
parte2 = ["possui excelente desempenho",
"oferece garantias de precisao acima da media",
"preenche uma lacuna significativa"]
parte3 = ["nas aplicacoes a que se destina",
"em relacao as opcoes disponiveis no mercado",
", provendo ampla vantagem competitiva a seus usuarios"]

print(choice(parte1),choice(parte2),choice(parte3))
