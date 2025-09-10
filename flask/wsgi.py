import sys
import os

path = '/home/ton_nom_utilisateur/ton_dossier'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)

from serveur import app as application
