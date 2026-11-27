########################
## CLASE : DISPOSITIU ##
########################

# Tots els dispositius de la xarxa seran un objecte d'aquesta clase
# Els dispositius s'enllacen entre si (forman relacions pare-fill)
# Aquests enllaços formen l'arbre de dependència

from dataclasses import dataclass, field
from typing import Optional, List

# **from dataclasses import dataclass** ens facilitarà la manera d'escriure el codi de la classe
# Genera automàticament el __init__, fent que no s'hagi d'escriure self. per tots els elements

# **from typing import Optional, List** Optional ens permetrà indicar que una variable pot ser del tipus indicat o None
# List ens permetrà indicar que una variable és una llista de valors del tipus indicat


@dataclass  # Genera automàticament __init__ amb els atributs de la classe
class Dispositiu:
    """Representació d'un node de la xarxa."""

# ---- DADES DE L'INVENTARI JSON ----

    id:       str                   # Identificador del dispositiu
    nom:      str                   # Nom descriptiu del dispositiu
    tipus:    str                   # Categoria del dispositiu (router, switch...)
    ip:       str                   # Adreça IPv4 assignada al dispositiu
    ubicacio: str                   # Ubicació dins de l'edifici
    id_pare:  Optional[str] = None  # id del node del que depèn
        # si id_pare és None, el dispositiu és un node arrel
        # Optiona[str] equival a str | None. = None indica que el valor per defecte és None

# -------- ENLLAÇ A L'ARBRE --------

    pare: Optional["Dispositiu"] = field(default = None, repr = False)
        # Cada node tindrà la opció de pare. Serveix per indicar a quin node depèn. Si no en té, serà None.

        # Optional["Dispositiu"] indica que pare guarda un objecte de tipus Dispositiu o None. S'ha de posar entre cometes
        # perquè encara no s'ha definit la classe Dispositiu

        # repr = False serveix per evitar bucles a la hora de mostrar l'objecte per pantalla.
        # Si no es posa, quan es mostri un dispositiu, mostrarà el pare, i aquest tornarà a mostrar el fill, i així infinitament.

    fills: List["Dispositiu"] = field(default_factory = list, repr = False)
        # Cada node tindrà la opció de fills. Serveix per guardar els nodes que depenen d'aquest. Si no en té, serà una llista buida.

        # List["Dispositiu"] indica que fills guarda una llista d'objectes de tipus Dispositiu. S'ha de posar entre cometes perquè
        # perquè encara no s'ha definit la classe Dispositiu

        # default_factory = list indica que el valor per defecte és una llista (buida). Si no es posa, tots els objectes compartirien
        # la mateixa llista.

# ----- RESULTATS DE L'ANÀLISI -----

# Posarem tots els camps en None per defecte, ja que encara no s'han analitzat

    disponibilitat:     Optional[float] = None  # % de pings respostos
    perdues:            Optional[float] = None  # % de pings perduts
    latencia_mitjana:   Optional[float] = None  # Latència mitjana (ms)
    jitter:             Optional[float] = None  # Variació de la latència (ms)
    estat:              Optional[str]   = None  # Estat del dispositiu (ÒPTIM, DEGRADAT O CAIGUT)
    causa:              Optional[str]   = None  # Causa de l'estat del dispositiu (ARREL O COLATERAL)

# ------------ MÈTODES ------------

# AÚN FALTA, VOY A IR A POR OTRA CLASE (Adri)