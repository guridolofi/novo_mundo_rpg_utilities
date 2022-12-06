from dice import roll
import sqlite3


def busca_monstro(nome):
    
    conexao = sqlite3.connect('banco_de_monstro.db')
    cursor = conexao.cursor()

    cursor.execute(f'SELECT nome, qtd_min, qtd_max FROM monstros WHERE nome == "{nome}"')

    dados = ()
    for linha in cursor.fetchall():
        dados += linha
        
    cursor.close()
    conexao.close()
    
    print(dados)
    return dados
    
def gera_distancia(area):
    
    retorno = ''
    
    if area == 'aberto':
        distancia = (roll(4,6))*10
        retorno = f'Em uma distancia de {distancia}'
    
    elif area == 'fechado':
        distancia = (roll(1,6))*10
        retorno = f'Em uma distancia de {distancia}'
    
    elif area == 'masmorra' or 'cidade_dia':
        distancia = (roll(1,6))*3
        retorno = f'Em uma distancia de {distancia}'
    
    elif area == 'cidade_noite':
        distancia = (roll(1,6))*10
        retorno = f'Em uma distancia de {distancia}'
    
    else:
        retorno = f'Em uma distancia proxima.'
        
    return retorno
    


def gera_monstro(area = 'planicie'):
    area = area
    d100 = roll(1, 100)
    retorno = f'Aventureiros Encontram '
    if area == 'planicie':
        if d100 < 43:
            dados = busca_monstro('Goblin')
            retorno += f'{roll(dados[1], dados[2])} {dados[0]}. {gera_distancia("aberto")} metros.'
        elif 43 <= d100 < 73:
            dados = busca_monstro('Gnoll')
            retorno += f'{roll(dados[1], dados[2])} {dados[0]}. {gera_distancia("aberto")} metros.'
        elif 73 <= d100 < 85:
            dados = busca_monstro('Besouro de Fogo Gigante')
            retorno += f'{roll(dados[1], dados[2])} {dados[0]}. {gera_distancia("aberto")} metros.'
        elif 85 <= d100 < 86:
            dados = busca_monstro('Golem de Pedra')
            retorno += f'{roll(dados[1], dados[2])} {dados[0]}. {gera_distancia("aberto")} metros.'
        elif 86 <= d100 < 89:
            dados = busca_monstro('Troll')
            retorno += f'{roll(dados[1], dados[2])} {dados[0]}. {gera_distancia("aberto")} metros.'
        elif 89 <= d100 < 99:
            dados = busca_monstro('Cocatriz')
            retorno += f'{roll(dados[1], dados[2])} {dados[0]}. {gera_distancia("aberto")} metros.'
        elif 99 <= d100:
            dados = busca_monstro('Górgon')
            retorno += f'{roll(dados[1], dados[2])} {dados[0]}. {gera_distancia("aberto")} metros.'
    else:
        pass
    
    return retorno
    
    
print(gera_monstro())