import time
import random
import os
import keyboard
import pygame
from pygame import mixer
from colorama import *
from config import *
mixer.init()
sound = pygame.mixer.Sound("audio_file.mp3")
sound.set_volume(0.2)
sound.play()
os.system("mode con cols=35 lines=10")

def generate_6ape6yx():
    random_num = random.randint(0, 12)
    first_map.remove("#")
    first_map.insert(random_num, "0")

def print_map():
    print("\n" * 70)
    print("",*first_map, "\n", *second_map, "\n", *third_map, "\n", *fifth_map, "\n", *seventh_map, "\n", *eight_map, "\n", *ninth_map, "\n", *war_map)

def player_move1():
    global war_map, x
    war_map.remove(player_ico)
    x += 1
    war_map.insert(x, player_ico)


def player_move2():
    global war_map, x
    war_map.remove(player_ico)
    x -= 1
    war_map.insert(x, player_ico)


def game():
    while True:
        time.sleep(fps)
        if keyboard.is_pressed("d"):
            player_move1()
            print_map()
        elif keyboard.is_pressed("a"):
            player_move2()
            print_map()
        else:
            print_map()


def main_menu():
    print("\n           ", Back.BLACK, Fore.WHITE + "БАРЕБУШКИ")
    time.sleep(1)
    print("   ", "Нажми \"Enter\", что бы гамать")
    while True:
        if keyboard.is_pressed("Enter"):
            game()


if __name__ == "__main__":
    generate_6ape6yx()
    init()
    main_menu()