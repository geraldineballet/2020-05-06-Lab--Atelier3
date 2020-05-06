# 2020-05-06-Lab--Atelier3

## Mise en place d'un client FTP avec Python

Préparation d’une deuxième machine Debian, cette machine devra être sur le même réseau que la première.
Une machine aura pour rôle le serveur FTP, tandis que la deuxième sera le client ftp.
Réaliser un script python qui jouera le rôle de client ftp.

• Pouvoir se connecter, donc :
 o Entrer le nom d’hôte
 o Le nom d’utilisateur
 o Et le mot de passe, très important !
• Pouvoir envoyer une commande (nous les listerons un peu plus bas)
• Pouvoir taper une commande, mais avec des arguments ! (Petite nuance)

### Objectifs
• Créer
• Renommer
• Déplacer
• Supprimer
des fichiers et des dossiers

Ainsi que 
• Se déplacer entre les répertoires
• Lister leur contenu
• Envoyer un fichier sur notre serveur


#### Listing 
##### CWD (change current directory) *pour changer de répertoire*

##### DEL (delete) *pour supprimer un fichier / dossier*
##### LIST *pour lister les fichiers et dossiers d’un répertoire (si vous n’en spécifiez pas, alors ce sera le répertoire courant qui sera listé)*
##### MKD (make directory) *pour créer un répertoire*
##### RMD (remove directory) *pour supprimer un répertoire* 
##### RNFR (rename a file from (name …)) *pour renommer un répertoire X en … *
##### STOR (store a file) *pour envoyer un fichier sur le serveur.*
