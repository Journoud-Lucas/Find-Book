[Français](README.md) | English

# 📚  **Find Book**
![License](https://img.shields.io/badge/License-UNLICENSE-red)![Latest Version](https://img.shields.io/badge/Version-1.0.0-blue) ![OS](https://img.shields.io/badge/OS-Windows%2FmacOS%2FLinux-green)

Find Book is an application that lets you find the name of a book (and its author) from a photo of its cover.
A library could use it, for example, so that its users can take a photo of a book they own and see if the library has the same copy, thanks to this application.
You don't need to know the book's ISBN to be able to search for it, which can be useful for old or self-published books. 
The application works on the basis of a database of books containing their cover, the name of the book and the name of the author.
Once the user has selected a book photo, the algorithm compares the image with all those in the database using ORB (Oriented FAST and Rotated BRIEF), calculating a match score for each image.
Once the entire database has been searched, the program will display the name of the book (as well as the author's name) on the cover with the highest match score with the photo of the book the user is looking for.

![Find Book](https://i.ibb.co/LR70by5/image.png)

## 🎓 School project
This is a small project for [Université Lumière Lyon 2](https://www.univ-lyon2.fr/).
We had to work in pairs for 2 hours on a Python project using an image extraction and description algorithm with OpenCV.

## 🔧 Features

- **Find a book:** Find the name of a book and its author from a photo of its cover.
- **Intuitive user interface:** A user interface simplifies interaction with the application.
- **Database management:** Easily add, modify or remove books from the database by modifying the contents of the .json file.

## 📖 How to use it

1. **Open:** Launch the application via main.py and click on "Browse images".
3. **Select image:** Select the image of the book whose name and author you are looking for.
2. **Observe:** The name of the book and its author will then be displayed on the graphical interface.

## 🔢 Versioning
This project is following [semantic versioning schema](https://semver.org/).

## 🤝 Credits
This project was created by:
- COSTA Julien
- JOURNOUD Lucas

## 📄 License
This software is under the [Unlicense](https://web.archive.org/web/20230703162904/https://unlicense.org/), terms of which are available in [UNLICENSE.txt](UNLICENSE.txt)
