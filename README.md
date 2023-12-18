[Français](README.md) | English

# 📚  **Find Book**
![License](https://img.shields.io/badge/License-UNLICENSE-red)![Latest Version](https://img.shields.io/badge/Version-1.0.0-blue) ![OS](https://img.shields.io/badge/OS-Windows%2FmacOS%2FLinux-green)

Find Book est une application permetant de trouver le nom d'un livre (et de son auteur) à partir d'une photo de sa couverture.
Une bibliothèque pourrais par exemple l'utiliser afin que leur utilisateur puisse prendre une photo d'un livre qu'ils possèdent et voir si la bibliothèque possède le même exemplaire grâce a cette application.
Il n'est donc pas nécessaire de connaître l'ISBN du livre afin de pouvoir le rechercher, ceux qui peux être utile pour des livres anciens ou bien des livres autopubliés. 
L'application fonctionne grâce a une base de donnée de lires contenant leur couverture, le nom du livre ainsi que le nom de l'auteur.
Quand l'utilisateur aura séléctionnez la photo de son livre, l'algorithme va comparer l'image avec toute celle de la base de donnée en utilisant l'ORB (Oriented FAST and Rotated BRIEF) en calculant un score de correspondance avec chacune des images.
Une fois toute la base de données parcouru, le programme va afficher le nom du livre (ainsi que le nom de l'auteur) de la couverture ayant eu le plus gros score de correspondance avec la photo du livre recherché par l'utilisateur.

![Find Book](https://i.ibb.co/LR70by5/image.png)


## 🎓 Projet d'école
Il s'agit d'un petit projet fait pour [l'Université Lumière Lyon 2](https://www.univ-lyon2.fr/).
En effet nous devions faire en binôme en 2heure un projet Python utilisant un algorithme d’extraction et de description d’image avec OpenCV.

## 🔧 Fonctionnalités

- **Trouvez un livre :** Trouvez le nom d'un livre ainsi que le nom de son auteur depuis une photo de sa couverture.
- **Interface Utilisateur Intuitive :** Une interface utilisateur simplifie l'interaction avec l'application.
- **Gestion de la base de donnée :** Ajoutez ou modifiez voire supprimez des livres de la base de données facilement en modifiant le contenu du .json.


## 📖 Comment l'utiliser

1. **Ouverture :** Lancez l'application, via main.py et cliquez sur "Parcourir les images".
3. **Séléctionnez l'image :** Séléctionnez l'image du livre dont vous cherchez le nom et l'auteur.
2. **Observer :** Le nom du livre ainsi que le nom de son auteur vont ensuite s'afficher sur l'interface graphique.

## 🔢 Versionnage
Ce projet suit un schéma de [versionnement sémantique](https://semver.org/).

## 🤝 Crédits
Ce projet a été créé par:
- COSTA Julien
- JOURNOUD Lucas

## 📄 License
Ce logiciel est sous [Unlicense](https://web.archive.org/web/20230703162904/https://unlicense.org/), dont les termes sont disponibles dans [UNLICENSE.txt](UNLICENSE.txt)
