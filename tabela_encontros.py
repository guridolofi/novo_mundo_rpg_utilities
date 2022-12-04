from random import choice
from dice import roll



def encontro(tipo = 'normal', area = 'planicie'):

    d100 = roll(1, 100)
    tipo = tipo
    area = area
    
    encontro_aldeao = tipo == 'dominio' and d100 < 43 or tipo == 'normal' and d100 < 34 or\
        tipo == 'perigoso' and d100 < 22 or tipo == 'extremo' and d100 < 10
    encontro_guarda = tipo == 'dominio' and 43 <= d100 < 59 or tipo == 'normal' and 34 <= d100 < 42 or\
        tipo == 'perigoso' and 22 <= d100 < 27 or tipo == 'extremo' and 10 <= d100 < 12
    encontro_bandido = tipo == 'dominio' and 59 <= d100 < 75 or tipo == 'normal' and 42 <= d100 < 58 or\
        tipo == 'perigoso' and 27 <= d100 < 45 or tipo == 'extremo' and 12 <= d100 < 32
    encontro_animais = tipo == 'dominio' and 75 <= d100 < 87 or tipo == 'normal' and 58 <= d100 < 75 or\
        tipo == 'perigoso' and 45 <= d100 < 65 or tipo == 'extremo' and 32 <= d100 < 52
    encontro_monstros = tipo == 'dominio' and 87 <= d100 < 95 or tipo == 'normal' and 75 <= d100 < 92 or\
        tipo == 'perigoso' and 65 <= d100 < 85 or tipo == 'extremo' and 52 <= d100 < 82
    encontro_eventos = tipo == 'dominio' and 95 <= d100 or tipo == 'normal' and 92 <= d100 or\
        tipo == 'perigoso' and 85 <= d100 or tipo == 'extremo' and 82 <= d100
    
    
    if encontro_aldeao:
        pass
    elif encontro_guarda:
        pass
    elif encontro_bandido:
        pass
    elif encontro_animais:
        pass
    elif encontro_monstros:
        pass
    elif encontro_eventos:
        pass