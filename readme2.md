# Problème du Voyageur de Commerce (TSP) - Recuit Simulé

##  Description du projet

Ce projet implémente l'algorithme **du Recuit Simulé (Simulated Annealing)** pour résoudre le **problème du voyageur de commerce (TSP)**.  
Le but est de trouver le chemin le plus court passant par toutes les villes une seule fois et revenant au point de départ.

L'algorithme explore des solutions voisines et accepte parfois des solutions moins bonnes pour **échapper aux minima locaux**, en utilisant un paramètre de **température** qui décroît progressivement.

---

##  Principe du Recuit Simulé

1. Générer une **solution initiale aléatoire**.
2. Tant que la température est suffisante :
   - Générer un **voisin aléatoire** (échanger deux villes).
   - Calculer la **distance totale** de ce voisin.
   - Si la distance est meilleure, accepter la solution.
   - Si la distance est pire, l'accepter **avec une probabilité** :  
     `P = exp(-Δdistance / température)`
   - Diminuer la température progressivement.
3. Garder en mémoire la **meilleure solution** rencontrée.

---

##  Visualisation 
Exemple de graphique généré : 
<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/b4a02ff8-10b8-4288-8380-3744e0c74758" />


L'évolution de la distance minimale est visualisée sur un graphique, enregistré automatiquement dans le fichier :

