import pygame
import asyncio
import random
from pygame.locals import *

# Nigel Garcia
# simulation.py
# simulation window, only runs when the user presses space in the title screen
# This script will feature the visual simulation, as well as settings.

# Other Scripts
import constants as CONST

# Generates a list with custom length and custom max value
async def GenerateList(screen):
    arr = CONST.arr
    for i in range(CONST.length):
        randVal = int(random.random() * CONST.maxVal)
        arr[i] = randVal
    pos = 20
    CONST.arr = arr
    for i in range(len(CONST.arr)):
        pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (pos, 300, 15, CONST.arr[i]))
        pos += 20

# accepts a value and calles a function depending on the value
async def MenuOperations(selOp):
    pass

# Input manager
async def Inputs(screen): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keystate = pygame.key.get_pressed() 

    # Early exit if no keys are down
    if not True in keystate: return 
    
    # Opening/Closing Menu
    if keystate[pygame.K_UP] and not CONST.menuOpen: # https://www.pygame.org/docs/ref/key.html
        CONST.menuOpen = True
    elif keystate[pygame.K_DOWN] and CONST.menuOpen:
        CONST.menuOpen = False
    
    #------------------------------------------------Debugging start----------------------------------------------------------------

    # random button functionality
    if keystate[pygame.K_0] and not CONST.x: 
        await GenerateList(screen)
        CONST.x = True
    
    # start button functionality
    if keystate[pygame.K_9] and CONST.x: 
        arr = await sort(CONST.arr)
        CONST.arr = arr
        CONST.x = False
    
    # Ascending or descending Selection
    if keystate[pygame.K_8]: 
        pass
    
    # Max value selection
    if keystate[pygame.K_7]: 
        pass

    # Element count selection
    if keystate[pygame.K_7]: 
        pass
    #---------------------------------------------------Debugging end---------------------------------------------------------------------
    
    # Menu Navigation
    if CONST.menuOpen: 
        if keystate[pygame.K_RIGHT] and CONST.curBtn < CONST.SELECT_START:
            CONST.curBtn += 1
        elif keystate[pygame.K_LEFT] and CONST.curBtn > CONST.CHANGE_SIZE:
            CONST.curBtn -= 1
        
        # Menu Mode Select
        if keystate[pygame.K_KP_ENTER]: 
            await MenuOperations(CONST.curBtn)
        
# deals with image renders
async def RenderImages(screen, currentFrame, currentAnim): 
    titleScreenImg = pygame.image.load(currentAnim[currentFrame])
    screen.blit(titleScreenImg, (0,0))

    # Render list and display if its generated/sorted
    if CONST.arr != None:
        pos = 20
        for i in range(len(CONST.arr)):
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (pos, 300, 15, CONST.arr[i]))
            pos += 20

# deals with menu rendering (main dropdown, all the buttons)
async def SimulationRender(screen): 
    #Menu dropdown
    curPos = await SimulationInputs()
    screen.blit(CONST.dropDown, (0,curPos))

    # render buttons
    if CONST.menuOpen:
        if CONST.curBtn == 1:
            screen.blit(CONST.sizeSel, (40, 400))
        else:
            screen.blit(CONST.sizeBtn, (40, 400))
        if CONST.curBtn == 2:
            screen.blit(CONST.orderSel, (340, 400))
        else:
            screen.blit(CONST.orderBtn, (340, 400))
        if CONST.curBtn == 3:
            screen.blit(CONST.randSel, (640, 400))
        else:
            screen.blit(CONST.randBtn, (640, 400))
        if CONST.curBtn == 4:
            screen.blit(CONST.startSel, (940, 400))
        else:
            screen.blit(CONST.startBtn, (940, 400))
    
# returns dropdown position y value depending on menu state
async def SimulationInputs(): 
    if not CONST.menuOpen:
        return 700
    else:
        return 300

# Render loop
async def Update(screen):
    currentFrame = 0
    endFrame = len(CONST.settingsImgList)
    while CONST.currentState == CONST.SETTINGS_SCREEN:
        while currentFrame < endFrame:
            await Inputs(screen)
            await RenderImages(screen, currentFrame, CONST.settingsImgList)
            await SimulationRender(screen)
            pygame.display.flip()
            pygame.time.wait(40) # Frame delay
            await asyncio.sleep(0)
            currentFrame += 1
        currentFrame = 0

# Transition loop: runs once and before the update loop
async def Transition(screen, currentFrame, endFrame, curAnim):
    while currentFrame < endFrame:
        await Inputs(screen)
        await RenderImages(screen, currentFrame, curAnim)
        pygame.display.flip()
        pygame.time.wait(30) # Frame delay
        await asyncio.sleep(0)
        currentFrame += 1

# OnStart
async def Start(screen):
    await Transition(screen, 0, len(CONST.transitionImgList1), CONST.transitionImgList1)
    await Transition(screen, 0, len(CONST.transitionImgList2), CONST.transitionImgList2)
    await Update(screen)

# Merge sort
async def merge(left, right):
    finalList = []
    i, j, = 0, 0
    while i < len(left) and j < len(right):
        print(left, right)
        if left[i] <= right[j]:
            finalList.append(left[i])
            i += 1
        else:
            finalList.append(right[j])
            j += 1
    while i < len(left):
        print(finalList)
        finalList.append(left[i])
        i += 1
    while j < len(right):
        print(finalList)
        finalList.append(right[j])
        j += 1
    return finalList
async def sort(list):
    length = len(list)
    if length < 2:
        return(list)
    else:
        left = list[:length//2]
        right = list[length//2:]
    return await merge(await sort(left), await sort(right))
    