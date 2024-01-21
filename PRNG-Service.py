# Name: Patrick Lim
# OSU Email: limpa@oregonstate.edu
# Course: CS361 - Microservices Warm-up
# Assignment: 1
# Due Date: 1/16/24
# Description: This program acts as a image service by using a pseudo-random number from the PRNG service.

import random
import time

while True:
    num = random.randrange(1, 1000)

    read_txt = open('prng-service.txt', 'r+', encoding="utf-8")
    if read_txt.read() == "run":
        time.sleep(3)
        read_txt.seek(0)
        read_txt.truncate()
        read_txt.write(str(num))
    read_txt.close()
