import random
import matplotlib.pyplot as plt

# --- Fonction pour calculer la distance totale ---
def calculer_distance_totale(solution, matrice_distances):
    distance = 0
    for i in range(len(solution)-1):
        distance += matrice_distances[solution[i]][solution[i+1]]
    distance += matrice_distances[solution[-1]][solution[0]]
    return distance

# --- Initialisation de la population ---
def initialiser_population(taille_pop, nombre_villes):
    population = []
    for _ in range(taille_pop):
        sol = list(range(nombre_villes))
        random.shuffle(sol)
        population.append(sol)
    return population

# --- Sélection par tournoi ---
def selection_tournoi(population, matrice_distances):
    a, b = random.sample(population, 2)
    return a if calculer_distance_totale(a, matrice_distances) < calculer_distance_totale(b, matrice_distances) else b

# --- Croisement (Order Crossover simple) ---
def croisement(parent1, parent2):
    taille = len(parent1)
    debut, fin = sorted(random.sample(range(taille), 2))
    enfant = [None]*taille
    enfant[debut:fin] = parent1[debut:fin]
    pos = fin
    for g in parent2:
        if g not in enfant:
            if pos>=taille: pos=0
            enfant[pos] = g
            pos += 1
    return enfant

# --- Mutation (échange de deux villes) ---
def mutation(solution, proba=0.1):
    if random.random() < proba:
        i,j = random.sample(range(len(solution)),2)
        solution[i], solution[j] = solution[j], solution[i]
    return solution

# --- Algorithme génétique ---
def algorithme_genetique(matrice_distances, taille_pop=50, generations=100):
    nombre_villes = len(matrice_distances)
    population = initialiser_population(taille_pop, nombre_villes)
    meilleure_solution = min(population, key=lambda x: calculer_distance_totale(x, matrice_distances))
    meilleure_distance = calculer_distance_totale(meilleure_solution, matrice_distances)

    for _ in range(generations):
        nouvelle_population = []
        for _ in range(taille_pop):
            p1 = selection_tournoi(population, matrice_distances)
            p2 = selection_tournoi(population, matrice_distances)
            enfant = croisement(p1,p2)
            enfant = mutation(enfant)
            nouvelle_population.append(enfant)
        population = nouvelle_population
        candidat = min(population, key=lambda x: calculer_distance_totale(x, matrice_distances))
        dist = calculer_distance_totale(candidat, matrice_distances)
        if dist < meilleure_distance:
            meilleure_solution = candidat[:]
            meilleure_distance = dist

    return meilleure_solution, meilleure_distance

# --- Coordonnées fictives pour visualisation ---
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
meilleure_solution, meilleure_distance = algorithme_genetique(matrice_distances)
print(" Meilleure solution GA :", meilleure_solution)
print(" Distance minimale GA :", meilleure_distance)

# --- Visualisation du chemin ---
x = [coord_villes[v][0] for v in meilleure_solution + [meilleure_solution[0]]]
y = [coord_villes[v][1] for v in meilleure_solution + [meilleure_solution[0]]]

plt.figure(figsize=(8,6))
plt.plot(x, y, 'g--', marker='o')
for i, ville in enumerate(meilleure_solution):
    plt.text(coord_villes[ville][0], coord_villes[ville][1], str(ville), fontsize=12)
plt.title("Chemin optimal - Algorithme Génétique")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.savefig("chemin_solution_genetique.png")
plt.show()
