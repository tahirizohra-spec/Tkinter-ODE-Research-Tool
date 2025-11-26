# 🧮 Tkinter ODE Research Tool  
**Application Python pour visualiser et analyser des équations différentielles dans le cadre d’un projet de recherche.**

Ce projet a été conçu dans le contexte d’un travail doctoral portant sur la résolution et la visualisation de solutions d’équations différentielles (ODE).  
Il propose une interface graphique Tkinter permettant :

- l’importation de données expérimentales ou simulées (CSV),
- l’affichage de statistiques avancées,
- la visualisation graphique des solutions,
- la résolution numérique d'une équation différentielle simple avec Runge–Kutta 4,
- l’export des données au format JSON.

---

## 📌 Fonctionnalités principales

### ✔ 1. Importation de fichiers CSV
L’utilisateur peut charger des fichiers contenant :
- le temps \( t \)
- des solutions \( y(t) \)
- éventuellement des dérivées \( y'(t) \)

Exemple fourni : `oscillator_solution.csv`.

---

### ✔ 2. Affichage des statistiques
Utilise `pandas.DataFrame.describe()` pour afficher :

- moyenne
- variance
- min / max
- quartiles
- comptages

Les résultats apparaissent dans la zone de texte de l’interface.

---

### ✔ 3. Visualisation graphique (matplotlib)
L’application trace :

- la solution \( y(t) \)
- ou toute paire de colonnes numériques

Graphique personnalisé avec :
- titre
- labels
- grille

---

### ✔ 4. Résolution numérique d’ODE (Runge–Kutta 4)
L’application inclut un solveur interne pour :

\[
y' = -2y,\quad y(0)=1
\]

Les valeurs calculées sont automatiquement affichées et peuvent être tracées.

---

### ✔ 5. Exportation JSON
Les données actuellement chargées peuvent être exportées en :

