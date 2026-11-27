#######################
## CLASE: DISPOSITIU ##
#######################

# Tots els dispositius de la xarxa seran un objecte d'aquesta clase
# Els dispositius s'enllacen entre si (forman relacions pare-fill)
# Aquests enllaços formen l'arbre de dependència

from dataclasses import dataclass

# **from dataclasses import dataclass** ens facilitarà la manera d'escriure el codi de la classe
# Genera automàticament el __init__, fent que no s'hagi d'escriure self. per tots els elements


@dataclass
class Dispositiu:
    """Representació d'un node de la xarxa."""

# ---- DADES DE L'INVENTARI JSON ----
    id: str                     # Identificador del dispositiu
    nom: str                    # Nom descriptiu del dispositiu
    tipus: str                  # Categoria del dispositiu (router, switch...)
    ip: str                     # Adreça IPv4 assignada al dispositiu
    ubicacio: str               # Ubicació dins de l'edifici
    id_pare: str | None = None  # id del node del que depèn
                                # si id_pare és None, el dispositiu és un node arrel
                                # = None és per oferir que l'argument sigui opcional

    