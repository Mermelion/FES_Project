#######################
## CLASE: DISPOSITIU ##
#######################

# Tots els dispositius de la xarxa seran un objecte d'aquesta clase
# Els dispositius s'enllacen entre si (forman relacions pare-fill)
# Aquests enllaços formen l'arbre de dependència

class Dispositiu:
# ---- DADES DE L'INVENTARI JSON ----
    id: str         # Identificador del dispositiu
    nom: str        # Nom del dispositiu
    tipus: str      # Categoria del dispositiu (router, switch...)
    ip: str         # Adreça IPv4 assignada al dispositiu
    ubicacio: str   # Ubicació dins de l'edifici
    node_pare:      # id del node del que depèn

