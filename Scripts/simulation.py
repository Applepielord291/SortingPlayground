import pygame
import asyncio
from pygame.locals import *

# Nigel Garcia
# simulation.py
# simulation window, only runs when the user presses space in the title screen
# This script will feature the visual simulation, as well as settings.

# Other Scripts
import constants as CONST

async def Inputs():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        keystate = pygame.key.get_pressed()
        # if keystate[pygame.K_SPACE]: # https://www.pygame.org/docs/ref/key.html
        #     currentState = CONST.SETTINGS_SCREEN
        #     print(currentState)
        #     break
async def RenderImages(screen, currentFrame, currentAnim):
    titleScreenImg = pygame.image.load(currentAnim[currentFrame]) # retrieve the image from the animation sheet
    screen.blit(titleScreenImg, (0,0))
    screen.blit(CONST.dropDown, (0,700))

async def Update(screen):
    currentFrame = 0
    endFrame = len(CONST.settingsImgList)
    # -------------------------------UPDATE LOOP-----------------------------------
    while CONST.currentState == CONST.SETTINGS_SCREEN:
        while currentFrame < endFrame:
            await Inputs()
            await RenderImages(screen, currentFrame, CONST.settingsImgList)

            pygame.display.flip()
            pygame.time.wait(50) # Frame delay
            await asyncio.sleep(0)

            currentFrame += 1
        currentFrame = 0
async def Transition(screen, currentFrame, endFrame, curAnim):
    # -------------------------------UPDATE LOOP-----------------------------------
    while currentFrame < endFrame:
        #----------------------------INPUTS-----------------------------------------
        await Inputs()
        # -----------------------RENDER SPRITES----------------------------------
        await RenderImages(screen, currentFrame, curAnim)

        pygame.display.flip()
        pygame.time.wait(40) # Frame delay
        await asyncio.sleep(0)

        currentFrame += 1
async def Start(screen):
    await Transition(screen, 0, len(CONST.transitionImgList1), CONST.transitionImgList1)

    await Transition(screen, 0, len(CONST.transitionImgList2), CONST.transitionImgList2)

    await Update(screen)

async def merge(left, right):
    finalList = []
    i, j, = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            finalList.append(left[i])
            i += 1
        else:
            finalList.append(right[j])
            j += 1
    while i < len(left):
        finalList.append(left[i])
        i += 1
    while j < len(right):
        finalList.append(right[j])
        j += 1
    return finalList
async def sort(list):
    length = len(list)
    if length < 2:
        return len(list)
    else:
        left = list[:length//2]
        right = list[length//2:]
    return merge(sort(left), sort(right))
    