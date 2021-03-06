from utils import *
from tekore import Spotify
from wordcloud import WordCloud
from spotify_api import *
from youtube_api import *
from lyricsgenius import Genius
import re
import matplotlib.pyplot as plt


def obetener_info_de_tracks_spotify(spotify: Spotify)-> dict:
    """obtiene la informacion de las canciones de la playlist elegida del usuario actual
    Args:
        spotify (Spotify): Instancia de la api de spotify

    Returns:
        dict: Diccionario con la informacion de las canciones
    """
    playlist_tracks_info = {}

    id_playlist_buscada = buscar_playlist_spotify(spotify)
    playlist = spotify.playlist(id_playlist_buscada)

    # obtengo los objetos 'PlaylistTrack' de la playlist
    oj_playlist_tracks = playlist.tracks.items
    # guardo la el nombre de la cancion y el nombre del artista
    for oj_track in oj_playlist_tracks:
        playlist_tracks_info[oj_track.track.name] = oj_track.track.artists[0].name
    
    return playlist_tracks_info


def limpiar_letras(letras: tuple) -> str:
    """limpia las letras de las canciones de playlist elegida del usuario actual"""
    # creo un string con todas las letras de las canciones
    letras_canciones_string = ' '.join(letras)

    letras_canciones_string = letras_canciones_string.replace('\n', ' ')
    letras_canciones_string = letras_canciones_string.replace('\r', ' ')
    # elimino el "(Text Back)" de las letras
    letras_canciones_string = re.sub(r'\(Text Back\)', '', letras_canciones_string) 
    # elimino lo que esta entre [] en las letras
    letras_canciones_string = re.sub(r'\[.*?\]', '', letras_canciones_string)
    
    return letras_canciones_string



def limpiar_nombres_canciones_youtube(canciones: dict)-> dict:
    """limpia los nombres de las canciones de la playlist elegida del usuario actual"""
    # creo un string con todas las letras de las canciones
    nombres_limpios: dict = {}
    for autor, cancion in canciones.items():
        nombre_limpio: str = ""
        nombre_limpio = re.sub(r'\(.*?\)', '', cancion)
        nombre_limpio = re.sub(r'\[.*?\]', '', nombre_limpio)
        nombres_limpios[autor] = nombre_limpio
    
    return nombres_limpios

def generar_wc():
    """genera un wordcloud con las letras de las canciones de playlist elegida del usuario actual"""
    genius = Genius(CLIENT_ID_GENIUS)
    plataforma = seleccionar_plataforma()

    if plataforma == 'spotify':
        spotify = llamar_api_spotify()
        playlist_tracks_info = obetener_info_de_tracks_spotify(spotify)
    # playlist_tracks_info = obetener_info_de_tracks_spotify(spotify)
    elif plataforma == 'youtube':
        youtube = autenticar_youtube()
        playlist_tracks_info = obtener_nombres_de_canciones_youtube(youtube)
        playlist_tracks_info = limpiar_nombres_canciones_youtube(playlist_tracks_info)

    # creo un diccionario con las letras de las canciones
    letras_canciones = {}

    for key, value in playlist_tracks_info.items():
        try:
            letras_canciones[key] = genius.search_song(value, key)
        
        except Exception as e:
            print("")
            
    for key, value in letras_canciones.items():
        
        if value is None:
            letras_canciones[key] = ''
        else:
            letras_canciones[key] = value.lyrics

    # limpio las letras
    letras_str: str = limpiar_letras(letras_canciones.values())
    # genero un wordcloud con las letras de las canciones
    try:
        wordcloud = WordCloud(width=800, height=400, random_state=21, max_words=10).generate(letras_str)
        # muestro el wordcloud
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    except ValueError as e:
        print('No se pudo generar el wordcloud porque no hay letras para generar el wordcloud: ', e)
        input('Pulse enter para continuar')