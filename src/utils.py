import os
from tekore import Spotify

# direccion del path principal
BASE_DIR: str = os.path.dirname(os.path.dirname(__file__))


# tekore .cfg path
FILE_TEKORE: str = os.path.join(BASE_DIR, "tekore.cfg")


# carpeta donde se exportan las playlists
PLAYLISTS_DIR: str = os.path.join(BASE_DIR, "playlists")

# credenciales de la api spotify
CLIENT_ID_SPOTIFY: str = '1e0c8ce0ab5c4bb6a4bdf6735ab9e950'
CLIENT_SECRET_SPOTIFY: str = '9ecfcf4d27d94a4e908c644b45b68f84'
REDIRECT_URI_SPOTIFY: str = 'https://localhost:8000/callback'

# credenciales de youtube
API_KEY_YOUTUBE: str = "AIzaSyDxBafqudDX7YE7N5SJww_3OxIESSN77s8"

# credenciales de la api de genius
CLIENT_ID_GENIUS: str = "fYI4WYtFKPrbhG40VGPhGd2rv7pLBmMCpjIG3mgrl1JmXxcESW6YozwTg7CjvZu_"
CLIENT_SECRET_GENIUS: str = "7oaL53G1sgCaATqX1bXcrtA7uj9taxe6KhCPXfnyV7Xof9BXSqCVWF5E_284OmXQVRAMV_WPyusMNyA5p0e6PA"


def cls() -> None:
    """Limpia la terminal segun el sistema operativo"""

    command: str = 'clear'

    if os.name in ('nt', 'dos'):
        command = 'cls'

    os.system(command)


def validar_opcion(options: list) -> str:
    """Valida si la opción esta en la lista de opciones
    Args:
        options (list): Lista con las opciones disponibles
    Returns:
        str: Opción elegida
    """

    option: str = input("-> ")

    while (option not in options):
        option = input("Opción invalida, intente nuevamente: ")

    return option

def seleccionar_plataforma()-> str:
    print("Elija una la plataforma: ")
    print("[1]- Spotify")
    print("[2] - Youtube")
    
    opcion: str = validar_opcion(["1", "2"])
    
    if (opcion == "1"):
        return "spotify"
    else:
        return "youtube"   