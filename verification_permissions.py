from androguard.misc import AnalyzeAPK

"""
2 : Bonne initialisation des objets : cette analyse permet de verifier qu’il n’y a aucun acces (lecture/ecriture d’un 
champ, appel de methode) a un objet alloue mais non initialise.
"""

# Analyse 2