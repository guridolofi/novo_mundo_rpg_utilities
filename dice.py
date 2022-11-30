from random import randint

def roll(qtd = 1, sides = 6):
    sides = qtd*sides
    result = randint(qtd, sides)
    return result