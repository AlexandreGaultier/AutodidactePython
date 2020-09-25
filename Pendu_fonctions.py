import os
import pickle
from random import choice
from Pendu_donnees import *

def recup_scores():
    if os.path.exists(nom_fichier_scores):
        ficher_scores = open(nom_fichier_scores, "rb")
        mon_depickler = pickle.Unpickler(ficher_scores)
        scores = mon_depickler.load()
        ficher_scores.close()
    else:
        scores = {}
    return scores

def enregistrer_scores(scores):
    fichier_scores = open(nom_fichier_scores, "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()

