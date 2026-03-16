"""
🕵️‍♂️ TP EXIF - ENQUÊTE SUR LES MÉTADONNÉES
==========================================

Ce script permet d'explorer les données cachées dans vos fichiers images.
Nécessite la bibliothèque Pillow : pip install Pillow
"""

from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def to_degrees(value):
    """
    Helper pour convertir un tuple (num, den) ou un IFDRational en float.
    """
    if isinstance(value, tuple) and len(value) == 2:
        if value[1] == 0: 
            return 0.0
        return value[0] / value[1]
    
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0

def convertir_gps(coordonnees, reference):
    """
    Convertit les coordonnées DMS (Degrés, Minutes, Secondes) en format décimal.
    """
    if not coordonnees or len(coordonnees) < 3:
        return 0.0
        
    # Extraction des valeurs avec notre fonction helper sécurisée
    d = to_degrees(coordonnees[0])
    m = to_degrees(coordonnees[1])
    s = to_degrees(coordonnees[2])
    
    decimal = d + (m / 60.0) + (s / 3600.0)
    
    # Gestion de la direction (Nord/Sud, Est/Ouest)
    # Parfois 'reference' est en bytes (ex: b'N')
    if isinstance(reference, bytes):
        try:
            reference = reference.decode()
        except:
            reference = str(reference)
            
    reference = str(reference).upper()
    
    # Sud ou Ouest = Valeur négative
    if 'S' in reference or 'W' in reference:
        decimal = -decimal
        
    return decimal

def analyser_image(nom_fichier):
    """
    Extrait et affiche les principales données EXIF.
    """
    print(f"\n--- Analyse de : {nom_fichier} ---")
    
    try:
        img = Image.open(nom_fichier)
        exif_raw = img._getexif()
        
        if exif_raw is None:
            print("❌ Aucune donnée EXIF trouvée dans cette image.")
            return

        # Dictionnaire pour stocker les infos converties
        exif_info = {}
        gps_info = {}

        for tag_id, value in exif_raw.items():
            tag_name = TAGS.get(tag_id, tag_id)
            
            # Cas particulier : Données GPS
            if tag_name == "GPSInfo":
                try:
                    for gps_id in value:
                        gps_tag_name = GPSTAGS.get(gps_id, gps_id)
                        gps_info[gps_tag_name] = value[gps_id]
                except Exception as e:
                    print(f"⚠️ Erreur lecture GPS : {e}")
            else:
                exif_info[tag_name] = value

        print(f"📷 Appareil   : {exif_info.get('Make', 'Inconnu')} {exif_info.get('Model', '')}")
        print(f"📅 Date/Heure : {exif_info.get('DateTime', 'Inconnue')}")
        print(f"⚙️  Logiciel   : {exif_info.get('Software', 'Inconnu')}")
        
        # Affichage GPS si présent
        # On vérifie qu'on a bien Latitude et Longitude
        if 'GPSLatitude' in gps_info and 'GPSLongitude' in gps_info:
            try:
                lat_dms = gps_info.get('GPSLatitude')
                lat_ref = gps_info.get('GPSLatitudeRef')
                lon_dms = gps_info.get('GPSLongitude')
                lon_ref = gps_info.get('GPSLongitudeRef')
                
                lat_dec = convertir_gps(lat_dms, lat_ref)
                lon_dec = convertir_gps(lon_dms, lon_ref)
                
                if lat_dec != 0.0 or lon_dec != 0.0:
                    print(f"📍 Coordonnées : {lat_dec:.6f}, {lon_dec:.6f}")
                    print(f"🔗 Lien Maps   : https://www.google.com/maps?q={lat_dec},{lon_dec}")
                else:
                    print("📍 Coordonnées : Format illisible ou vide.")
            except Exception as e:
                print(f"⚠️ Erreur calcul coordonnées : {e}")
        else:
            print("📍 Coordonnées : Aucune donnée GPS trouvée.")

    except FileNotFoundError:
        print(f"⚠️ Erreur : Le fichier '{nom_fichier}' est introuvable.")
    except Exception as e:
        print(f"⚠️ Une erreur est survenue : {e}")

def nettoyer_image(nom_fichier):
    """
    Crée une copie de l'image sans aucune métadonnée.
    """
    try:
        img = Image.open(nom_fichier)
        # Supprime les données EXIF (pas de mot clé exif dans save)
        # Mais pour être sûr, on crée une nouvelle image
        data = list(img.getdata())
        nouvelle_img = Image.new(img.mode, img.size)
        nouvelle_img.putdata(data)
        
        nouveau_nom = "CLEAN_" + nom_fichier
        nouvelle_img.save(nouveau_nom)
        print(f"✅ Image nettoyée sauvegardée sous : {nouveau_nom}")
    except Exception as e:
        print(f"⚠️ Impossible de nettoyer l'image : {e}")

# ============================================================================
# PROGRAMME PRINCIPAL
# ============================================================================

if __name__ == "__main__":
    print("      🔍 BIENVENUE DANS L'EXTRACTEUR EXIF 🔍")
    print("==============================================")
    
    # Recherche automatique des images mystères
    import os
    fichiers = [f for f in os.listdir('.') if f.startswith('photo_mystere') and f.endswith('.jpg')]
    fichiers.sort()
    
    nom_choisi = ""
    
    if fichiers:
        print("\nImages disponibles :")
        for i, f in enumerate(fichiers):
            print(f"  {i+1}. {f}")
        
        choix = input("\nChoisissez le numéro de l'image (ou entrez un nom de fichier) : ")
        
        if choix.isdigit() and 1 <= int(choix) <= len(fichiers):
            nom_choisi = fichiers[int(choix)-1]
        else:
            nom_choisi = choix
    else:
        nom_choisi = input("Entrez le nom de l'image à analyser (ex: ma_photo.jpg) : ")

    if nom_choisi == "":
        print("❌ Aucun fichier sélectionné.")
    else:
        analyser_image(nom_choisi)
        
        reponse = input("\nVoulez-vous créer une version 'propre' sans métadonnées ? (o/n) : ")
        if reponse.lower() == 'o':
            nettoyer_image(nom_choisi)
    
    print("\n👋 Fin du programme.")
