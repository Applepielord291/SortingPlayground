import pygame
import asyncio
from pygame.locals import *

# Nigel Garcia
# tutorial.py
# The transition between the title and the game, plays two transition animations and a quick tutuorial.

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

    # Early exit if no keys are down
    if not True in keystate: return 

    # Opening/Closing Menu
    if keystate[pygame.K_UP] and not CONST.menuOpen:
        CONST.menuOpen = True
    
    if keystate[pygame.K_DOWN] and CONST.menuOpen:
        CONST.menuOpen = False
    
    if keystate[pygame.K_k] and CONST.canSort:
        CONST.canSort = False
    elif keystate[K_s] and not CONST.canSort:
        CONST.canSort = True
        
    # Menu Mode Select
    if keystate[pygame.K_RETURN] and CONST.menuOpen:
        CONST.menuOpen = False 
        CONST.canSort = False
        await Transition(screen, 0, len(CONST.transitionImgList2), CONST.transitionImgList2)
        await SIM.Start(screen) 

async def SimulationRender(screen): 
    #Menu dropdown
    curPos = await SimulationInputs()
    screen.blit(CONST.dropDown, (0,curPos))

    if not CONST.canSort:
        screen.blit(CONST.randBtn, (365, 135))
        screen.blit(CONST.startSel, (610, 135))
    elif CONST.canSort:
        screen.blit(CONST.randSel, (365, 135))
        screen.blit(CONST.startBtn, (610, 135))

    # render buttons
    if CONST.menuOpen:
        screen.blit(CONST.readyBtn, (1200 // 2.5, 400))
    
# returns dropdown position y value depending on menu state
async def SimulationInputs(): 
    if not CONST.menuOpen:
        return 700
    else:
        return 300

# deals with the visuals on screen, called in the update loop
async def RenderImages(screen): 
    screen.fill((0, 0, 0))

    title = "Quick Tutorial"
    btnClick = "Click S to Generate a random list, Click K to merge sort the list."
    reminder = "(Theres no list here right now, but in the game there will be a visual of the list)"
    nav = "Open/Navigate Menus with arrow keys, press ENTER to select."
    end = "Once you're ready, open the menu and press READY (with ENTER)"

    titleTxt = CONST.font.render(title, True, (0, 255, 0), (0, 0, 0, 0))
    titleRect = titleTxt.get_rect()
    titleRect.center = (1200 // 2, 45)
    screen.blit(titleTxt, titleRect)

    btnClickTxt = CONST.font.render(btnClick, True, (0, 255, 0), (0, 0, 0, 0))
    btnClickRect = btnClickTxt.get_rect()
    btnClickRect.center = (1200 // 2, 85)
    screen.blit(btnClickTxt, btnClickRect)

    remTxt = CONST.font.render(reminder, True, (0, 255, 0), (0, 0, 0, 0))
    remRect = remTxt.get_rect()
    remRect.center = (1200 // 2, 230)
    screen.blit(remTxt, remRect)

    navTxt = CONST.font.render(nav, True, (0, 255, 0), (0, 0, 0, 0))
    navRect = navTxt.get_rect()
    navRect.center = (1200 // 2, 285)
    screen.blit(navTxt, navRect)

    endTxt = CONST.font.render(end, True, (0, 255, 0), (0, 0, 0, 0))
    endRect = endTxt.get_rect()
    endRect.center = (1200 // 2, 345)
    screen.blit(endTxt, endRect)


async def Transition(screen, currentFrame, endFrame, curAnim):
    while currentFrame < endFrame:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        titleScreenImg = pygame.image.load(curAnim[currentFrame])
        screen.blit(titleScreenImg, (0,0))

        pygame.display.flip()
        pygame.time.wait(30) # Frame delay
        await asyncio.sleep(0)
        currentFrame += 1

async def Update(screen):
    while True:
        await Inputs(screen) 
        await RenderImages(screen)
        await SimulationRender(screen)
        pygame.display.flip()
        pygame.time.wait(30) # Frame delay
        await asyncio.sleep(0)

async def Start(screen):
    await Transition(screen, 0, len(CONST.transitionImgList1), CONST.transitionImgList1)
    await Update(screen)