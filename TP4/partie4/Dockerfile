# Image de base Python
FROM python:3.11-slim

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY templates/ templates/

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "app.py"]

