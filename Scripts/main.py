import pygame
import asyncio
from pygame.locals import *

# Nigel Garcia
# main.py
# Main script, run this to run the program.
# This is the title screen, which can transition into the Simulation screen. 

# Throughout all these scripts, you're gonna see functions defined with "async def" and functions called with "await function()"
# A library im using (pygbag), allows web builds of pygame applications, which is what im using
# however, 

# Other Scripts
import simulation as SIM
import constants as CONST
import tutorial as TRANSITION

# deals with user inputs, called in the update loop
async def Inputs(screen): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            quit()
    # All keyboard inputs are stored in a massive array as a bool value (false by default, true when pressed)
    # To check if a certain key is pressed, we can check if its true in the keystate array
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]:
        await TRANSITION.Start(screen)

# deals with the visuals on screen, called in the update loop
async def RenderImages(screen, currentFrame): 
    titleScreenImg = pygame.image.load(CONST.titleScreenImgList[currentFrame]) # retrieve the image from the animation sheet
    screen.blit(titleScreenImg,(0,0)) # blit just means to render the current image at position x (in this case, its (0, 0))

async def Update(screen):
    currentFrame = 0
    endFrame = len(CONST.titleScreenImgList)   

    while True:
        while currentFrame < endFrame: 
            await Inputs(screen) 
            await RenderImages(screen, currentFrame)
            pygame.display.flip()
            pygame.time.wait(30) # Frame delay
            await asyncio.sleep(0)
            currentFrame += 1
        currentFrame = 0 # Reset current frame to loop animation

# -----------------------START----------------------------------
async def main():
    pygame.init()
    pygame.display.set_caption('Merge Sort Simulation') # Window title
    display = (1200, 800)
    screen = pygame.display.set_mode(display)
    await Update(screen)

if __name__ == "__main__":
    asyncio.run(main())