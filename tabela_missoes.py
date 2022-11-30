from random import choice
from dice import roll


def missao_comum():
    
    base_missao = choice(['transporte', 'coleta', 'guarda', 'mensagem', 'regate'])
    tipos_transporte = choice(['animais', 'itens comuns', 'itens magicos',])
    tipos_coleta = choice(['frutas', 'minerios', 'recursos', 'animais'])
    tipos_guarda = choice(['aldeao', 'nobre', 'bandidos'])
    tipos_mensagem = choice(['mensagem comum', 'mensagem com dinheiro', 'mensagem com item'])
    tipos_resgate = choice(['aldeao', 'nobre', 'animal','carga' ,'item'])
    d100 = roll(1, 100)
    
    
    missao = f''
    if base_missao == 'transporte':
        if tipos_transporte == 'animais':
            if d100 <= 13:
                missao = f'Missão de Transporte para {roll(4,4)} Bois, que devem ser entregues a '\
                         f'cidade mais proxima com o Pagamento de {roll(4,4)} Peças de Ouro.'
            elif d100 <= 26:
                missao = f'Missão de Transporte para {roll(2,4)} Cavalos de Montaria que devem ser '\
                         f'entregues a cidade mais proxima, com o Pagamento de {roll(6,2)} Peças de Ouro.'
            else:
                pass
        
            
    
    
    return missao
    
print(missao_comum())