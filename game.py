import pyautogui 
from PIL import Image, ImageGrab
import time 

def hit(key):
    pyautogui.keyDown(key)
    return 

def isCollide(data):

    #birds
    """for i in range(477, 498):
        for j in range(120, 227):
            if data[i,j] > 100:
                hit('down')
                return """
    """           
    #cactus
    for i in range(481, 530):
        for j in range(226, 260):
            if data[i,j] > 100:
                hit('up')
                return 
                """
    for i in range(345, 437):
        for j in range(365, 408):
            if data[i,j] < 100:
                hit('up')
                return 
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    hit('up') 
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        """
        #Draw the rectangle for cactus 
        for i in range(345, 437):
            for j in range(365, 408):
                data[i, j] = 0

        #Draw the rectangle for birds
        for i in range(334, 357):
            for j in range(280, 365):
                data[i, j] = 171

        image.show()
        break
    """
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        

