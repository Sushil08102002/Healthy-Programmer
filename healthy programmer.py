
#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer         #to deal with .mp3 files
from datetime import datetime    #to deal with present date and time
from time import time            #to deal with secs time

def musiconloop(file, stopper):    #function to stop or play the music
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):               #function used to put your data in file
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyessecs = 15

    while True:
        if time() - init_water > watersecs:            #run at every 5 seconds
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:               #run at every 10 seconds
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:            #run at every 15 seconds
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")


