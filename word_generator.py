

import csv
import random

def lire_csv(fichier_csv): #lis le csv dans un dictionnaire et compile le dictionnaire dans une liste
    list_mots = []
    print('opening file ', fichier_csv)
    with open(fichier_csv) as list_csv:
        reader = csv.DictReader(list_csv, delimiter=',')
        for word in reader:
            list_mots.append(word)
    return list_mots

def choix_nb_de_mots():
    print("Combien de mots voulez vous reviser ?")
    choix = int(input("Entrez un nombre de 1 a 40 : "))
    while (choix<1) or (choix>40):
        choix = input("Choix invalide. Entrez un nombre de 1 a 40 : ")
    return choix

def generation_mot_aleatoire(list_mots, choix): #selection n mots aleatoirement dans list_mots
    mots_selectionnes = [] 
    n = len(list_mots)
    m = len(mots_selectionnes)
    while m < choix:
        rand_index = random.randrange(0, n-1, 1)
        mots_selectionnes.append(list_mots[rand_index])
        list_mots.pop(rand_index)
        m += 1
        n -= 1
    return mots_selectionnes

def user_ready():
    print("Etes vous pret a commencer ?")
    suivant = input("Rentrez 1 quand vous etes pres a continuer : ")
    while suivant != '1':
        suivant = input("Choix invalide. Rentrez 1 quand vous etes pret a continuer : ")
    return suivant

def print_result(): #affiche les kanji des mots correspondant
    pass

def affiche_les_mots(suivant, mots_selectionnes):
    i = 0
    while i < len(mots_selectionnes):
       match suivant:
           case '1':
               word = mots_selectionnes[i]
               print(word)
               suivant = input("Rentrez 1 quand vous etes pres a continuer : ")
           case _:
               print('Choix invalide !')
       i = i+1
    print("C'est fini !!")



list_mots = lire_csv('vocab_list.csv')

choix = choix_nb_de_mots()

mots_selectionnes = generation_mot_aleatoire(list_mots, choix)

suivant = user_ready()
affiche_les_mots(suivant, mots_selectionnes)