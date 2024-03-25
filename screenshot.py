import time
import pyautogui
import tkinter as tk 


def screenshot():
    name = int(round(time.time() * 1000))
    name = f"C:\\Users\\joaov\\OneDrive\\Área de Trabalho\\Desenvolvimento\\ScreenShot App\\screenshots data\\{name}.png" # Atualizando o name para o nome de um arquivo png
    time.sleep(5) # Faz o programa esperar 5 segundos para a execução
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# Cria um botão interativo para tirar print
button = tk.Button(
    frame, 
    text = "Take ScreenShot",
    command = screenshot()
)

button.pack(side = tk.LEFT)

# Cria um botão interativo para sair do programa
close = tk.Button(
    frame,
    text = "Quit",
    command = quit
)

close.pack(side = tk.LEFT)

root.mainloop()