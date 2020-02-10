# PersonnalData

## Structure de données
 Concevoir et implementer les structures de donnees pour modeliser les
donnees personnelles, les noeuds systeme et les utilisateurs. La structure
devra, entre autres, impl´ementer les champs suivants:

#### Donnees
– ID : Un entier unique

– Taille : Un entier
 
  #### Utilisateurs
– ID : Un entier unique

– Liste de donnees d’interet : Une liste d’ID (donnees)

– Noeud systeme accessible : Un ID (noeud systeme)

#### Noeuds systeme:
– ID : Un entier unique

– capacite memoire : Un entier

– Liste des donnees stockees localement : Une liste d’ID (donnees)

– Liste des noeuds accessibles : Une liste d’ID (noeud systeme/Utilisateur)


## Q2
On cherche à trouver un placement efficace pour les donnees du systeme:
chaque donnee doit etre placée au plus près de l’utilisateur interessé par
cette donnée. Implémentez une méthode permettant au système de savoir
ou placer les données du systémes. Cette méthode devra prendre en
compte la place restante sur les différents noeuds du systéme. Dans cette
méthode, on s’intéressera à placer les donnees une par une, par ordre d’ID.

## Q3
Adaptons le programme pour que deux utilisateurs puissent être intéressés
par une même donnée. On pourra, par exemple, calculer le noeud système
a recevoir la donnée pour le premier utilisateur puis calculer le plus chemin
entre ce noeud et le second utilisateur. Il faudra alors choisir le noeud de
ce chemin qui minimise le temps d’accès pour les deux utilisateurs.
## Q4
Le placement des données une par une pouvant mener à des résultats non optimaux, il convient d’utiliser des algorithmes permettant de repartir efficacement l’espace disponible. Ce problème est connu sous le noms de“Sac à dos Multiple (MKP problem)”. Implémentez une solution à ce probleme dans le cadre du stockage de données personnelles.

Lors de ce projet j'ai utilisé la bibliothèque NetworkX, voici le lien avec les indications afin de l'installer et d'avoir la documention

Installer NetworkX : https://networkx.github.io/documentation/stable/install.html

Documentation NetworkX : https://networkx.github.io/documentation/networkx-1.10/install.html

### Sujet Polytech Annecy-Chambéry




