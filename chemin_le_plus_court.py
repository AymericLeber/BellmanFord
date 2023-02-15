graphe1 = ['S', 'A', 'B', 'C', 'D']

couts1 = {(0,1): 3.0, (0,3): 5.0,
          (1,2): 5.0, (1,3): 1.0,
          (2,4): 1.0, (3,1): 1.0,
          (3,2): 5.0, (3,4): 5.0,
          (4,1): 3.0, (4,2): 3.0}

graphe2 = ['Z', 'U', 'V', 'X', 'Y']
couts2 = {(0,1):  6.0, (0,3):  7.0,
          (1,2):  5.0, (1,3):  8.0,
          (1,4): -4.0, (2,1): -2.0,
          (3,2): -3.0, (3,4):  9.0,
          (4,0):  2.0, (4,2):  7.0}

graphe3 = ['A', 'B', 'C', 'D']
couts3 = {(0,1):  5.0, (0,2):  3.0,
          (1,0): -2.0, (1,2):  6.0,
          (1,3):  3.0, (2,0): -1.0,
          (2,3): -1.0, (3,2):  1.0}

graphe4 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
couts4 = {(0,1):  2.0, (0,2):  3.0,
          (1,3):  1.0, (2,3):  2.0,
          (3,4):  3.0, (4,5):  4.0,
          (4,6):  5.0, (5,6):  1.0,
          (6,0): -3.0, (6,7):  1.0}

def Bellman_Ford(graphe, couts, sommet) :
    d = len(graphe)*[float('inf')]
    d[sommet] = 0.0
    paths = []
    for i in range(len(graphe)) :
        
        paths.append(f"{graphe[sommet]} -> {graphe[i]} : {graphe[sommet]} > ")
    paths[sommet] = f"{graphe[sommet]} -> {graphe[sommet]} : {graphe[sommet]} > "
    paths[sommet] += graphe[sommet]
    for i in range(len(graphe)-2) :
        for key in couts.keys() :
            if d[key[1]] > d[key[0]] + couts[key] :
                d[key[1]] = d[key[0]] + couts[key]
                if paths[key[0]][13:] == graphe[sommet] :
                    paths[key[1]] = paths[key[1]] + f"{graphe[key[1]]}"
                else :
                    paths[key[1]] = paths[key[1]] + f"{paths[key[0]][13:]} > {graphe[key[1]]}"
    
    print()
    for i in range(len(paths)) :
        print(f"{paths[i]}\nCout du chemin : {int(d[i])}\n\n")
    
    condition = True
    for key in couts.keys() :
        if d[key[1]] > d[key[0]] + couts[key] :
            condition = False
            print("Il y a un circuit absorbant !\n")
    
    if condition :
        print("Il n'y a pas de circuit absorbant.\n")
    return d

Bellman_Ford(graphe4, couts4, 0)