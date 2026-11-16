import serial
import subprocess
import time

# Замени COM3 на порт своей Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)

# Открытие Serial-порта может перезапустить Arduino Nano.
time.sleep(2)

print("Stream Deck запущен!")

while True:
    command = arduino.readline().decode(errors="ignore").strip()

    if command == "OPEN_NOTEPAD":
        print("Открываю Блокнот!")
        subprocess.Popen("notepad.exe")