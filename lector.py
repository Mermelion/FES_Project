########################
##   CLASE : LECTOR   ##
########################

# Aquesta clase permet llegir els json carregats per l'usuari
# Amb les dades llegides crearà dispositius

import json

class Lector:
    """Llegeix un fitxer JSON (configuració o llindars) i un objecte Dispositiu."""

    # Camps obligatoris que han de tenir cada tipus de fitxer JSON
    camps_config = ("id", "nom", "tipus", "ip", "ubicacio") # No posem el node pare perquè no és obligatori
    camps_llindars = ("latencia_max", "jitter_max", "perdues_max")

