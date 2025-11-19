import pygame
import asyncio
from pygame.locals import *

# Other Scripts
import settings as SETTINGS
import constants as CONSTANTS

# Window States
currentState = 0
screen = None

async def main():
    # -----------------------START----------------------------------
    currentState = 0
    currentFrame = 0
    endFrame = len(CONSTANTS.titleScreenImgList)

    pygame.init()
    pygame.display.set_caption('Merge Sort Simulation')
    display = (1200, 800)
    screen = pygame.display.set_mode(display)

    while currentState == CONSTANTS.TITLE_SCREEN:
        # --------------------------------Title screen keyframes here----------------------------------------------------------
        while currentFrame < endFrame:
            # -------------------------------UPDATE LOOP-----------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #----------------------------INPUTS-----------------------------------------
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]: # https://www.pygame.org/docs/ref/key.html
                currentState = CONSTANTS.SETTINGS_SCREEN
                await SETTINGS.Start(screen, display)
                break
            
            # -----------------------RENDER SPRITES----------------------------------
            titleScreenImg = pygame.image.load(CONSTANTS.titleScreenImgList[currentFrame]) # retrieve the image from the animation sheet
            screen.blit(titleScreenImg,(0,0)) # Display it onto the window

            pygame.display.flip()
            pygame.time.wait(50) # Frame delay
            await asyncio.sleep(0)
            currentFrame += 1
        currentFrame = 0
        
if __name__ == "__main__":
    currentState = CONSTANTS.TITLE_SCREEN
    asyncio.run(main())



# quick comment: ctrl k, ctrl c
# import bpy
# obdata = bpy.context.object.data
# print("Vertices")
# for v in obdata.vertices:
#     print(" ({}, {}, {})".format(v.co.x, v.co.y, v.co.z))

# print("edges")
# for e in obdata.edges:
#     print("({}, {})".format(e.vertices[0], e.vertices)[1])

# print("faces")
# for f in obdata.polygons:
#     for v in f.vertices:
#         print("{}, ".format(v), end='')
#     print()