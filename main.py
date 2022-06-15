import os
from autenticar_en_plataformas import *


def cls() -> None:
    """Limpia la terminal segun el sistema operativo"""

    command: str = 'clear'

    if os.name in ('nt', 'dos'):
        command = 'cls'

    os.system(command)


def validate_option(options: list) -> str:
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


def main() -> None:

    cls()
    flag: bool = True


    while (flag):
        print("""
        [1] Listar las playlists actuales para un determinado usuario y plataforma
        [2] Elegir una playlist y exportarla a CSV indicando los 10 atributos principales
        [3] Crear una nueva playlist
        [4] Buscar nuevos elementos para visualizar o agregarlos a una playlist
        [5] Sincronizar una playlist entre Youtube y Spotify, (se exportaran en un archivo
            CSV los elementos que no encuentren en la plataforma de destino)
        [6] Analizar una playlist y construir la nube de palabras y el ranking del top 10 de
            palabas más utilizadas en las letras de dicha playlist
        [7] Salir
        """)
        option: str = validate_option(["1", "2", "3", "4", "5", "6"])

        if (option == "1"):
            autenticar_en_spotify()

        elif (option == "2"):
            pass
        
        elif (option == "3"):
            pass

        elif (option == "4"):
            pass

        elif (option == "5"):
            pass

        elif (option == "6"):
            pass

        elif (option == "7"):
            flag = False

main()