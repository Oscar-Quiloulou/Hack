# Script PowerShell pour créer un nouveau compte utilisateur avec permissions administratives sans permissions administratives initiales

# Définir le nom d'utilisateur et le mot de passe
$username = "NewAdminUser"
$password = "Password123"

# Créer un objet de sécurité pour le mot de passe
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force

# Créer le nouveau compte utilisateur
New-LocalUser -Name $username -Password $securePassword -FullName "New Admin User" -Description "Account created without admin privileges"

# Ajouter le nouvel utilisateur au groupe Administrateurs
Add-LocalGroupMember -Group "Administrators" -Member $username

# Afficher un message de confirmation
Write-Output "Le compte utilisateur $username a été créé avec succès et ajouté au groupe Administrateurs."
