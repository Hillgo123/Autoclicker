# make an autoclicker
import pyautogui
import keyboard


def clicker():
    while True:
        pyautogui.click()
        if keyboard.is_pressed('esc'):
            print('Stopped clicking')
            break


def main():
    while True:
        if keyboard.is_pressed('ctrl+esc'):
            print('Started clicking')
            clicker()


if __name__ == "__main__":
    main()
