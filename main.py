mapa2 = {"chave": "valor"}

mapa = [
    [2,1,9,9,9],
    [None,0,1,1,9],
    [1,1,1,1,1],
    [9,9,1,1,1]
]
custos = []

def validar_entrada(mapa):

    #verifica se é lista e se não é vazia
    if isinstance(mapa, list) == False or len(mapa) == 0 or len(mapa[0]) == 0:
        return False

    #pecorre a matriz inteira pra verificar os elementos
    for i in mapa:
        if isinstance(i, list) == False or len(i) == 0:
            return False
        if len(i) != len(mapa[0]): #matriz invalida esse caralho
            return False
        for x in i:
            if x is None:
                continue
            if type(x) is not int or x < 0:
                return False
            
    return True

def caminhada(mapa, x_atual, y_atual, custo):
    if mapa[x_atual][y_atual] != 0 and mapa[x_atual][y_atual] != None:
        custo += mapa[x_atual][y_atual]

    #verifica se chegou no destino // supondo que o destino é sempre o canto inferior direito do mapa
    if x_atual == len(mapa) - 1 and y_atual == len(mapa[0]) - 1:
        custos.append(custo)
    else: 
        if y_atual+1 < len(mapa[0]): #certifica que não sai do mapa
            if mapa[x_atual][y_atual+1] != 0 and mapa[x_atual][y_atual+1] != None: #direita
                caminhada(mapa, x_atual, y_atual+1, custo)

        if x_atual+1 <len(mapa): #certifica que não sai do mapa
            if mapa[x_atual+1][y_atual] != 0 and mapa[x_atual+1][y_atual] != None: #baixo
                caminhada(mapa, x_atual+1, y_atual, custo)

def guloso(mapa, x_atual, y_atual, custo):

    x_chegada = len(mapa) - 1
    y_chegada = len(mapa[0]) - 1

    while x_atual != x_chegada or y_atual != y_chegada:
        #variavel para o algoritmo guloso
        direita_disponivel = False
        baixo_disponivel = False
        
        if mapa[x_atual][y_atual] != 0 and mapa[x_atual][y_atual] != None:
            custo += mapa[x_atual][y_atual]

        if y_atual+1 < len(mapa[0]): #verifica se não sai do mapa
            #define a disponibilidade
            if mapa[x_atual][y_atual+1] != 0 and mapa[x_atual][y_atual+1] != None:
                direita_disponivel = True

        if x_atual+1 < len(mapa): #verifica se não sai do mapa
            #define a disponibilidade
            if mapa[x_atual+1][y_atual] != 0 and mapa[x_atual+1][y_atual] != None: 
                baixo_disponivel = True

        #verifica qual é maior
        if direita_disponivel and baixo_disponivel:
            if mapa[x_atual][y_atual+1] <= mapa[x_atual+1][y_atual]: #direita
                y_atual += 1
            else: #baixo
                x_atual += 1
        elif direita_disponivel and not baixo_disponivel:
            y_atual += 1
        elif not direita_disponivel and baixo_disponivel:
            x_atual += 1
        else:
            break


def projeto_do_robo(mapa):
    x_atual = 0
    y_atual = 0
    custo = 0
    
    if validar_entrada(mapa):
        if mapa[0][0] == 0 or mapa[0][0] == None:
            print("sem_caminho")
        elif mapa[len(mapa)-1][len(mapa[0])-1] == 0 or mapa[len(mapa)-1][len(mapa[0])-1] == None: # essa porra é pra ver se o destino é vazio
            print("sem_caminho")
        else: # TROCA DE ALGORITMOS ----AQUI-----

            #caminhada(mapa, x_atual, y_atual, custo)
            guloso(mapa, x_atual, y_atual, custo)

            if len(custos) > 0:
                print("OK, custo "+ str(min(custos)))
            else:
                print("sem_caminho")
    else:
        print("entrada_invalida")

projeto_do_robo(mapa)