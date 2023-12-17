import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import cv2
import json
import os

def preprocess_image(image_path):
    # Charge l'image, la convertit en niveaux de gris et applique un filtre
    try:
        image = cv2.imread(image_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        processed_image = cv2.GaussianBlur(gray, (5, 5), 0)
        return processed_image
    except: 
        # Vérifie si l'image a bien été traité
        # La plupart des exceptions viendrons d'une image qui n'as pas pu être ouvert (chemin incorrect, privilège insuffisant, image utilisé par un autre processus etc...)
        messagebox.showerror("Erreur lors du traitement de l'image", f"Erreur lors du prétraitement de l'image : {image_path}\r\n")
        return None

def detect_and_describe(image):
    # Initialise l'ORB detector
    orb = cv2.ORB_create()
    # Détecte les points clés et les descripteurs
    _, descriptors = orb.detectAndCompute(image, None)
    return descriptors

def match_descriptors(descriptor1, descriptor2):
    # Utilise le matcher BF avec la distance de Hamming pour trouver les correspondances
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptor1, descriptor2)
    # Trie les correspondances basées sur leur distance (les meilleures en premier)
    matches = sorted(matches, key=lambda x: x.distance)
    return matches
    
def find_book_cover(user_image_path, database):
    # Prétraitement de l'image de l'utilisateur
    user_image = preprocess_image(user_image_path)
    user_descriptors = detect_and_describe(user_image)

    # Initialisation des variables pour stocker la meilleure correspondance
    best_match = None
    best_score = 0
    best_match_info = ()

    # Parcours de chaque entrée dans la base de données
    for entry in database:
        db_image_path, book_title, author_name = entry
        
        # Prétraitement de l'image de la base de données
        db_image = preprocess_image(db_image_path)
        db_descriptors = detect_and_describe(db_image)

        # Comparaison des descripteurs et récupération des correspondances
        matches = match_descriptors(user_descriptors, db_descriptors)
        
        # Si des correspondances sont trouvées et le score est meilleur que la meilleure correspondance actuelle
        if matches and len(matches) > best_score:
            best_score = len(matches)
            best_match = db_image_path
            best_match_info = (book_title, author_name)

    # Retourne le chemin de la meilleure correspondance, le score et les informations du livre
    return best_match, best_score, best_match_info

def load_database_from_json(json_file):
    # Chargement de la base de données des images depuis le json
    with open(json_file, 'r', encoding="UTF-8") as file:
        return json.load(file)
    
def browse_image():
    # Séléction de l'image du livre par l'utilisateur
    filename = filedialog.askopenfilename(title="Sélectionner une image", filetypes=[("Fichiers images", "*.bmp;*.dib;*.jpeg;*.jpg;*.jpe;*.jp2;*.png;*.webp;*.pbm;*.pgm;*.ppm;*.pxm;*.pnm;*.pfm;*.sr;*.ras;*.tiff;*.tif;*.exr;*.hdr;*.pic")])
    if filename:
        # Récupération de la meilleur correspondance
        matched_cover, score, (book_title, author_name) = find_book_cover(filename, database) 
        if matched_cover:
                # Si une correspondance a bien été trouvé, alors on l'affiche a l'utilisateur
            result_text.set(f"Titre du livre: {book_title}\r\nAuteur: {author_name}\r\nScore de correspondance: {score}")
        else:
            result_text.set("Aucune correspondance suffisante n'a été trouvée.")
    else:
        messagebox.showerror("Erreur", "Aucune image n'a été sélectionnée")

# Emplacement du script pour le chemin relatif au .py
script_directory = os.path.dirname(os.path.realpath(__file__))
try:
    # Chemin du .json
    json_file_path = os.path.join(script_directory, 'database.json')
    # Chargement des données
    database = load_database_from_json(json_file_path)
except:
    # Vérifie si les données du json ont bien été récupéré
    # La plupart des exceptions viendrons d'une bdd qui n'as pas pu être ouvert (chemin incorrect, privilège insuffisant, fichier utilisé par un autre processus etc...)
    messagebox.showerror("Erreur lors de l'ouveture de la base de donnée", f"Erreur lors de l'ouveture de la base de donnée.\r\nVérifier que la base de donnée existe et est accesible a ce chemin: {json_file_path}")
    exit

# Rajout du chemin du .py avant tout les chemins des images.
# Exemple: BDD\\Marc Levy Noa.jpg
# Deviens: D:\Bureau\python\BDD\Marc Levy Noa.jpg
for sous_liste in database:
    sous_liste[0] = os.path.join(script_directory, sous_liste[0])

# Initialiser l'interface graphique principale
root = tk.Tk()
root.title("Reconnaissance de couverture de livre")
root.configure(bg="grey")

# État du texte du résultat
result_text = tk.StringVar()

# Ajouter un bouton pour parcourir les images de couverture de livre
browse_button = tk.Button(root, text="Parcourir les Images", command=browse_image)
browse_button.pack()

# Ajouter un label pour afficher le résultat
result_label = tk.Label(root, textvariable=result_text, bg="grey", width=80, height=10)
result_label.pack()
result_text.set("Aucune image n'as été séléctionné.")

# Boucle principale de Tkinter
root.mainloop()