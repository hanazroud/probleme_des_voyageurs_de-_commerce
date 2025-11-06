# Problème du Voyageur de Commerce - Recuit Simulé

Ce projet implémente l'algorithme de **Recuit Simulé** pour résoudre le problème du **Voyageur de Commerce (TSP)** sur une matrice de distances entre 10 villes. Le but est de trouver le **chemin minimal** passant par toutes les villes exactement une fois et revenant au point de départ.

## Algorithme

- **Recuit Simulé (Simulated Annealing)** :
  - Commence avec une solution aléatoire.
  - Génère des voisins par échange de deux villes.
  - Accepte une nouvelle solution si elle est meilleure ou selon une probabilité liée à la température.
  - Refroidit progressivement la température jusqu'à un seuil minimal.

## Matrice des distances

```text
0  2  2  7 15  2  5  7  6  5
2  0 10  4  7  3  7 15  8  2
2 10  0  1  4  3  3  4  2  3
7  4  1  0  2 15  7  7  5  4
7 10  4  2  0  7  3  2  2  7
2  3  3  7  7  0  1  7  2 10
5  7  3  7  3  1  0  2  1  3
7  7  4  7  2  7  2  0  1 10
6  8  2  5  2  2  1  1  0 15
5  2  3  4  7 10  3 10 15  0
Exemple de graphique généré : 
<img width="800" height="600" alt="image" src="https://github.com/user-attachments/assets/950c335c-def3-45ed-b8a0-a4337832e1e3" />
