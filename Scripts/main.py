import pygame
import asyncio
from pygame.locals import *

# Nigel Garcia
# main.py
# Main script, run this to run the program.
# This is the title screen, which can transition into the Simulation screen. 

# Other Scripts
import simulation as SIM
import constants as CONST

# deals with user inputs, called in the update loop
async def Inputs(screen): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            quit()
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_SPACE]: # https://www.pygame.org/docs/ref/key.html
        await SIM.Start(screen)

# deals with the visuals on screen, called in the update loop
async def RenderImages(screen, currentFrame): 
    titleScreenImg = pygame.image.load(CONST.titleScreenImgList[currentFrame]) # retrieve the image from the animation sheet
    screen.blit(titleScreenImg,(0,0)) # Display it onto the window

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

async def main():
    # -----------------------START----------------------------------
    pygame.init()
    pygame.display.set_caption('Merge Sort Simulation')
    display = (1200, 800)
    screen = pygame.display.set_mode(display)
    await Update(screen)

if __name__ == "__main__":
    asyncio.run(main())