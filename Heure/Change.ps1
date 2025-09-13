# Script PowerShell pour changer l'heure sur Windows 10 sans permissions administratives

# Définir la nouvelle heure (format: HH:MM)
$newHour = "14:30"

# Extraire les composants de l'heure
$hours, $minutes = $newHour -split ':'

# Convertir les composants en entiers
$hours = [int]$hours
$minutes = [int]$minutes

# Obtenir l'objet DateTime actuel
$currentDate = Get-Date

# Créer un nouvel objet DateTime avec la nouvelle heure
$newDate = $currentDate.AddHours($hours - $currentDate.Hour).AddMinutes($minutes - $currentDate.Minute)

# Utiliser WMI pour définir la nouvelle heure
$wmiService = Get-WmiObject -Class Win32_LocalTime
$wmiService.Year = $newDate.Year
$wmiService.Month = $newDate.Month
$wmiService.Day = $newDate.Day
$wmiService.Hour = $newDate.Hour
$wmiService.Minute = $newDate.Minute
$wmiService.Second = $newDate.Second
$wmiService.Put()

# Afficher un message de confirmation
Write-Output "L'heure a été changée avec succès à $newHour."
