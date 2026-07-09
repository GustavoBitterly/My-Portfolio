from pynput.keyboard import Controller
import random
import string
import time

keyboard = Controller()

def presionar_teclas(teclas_por_segundo, minutos):
    teclas = list(string.ascii_lowercase + string.digits)

    tiempo_fin = time.time() + minutos * 60
    intervalo = 1 / teclas_por_segundo

    print("Comenzando en 3 segundos...")
    time.sleep(3)

    while time.time() < tiempo_fin:
        keyboard.press(random.choice(teclas))
        keyboard.release(random.choice(teclas))
        time.sleep(intervalo)

    print("Finalizado.")

tps = float(input("Teclas por segundo: "))
mins = float(input("Minutos: "))

presionar_teclas(tps, mins)