import random
import matplotlib.pyplot as plt
from collections import deque

# --- cette fonction calcule la distance totale dun circuit ---
def calculer_distance_totale(solution, matrice_distances):
    distance_totale = 0
    for i in range(len(solution) - 1):
        distance_totale += matrice_distances[solution[i]][solution[i + 1]]
    distance_totale += matrice_distances[solution[-1]][solution[0]]  # pour retourner à la ville de départ
    return distance_totale

# --- Génération du voisinage ---
def generer_voisins(solution):
    voisins = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            voisin = solution[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            voisins.append(voisin)
    return voisins

# --- l algorithme de recherche tabou ---
def tabu_search(matrice_distances, nombre_iterations, taille_tabu):
    nombre_villes = len(matrice_distances)
    solution_actuelle = list(range(nombre_villes))
    random.shuffle(solution_actuelle)

    meilleure_solution = solution_actuelle[:]
    meilleure_distance = calculer_distance_totale(solution_actuelle, matrice_distances)

    tabu_list = deque(maxlen=taille_tabu)

    for _ in range(nombre_iterations):
        voisins = generer_voisins(solution_actuelle)
        voisins_non_tabu = [
            v for v in voisins if tuple(v) not in [tuple(t) for t in tabu_list]
        ]

        if not voisins_non_tabu:
            break

        solution_actuelle = min(
            voisins_non_tabu,
            key=lambda x: calculer_distance_totale(x, matrice_distances)
        )
        distance_actuelle = calculer_distance_totale(solution_actuelle, matrice_distances)

        tabu_list.append(solution_actuelle)

        if distance_actuelle < meilleure_distance:
            meilleure_distance = distance_actuelle
            meilleure_solution = solution_actuelle[:]

    return meilleure_solution, meilleure_distance


# --- Mon matrice des distances donnee  ---
matrice_distances = [
    [0, 2, 2, 7, 15, 2, 5, 7, 6, 5],
    [2, 0, 10, 4, 7, 3, 7, 15, 8, 2],
    [2, 10, 0, 1, 4, 3, 3, 4, 2, 3],
    [7, 4, 1, 0, 2, 15, 7, 7, 5, 4],
    [7, 10, 4, 2, 0, 7, 3, 2, 2, 7],
    [2, 3, 3, 7, 7, 0, 1, 7, 2, 10],
    [5, 7, 3, 7, 3, 1, 0, 2, 1, 3],
    [7, 7, 4, 7, 2, 7, 2, 0, 1, 10],
    [6, 8, 2, 5, 2, 2, 1, 1, 0, 15],
    [5, 2, 3, 4, 7, 10, 3, 10, 15, 0]
]

# --- les paramètres ---
nombre_iterations = 1000
taille_tabu = 50

# --- Exécution ---
meilleure_solution, meilleure_distance = tabu_search(matrice_distances, nombre_iterations, taille_tabu)

# --- Résultats ---
print(" la meilleure solution trouvée (par ordre des villes) :", meilleure_solution)
print(" la distance minimale trouvée est --> :", meilleure_distance)




# --- la visualisation du chemin trouvé  ---
def afficher_chemin(solution, matrice_distances):
    n = len(solution)

    # On génère des positions (x, y) aléatoires pour chaque ville (juste pour la visualisation)
    positions = {i: (random.randint(0, 100), random.randint(0, 100)) for i in range(n)}

    plt.figure(figsize=(8, 6))

    # Tracer les villes
    for ville, (x, y) in positions.items():
        plt.scatter(x, y, c='blue')
        plt.text(x + 1, y + 1, str(ville), fontsize=12, color='darkred')

    # Tracer le chemin dans l'ordre de la meilleure solution
    for i in range(len(solution) - 1):
        x1, y1 = positions[solution[i]]
        x2, y2 = positions[solution[i + 1]]
        plt.plot([x1, x2], [y1, y2], 'k-')

    # Retour à la première ville (boucle fermée)
    x1, y1 = positions[solution[-1]]
    x2, y2 = positions[solution[0]]
    plt.plot([x1, x2], [y1, y2], '--', color='red')

    plt.title("le chemin trouvé par la Recherche Tabou (TSP)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


# --- Appel de la fonction ---
afficher_chemin(meilleure_solution, matrice_distances)
