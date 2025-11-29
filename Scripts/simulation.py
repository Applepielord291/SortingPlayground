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
async def StateManager():
    if CONST.menuOpen and not CONST.shopOpen:
        CONST.currentState = CONST.MENU_SCREEN
    elif CONST.shopOpen:
        CONST.currentState = CONST.SHOP_SCREEN
    elif not CONST.menuOpen and not CONST.shopOpen:
        CONST.currentState = CONST.CLICK_SCREEN

# Generates a list with custom length and custom max value
async def GenerateList():
    arr = [0] * CONST.length
    for i in range(CONST.length):
        randVal = int(random.random() * CONST.maxVal)
        arr[i] = randVal
    CONST.arr = arr

# accepts a value and calles a function depending on the value
async def MenuOperations(selOp, screen):
    if selOp == CONST.CHANGE_DIR:
        if CONST.AscOrDesc:
            CONST.AscOrDesc = False
        else:
            CONST.AscOrDesc = True
    
    elif selOp == CONST.CHANGE_SIZE:
        if not CONST.pickMaxElem:
            CONST.pickMaxElem = True
            CONST.pickMaxVal = False
        else:
            CONST.pickMaxElem = False
            CONST.pickMaxVal = False
    
    elif selOp == CONST.CHANGE_MAX:
        if not CONST.pickMaxVal:
            CONST.pickMaxElem = False
            CONST.pickMaxVal = True
        else:
            CONST.pickMaxElem = False
            CONST.pickMaxVal = False

    elif selOp == CONST.SHOP_SEL:
        if not CONST.shopOpen:
            CONST.shopOpen = True
        else:
            CONST.shopOpen = False

async def BuyItem(selItem):
    if CONST.shopItems[selItem] != "Elements":
        if CONST.sortedElements >= CONST.shopItemPrice[selItem]:
            CONST.shopItemCount[selItem] += 1
            CONST.sortedElements -= CONST.shopItemPrice[selItem]
            CONST.shopItemPrice[selItem] //= 0.95
    else:
        if CONST.timesSorted >= CONST.shopItemPrice[selItem]:
            CONST.shopItemCount[selItem] += 1
            CONST.length += 1
            CONST.shopItemPrice[selItem] += 50


# Input manager
async def Inputs(screen): 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keystate = pygame.key.get_pressed() 

    # Early exit if no keys are down
    if not True in keystate: return 

    # Clicker Buttons
    if CONST.currentState == CONST.CLICK_SCREEN:
        if keystate[pygame.K_k] and CONST.canSort:
            CONST.timesSorted += 1
            CONST.sortedElements += CONST.length
            arr = await sort(CONST.arr, screen)
            CONST.arr = arr
            CONST.canSort = False
        elif keystate[K_s] and not CONST.canSort:
            await GenerateList()
            CONST.canSort = True

        # Opening/Closing Menu
        if keystate[pygame.K_UP] and not CONST.menuOpen: # https://www.pygame.org/docs/ref/key.html
            CONST.menuOpen = True
    
    #------------------------------------------------Debugging start----------------------------------------------------------------
        
    # if keystate[pygame.K_d] and CONST.pickMaxVal:
    #     CONST.maxVal += 1
    # elif keystate[pygame.K_a] and CONST.pickMaxVal:
    #     CONST.maxVal -= 1

    # if keystate[pygame.K_d] and CONST.pickMaxElem:
    #     CONST.length += 1
    # elif keystate[pygame.K_a] and CONST.pickMaxElem:
    #     CONST.length -= 1
    #---------------------------------------------------Debugging end---------------------------------------------------------------------
    
    # Menu Navigation
    if CONST.currentState == CONST.MENU_SCREEN: 
        if keystate[pygame.K_DOWN] and CONST.menuOpen:
            CONST.menuOpen = False
        
        if keystate[pygame.K_RIGHT] and CONST.curBtn < CONST.SHOP_SEL:
            CONST.curBtn += 1
        elif keystate[pygame.K_LEFT] and CONST.curBtn > CONST.CHANGE_SIZE:
            CONST.curBtn -= 1
        
        # Menu Mode Select
        if keystate[pygame.K_RETURN]: 
            await MenuOperations(CONST.curBtn, screen)
    
    if CONST.currentState == CONST.SHOP_SCREEN:
        if keystate[pygame.K_DOWN] and CONST.curShopSel < CONST.BACK:
            CONST.curShopSel += 1
        elif keystate[pygame.K_UP] and CONST.curShopSel > CONST.SCRIPT:
            CONST.curShopSel -= 1
        
        if keystate[pygame.K_RETURN]:
            if CONST.curShopSel != CONST.BACK:
                await BuyItem(CONST.curShopSel)
            else:
                CONST.shopOpen = False

