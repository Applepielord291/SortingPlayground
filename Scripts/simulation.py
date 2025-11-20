import pygame
import asyncio
from pygame.locals import *

# Nigel Garcia
# simulation.py
# simulation window, only runs when the user presses space in the title screen
# This script will feature the visual simulation, as well as settings.

# Other Scripts
import constants as CONST

async def Update(screen):
    currentFrame = 0
    endFrame = len(CONST.settingsImgList)

    # -------------------------------UPDATE LOOP-----------------------------------
    while CONST.currentState == CONST.SETTINGS_SCREEN:
        while currentFrame < endFrame:
            #----------------------------INPUTS-----------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            keystate = pygame.key.get_pressed()
            # if keystate[pygame.K_SPACE]: # https://www.pygame.org/docs/ref/key.html
            #     currentState = CONST.SETTINGS_SCREEN
            #     print(currentState)
            #     break

            # -----------------------RENDER SPRITES----------------------------------
            titleScreenImg = pygame.image.load(CONST.settingsImgList[currentFrame]) # retrieve the image from the animation sheet
            screen.blit(titleScreenImg, (0,0))

            pygame.display.flip()
            pygame.time.wait(50) # Frame delay
            await asyncio.sleep(0)
            currentFrame += 1
        currentFrame = 0

async def Start(screen):
    currentFrame = 0
    endFrame = len(CONST.transitionImgList1)

    # -------------------------------UPDATE LOOP-----------------------------------
    while currentFrame < endFrame:
            #----------------------------INPUTS-----------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            # -----------------------RENDER SPRITES----------------------------------
            titleScreenImg = pygame.image.load(CONST.transitionImgList1[currentFrame]) # retrieve the image from the animation sheet
            screen.blit(titleScreenImg, (0,0))

            pygame.display.flip()
            pygame.time.wait(50) # Frame delay
            await asyncio.sleep(0)
            currentFrame += 1
    await Update(screen)
    