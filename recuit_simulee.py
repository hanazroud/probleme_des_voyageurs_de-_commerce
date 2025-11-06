import random
import math
import matplotlib.pyplot as plt

# --- Fonction pour calculer la distance totale d'un circuit ---
def calculer_distance_totale(solution, matrice_distances):
    distance_totale = 0
    for i in range(len(solution)-1):
        distance_totale += matrice_distances[solution[i]][solution[i+1]]
    distance_totale += matrice_distances[solution[-1]][solution[0]]  # retour à la ville de départ
    return distance_totale

# --- Génération d’un voisin (échange de deux villes) ---
def generer_voisin(solution):
    voisin = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    voisin[i], voisin[j] = voisin[j], voisin[i]
    return voisin

# --- Algorithme du Recuit simulé ---
def recuit_simule(matrice_distances, temperature_initiale, refroidissement, iterations):
    nombre_villes = len(matrice_distances)
    solution_actuelle = list(range(nombre_villes))
    random.shuffle(solution_actuelle)

    meilleure_solution = solution_actuelle[:]
    distance_actuelle = calculer_distance_totale(solution_actuelle, matrice_distances)
    meilleure_distance = distance_actuelle

    temperature = temperature_initiale

    for _ in range(iterations):
        voisin = generer_voisin(solution_actuelle)
        distance_voisin = calculer_distance_totale(voisin, matrice_distances)
        delta = distance_voisin - distance_actuelle

        # Critère d'acceptation
        if delta < 0 or random.random() < math.exp(-delta / temperature):
            solution_actuelle = voisin[:]
            distance_actuelle = distance_voisin

            if distance_actuelle < meilleure_distance:
                meilleure_solution = solution_actuelle[:]
                meilleure_distance = distance_actuelle

        temperature *= refroidissement
        if temperature < 1e-3:
            break

    return meilleure_solution, meilleure_distance

# --- Matrice des distances ---
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

# --- Coordonnées fictives pour visualiser le trajet ---
coord_villes = [
    (0,0), (1,5), (2,3), (3,7), (4,1),
    (5,4), (6,0), (7,6), (8,2), (9,5)
]

# --- Paramètres du Recuit Simulé ---
temperature_initiale = 100
refroidissement = 0.98
iterations = 5000

# --- Exécution ---
meilleure_solution, meilleure_distance = recuit_simule(
    matrice_distances, temperature_initiale, refroidissement, iterations
)

print(" Meilleure solution trouvée :", meilleure_solution)
print(" Distance minimale :", meilleure_distance)

# --- Préparer les coordonnées pour tracer le chemin ---
x = [coord_villes[v][0] for v in meilleure_solution + [meilleure_solution[0]]]
y = [coord_villes[v][1] for v in meilleure_solution + [meilleure_solution[0]]]

# --- Visualisation du chemin ---
plt.figure(figsize=(8,6))
plt.plot(x, y, 'k--', marker='o')  # lignes et points
for i, ville in enumerate(meilleure_solution):
    plt.text(coord_villes[ville][0], coord_villes[ville][1], str(ville), fontsize=12)
plt.title("Chemin optimal - Recuit Simulé")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.savefig("chemin_solution_recuit.png")
plt.show()

print("Graphique sauvegardé sous : chemin_solution_recuit.png")

