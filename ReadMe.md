# Outil Vérificateur de Bytecode

Projet réalisé par Clément Charrier et Baptiste Letord

## Utilisation de l'outil 

```shell
python main.py app-debug MainActivity
```

* **main.py** : nom du fichier python à exécuter
* **app-debug** : nom du paquet apk
* **MainActivity** :  nom de la classe à analyser



#### Fichier généré par l'outil 

Le programme Python génére un fichier ayant le nom de la classe analysée.

Par exemple avec la commande ci-dessus génére un fichier MainActivity.report.



## Architecture de l'application

Liste des fichiers : 

* **main.py** est le fichier principal permettant de lancer l'outil  
* **basic.py** est un fichier contennant de nombreuses fonctions utilisées dans les autres fichiers
* **simulation_registre.py** est le fichier contenant les fonctions permettant de faire la vérification de bytecode simple (analyse n°1).
* **verification_permissions.py** est le fichier contenant les fonctions permettant de vérifier la bonne initialisation des objets (analyse n°2 - Non traitée).
* **extraction_registre.py** est le fichier contenant les fonctions permettant l'extraction des données de la classe et de ses méthodes dans le fichier .report (analyse n°3).
* **app-debug.apk** est un fichier pour tester l'outil.

