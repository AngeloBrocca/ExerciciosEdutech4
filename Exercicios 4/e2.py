p_probabilidade = float(input('Qual a probabilidade do item ser obtido? De 1 para quantos? '))
probabilidade = (1/p_probabilidade) * 100 
tentativas = int(input('Quantas vezes você derrotou o inimigo para tentar conseguir o item?'))

def calcula_chance(numero):
    calculo = (numero * tentativas)/ probabilidade
    return round(calculo)

resultado =  f"""
Para você ter 30% de chances de conseguir o item você deverá matar {calcula_chance(30)} inimigos no jogo.
Para você ter 40% de chances de conseguir o item você deverá matar {calcula_chance(40)} inimigos no jogo.
Para você ter 50% de chances de conseguir o item você deverá matar {calcula_chance(50)} inimigos no jogo.
Para você ter 60% de chances de conseguir o item você deverá matar {calcula_chance(60)} inimigos no jogo.
Para você ter 70% de chances de conseguir o item você deverá matar {calcula_chance(70)} inimigos no jogo.
Para você ter 80% de chances de conseguir o item você deverá matar {calcula_chance(80)} inimigos no jogo.
Para você ter 90% de chances de conseguir o item você deverá matar {calcula_chance(90)} inimigos no jogo.
Para você ter 95% de chances de conseguir o item você deverá matar {calcula_chance(95)} inimigos no jogo.
Para você ter 97% de chances de conseguir o item você deverá matar {calcula_chance(97)} inimigos no jogo.
"""

print(resultado)