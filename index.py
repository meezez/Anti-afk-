import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Key, Controller
import threading
import time

intervalle = 1
clavier = Controller()
running = False

def appuyer_sur_wasd():
    global running
    touches = ['w', 'a', 's', 'd']
    while running:
        for touche in touches:
            if not running:
                break
            clavier.press(touche)
            time.sleep(0.8)
            clavier.release(touche)
            time.sleep(intervalle)

def start():
    global running
    if not running:
        running = True
        thread = threading.Thread(target=appuyer_sur_wasd)
        thread.start()

def stop():
    global running
    running = False

def on_closing():
    stop()
    root.destroy()

root = tk.Tk()
root.title("Automatisation des touches WASD")

start_button = tk.Button(root, text="Démarrer", command=start)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Arrêter", command=stop)
stop_button.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()


