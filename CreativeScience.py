###########################################################################
#
# https://www.creative-science.org.uk/max7219.html
#
###########################################################################

import urandom
from time import sleep

WAVES    = [3,3,2,1,2,3,4,5,6,6,5,4,3,2,1,2,3,3,4,5,6,6,5,4]
FLAME    = [1,1,2,4,4,4,2,2,1]
SINE     = [0,4,6,6,5,3,2,2,4]
SQUARE   = [0,6,6,2,2,6,6,2,2]
TRIANGLE = [0,4,5,6,5,4,3,2,4]
PULSE    = [0,1,1,2,4,7,4,2,1]


class CreativeScience:
 
    def __init__(self, spi, cs):
        
        self.spi = spi
        self.cs = cs
        
    # chip select 'ping'
    def _set(self):
        
        self.cs.value(1)
        sleep(.001)        
        self.cs.value(0)
        
    # dot gen
    def dot(self, a, b):     # a=reg b=value

        buff = [0,0]
        buff[0] = 9-a      # reg invert
        buff[1] = (2**(b-1))  # converts binary to dot
        if b == 0:
            buff[1] = (0)    
        self.spi.write(bytearray(buff))   
        self._set()
    
    # bar gen
    def bar(self, a, b):      # a=reg b=value
        
        buff = [0,0]
        buff[0] = 9-a      # reg invert
        buff[1] = ((2**(b)-1))  # converts binary to bar
        self.spi.write(bytearray(buff))   
        # self._set()

    # adjust brightness
    def bright(self, a):
        
        buff = [0,0]
        buff[0] = 0b00001010
        buff[1] = a
        self.spi.write(bytearray(buff))
        self._set()
        
    def flame(self, buff):
        
        k = int (urandom.uniform (1, 9)) # register
        j = int (urandom.uniform (2, 7)) # bar value
        l = int (urandom.uniform (0, 255)) # brightness
        
        m = int ((j * buff[k] )/ 4) # adjust bar value for flame shape
        if m < 1:
            m = 1
        
        self.bar(k,m) # send bar value
        self.bright(l) # send brightness
        sleep(.07)
        
    def wave_simple(self, buff):
        
        for k in range (1,9): 
            m = int (buff[k]) # call up parts
        
            self.dot(k,m) # send bar value
            sleep(.07)
        
        val = buff.pop(0)
        buff.append(val)

    def walk(self, b):
        
        for k in range (1,9): 
            a = int (urandom.uniform (0, 3)) # random: 1, 2 or 3
            b = b + (a-1)  # make -1, 0 or +1
            if b == 0:  # dont go below screen
                b = 1
            if b == 9: # dont go above screen
                b = 8
            self.dot(k,b) # send dot value
            sleep(.1)