###########################################################################
#
#
#
###########################################################################

import sys
from machine import Pin, SPI
import max7219
import random
import hiragana
import math
from matrix import matrix, NUM_OF_MATRIX, UP, DOWN
from CreativeScience import CreativeScience, WAVES

from time import sleep

def main():
 
    spi = SPI(0,sck=Pin(2),mosi=Pin(3))
    cs = Pin(5, Pin.OUT)
    display = max7219.Matrix8x8(spi, cs, NUM_OF_MATRIX)
    display.brightness(1)

    my_matrix = matrix(display)
    
    while(1):
        
        display.fill(0)
        display.show()
        sleep(0.5)
    
        # display welcome to JBF in Japanese
        for kana in hiragana.WELCOME:
            my_matrix.render_kana(kana)
            my_matrix.matrix_scroll(UP)
        
        my_matrix.matrix_scroll(UP, 3)
        sleep(0.3)
        
        # display pac-man
        my_matrix.clear()
        my_matrix.pacman(hiragana.PACMAN)
        sleep(0.3)

        # display welcome to JBF in English
        my_matrix.text_scroll("Welcome to...")
        sleep(0.3)

        my_matrix.clear()
        my_matrix.text_blink("JBF!", 5)
        sleep(0.3)
        
        # display moving sin wave
        for i in range(180):
            display.fill(0)
            my_matrix.draw_sin(display, 4, 9*360, i, 4)
            display.show()
            
        my_matrix.matrix_scroll(DOWN, 4)
        sleep(0.3)
        
        # display space invader
        for kana in hiragana.INVADERS:
            my_matrix.render_kana(kana)
            my_matrix.matrix_scroll(UP)
            
        my_matrix.matrix_scroll(UP, 3)
        sleep(0.3)
        
        # display "Obey Bricky!" in English
        my_matrix.text_scroll("Obey Bricky!")
        sleep(0.3)

        my_matrix.clear()
        my_matrix.text_blink("obey", 3)
        sleep(0.3)
        
        # display obey in English
        for kana in hiragana.OBEY_2:
            my_matrix.render_kana(kana)
            sleep(0.3)
            my_matrix.matrix_scroll(DOWN)
        
        sleep(0.3)
        
        # display obey in Japanese
        for kana in hiragana.OBEY:
            my_matrix.render_kana(kana)
            my_matrix.matrix_scroll(UP)
        
        my_matrix.matrix_scroll(UP, 3)
        sleep(0.3)
    
    #display.fill(0)
    #display.show()
    #sleep(3)

    # display.pixel(0,0,1)
    #display.pixel(1,1,1)
    #display.hline(0,4,8,1)
    #display.vline(4,0,8,1)
    #display.line(8, 0, 16, 8, 1)
    #display.rect(17,1,6,6,1)
    #display.fill_rect(25,1,6,6,1)
    # display.show()
    # sleep(3)

    #display.fill(0)
    #display.text('dead',0,0,1)
    #display.text('beef',32,0,1)
    #display.show()
    #sleep(3)

    #display.fill(0)
    #display.text('12345678',0,0,1)
    #display.show()
    #display.scroll(-8,0) # 23456788
    #display.scroll(-8,0) # 34567888
    #display.show()
    #sleep(3)

if __name__ == "__main__":
 
    try:
        main()
 
    except KeyboardInterrupt:
        pass