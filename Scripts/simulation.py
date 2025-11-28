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
async def GenerateList():
    arr = [0] * CONST.length
    for i in range(CONST.length):
        randVal = int(random.random() * CONST.maxVal)
        arr[i] = randVal
    CONST.arr = arr

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
        await GenerateList()
        CONST.x = True
    
    # start button functionality
    if keystate[pygame.K_9] and CONST.x: 
        arr = await sort(CONST.arr, screen)
        CONST.arr = arr
        CONST.x = False
    
    # Ascending or descending Selection
    if keystate[pygame.K_8]: 
        if CONST.AscOrDesc:
            CONST.AscOrDesc = False
        else:
            CONST.AscOrDesc = True
    
    # Max value selection
    if keystate[pygame.K_7]: 
        if not CONST.pickMaxVal and not CONST.pickMaxElem:
            CONST.pickMaxVal = True
        elif CONST.pickMaxVal and not CONST.pickMaxElem:
            CONST.pickMaxVal = False
    if keystate[pygame.K_d] and CONST.pickMaxVal:
        CONST.maxVal += 1
    elif keystate[pygame.K_a] and CONST.pickMaxVal:
        CONST.maxVal -= 1

    # Element count selection
    if keystate[pygame.K_6]: 
        if not CONST.pickMaxElem and not CONST.pickMaxVal:
            CONST.pickMaxElem = True
        elif CONST.pickMaxElem and not CONST.pickMaxVal:
            CONST.pickMaxElem = False
    if keystate[pygame.K_d] and CONST.pickMaxElem:
        CONST.length += 1
    elif keystate[pygame.K_a] and CONST.pickMaxElem:
        CONST.length -= 1
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

# Render Sort algorithm
async def RenderBars(screen):
    if CONST.arr != None:
        pos = 20
        for i in range(len(CONST.arr)):
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (pos, 25, 15, CONST.arr[i]))
            pos += 20
        
# deals with image renders
async def RenderImages(screen, currentFrame, currentAnim): 
    titleScreenImg = pygame.image.load(currentAnim[currentFrame])
    screen.blit(titleScreenImg, (0,0))

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
    
async def SettingsRender(screen):
    if not CONST.pickMaxVal and not CONST.pickMaxElem: return

    if CONST.pickMaxElem and not CONST.pickMaxVal:
        displayTxt = "Max Elements: {0}".format(CONST.length)
        text = CONST.font.render(displayTxt, True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (1200 // 2, 400 // 2)
        screen.blit(text, textRect)
    
    if CONST.pickMaxVal and not CONST.pickMaxElem:
        displayTxt = "Max Value: {0}".format(CONST.maxVal)
        text = CONST.font.render(displayTxt, True, (0, 255, 0), (0, 0, 128))
        textRect = text.get_rect()
        textRect.center = (1200 // 2, 400 // 2)
        screen.blit(text, textRect)

# Render loop
async def Update(screen):
    currentFrame = 0
    endFrame = len(CONST.settingsImgList)
    while CONST.currentState == CONST.SETTINGS_SCREEN:
        while currentFrame < endFrame:
            await Inputs(screen)
            await RenderImages(screen, currentFrame, CONST.settingsImgList)
            await RenderBars(screen)
            await SimulationRender(screen)
            await SettingsRender(screen)
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
async def merge(left, right, screen):
    finalList = []
    i, j, = 0, 0
    while i < len(left) and j < len(right):
        if CONST.AscOrDesc:
            if left[i] <= right[j]:
                finalList.append(left[i])
                i += 1
            else:
                finalList.append(right[j])
                j += 1
        else:
            if left[i] >= right[j]:
                finalList.append(left[i])
                i += 1
            else:
                finalList.append(right[j])
                j += 1
        await RenderBars(screen)
    while i < len(left):
        finalList.append(left[i])
        i += 1
    while j < len(right):
        finalList.append(right[j])
        j += 1
    return finalList
async def sort(list, screen):
    length = len(list)
    if length < 2:
        return(list)
    else:
        left = list[:length//2]
        right = list[length//2:]
        print(left, right)
    return await merge(await sort(left, screen), await sort(right, screen), screen)
    