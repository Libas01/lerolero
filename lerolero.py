#!/usr/bin/python3
# Repo: https://github.com/Libas01/lerolero
'''GERADOR DE LERO LOUR GERA FRASES DE EFEITO''' 
from random import choice

parte1 = ["O sistema em desenvolvimento",
        "O novo protocolo de comunicacao",
        "O algoritmo foi otimizado e"]
parte2 = ["possui excelente desempenho",
        "oferece garantias de precisao acima da media",
        "preenche uma lacuna significativa"]
parte3 = ["nas aplicacoes a que se destina",
        "em relacao as opcoes disponiveis no mercado",
        ", provendo ampla vantagem competitiva a seus usuarios"]

lingua = int(input("escolha o linguini: 1 - portugues, 2 - ingles")

if lingua == 2:
    parte1 = ["The system in development",
              "The new communication protocol",
              "The algorithm was optimized and"]
    parte2 = ["has excellent performance",
              "offers accuracy guarantees above average",
              "fills a significant gap"]
    parte3 = ["in the applications it is made for",
              "comparing to the available options in the market",
              ", providing vast competitive advantages to its users"]

print(choice(parte1),choice(parte2),choice(parte3))
