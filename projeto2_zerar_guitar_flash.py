import pyautogui as pag
from time import sleep
import keyboard

#1 -verificar se a cor correspondente esta na localização correta

while keyboard.is_pressed("1") == False: 

    if pag.pixelMatchesColor(913,562,(0,152,0)):
        pag.press('a')
        sleep(0.5)
    if pag.pixelMatchesColor(1001,562,(255,0,0)):
        pag.press('s')
        sleep(0.5)
    if pag.pixelMatchesColor(1089,561,(244,244,2)):
        pag.press('j')
        sleep(0.5)
