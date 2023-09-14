import pyautogui
import webbrowser
from time import sleep

def sair():
    pyautogui.click(1311,145, duration=2)
    sleep(2)
    pyautogui.click(1267,678,duration=2)
    sleep(2)
    pyautogui.click(979,202,duration=2)
    sleep(2)
    pyautogui.click(1039,515, duration=2)
    sleep(5)
while True:
    # Passos para criação do Bot de curtidas e comentarios.
    # 1-abrir uma aba no navegador
    webbrowser.open_new_tab('https://instagram.com')
    sleep(20)
    pyautogui.click(987,525,duration=2)
    sleep(2)
    # 2-vá ate campo de usuario, clicar e digitar o usuario
    pyautogui.click(1000,319,duration=2)
    pyautogui.typewrite('wesley.jr95')
    sleep(1)
    # 3-vá ate campo de senha,clicar e digitar a senha
    pyautogui.click(1004,370,duration=2)
    pyautogui.typewrite('lovesong')
    sleep(1)
    # 4-vá ate entrar, clicar
    pyautogui.click(1007,415,duration=2)
    sleep(20)
    # 5-clicar no botão de (agora não)
    pyautogui.click(1038,520,duration=2)
    sleep(40)
    # 6-clicar na barra de pesquisa,digitar (PUMA) + enter
    pyautogui.click(1124,151,duration=2)
    sleep(15)
    pyautogui.click()
    pyautogui.typewrite('puma')
    sleep(4)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.press('enter')
    sleep(30)
    # 7-clicar na publicação mais recente(primeira)
    pyautogui.click(832,604, duration=2)
    sleep(3)
    # 8-verificar se já foi curtida
    coracao = pyautogui.locateCenterOnScreen('coracao.png')
    sleep(2)
    # 9-se já curtiu ,fazer nada pausa bot por 24 horas
    if coracao is not None:
        sair()
        sleep(86400)
    # 10- se não curti a foto, curti
    elif coracao == None:
        pyautogui.click(953,564, duration=2)
        sleep(5)
        # 11-ir para comentario e clicar
        pyautogui.click(992,564,duration=2)
        sleep(2)
        # 12-vá para campo e digite o comentario
        pyautogui.click(1034,664, duration=2)
        pyautogui.typewrite('gostei muito da foto!')
        sleep(2)
        # 13- clicar botao publicar
        pyautogui.click(1213,665, duration=2)
        sleep(5)
        sair()
        sleep(86400)
