#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercices  : Bases de Python pour le scripting d'automatisation
"""

import os
import shutil
import sys
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

    #TODO

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

    #TODO

# =============================================
# Exercice 3 : Boucles (for et while)
# =============================================
def exercice_boucles(n):
    """
    Écrivez une fonction qui affiche :
    - Les nombres de 1 à n (inclus) avec une boucle for.
    - La somme des nombres de 1 à n avec une boucle while.
    """

    #TODO


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

    #TODO

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

    #TODO

# =============================================
# Exercice 6 : Modules (os et shutil)
# =============================================
def exercice_modules(chemin_dossier):
    """
    Utilisez les modules os et shutil pour :
    1. Lister tous les fichiers d'un dossier.
    2. Créer une copie d'un fichier dans un sous-dossier "backup".
    """
    
    # 1. Lister les fichiers
    
    #TODO

    # 2. Créer un backup
    #TODO

    # Exemple : copier un fichier (remplacez 'fichier.txt' par un fichier existant)
    #TODO


# =============================================
# Exercice 7 : Gestion des erreurs
# =============================================
def exercice_erreurs(numerateur, denominateur):
    """
    Écrivez une fonction qui divise deux nombres et gère :
    - La division par zéro.
    - Les erreurs de type (si les entrées ne sont pas des nombres).
    """
    # Solution corrigée
    #TODO

# =============================================
# Exercice 8 : Automatisation (renommage de fichiers)
# =============================================
def exercice_automatisation(chemin_dossier, prefixe):
    """
    Écrivez un script qui renomme tous les fichiers d'un dossier en ajoutant un préfixe.
    Exemple : "fichier.txt" -> "prefixe_fichier.txt"
    """
    #TODO

# =============================================
# Exercice 9 : Challenge - Suppression de fichiers vides
# =============================================
def exercice_challenge(chemin_dossier):
    """
    Écrivez un script qui parcourt un répertoire et supprime les fichiers vides.
    """
    #TODO

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
    #TODO

# =============================================
# Fonction principale pour tester les exercices
# =============================================
def main():
    print("=== Exercices corrigés : Bases de Python pour le scripting ===\n")

    # Exercice 1
    print("\n--- Exercice 1 : Variables ---")
    exercice_variables()

    # Exercice 2
    print("\n--- Exercice 2 : Conditions ---")
    exercice_conditions(15)
    exercice_conditions(8)
    exercice_conditions(70)

    # Exercice 3
    print("\n--- Exercice 3 : Boucles ---")
    exercice_boucles(5)

    # Exercice 4
    print("\n--- Exercice 4 : Fonctions ---")
    exercice_fonctions(3, 7)

    # Exercice 5
    print("\n--- Exercice 5 : Manipulation de fichiers ---")
    exercice_fichiers("test.txt", "Bonjour le monde ! C'est un exercice de Python.")

    # Exercice 6 (à adapter avec un chemin valide)
    print("\n--- Exercice 6 : Modules (os/shutil) ---")
    # Remplacez par un chemin valide sur votre système
    exercice_modules(".")

    # Exercice 7
    print("\n--- Exercice 7 : Gestion des erreurs ---")
    exercice_erreurs(10, 2)
    exercice_erreurs(10, 0)
    exercice_erreurs("10", 2)

    # Exercice 8 (à adapter avec un chemin valide)
    print("\n--- Exercice 8 : Automatisation (renommage) ---")
    # Créez un dossier "test_renommage" avec des fichiers pour tester
    exercice_automatisation(".", "prefixe")

    # Exercice 9 (à adapter avec un chemin valide)
    print("\n--- Exercice 9 : Challenge - Suppression de fichiers vides ---")
    # Créez un fichier vide "fichier_vide.txt" pour tester
    exercice_challenge(".")

    # Exercice 10 (à adapter avec un chemin valide)
    print("\n--- Exercice 10 : Challenge final ---")
    # Créez des fichiers avec des dates de modification anciennes pour tester
    exercice_final(".", jours_seuil=1)

if __name__ == "__main__":
    main()