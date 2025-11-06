import random
import matplotlib.pyplot as plt

# --- Distance totale ---
def calculer_distance_totale(solution, matrice_distances):
    distance = 0
    for i in range(len(solution)-1):
        distance += matrice_distances[solution[i]][solution[i+1]]
    distance += matrice_distances[solution[-1]][solution[0]]
    return distance

# --- Génération de voisins ---
def generer_voisins(solution):
    voisins = []
    for i in range(len(solution)):
        for j in range(i+1, len(solution)):
            voisin = solution[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            voisins.append(voisin)
    return voisins

# --- Hill Climbing ---
def hill_climbing(matrice_distances, iterations=1000):
    nombre_villes = len(matrice_distances)
    solution_actuelle = list(range(nombre_villes))
    random.shuffle(solution_actuelle)
    meilleure_solution = solution_actuelle[:]
    meilleure_distance = calculer_distance_totale(solution_actuelle, matrice_distances)

    for _ in range(iterations):
        voisins = generer_voisins(solution_actuelle)
        solution_voisin = min(voisins, key=lambda x: calculer_distance_totale(x, matrice_distances))
        distance_voisin = calculer_distance_totale(solution_voisin, matrice_distances)
        if distance_voisin < meilleure_distance:
            solution_actuelle = solution_voisin
            meilleure_solution = solution_voisin[:]
            meilleure_distance = distance_voisin
        else:
            break
    return meilleure_solution, meilleure_distance

# --- Coordonnées fictives ---
coord_villes = [
    (0,0), (1,5), (2,3), (3,7), (4,1),
    (5,4), (6,0), (7,6), (8,2), (9,5)
]

# --- Matrice des distances ---
matrice_distances = [
    [0,2,2,7,15,2,5,7,6,5],
    [2,0,10,4,7,3,7,15,8,2],
    [2,10,0,1,4,3,3,4,2,3],
    [7,4,1,0,2,15,7,7,5,4],
    [7,10,4,2,0,7,3,2,2,7],
    [2,3,3,7,7,0,1,7,2,10],
    [5,7,3,7,3,1,0,2,1,3],
    [7,7,4,7,2,7,2,0,1,10],
    [6,8,2,5,2,2,1,1,0,15],
    [5,2,3,4,7,10,3,10,15,0]
]

# --- Exécution ---
meilleure_solution, meilleure_distance = hill_climbing(matrice_distances)
print(" Meilleure solution Hill Climbing :", meilleure_solution)
print("Distance minimale Hill Climbing :", meilleure_distance)

# --- Visualisation ---
x = [coord_villes[v][0] for v in meilleure_solution + [meilleure_solution[0]]]
y = [coord_villes[v][1] for v in meilleure_solution + [meilleure_solution[0]]]

plt.figure(figsize=(8,6))
plt.plot(x, y, 'b--', marker='o')
for i, ville in enumerate(meilleure_solution):
    plt.text(coord_villes[ville][0], coord_villes[ville][1], str(ville), fontsize=12)
plt.title("Chemin optimal - Hill Climbing")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.savefig("chemin_solution_hill.png")
plt.show()
