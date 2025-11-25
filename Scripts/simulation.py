import pygame
import asyncio
from pygame.locals import *

# Nigel Garcia
# simulation.py
# simulation window, only runs when the user presses space in the title screen
# This script will feature the visual simulation, as well as settings.

# Other Scripts
import constants as CONST

async def Inputs(): # General inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP] and not CONST.menuOpen: # https://www.pygame.org/docs/ref/key.html
            CONST.menuOpen = True
        elif keystate[pygame.K_DOWN] and CONST.menuOpen:
            CONST.menuOpen = False
        
async def RenderImages(screen, currentFrame, currentAnim): #deals with image renders
    titleScreenImg = pygame.image.load(currentAnim[currentFrame]) # retrieve the image from the animation sheet
    screen.blit(titleScreenImg, (0,0))

async def SimulationRender(screen): # deals with dropdown position 
    curPos = await SimulationInputs()
    screen.blit(CONST.dropDown, (0,curPos))

async def SimulationInputs(): #returns dropdown position y val depending on menu Open state
    if not CONST.menuOpen:
        return 700
    else:
        return 300

async def Update(screen):
    currentFrame = 0
    endFrame = len(CONST.settingsImgList)
    while CONST.currentState == CONST.SETTINGS_SCREEN:
        while currentFrame < endFrame:
            await Inputs()
            await RenderImages(screen, currentFrame, CONST.settingsImgList)
            await SimulationRender(screen)
            

            pygame.display.flip()
            pygame.time.wait(40) # Frame delay
            await asyncio.sleep(0)

            currentFrame += 1
        currentFrame = 0

async def Transition(screen, currentFrame, endFrame, curAnim):
    while currentFrame < endFrame:
        await Inputs()
        await RenderImages(screen, currentFrame, curAnim)

        pygame.display.flip()
        pygame.time.wait(30) # Frame delay
        await asyncio.sleep(0)

        currentFrame += 1
async def Start(screen):
    await Transition(screen, 0, len(CONST.transitionImgList1), CONST.transitionImgList1)
    await Transition(screen, 0, len(CONST.transitionImgList2), CONST.transitionImgList2)
    await Update(screen)

#----------------------Merge sort function here-----------------------------------------------
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
    