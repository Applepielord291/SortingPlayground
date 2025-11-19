#from OpenGL.GL import *
#from OpenGL.GLU import *
import pygame
import asyncio
import glob
from pygame.locals import *

#import SettingsWindow as sw
#import ShapePoints as sp

# Window States
currentState = 0

# Constant States
TITLE_SCREEN = 0
SETTINGS_SCREEN = 1
SIMULATION_SCREEN = 2
INFO_SCREEN = 3

# Paths
debugTitle = 'Scripts/TitleScreen/*.bmp'
buildTitle = 'TitleScreen/*.bmp'

# Images
titleScreenImgList = []
for image in glob.glob(debugTitle):
    titleScreenImgList.append(image)
titleScreenImgList.sort()


async def main():
    # -----------------------START----------------------------------
    i = 0
    n = len(titleScreenImgList)
    pygame.init()
    pygame.display.set_caption('Merge Sort Simulation')
    display = (1200, 800)
    screen = pygame.display.set_mode(display)
    white = (255, 64, 64)
    while True:
        # --------------------------------Title screen keyframes here----------------------------------------------------------
        while i < n:
            # -------------------------------UPDATE LOOP-----------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #----------------------------INPUTS-----------------------------------------
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_SPACE]: # https://www.pygame.org/docs/ref/key.html
                print(i)
            
            # -----------------------RENDER SPRITES----------------------------------
            titleScreenImg = titleScreenImg = pygame.image.load(titleScreenImgList[i]) # retrieve the image from the animation sheet
            screen.blit(titleScreenImg,(0,0)) # Display it onto the window

            pygame.display.flip()
            pygame.time.wait(50) # Frame delay
            await asyncio.sleep(0)
            i += 1
        i = 0
        
if __name__ == "__main__":
    currentState = TITLE_SCREEN
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