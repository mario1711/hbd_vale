import pyautogui
import os
import time
import requests
from PIL import Image
from io import BytesIO
import threading
import pymsgbox
import subprocess


def escribir_letra_por_letra(text, retraso=0.1):
    for caracter in text:
        pyautogui.write(caracter)
        time.sleep(retraso)


letras = {
    'V': [(x + 20, y + 170) for x, y in [(0, 0), (20, 40), (20, 40), (40, 0)]],
    'a': [(x + 20, y + 170) for x, y in [(60, 40), (80, 0), (80, 0), (100, 40)]],
    'l': [(x + 20, y + 170) for x, y in [(120, 0), (120, 20), (120, 40), (140, 40)]],
    'e': [(x + 20, y + 170) for x, y in [(200, 0), (160, 0), (180, 20), (160, 40), (200, 40)]],
    'r': [(x + 20, y + 170) for x, y in [(220, 40), (220, 0), (260, 0), (240, 20), (260, 40)]],
    'y': [(x + 20, y + 170) for x, y in [(280, 0), (300, 20), (320, 0), (300, 20), (300, 40)]]
}


# Función para dibujar una letra
def dibujar_letra(coordenadas):
    for coord_inicio, coord_fin in zip(coordenadas[:-1], coordenadas[1:]):
        pyautogui.moveTo(*coord_inicio)
        pyautogui.dragTo(*coord_fin, duration=0.3)


# Función para dibujar el nombre "Valery"
def dibujar_nombre():
    for letra, coordenadas in letras.items():
        dibujar_letra(coordenadas)


def mostrar_alerta(text):
    pymsgbox.alert(
        text=text, title='Prueba Final', button='OK')
    time.sleep(2)


def abrir_bloc():
    pyautogui.press('win')
    pyautogui.write('Bloc de notas')
    pyautogui.press('enter')
    time.sleep(2)


def abrir_paint():
    pyautogui.press('win')
    pyautogui.write('paint')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('win', 'up')
    time.sleep(2)


def corazones_terminal():
    comando = "@echo off color 04  && echo Hola "

    for _ in range(1, 10):
        subprocess.run(comando, shell=True)


url = "https://colorir.me/wp-content/uploads/2023/03/kuromi-sorridente.jpg"
response = requests.get(url)

if __name__ == '__main__':
    #   mostrar_alerta('Felicidades has pasado a la prueba final \nPresiona el boton de okay y no hagas nada hasta que '
    #                  'se te pida que lo hagas')

    #   abrir_bloc()
    #   escribir_letra_por_letra('Hola Valery , felicidades has conseguido llegar hasta la prueba final')
    # abrir_paint()
    # dibujar_nombre()

    corazones_terminal()

'''
    if response.status_code == 200:

        image = Image.open(BytesIO(response.content))

        image.show()
    else:
        print("Error al descargar la imagen:", response.status_code)

'''
