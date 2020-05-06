# !/usr/bin/python3
# -*- coding : UTF-8 -*-
# Aurélie Berhault
# 6 mai 2020

from ftplib import FTP
from getpass import getpass

# Connexion
ftp = FTP('pc2')
login = input("login ? ")
mdp = getpass("mdp ? ")
ftp.login(user=login, passwd=mdp)

etat = ftp.getwelcome()
print("Etat:", etat)

# envoyer un fichier
fichier = "C:\Python_exercices\ftp.py"
file = open(fichier, 'rb')  # ici, j'ouvre le fichier ftp.py
connect.storbinary('STOR ' + fichier,
                   file)  # ici (où connect est encore la variable de la connexion), j'indique le fichier à envoyer
file.close()  # on ferme le fichier

# DELE (delete) pour supprimer un fichier / dossier
effacer = raw_input(
    'Tapez le nom du fichier à effacer : ')  # vous indiquez dans la console le fichier, ex. : fichier.py
delete = connect.delete(effacer)  # là, c'est la fonction en elle-même

# LIST pour lister les fichiers et dossiers d’un répertoire (si vous n’en spécifiez pas, alors ce sera le répertoire courant qui sera listé)
rep = connect.dir()  # on récupère le listing
print(rep)  # on l'affiche dans la console

# MKD (make directory) pour créer un répertoire
rep = raw_input('Tapez le nom du répertoire à créer : ')  # entrez le nom du répertoire, sans les slash ( / )
repertoire = connect.mkd(rep)  # la fonction pour le créer, "mkd()"

# RMD (remove directory) pour supprimer un répertoire
supprimer = raw_input('Tapez le nom du répertoire à supprimer : ')  # entrez le nom du dossier
delete_dir = connect.rmd(supprimer)  # la fonction rmd supprime le dossier

# RNFR (rename a file from (name …)) pour renommer un répertoire/fichier
renommer = raw_input(
    'Tapez le nom du fichier / dossier à renommer : ')  # ici, vous devez entrer le nom du fichier à renommer, par exemple fichier.txt ou le nom du dossier sans les /
renommer_en = raw_input('Le renommer en : ')  # le nom de sortie, vous pouvez aussi changer l'extension
rename = connect.rename(renommer, renommer_en)  # maintenant, on effectue vraiment l'action

# STOR (store a file) pour envoyer un fichier sur le serveur
fichier = "C:\Python_exercices\ftp.py"
file = open(fichier, 'rb')  # ici, j'ouvre le fichier ftp.py
connect.storbinary('STOR ' + fichier,
                   file)  # ici (où connect est encore la variable de la connexion), j'indique le fichier à envoyer
file.close()  # on ferme le fichier