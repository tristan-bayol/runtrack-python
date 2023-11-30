def time_to_text(minutes):
    if minutes < 0:
        print("Le nombre de minutes doit être positif.")
        return
    
    heures = minutes // 60
    minutes_restantes = minutes % 60

    if heures == 0:
        print(f"{minutes_restantes} minutes")
    elif heures == 1 and minutes_restantes == 0:
        print("1 heure")
    elif heures == 1 and minutes_restantes == 1:
        print("1 heure et 1 minute")
    elif heures == 1:
        print(f"1 heure et {minutes_restantes} minutes")
    elif minutes_restantes == 0:
        print(f"{heures} heures")
    elif minutes_restantes == 1:
        print(f"{heures} heures et 1 minute")
    else:
        print(f"{heures} heures et {minutes_restantes} minutes")

# Exemple d'utilisation
time_to_text(120)
time_to_text(275)