# Render Sort algorithm
async def RenderBars(screen):
    if CONST.arr != None:
        pos = 20
        for i in range(len(CONST.arr)):
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (pos, 75, 15, CONST.arr[i]))
            pos += 20

async def RenderTransitions(screen, currentFrame, currentAnim):
    titleScreenImg = pygame.image.load(currentAnim[currentFrame])
    screen.blit(titleScreenImg, (0,0))
        
# deals with image renders
async def RenderImages(screen, currentFrame, currentAnim): 
    titleScreenImg = pygame.image.load(currentAnim[currentFrame])
    screen.blit(titleScreenImg, (0,0))

    if not CONST.canSort:
        screen.blit(CONST.randBtn, (365, 550))
        screen.blit(CONST.startSel, (610, 550))
    elif CONST.canSort:
        screen.blit(CONST.randSel, (365, 550))
        screen.blit(CONST.startBtn, (610, 550))

# deals with menu rendering (main dropdown, all the buttons)
async def SimulationRender(screen): 
    #Menu dropdown
    curPos = await SimulationInputs()
    screen.blit(CONST.dropDown, (0,curPos))

    # render buttons
    if CONST.menuOpen:
        if CONST.curBtn == 1:
            screen.blit(CONST.sizeSel, (30, 400))
        else:
            screen.blit(CONST.sizeBtn, (30, 400))

        if CONST.curBtn == 2:
            screen.blit(CONST.maxSel, (260, 400))
        else:
            screen.blit(CONST.maxBtn, (260, 400))

        if CONST.curBtn == 3:
            screen.blit(CONST.orderSel, (490, 400))
        else:
            screen.blit(CONST.orderBtn, (490, 400))
        
        if CONST.curBtn == 4:
            screen.blit(CONST.shopSel, (720, 400))
        else:
            screen.blit(CONST.shopBtn, (720, 400))
    
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
        text = CONST.font.render(displayTxt, True, (0, 255, 0), (0, 0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1200 // 2, 1200 // 2)
        screen.blit(text, textRect)
    
    if CONST.pickMaxVal and not CONST.pickMaxElem:
        displayTxt = "Max Value: {0}".format(CONST.maxVal)
        text = CONST.font.render(displayTxt, True, (0, 255, 0), (0, 0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1200 // 2, 1200 // 2)
        screen.blit(text, textRect)

async def SideBarRender(screen):
    displayTxt = "Sort Stats: Size: {0} || Max: {1} || Asc: {2} || Times sorted: {3} || Sorted Elements: {4}".format(CONST.length, CONST.maxVal, CONST.AscOrDesc, CONST.timesSorted, CONST.sortedElements)

    text = CONST.font.render(displayTxt, True, (0, 255, 0), (0, 0, 0, 0))
    textRect = text.get_rect()
    screen.blit(text, textRect)

# Renders shop menu
async def ShopRender(screen):
    if CONST.shopOpen:
        pygame.draw.rect(screen, pygame.Color(0, 0, 0, 200), (1200 // 4, 150, 1200 // 2, 500))
        posY = 200
        for i in range(len(CONST.shopItems)):
            displayTxt = "{0} {1}: {2} {3}".format(CONST.shopItemCount[i], CONST.shopItems[i], CONST.shopItemPrice[i], CONST.shopItemCurrency[i])
            text = CONST.font.render(displayTxt, True, (0, 255, 0), (0, 0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (1200 // 2, posY)
            screen.blit(text, textRect)

            if CONST.curShopSel == i:
                screen.blit(CONST.shopArrowSel, (850, posY-15))
            posY += 35
    
async def MoneyGen():
    for i in range(len(CONST.shopItemCount)-1):
        if CONST.shopItemCount[i] != 0:
            CONST.sortedElements += CONST.shopItemCount[i] * i+1

# Render loop
async def Update(screen):
    currentFrame = 0
    endFrame = len(CONST.settingsImgList)
    while True:
        while currentFrame < endFrame:
            await StateManager()
            await Inputs(screen)
            await RenderImages(screen, currentFrame, CONST.settingsImgList)
            await SideBarRender(screen)
            await RenderBars(screen)
            await SimulationRender(screen)
            await SettingsRender(screen)
            await ShopRender(screen)
            
            # Gameplay loops
            await MoneyGen()

            pygame.display.flip()
            pygame.time.wait(40) # Frame delay
            await asyncio.sleep(0)
            currentFrame += 1
        currentFrame = 0

# Transition loop: runs once and before the update loop
async def Transition(screen, currentFrame, endFrame, curAnim):
    while currentFrame < endFrame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        await RenderTransitions(screen, currentFrame, curAnim)
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
    return await merge(await sort(left, screen), await sort(right, screen), screen)
    