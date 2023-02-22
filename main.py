import time
import random
import os
import keyboard
import pygame
import getpass
from pygame import mixer
from colorama import *
from config import *
print("\n\n\n        Загрузка")
mixer.init()
user_name = getpass.getuser()
volume = 0.2
sound = pygame.mixer.Sound("audio_file.mp3")
sound.set_volume(volume)
menu_sound = pygame.mixer.Sound("main_menu.mp3")
menu_sound.set_volume(volume)
os.system("mode con cols=35 lines=20")

globaltime = int()
barebuhpos = 0
run = True
score = 0
health = 3
difficulty = 0


def clear():
    global globaltime, barebuhpos, run, score, health, difficulty, first_map, second_map, third_map, fourth_map, fifth_map, sixth_map, seventh_map, eight_map, ninth_map, war_map
    globaltime = int()
    run = True
    score = 0
    health = 3
    difficulty = 0

def move_barebuh():
    global score, difficulty, first_map, second_map, third_map, fourth_map, fifth_map, sixth_map, seventh_map, eight_map, ninth_map, war_map, barebuhpos, health, globaltime
    globaltime = time.time()
    a1 = str(first_map).find(barebuh)
    a2 = str(second_map).find(barebuh)
    a3 = str(third_map).find(barebuh)
    a4 = str(fourth_map).find(barebuh)
    a5 = str(fifth_map).find(barebuh)
    a6 = str(sixth_map).find(barebuh)
    a7 = str(seventh_map).find(barebuh)
    a8 = str(eight_map).find(barebuh)
    a9 = str(ninth_map).find(barebuh)

    if a9 >= 0:
        if barebuhpos == x+1:
            ninth_map.remove(barebuh)
            ninth_map.insert(barebuhpos, back_ground)
            score += 1
            generate_barebuh()
            difficulty += 0.05

        else:
            ninth_map.remove(barebuh)
            ninth_map.insert(barebuhpos, back_ground)
            health -= 1
            generate_barebuh()
            difficulty -= 0.2

    if a1 >= 0:
        first_map.remove(barebuh)
        first_map.insert(barebuhpos, back_ground)
        second_map.remove(back_ground)
        second_map.insert(barebuhpos, barebuh)
        return

    if a2 >= 0:
        second_map.remove(barebuh)
        second_map.insert(barebuhpos, back_ground)
        third_map.remove(back_ground)
        third_map.insert(barebuhpos, barebuh)
        return

    if a3 >= 0:
        third_map.remove(barebuh)
        third_map.insert(barebuhpos, back_ground)
        fourth_map.remove(back_ground)
        fourth_map.insert(barebuhpos, barebuh)
        return

    if a4 >= 0:
        fourth_map.remove(barebuh)
        fourth_map.insert(barebuhpos, back_ground)
        fifth_map.remove(back_ground)
        fifth_map.insert(barebuhpos, barebuh)
        return

    if a5 >= 0:
        fifth_map.remove(barebuh)
        fifth_map.insert(barebuhpos, back_ground)
        sixth_map.remove(back_ground)
        sixth_map.insert(barebuhpos, barebuh)
        return

    if a6 >= 0:
        sixth_map.remove(barebuh)
        sixth_map.insert(barebuhpos, back_ground)
        seventh_map.remove(back_ground)
        seventh_map.insert(barebuhpos, barebuh)
        return

    if a7 >= 0:
        seventh_map.remove(barebuh)
        seventh_map.insert(barebuhpos, back_ground)
        eight_map.remove(back_ground)
        eight_map.insert(barebuhpos, barebuh)
        return

    if a8 >= 0:
        eight_map.remove(barebuh)
        eight_map.insert(barebuhpos, back_ground)
        ninth_map.remove(back_ground)
        ninth_map.insert(barebuhpos, barebuh)
        return

    if health == 0:
        print("        ТЫ ПРОЕБАЛ")
        time.sleep(1)
        print("\n" * 100)
        main_menu()

def generate_barebuh():
    global barebuhpos
    random_num = random.randint(1, 16)
    first_map.remove(back_ground)
    first_map.insert(random_num, barebuh)
    barebuhpos = random_num


def print_map():
    print("\n" * 70)
    print(f"      Score:{score}")
    print(f"      Health:{health}", "\n" * 2)
    print("", *first_map, "\n", *second_map, "\n", *third_map, "\n", *fourth_map, "\n", *fifth_map, "\n", *sixth_map, "\n", *seventh_map, "\n", *eight_map, "\n", *ninth_map, "\n", *war_map)


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
    sound.play()
    while run:
        time.sleep(fps)
        newtime = time.time()
        if newtime - globaltime > 1 - difficulty:
            move_barebuh()
        if keyboard.is_pressed("d"):
            if x <= 14:
                player_move1()
                print_map()
        elif keyboard.is_pressed("a"):
            if x >= 1:
                player_move2()
                print_map()
        else:
            print_map()


def main_menu():
    try:
        sound.stop()
    except:
        pass
    menu_sound.play()
    print("\n           ", Back.BLACK, Fore.WHITE + "БАРЕБУШКИ")
    time.sleep(1)
    print("   ", "Нажми \"Enter\", что бы гамать")
    clear()
    while True:
        if keyboard.is_pressed("Enter"):
            menu_sound.stop()
            game()


if __name__ == "__main__":
    generate_barebuh()
    init()
    main_menu()