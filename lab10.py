import numpy as np
A = np.array([10, 20, 30, 40, 50])
M = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]])

print("Tableau 1D A :", A)
print("Tableau 2D M :\n", M)
element_3 = A[2]     
element_fin = A[-1]   
print("A[2] =", element_3)
print("A[-1] =", element_fin)

valeur_12 = M[1, 2]   # Ligne 2, colonne 3
valeur_dernier = M[-1, -1]

print("M[1, 2] =", valeur_12)
print("M[-1, -1] =", valeur_dernier)

segment = A[1:4]
print("A[1:4] =", segment)  # [20 30 40]

sous_bloc = M[0:2, 1:]
print("M[0:2, 1:] =\n", sous_bloc)

ligne_2 = M[1, :]
print("Ligne 2 :", ligne_2)  # [5 6 7 8]

colonne_3 = M[:, 2]
print("Colonne 3 :", colonne_3)  # [ 3  7 11]

bloc_central = M[0:3, 1:3]
print("Bloc central :\n", bloc_central)

colonnes_alternées = M[:, ::2]
print("Colonnes 0 et 2 :\n", colonnes_alternées)

vue = M[0:2, 1:3]
print("Vue initiale :\n", vue)

vue[0, 0] = 999
print("Vue modifiée :\n", vue)
print("M après modification via la vue :\n", M)

M = np.array([[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]])

sous_copie = M[0:2, 1:3].copy()
print("Copie avant modification :\n", sous_copie)

sous_copie[0, 0] = 999
print("Copie modifiée :\n", sous_copie)
print("M restée intacte :\n", M)

M[:, -1] *= 10
print("M après multiplication de la dernière colonne :\n", M)

bloc_vue = M[1:, :2]
bloc_vue[:] = -1
print("M après bloc -1 (via vue) :\n", M)

bloc_copy = M[1:, :2].copy()
bloc_copy[:] = -1
print("Bloc copy modifié :\n", bloc_copy)
print("M (copie intacte) :\n", M)

A_original = A.copy()
A[1:-1] = 0
print("A modifié :", A)
A = A_original