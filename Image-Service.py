# Name: Patrick Lim
# OSU Email: limpa@oregonstate.edu
# Course: CS361 - Microservices Warm-up
# Assignment: 1
# Due Date: 1/16/24
# Description: This program acts as a PRNG service by generating a pseudo-random number. It then reads prng-service.txt,
# erases it, and writes a pseudo-random number to it.

import time
from os import listdir

while True:

    read_txt = open('image-service.txt', 'r+', encoding="utf-8")
    time.sleep(11)

    path = 'C:/Users/blaze/PycharmProjects361/images'
    images = listdir(path)

    number = read_txt.read()
    if '.jpg' not in number and number != '':
        num = int(number)
        if num >= 6:
            num = num % 6

        image_name = images[num]
        read_txt.seek(0)
        read_txt.truncate()
        read_txt.write('C:/Users/blaze/PycharmProjects361/images/' + str(image_name))
    read_txt.close()