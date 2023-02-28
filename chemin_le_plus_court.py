# import pour le test des post-conditions
from doctest import testmod

# Exemples de graphes

# graphe1 = ['S', 'A', 'B', 'C', 'D']
# couts1 = {(0,1): 3.0, (0,3): 5.0,
#           (1,2): 5.0, (1,3): 1.0,
#           (2,4): 1.0, (3,1): 1.0,
#           (3,2): 5.0, (3,4): 5.0,
#           (4,1): 3.0, (4,2): 3.0}

# graphe2 = ['Z', 'U', 'V', 'X', 'Y']
# couts2 = {(0,1):  6.0, (0,3):  7.0,
#           (1,2):  5.0, (1,3):  8.0,
#           (1,4): -4.0, (2,1): -2.0,
#           (3,2): -3.0, (3,4):  9.0,
#           (4,0):  2.0, (4,2):  7.0}

# graphe3 = ['A', 'B', 'C', 'D']
# couts3 = {(0,1):  5.0, (0,2):  3.0,
#           (1,0): -2.0, (1,2):  6.0,
#           (1,3):  3.0, (2,0): -1.0,
#           (2,3): -1.0, (3,2):  1.0}

# graphe4 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# couts4 = {(0,1):  2.0, (0,2):  3.0,
#           (1,3):  1.0, (2,3):  2.0,
#           (3,4):  3.0, (4,5):  4.0,
#           (4,6):  5.0, (5,6):  1.0}

def creerGraphe() :
    """
    Fonction qui demande à l'utilisateur de créer son graphe avec sa matrice de coûts via des input().

    Entrées :

    Aucunes

    Sorties :

    - graphe : liste de caractères
        Elle contient le nom des sommets du graphe.

    - couts : dictionnaire de tuples définissant des réels.
        Il contient les arètes du graphe avec leur coût correspondant. Les clés sont des tuples contenant 2 entiers.
        Le premier entier(de 0 à n-1 sommets) correspond au sommet de départ et le second à celui d'arrivée(différent de celui de départ).
        La valeur(le réel) correspond au coût de l'arète en question.

    - sommet : entier
        Il correspond au sommet principal du graphe à partir duquel on veut calculer les chemins les plus courts en lui et les autres
        sommets.
    """

    # code
    # on initialise les variables de sortie ("sommet" est un caractère pour faciliter l'interaction avec l'utilisateur)
    graphe = []
    couts = {}
    sommet = "Z"

    # variable pour le nombre de sommets
    nbSommets = 0

    # on demande un nombre de sommets pour le graphe à l'utilisateur tant qu'il ne donne pas une entree valide
    while nbSommets < 1 or nbSommets > 16 :
        nbSommets = input("\nEntrez le nombre de sommets : ")

        # le resultat d'un input() est sous forme de string, il faut donc le convertir
        try :
            nbSommets = int(nbSommets)
        # si on ne peut pas, on envoie un message d'erreur et on recommence
        except :
            print("\nEntrée invalide.")
            nbSommets = 0

    # après avoir récupérer un nombre de sommets valides, on en ajoute autant dans le graphe
    for i in range(nbSommets) :
        graphe.append(chr(i+65))

    # on affiche les sommets à l'utilisateur
    print(f"\nVoici les sommets du graphe : {graphe}")

    # on initialise la variable qui sert à récupérer les arètes entrées par l'utilisateur
    chaine = ["Z", "Z", 0]

    # ainsi que la condition de sortie pour quand qu'il a terminé
    condition = True

    while condition :

        # puis on demande à l'utilisateur de saisir les arètes qu'il souhaite une par une
        while not(64 < ord(chaine[0]) < 81) or not(64 < ord(chaine[1]) < 81) or chaine[2] == 0 or chaine[2] == float('inf') or chaine[2] == float('-inf') :
            print("\nSaisissez une arète (donnez le sommet de départ, d'arrivée, le coût et espacez les informations avec des espaces)")
            chaine = input("(appuyez sur \"entrée\" pour arreter): ")
            chaine = chaine.split(" ")

            # cas où l'utilisateur a terminé de saisir des arètes
            if chaine == [""] :

                # on affecte les variables de manière à sortir de la boucle
                chaine = ["A", "A", 1]
                condition = False

            # cas où il y a plus de 3 entrées différentes (plus de 2 espaces)
            elif len(chaine) != 3 :
                print("\nEntrées invalides.")

            # cas où l'utilisateur donne des sommets qui ne font pas partie du graphe
            elif chaine[0] == chaine[1] or chaine[0] not in graphe or chaine[1] not in graphe :
                print("\nSommets invalides.")

            # si on ne rentre pas dans les autres cas, on va alors pouvoir vérifier le coût de l'arète donné
            else :

                # même problème et solution que dans le try précédent
                try :
                    chaine[2] = float(chaine[2])
                except :
                    print("\nCoût invalide.")
                    chaine = ["Z", "Z", 0]

                # une fois le coût correctement récupéré, on l'assigne à l'arète dans le dictionnaire
                couts[(ord(chaine[0])-65, ord(chaine[1])-65)] = chaine[2]

                # une fois l'arète complètement récupérée, on réinitialise la variable de récupération pour re-rentrer dans la boucle
                chaine = ["Z", "Z", 0]

    # une fois que l'utilisateur a rentré toutes ses arètes, on lui demande de choisir un sommet principal à son graphe
    # c'est pour cette condition en particulier que "sommet" est un caractère pour le moment
    while sommet not in graphe :
        sommet = input("\nChoisissez un sommet pour le graphe : ")

    # une fois le sommet principal récupéré, on le transforme entier qui correspond à la position de ce dernier dans la liste des sommets
    sommet = ord(sommet) - 65

    # enfin, on retourne le graphe, la matrice des coûts ainsi que le sommet principal
    return graphe, couts, sommet

