#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercices : Bases de Python pour le scripting d'automatisation
"""

import os
import shutil
import sys
import time # Ajouté pour l'exercice 10
from pathlib import Path

# =============================================
# Exercice 1 : Variables et types de données
# =============================================
def exercice_variables():
    """
    Créez des variables pour stocker :
    - Votre nom (str)
    - Votre âge (int)
    - Votre taille en mètres (float)
    - Si vous êtes étudiant (bool)
    Puis affichez-les avec un message formaté.
    """
    nom = "Jean"
    age = 28
    taille = 1.75
    est_etudiant = False
    
    print(f"Je m'appelle {nom}, j'ai {age} ans et je mesure {taille}m.")
    print(f"Statut étudiant : {est_etudiant}")

# =============================================
# Exercice 2 : Conditions (if/elif/else)
# =============================================
def exercice_conditions(age):
    """
    Écrivez une fonction qui prend un âge en paramètre et affiche :
    - "Enfant" si age < 12
    - "Adolescent" si 12 <= age < 18
    - "Adulte" si 18 <= age < 65
    - "Senior" si age >= 65
    """
    if age < 12:
        print(f"Âge {age} : Enfant")
    elif 12 <= age < 18:
        print(f"Âge {age} : Adolescent")
    elif 18 <= age < 65:
        print(f"Âge {age} : Adulte")
    else:
        print(f"Âge {age} : Senior")

# =============================================
# Exercice 3 : Boucles (for et while)
# =============================================
def exercice_boucles(n):
    """
    Écrivez une fonction qui affiche :
    - Les nombres de 1 à n (inclus) avec une boucle for.
    - La somme des nombres de 1 à n avec une boucle while.
    """
    print("Boucle for (1 à n) : ", end="")
    for i in range(1, n + 1):
        print(i, end=" ")
    print() # Retour à la ligne

    somme = 0
    i = 1
    while i <= n:
        somme += i
        i += 1
    print(f"Somme des nombres de 1 à {n} (avec while) : {somme}")


# =============================================
# Exercice 4 : Fonctions
# =============================================
def exercice_fonctions(a, b):
    """
    Créez une fonction qui prend deux nombres en paramètre et retourne :
    - Leur somme
    - Leur produit
    - Le maximum entre les deux
    """
    somme = a + b
    produit = a * b
    maximum = max(a, b)
    
    print(f"Pour a={a} et b={b} -> Somme: {somme}, Produit: {produit}, Max: {maximum}")
    return somme, produit, maximum

# =============================================
# Exercice 5 : Manipulation de fichiers
# =============================================
def exercice_fichiers(nom_fichier, contenu):
    """
    Écrivez un script qui :
    1. Crée un fichier texte avec le contenu donné.
    2. Lit le contenu du fichier.
    3. Affiche le nombre de mots dans le fichier.
    """
    # 1. Créer et écrire dans le fichier
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(contenu)
        
    # 2. Lire le contenu du fichier
    with open(nom_fichier, "r", encoding="utf-8") as f:
        texte_lu = f.read()
        
    # 3. Compter et afficher le nombre de mots
    mots = texte_lu.split()
    print(f"Le fichier '{nom_fichier}' contient {len(mots)} mots.")

# =============================================
# Exercice 6 : Modules (os et shutil)
# =============================================
def exercice_modules(chemin_dossier):
    """
    Utilisez les modules os et shutil pour :
    1. Lister tous les fichiers d'un dossier.
    2. Créer une copie d'un fichier dans un sous-dossier "backup".
    """
    dossier = Path(chemin_dossier)
    
    # 1. Lister les fichiers
    fichiers = [f for f in dossier.iterdir() if f.is_file()]
    print(f"Fichiers dans '{chemin_dossier}' :")
    for f in fichiers:
        print(f" - {f.name}")

    # 2. Créer un backup
    dossier_backup = dossier / "backup"
    dossier_backup.mkdir(exist_ok=True) # Crée le dossier s'il n'existe pas

    # Exemple : copier le premier fichier de la liste (s'il y en a un)
    if fichiers:
        fichier_a_copier = fichiers[0]
        destination = dossier_backup / fichier_a_copier.name
        shutil.copy2(fichier_a_copier, destination)
        print(f"Le fichier '{fichier_a_copier.name}' a été copié dans '{dossier_backup}'.")
    else:
        print("Aucun fichier à copier.")

# =============================================
# Exercice 7 : Gestion des erreurs
# =============================================
def exercice_erreurs(numerateur, denominateur):
    """
    Écrivez une fonction qui divise deux nombres et gère :
    - La division par zéro.
    - Les erreurs de type (si les entrées ne sont pas des nombres).
    """
    try:
        resultat = numerateur / denominateur
        print(f"Résultat : {numerateur} / {denominateur} = {resultat}")
    except ZeroDivisionError:
        print(f"Erreur : Impossible de diviser {numerateur} par zéro.")
    except TypeError:
        print(f"Erreur : Le numérateur et le dénominateur doivent être des nombres (reçu: {type(numerateur)} et {type(denominateur)}).")

# =============================================
# Exercice 8 : Automatisation (renommage de fichiers)
# =============================================
def exercice_automatisation(chemin_dossier, prefixe):
    """
    Écrivez un script qui renomme tous les fichiers d'un dossier en ajoutant un préfixe.
    Exemple : "fichier.txt" -> "prefixe_fichier.txt"
    """
    dossier = Path(chemin_dossier)
    compteur = 0
    
    for fichier in dossier.iterdir():
        # On ignore les dossiers, et on évite de renommer des fichiers qui ont déjà le préfixe
        if fichier.is_file() and not fichier.name.startswith(prefixe):
            nouveau_nom = f"{prefixe}_{fichier.name}"
            fichier.rename(dossier / nouveau_nom)
            print(f"Renommé : {fichier.name} -> {nouveau_nom}")
            compteur += 1
            
    print(f"Total de fichiers renommés : {compteur}")

# =============================================
# Exercice 9 : Challenge - Suppression de fichiers vides
# =============================================
def exercice_challenge(chemin_dossier):
    """
    Écrivez un script qui parcourt un répertoire et supprime les fichiers vides.
    """
    dossier = Path(chemin_dossier)
    compteur = 0
    
    for fichier in dossier.iterdir():
        if fichier.is_file():
            # st_size retourne la taille du fichier en octets
            if fichier.stat().st_size == 0:
                fichier.unlink() # Supprime le fichier
                print(f"Supprimé (fichier vide) : {fichier.name}")
                compteur += 1
                
    print(f"Total de fichiers vides supprimés : {compteur}")

# =============================================
# Exercice 10 : Challenge final - Archivage de fichiers anciens
# =============================================
def exercice_final(chemin_dossier, jours_seuil=30):
    """
    Écrivez un script qui :
    1. Parcourt un répertoire.
    2. Déplace les fichiers modifiés il y a plus de `jours_seuil` jours dans un sous-dossier "anciens".
    3. Affiche le nombre de fichiers déplacés.
    """
    dossier = Path(chemin_dossier)
    dossier_anciens = dossier / "anciens"
    
    maintenant = time.time()
    seuil_en_secondes = jours_seuil * 24 * 3600
    compteur = 0

    for fichier in dossier.iterdir():
        if fichier.is_file():
            # st_mtime est le timestamp de la dernière modification
            age_en_secondes = maintenant - fichier.stat().st_mtime
            
            if age_en_secondes > seuil_en_secondes:
                dossier_anciens.mkdir(exist_ok=True)
                destination = dossier_anciens / fichier.name
                shutil.move(str(fichier), str(destination))
                print(f"Déplacé vers les archives : {fichier.name}")
                compteur += 1
                
    print(f"Nombre de fichiers anciens (>{jours_seuil} jours) déplacés : {compteur}")

# =============================================
# Fonction principale pour tester les exercices
# =============================================
def main():
    print("=== Exercices corrigés : Bases de Python pour le scripting ===\n")

    print("\n--- Exercice 1 : Variables ---")
    exercice_variables()

    print("\n--- Exercice 2 : Conditions ---")
    exercice_conditions(15)
    exercice_conditions(8)
    exercice_conditions(70)

    print("\n--- Exercice 3 : Boucles ---")