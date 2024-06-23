# Service d'Extraction de Texte et de Conversion en Parole

Ce projet propose un service d'extraction de texte à partir d'images avec une option de conversion du texte en parole. Il est composé d'un frontend en Vue.js et d'un backend en Flask.

## Fonctionnalités

- **Téléchargement d'Image**: Permet aux utilisateurs de télécharger une image depuis leur appareil.
- **Extraction de Texte**: Extrait le texte contenu dans l'image téléchargée.
- **Conversion Texte en Parole**: Convertit le texte extrait en fichier audio que l'utilisateur peut écouter.

## Installation des Dépendances

### Frontend

1. **Naviguez dans le répertoire du frontend** :
   ```sh
   cd Front

2. **Installez les dépendances avec npm ou yarn :
   ```sh
   npm install
   ```
   ou 
   
   ```sh
   yarn install
   
3. **Démarrez le serveur de développement :
   ```sh
   npm run dev

L'application frontend sera disponible à l'adresse suivante : http://localhost:3000.

### Backend
1. Naviguez dans le répertoire du backend :
   ```sh
   cd Back

2. (Optionnel) Créez un environnement virtuel :
   ```sh
   python -m venv venv

3. Activez l'environnement virtuel :
 - Sur Windows :
   ```sh
   venv\Scripts\activate
 - Sur macOS et Linux : 
   ```sh
   source venv/bin/activate

4. Installez les dépendances :
   ```sh
   pip install -r requirements.txt

5. Démarrez le serveur Flask :
   ```sh
   python app.py

L'API backend sera disponible à l'adresse suivante : http://localhost:5000.

### Utilisation
1. **Téléchargez une image :** Utilisez le champ de téléchargement pour sélectionner une image depuis votre appareil.
2. **Extrait le texte :** Cliquez sur le bouton "Extraire le texte" pour extraire le texte de l'image.
3. **Convertissez le texte en parole :** Après l'extraction du texte, cliquez sur l'icône de haut-parleur pour convertir le texte en parole et écouter le fichier audio généré.

### Technologies Utilisées
   **- Frontend :** Vue.js, Vuetify

   **- Backend :** Flask, Tesseract (pour l'extraction de texte), gTTS (pour la conversion texte en parole)

