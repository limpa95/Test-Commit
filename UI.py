# Name: Patrick Lim
# OSU Email: limpa@oregonstate.edu
# Course: CS361 - Microservices Warm-up
# Assignment: 1
# Due Date: 1/16/24
# Description: This program acts as a UI. It calls the prng service, the image service, and displays an image


import time
from PIL import Image

while True:
    prompt = input("Find out what your signature card is for Yu-Gi-Oh! To display the card, please press Enter:")

    prng_txt = open('prng-service.txt', 'r+', encoding="utf-8")
    prng_txt.seek(0)
    prng_txt.truncate()
    prng_txt.write("run")
    prng_txt.close()

    time.sleep(5)
    prng_num_txt = open('prng-service.txt', 'r+', encoding="utf-8")
    num = prng_num_txt.read()
    prng_num_txt.close()

    write_img_text = open('image-service.txt', 'w', encoding="utf-8")
    write_img_text.write(num)
    write_img_text.close()

    time.sleep(12)
    img_path = open('image-service.txt', 'r', encoding="utf-8")
    image = Image.open(img_path.read())
    image.show()
    img_path.close()
