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

graphe4 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
couts4 = {(0,1):  2.0, (0,2):  3.0,
          (1,3):  1.0, (2,3):  2.0,
          (3,4):  3.0, (4,5):  4.0,
          (4,6):  5.0, (5,6):  1.0}

def creerGraphe() :
    graphe = []
    couts = {}
    sommet = "Z"
    nbSommets = 0
    while nbSommets < 1 or nbSommets > 16 :
        nbSommets = input("\nEntrez le nombre de sommets : ")
        
        try :
            nbSommets = int(nbSommets)
        except :
            print("\nEntree invalide.")
            nbSommets = 0
    
    for i in range(nbSommets) :
        graphe.append(chr(i+65))
    
    chaine = ["Z", "Z", 0]
    condition = True
    while condition :
        while not(64 < ord(chaine[0]) < 81) or not(64 < ord(chaine[1]) < 81) or chaine[2] == 0 or chaine[2] == float('inf') or chaine[2] == float('-inf') :
            print("\nSaisissez une arete (donnez le sommet de depart, d'arrivee, le cout et espacez les informations avec des espaces)")
            chaine = input("(appuyez sur entree pour arreter): ")
            chaine = chaine.split(" ")
            
            if chaine == [""] :
                chaine = ["A", "A", 1]
                condition = False
            elif len(chaine) != 3 :
                print("\nEntrees invalides.")
            
            elif chaine[0] == chaine[1] or chaine[0] not in graphe or chaine[1] not in graphe :
                print("\nSommets invalides.")
            
            else :
                try :
                    chaine[2] = float(chaine[2])
                except :
                    print("\nCout invalide.")
                    chaine = ["Z", "Z", 0]
            
                couts[(ord(chaine[0])-65, ord(chaine[1])-65)] = chaine[2]
                chaine = ["Z", "Z", 0]
    
    while sommet not in graphe :
        sommet = input("\nChoisissez un sommet pour le graphe : ")
    sommet = ord(sommet) - 65
    
    return graphe, couts, sommet

def concatenerChemins(path1, path2) :
    chaine = ""
    i = 0
    while len(path1) != i and len(path2) != i and path1[i] == path2[i] :
        chaine += path1[i]
        i += 1
    
    chaine += path2[i:]
    
    return chaine

def Bellman_Ford(graphe, couts, sommet) :
    d = len(graphe)*[float('inf')]
    d[sommet] = 0.0
    paths = []
    for i in range(len(graphe)) :
        paths.append(graphe[sommet])
    for i in range(len(graphe)-1) :
        for key in couts.keys() :
            if d[key[1]] > d[key[0]] + couts[key] :
                d[key[1]] = d[key[0]] + couts[key]
                paths[key[1]] = concatenerChemins(paths[key[1]], paths[key[0]]) + graphe[key[1]]
    
    print()
    for i in range(len(paths)) :
        if d[i] != float('inf') :
            print(f"{paths[i][0]} -> {graphe[i]} : {paths[i][0]}", end="")
            for j in range(1, len(paths[i])) :
                print(f" > {paths[i][j]}", end="")
            print(f"\n\nCout du chemin : {int(d[i])}\n\n")
        else :
            print(f"{paths[i][:8]}\n Sommet inaccessible !\n\n")
    
    condition = True
    for key in couts.keys() :
        if d[key[1]] > d[key[0]] + couts[key] :
            condition = False
            print("Il y a un circuit absorbant !\n")
    
    if condition :
        print("Il n'y a pas de circuit absorbant.\n")
    return d

if __name__ == '__main__' :
    entrees = creerGraphe()
    Bellman_Ford(entrees[0], entrees[1], entrees[2])