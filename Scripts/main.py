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

async def Update(screen):
    # -------------------------------UPDATE LOOP-----------------------------------
    currentFrame = 0
    endFrame = len(CONST.titleScreenImgList)

    while CONST.currentState == CONST.TITLE_SCREEN:
        while currentFrame < endFrame:
            #----------------------------INPUTS-----------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]: # https://www.pygame.org/docs/ref/key.html
                CONST.currentState = CONST.SETTINGS_SCREEN
                await SIM.Start(screen)
                break
            # -----------------------RENDER SPRITES----------------------------------
            titleScreenImg = pygame.image.load(CONST.titleScreenImgList[currentFrame]) # retrieve the image from the animation sheet
            screen.blit(titleScreenImg,(0,0)) # Display it onto the window

            pygame.display.flip()
            pygame.time.wait(50) # Frame delay
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
    CONST.currentState = CONST.TITLE_SCREEN
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