import pyautogui as ag
from time import sleep
import random

# FAILSAFE is a small mechanism used by pyAutoGui as an emergency exit (hover the mouse over the top left of the screen for an emergency exit)
ag.FAILSAFE = True


def press_d():
    sleep(0.2)
    ag.keyDown("d")
    ag.keyUp("d")


def start(positions):
    try:
        while True:
            for i in positions:
                print(f"[+] MOVED TO: {i[0]} / {i[1]}")
                ag.moveTo(i[0], i[1])
                ag.click()
                sleep(.5)
                press_d()
                sleep(7)

    except ag.FailSafeException:
        print("[!] EXITED SUCCESSFULLY")

    except KeyboardInterrupt:
        print("[!] EXITED SUCCESSFULLY")


positions = []

while True:
    choice = input("[+] TYPE 'L' TO LOG / 'S' TO START: ").lower()
    if choice == "l":
        positions.append(ag.position())
    elif choice == "s":
        start(positions=positions)
    else:
        pass
