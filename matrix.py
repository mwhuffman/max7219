###########################################################################
#
#
#
###########################################################################

import math
from time import sleep

NUM_OF_MATRIX = 4

RIGHT = 1
LEFT  = -1
UP    = 1
DOWN  = -1
 
class matrix:
 
    def __init__(self, display):
        
        self.display = display
        
    def _dec2bin(self, value):
        
        return f'{value:0{8}b}'
            
    def render_kana(self, kana):
        
        for rows in range(0, 8, 1):
            for row in range (0, 8, 1):
                for col in range ( 7, -1, -1):
                    # print(f"row: {row} col: {col} v: {int(pacman_sp[0][row])}")
                    bin_str = self._dec2bin(kana[row])
                    self.display.pixel(rows - row, 7 - col, int(bin_str[col]))
                    # remove the light trail behind it
                    self.display.vline(rows - 9, 0, 8, 0)
                    self.display.show()
 
    # https://github.com/mcauser/micropython-pcd8544/blob/master/examples/sine_wave.py
    def draw_sin(self, display, amplitude, freq, phase, yoffset=24):
        for i in range(freq):
            y = int((math.sin((i + phase) * 0.017453) * amplitude) + yoffset)
            x = int((84 / freq) * i)
            self.display.pixel(x, y, 1)
            if (x > 32):
                break
            # print(f"x: {x} y: {y}")
    
    def draw_cos(display, amplitude, freq, phase, yoffset=24):
        for i in range(freq):
            y = int((math.cos((i + phase) * 0.017453) * amplitude) + yoffset)
            x = int((84 / freq) * i)
            self.display.pixel(x, y, 1)
            if ( x > 32):
                    break;
            # print(f"x: {x} y: {y}")
    
    def pacman(self, pacman_sp):
        
        self.clear()
        self.display.rect(3,3,2,2,1)
        self.display.rect(8+3,3,2,2,1)
        self.display.rect(16+3,3,2,2,1)
        self.display.rect(24+3,3,2,2,1)
        self.display.show()
        
        for rows in range(0, 42, 1):
            for row in range (0, 8, 1):
                for col in range ( 7, -1, -1):
                    # print(f"row: {row} col: {col} v: {int(pacman_sp[0][row])}")
                    bin_str = self._dec2bin(pacman_sp[rows % 8][row])
                    self.display.pixel(rows - row, col, int(bin_str[col]))
                    # remove the light trail behind it
                    self.display.vline(rows - 9, 0, 8, 0)
                    self.display.show()
        
    def clear(self):
 
        self.display.fill(0)
        self.display.show()
        sleep(0.5)
 
    def text(self, my_str):
 
        self.display.fill(0)
        self.display.text(my_str,0,0,1)
        self.display.show()
        sleep(1)
 
    def text_blink(self, my_str, times):
 
        for x in range(times):
                       
            self.display.text(my_str,0,0,1)
            self.display.show()
            sleep(0.3)
 
            self.clear()
            sleep(0.1)
 
    def text_scroll(self, my_str):
 
        self.length = len(my_str)
        self.column = (self.length * 8)
 
        self.clear()
 
        for x in range(8 * NUM_OF_MATRIX, -self.column, -1):
                       
            self.display.fill(0)
            self.display.text(my_str,x,0,1)
            self.display.show()
            sleep(0.1)
            
    def matrix_scroll(self, direction, count = 1):
        
        for x in range(count):
            for i in range(8):
                self.display.scroll(direction,0)
            
                # clean up light trail
                if (direction == LEFT):
                    self.display.vline(31 - i, 0, 8, 0)
                if ( direction == RIGHT):
                    self.display.vline(i, 0, 8, 0)
                
                self.display.show()
                sleep(0.1)