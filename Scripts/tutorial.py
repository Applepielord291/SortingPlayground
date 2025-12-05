import pygame
import asyncio
from pygame.locals import *

# NO AI USED, only documentation, and code examples in their documentation
# Documentation used:
#   https://www.pygame.org/docs/

# Nigel Garcia
# tutorial.py
# The transition between the title and the game, plays two transition animations and a quick tutuorial.

# it goes: main.py --> tutorial.py --> simulation.py
# questions.py and constants.py are global variables/classes stored in there for convenience

# Also im going to be copy-pasting the same comments alot throughout all the scripts, just for clarity.

# Throughout all these scripts, you're gonna see functions defined with "async def" and functions called with "await function()"
# A library im using (pygbag), allows web builds of pygame applications, which is what im using
# however, since this programs gonna be on the web, it needs something like async IO to handle the high-performance stuff on the web
# Thus the async and the awaits.

# Other Scripts
import simulation as SIM
import constants as CONST

# deals with user inputs, called in the update loop
async def Inputs(screen): 
    # pygame.event is just a list of all events
    # events are stuff like keyboard inputs, closing windows, mouse inputs, ...
    # In this specific case, we need to know if the quit event is true so that we know when to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            quit()

    # All keyboard inputs are stored in a massive array as a bool value (false by default, true when pressed)
    # To check if a certain key is pressed, we can check if its true in the keystate array
    keystate = pygame.key.get_pressed() 

    # Early exit if no keys are down
    # just so that it doesnt have to check these contitions every loop iteration
    if not True in keystate: return 

    # Open Dropdown menu
    if keystate[pygame.K_UP] and not CONST.menuOpen:
        CONST.menuOpen = True
    # Close drowdown menu
    elif keystate[pygame.K_DOWN] and CONST.menuOpen:
        CONST.menuOpen = False
    
    # Basic controls demo (The random and start sort buttons)
    # the controls are S --> K since there needs to be a list first to be sorted
    if keystate[pygame.K_k] and CONST.canSort:
        CONST.canSort = False
    elif keystate[K_s] and not CONST.canSort:
        CONST.canSort = True
        
    # Menu Mode Select
    # Controls are with arrow keys for navigation, then ENTER for button selection
    # In this case its just the Ready button, so selection brings us straight to the simulation
    if keystate[pygame.K_RETURN] and CONST.menuOpen:
        # Reset global variables
        CONST.menuOpen = False 
        CONST.canSort = False
        await Transition(screen, 0, len(CONST.transitionImgList2), CONST.transitionImgList2)
        await SIM.Start(screen) 


async def RenderImages(screen): 
    # Menu dropdown
    curPos = await GetMenuPosY()

    # blit just means to render the current image at position (x, y) (in this case, its (0, curPos))
    screen.blit(CONST.dropDown, (0,curPos))

    # So each button has two states: selected and unselected
    # This part is just to visually show the user which button is selected and which one isnt, since i made two diff sprites for each button
    # In this case, random and sort cant be selected at the same time
    if not CONST.canSort:
        screen.blit(CONST.randBtn, (365, 135))
        screen.blit(CONST.startSel, (610, 135))
    else:
        screen.blit(CONST.randSel, (365, 135))
        screen.blit(CONST.startBtn, (610, 135))

    # Renders the ready button only if the dropdown menu is open
    if CONST.menuOpen:
        screen.blit(CONST.readyBtn, (1200 // 2.5, 400))
    
# returns dropdown position y value depending on menu state
async def GetMenuPosY(): 
    if not CONST.menuOpen:
        return 700 # closed: DOWN
    else:
        return 300 # open: UP

# deals with the visuals on screen, called in the update loop
async def RenderText(screen): 
    # Kinda like screen.blit, but since its a solid color we dont need an image file: 
    # .fill() takes a color (r, g, b, a) or (r,g,b) and fills the screen with said color
    # Since it serves as a background in this case, we render it first, under everything
    screen.fill((0, 0, 0))

    # Display texts
    title = "Quick Tutorial"
    btnClick = "Click S to Generate a random list, Click K to merge sort the list."
    reminder = "(Theres no list here right now, but in the game there will be a visual of the list)"
    nav = "Open/Close menu with up/down arrow"
    nav2 = "Navigate Menu with left/right arrow keys, press ENTER to select/Buy Upgrades."
    end = "Once you're ready, open the menu and press READY (with ENTER)"

    # Takes the font stored in constants.py (a system font with size 24) and renders it
    # The first param is the string to be displayed
    # The second param is just whether anti-aliasing is used or not
    # The third parameter is the color of the text (r,g,b,a) or (r,g,b): in this case I made it green
    # The fourth parameter is the color of the background (r,b,g,a) or (r,g,b): I made it black and set the alpha to 0.
    titleTxt = CONST.font.render(title, True, (0, 255, 0), (0, 0, 0, 0))
    # The rect is pretty much the position property of the text on the screen. 
    titleRect = titleTxt.get_rect()
    # sets the position (x,y) relative to the center
    titleRect.center = (1200 // 2, 45)
    # blit just means to render the current image at position (x, y) (in this case, its the textRect)
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

    nav2Txt = CONST.font.render(nav2, True, (0, 255, 0), (0, 0, 0, 0))
    nav2Rect = nav2Txt.get_rect()
    nav2Rect.center = (1200 // 2, 345)
    screen.blit(nav2Txt, nav2Rect)

    endTxt = CONST.font.render(end, True, (0, 255, 0), (0, 0, 0, 0))
    endRect = endTxt.get_rect()
    endRect.center = (1200 // 2, 405)
    screen.blit(endTxt, endRect)

# Handles the transition animations between windows
# This is called only before and after the quick tutorial
async def Transition(screen, currentFrame, endFrame, curAnim):
    while currentFrame < endFrame:
        # pygame.event is just a list of all events
        # events are stuff like keyboard inputs, closing windows, mouse inputs, ...
        # In this specific case, we need to know if the quit event is true so that we know when to quit

        # The reason why im not just calling the input function instead is because this is run during transition animations
        # The user is not supposed to be doing any inputs during transition animations. Only the ability to quit.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        titleScreenImg = pygame.image.load(curAnim[currentFrame]) # retrieve the image from the animation sheet
        screen.blit(titleScreenImg, (0,0)) # blit just means to render the current image at position (x, y) (in this case, its (0, 0))

        pygame.display.flip() # Updates the entire screen to account for any new renders needed to be displayed
        pygame.time.wait(30) # Render loop delay (mainly so that the animation plays at a normal speed)
        await asyncio.sleep(0) # Required for async stuff or it will just crash
        currentFrame += 1

# The update loop
async def Update(screen):
    while True:
        await Inputs(screen) 
        await RenderText(screen)
        await RenderImages(screen)
        pygame.display.flip()
        pygame.time.wait(30) # Frame delay
        await asyncio.sleep(0)

# Start of the tutorial.py script
async def Start(screen):
    await Transition(screen, 0, len(CONST.transitionImgList1), CONST.transitionImgList1)
    await Update(screen)