def Bellman_Ford(graphe, couts, sommet) :
    """
    Fonction qui applique l'algorithme de Bellman-Ford sur un graphe donné.

    Entrées :

    - graphe : liste de caractères
        Elle contient le nom des sommets du graphe.

    - couts : dictionnaire de tuples définissant des réels.
        Il contient les arètes du graphe avec leur coût correspondant. Les clés sont des tuples contenant 2 entiers.
        Le premier entier(de 0 à n-1 sommets) correspond au sommet de départ et le second à celui d'arrivée(différent de celui de départ).
        La valeur(le réel) correspond au coût de l'arète en question.

    - sommet : entier
        Il correspond au sommet principal du graphe à partir duquel on veut calculer les chemins les plus courts en lui et les autres

    Sortie :

    - d : tableau de réels
        Pour chaque sommet, il contient le coût du chemin le plus rapide du sommet principal jusqu'à ces derniers.
        Les valeurs sont dans le même ordre que les sommets dans "graphe".
    
    Exemples :
    
    >>> graphe = ['S', 'A', 'B', 'C', 'D']
    >>> couts  = {(0,1):  6.0, (0,3):  7.0, (1,2):  5.0, (1,3):  8.0, (1,4): -4.0, (2,1): -2.0, (3,2): -3.0, (3,4):  9.0, (4,0):  2.0, (4,2):  7.0}
    >>> sommet = 0
    >>> Bellman_Ford(graphe, couts, sommet)
    <BLANKLINE>
    S -> S : S
    Cout du chemin : 0
    <BLANKLINE>
    <BLANKLINE>
    S -> A : S > C > B > A
    Cout du chemin : 2
    <BLANKLINE>
    <BLANKLINE>
    S -> B : S > C > B
    Cout du chemin : 4
    <BLANKLINE>
    <BLANKLINE>
    S -> C : S > C
    Cout du chemin : 7
    <BLANKLINE>
    <BLANKLINE>
    S -> D : S > C > B > A > D
    Cout du chemin : -2
    <BLANKLINE>
    <BLANKLINE>
    Il n'y a pas de circuit absorbant.
    <BLANKLINE>
    [0.0, 2.0, 4.0, 7.0, -2.0]
    """
    # assertions
    assert type(graphe) is list, "graphe doit être une liste."
    for som in graphe :
        assert type(som) is str and len(som) == 1 and (47 < ord(som) < 58 or 64 < ord(som) < 91 or 96 < ord(som) < 123), "Les sommets doivent être des caractères alphanumériques."
    assert type(couts) is dict, "couts doit être un dictionnaire."
    for key in couts.keys() :
        assert type(key) is tuple and len(key) == 2, "couts est invalide. Se référer à la documentation de la fonction."
        assert type(key[0]) is int and type(key[1]) is int, "couts est invalide. Se référer à la documentation de la fonction."
        assert key[0] < len(graphe) and key[1] < len(graphe) and key[0] != key[1], "couts est invalide. Se référer à la documentation de la fonction."
        assert type(couts[key]) is float and couts[key] != float('inf') and couts[key] != float('-inf'), "couts est invalide. Se référer à la documentation de la fonction."
    assert type(sommet) is int, "sommet doit être un entier."
    assert -1 < sommet < len(graphe), "sommet doit correspondre à l'un des sommets de graphe."

    # code
    # on initialise la variable de retour avec les plus grandes valeurs possibles
    d = len(graphe)*[float('inf')]
    d[sommet] = 0.0
    
    # on initialise la variable qui récupérera les différents chemins entre le sommet principal et les autres sommets
    paths = [f"{graphe[sommet]} -> {som} : {graphe[sommet]}" for som in graphe]
    
    # pour chaque sommet du graphe - 1
    for i in range(len(graphe)-1) :
        
        # pour chaque arète dans la matrice de coûts a(u, v) :
        for key in couts.keys() :
            
            # si d[v] > d[u] + a(u, v), alors d[v] = d[u] + a(u, v)
            if d[key[1]] > d[key[0]] + couts[key] :
                d[key[1]] = d[key[0]] + couts[key]
                
                # et le chemin du sommet principal à graphe[v] devient celui du sommet principal à graphe[u] + jusqu'à graphe[v]
                paths[key[1]] = paths[key[1]][:6] + paths[key[0]][6:] + f" > {graphe[key[1]]}"
    
    # saut de ligne pour l'affichage
    print()
    
    # à partir de là les chemins optimaux sont sensés être trouvé (sauf en cas de circuit absorbant)
    # on affiche donc les chemins trouvés pour chaque sommet avec leur coût respectif ou bien que le sommet est inaccessible
    # si le coût de départ n'a pas changé
    for i in range(len(paths)) :
        if d[i] != float('inf') :
            print(f"{paths[i]}\nCout du chemin : {int(d[i])}\n\n")
        else :
            print(f"{paths[i][:8]}\n Sommet inaccessible !\n\n")

    # on effectue un dernier parcours des arètes pour vérifier qu'il n'y a pas de circuit absorbant
    # initialisation de la condition de vérification
    condition = True
    for key in couts.keys() :
        
        # si on retrouve un meilleur coût pour l'un des chemins, c'est donc qu'il y a un circuit absorbant
        if d[key[1]] > d[key[0]] + couts[key] :
            condition = False
            print("Il y a un circuit absorbant !\n")

    # cas où il n'y a pas de circuit absorbant
    if condition :
        print("Il n'y a pas de circuit absorbant.\n")
    
    # enfin, on retourne le tableau des coûts
    return d

# lancement de la vérification des post-conditions et du programme
if __name__ == '__main__' :
    testmod(verbose=True)
    entrees = creerGraphe()
    Bellman_Ford(entrees[0], entrees[1], entrees[2])
