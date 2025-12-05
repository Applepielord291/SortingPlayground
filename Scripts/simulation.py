import pygame
import asyncio
import random
import math
from pygame.locals import *

# NO AI USED, only documentation, and code examples in their documentation
# Documentation used:
#   https://www.pygame.org/docs/

# Nigel Garcia
# simulation.py
# simulation window, where the actual game is, and many game stuff and cool things

# it goes: main.py --> tutorial.py --> simulation.py
# questions.py and constants.py are global variables/classes stored in there for convenience

# Also im going to be copy-pasting the same comments alot throughout all the scripts, just for clarity.

# Throughout all these scripts, you're gonna see functions defined with "async def" and functions called with "await function()"
# A library im using (pygbag), allows web builds of pygame applications, which is what im using
# however, since this programs gonna be on the web, it needs something like async IO to handle the high-performance stuff on the web
# Thus the async and the awaits.

# Other Scripts
import constants as CONST

# State manager
# Too many bool values for a single state, decided to make it more readable and assign a set of bools to a single int
async def StateManager():
    # user is at dropdown menu
    if CONST.menuOpen and not CONST.shopOpen and not CONST.errorUp and not CONST.modOpen: 
        CONST.currentState = CONST.MENU_SCREEN

    # user is in the shop 
    elif CONST.shopOpen and not CONST.errorUp and not CONST.modOpen: 
        CONST.currentState = CONST.SHOP_SCREEN

    # user is in the base state, clicking and merge-sorting
    elif not CONST.menuOpen and not CONST.shopOpen and not CONST.errorUp and not CONST.modOpen: 
        CONST.currentState = CONST.CLICK_SCREEN
    
    # Modify the sort for funnies
    elif CONST.modOpen and not CONST.shopOpen and not CONST.errorUp:
        CONST.currentState = CONST.MODIFY_SCREEN

    # user has a suprise error pop-up
    elif CONST.errorUp and not CONST.eduMode: 
        CONST.currentState = CONST.ERROR_SCREEN

# Generates a list with a dynamic length and max value
async def GenerateList():
    arr = [0] * CONST.length
    for i in range(CONST.length):
        randVal = random.randint(CONST.minVal, CONST.maxVal) 
        arr[i] = randVal
    CONST.arr = arr

# selOp is the int value corresponding to the selected button
# depending on that int, it would execute whatever function the buttons needs to do
# theres only one button so actually all of this is redundant
# but in the programs earlier stages there were going to be many more
# which is why the system is still here, in case I want to update the dropdown menu with more buttons to select
async def MenuOperations(selOp):
    if selOp == CONST.SHOP_SEL:
        if not CONST.shopOpen:
            CONST.shopOpen = True
        else:
            CONST.shopOpen = False
    elif selOp == CONST.MODIFY_SEL:
        if not CONST.modOpen:
            CONST.modOpen = True
        else:
            CONST.modOpen = False

# Buying shop upgrades system, function called when the user buys an item from the shop
# sel item is the selected upgrade (int)
async def BuyItem(selItem):
    # if its not buying extra list length then that means its an upgrade taht will cost SE
    # similar to buying things irl, you get thing and money gets subtracted
    # but it also gets more expensive, because game design.
    item = CONST.shopItems[selItem]
    if item.name != "Increase Elements":
        if CONST.sortedElements >= item.upgradePrice: # if you even have enough SE
            item.count += 1
            CONST.sortedElements -= item.upgradePrice
            item.upgradePrice //= 0.85
    
    # if it is buying extra list length then its an upgrade that will cost TS
    # TS is less of a currency and more of a milestone in this game, so you cant lose TS
    # similar to rewards, you show of your achievement, you get extra reward, and aim for greater!
    else:
        if CONST.timesSorted >= item.upgradePrice and CONST.length < CONST.MAX_LENGTH: # if you even have enough TS and it wont go past the max
            item.count += 1
            CONST.length += 1
            item.upgradePrice += 20

# Result after answering an error question
# if its right, growth multiplier (the rate at which your upgrades produce SE) increases!
# if you want a lore reason for that, its like fixing a runtime/logic error in your merge sort algorithm empire, making merge sort run faster
# if its wrong, then you lose 25% of your SE currency
# no lore reason, just reinforcement learning
async def ErrorResult(selVal):
    if selVal == CONST.selError.correctAnswer:
        CONST.correct = True
        CONST.growthMult += 1
    else:
        CONST.correct = False
        CONST.sortedElements -= int(CONST.sortedElements * 0.25)
    CONST.errorUp = False # so that the user isnt stuck on the error window

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
    if not True in keystate: return 

    # Clicker Buttons S --> K from the tutorial, but in action
    # there needs to be a list first to be sorted
    if CONST.currentState == CONST.CLICK_SCREEN: # is the user in the base screen?
        # Generate
        if keystate[pygame.K_k] and CONST.canSort: 
            pygame.mixer.Sound.play(CONST.click)
            CONST.timesSorted += 1
            CONST.sortedElements += CONST.length
            arr = await sort(CONST.arr, screen)
            CONST.arr = arr
            CONST.canSort = False
        # Sort
        elif keystate[K_s] and not CONST.canSort: 
            pygame.mixer.Sound.play(CONST.click)
            await GenerateList()
            CONST.canSort = True

        # Open the dropdwon menu (up arrow) and change the user state because now theyre on the dropdown menu
        if keystate[pygame.K_UP] and not CONST.menuOpen:
            CONST.menuOpen = True
    
    # Menu Navigation with arrow keys
    elif CONST.currentState == CONST.MENU_SCREEN: 
        # Close the dropdown menu (down arrow)
        if keystate[pygame.K_DOWN] and CONST.menuOpen:
            CONST.menuOpen = False
        
        # theres only one button so actually all of this is redundant
        # but in the programs earlier stages there were going to be many more
        # which is why the system is still here, in case I want to update the dropdown menu with more buttons to select
        if keystate[pygame.K_RIGHT] and CONST.curBtn < CONST.MODIFY_SEL:
            CONST.curBtn += 1
        elif keystate[pygame.K_LEFT] and CONST.curBtn > CONST.SHOP_SEL:
            CONST.curBtn -= 1
        
        # Selecting a button from the dropdown menu
        if keystate[pygame.K_RETURN]: 
            await MenuOperations(CONST.curBtn)
    
    # Shop navigation (same keybinds as dropdown menu)
    elif CONST.currentState == CONST.SHOP_SCREEN:
        if keystate[pygame.K_DOWN] and CONST.curShopSel < CONST.SUPERCOMPUTER:
            CONST.curShopSel += 1
        elif keystate[pygame.K_UP] and CONST.curShopSel > CONST.ELEMENT:
            CONST.curShopSel -= 1
        
        # Buy an upgrade
        if keystate[pygame.K_RETURN]:
            await BuyItem(CONST.curShopSel)
        # exit the shop menu with escape
        elif keystate[pygame.K_ESCAPE]:
            CONST.shopOpen = False
    
    # Array modify screen
    elif CONST.currentState == CONST.MODIFY_SCREEN:
        # Navigate the menu
        if keystate[pygame.K_DOWN] and CONST.curMod < CONST.EDUCATION:
            CONST.curMod += 1
        elif keystate[pygame.K_UP] and CONST.curMod > CONST.ORDER:
            CONST.curMod -= 1

        # order Selection
        if CONST.curMod == CONST.ORDER:
            if keystate[pygame.K_RIGHT]:
                CONST.AscOrDesc = False
            elif keystate[pygame.K_LEFT]: 
                CONST.AscOrDesc = True
        
        # Max value seleciton
        elif CONST.curMod == CONST.MAXIMUM:
            if keystate[pygame.K_RIGHT] and CONST.maxVal < 400:
                if keystate[pygame.K_LSHIFT]:
                    CONST.maxVal += 10
                elif not keystate[pygame.K_LSHIFT]:
                    CONST.maxVal += 1
            elif keystate[pygame.K_LEFT] and CONST.maxVal > CONST.minVal+1: 
                if keystate[pygame.K_LSHIFT]:
                    CONST.maxVal -= 10
                elif not keystate[pygame.K_LSHIFT]:
                    CONST.maxVal -= 1
        
        # Minimum value selection
        elif CONST.curMod == CONST.MINIMUM:
            if keystate[pygame.K_RIGHT] and CONST.minVal < CONST.maxVal-1:
                if keystate[pygame.K_LSHIFT]:
                    CONST.minVal += 10
                elif not keystate[pygame.K_LSHIFT]:
                    CONST.minVal += 1
            elif keystate[pygame.K_LEFT] and CONST.minVal > 0: 
                if keystate[pygame.K_LSHIFT]:
                    CONST.minVal -= 10
                elif not keystate[pygame.K_LSHIFT]:
                    CONST.minVal -= 1

        elif CONST.curMod == CONST.EDUCATION:
            if keystate[pygame.K_RIGHT]:
                CONST.eduMode = False
            elif keystate[pygame.K_LEFT]: 
                CONST.eduMode = True
        
        # Just so that the max/min value are in their bounds
        if CONST.maxVal < CONST.minVal+1: CONST.maxVal = CONST.minVal+1
        if CONST.minVal < 0: CONST.minVal = 0
        if CONST.minVal > CONST.maxVal-1: CONST.minVal = CONST.maxVal-1
        if CONST.maxVal > 400: CONST.maxVal = 400

        # Exit the array modify screen
        if keystate[pygame.K_ESCAPE]:
            CONST.modOpen = False

    # Error screen navigation (same as all the other menus)
    elif CONST.currentState == CONST.ERROR_SCREEN:
        # Each question has 4 answers, so i just hard coded it
        # but if i wanted it to be dynamic then i would add another paremeter in the questions class
        # to store the number of answers and use that as the condition below:
        if keystate[pygame.K_DOWN] and CONST.selAns < 3:
            CONST.selAns += 1
        elif keystate[pygame.K_UP] and CONST.selAns > 0:
            CONST.selAns -= 1
        
        # Select an answer
        if keystate[pygame.K_RETURN]:
            await ErrorResult(CONST.selAns)


# Render Sort algorithm made visual
# renders all the values as bars and draws them onto the screen
async def RenderBars(screen):
    if CONST.arr != None:
        pos = 100 # iterate x so that all the bars dont just render on top of each other
        width = 1000 // len(CONST.arr)
        if width == 0: width = 1
        increment = width
        for i in range(len(CONST.arr)):
            # draw.rect just draws a rectangle onto the screen, no image file required
            # the first parameter is what display the rect should be drawn to
            # the second parameter is the color of the rectabgle: in this case I made it white
            # the third parameter is the position and scale of the rects in (xPos, yPos, xScale, yScale)
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (pos, 75, width, CONST.arr[i]))
            pos += increment
        
# deals with image renders in the clicking screen (base state)
# so the main animation, and click buttons are here
async def RenderClickImages(screen, currentFrame, currentAnim): 
    titleScreenImg = pygame.image.load(currentAnim[currentFrame]) # retrieve the image from the animation sheet
    screen.blit(titleScreenImg, (0,0)) # blit just means to render the current image at position (x, y) (in this case, its (0, 0))

    # So each button has two states: selected and unselected
    # This part is just to visually show the user which button is selected and which one isnt, since i made two diff sprites for each button
    # In this case, random and sort cant be selected at the same time
    if not CONST.canSort:
        screen.blit(CONST.randBtn, (365, 550))
        screen.blit(CONST.startSel, (610, 550))
    else:
        screen.blit(CONST.randSel, (365, 550))
        screen.blit(CONST.startBtn, (610, 550))

# deals with menu rendering The dropdown menu (open/closed), and all the buttons in the dropdown menu
async def SimulationRender(screen): 
    #Menu dropdown
    curPos = await SimulationInputs()
    screen.blit(CONST.dropDown, (0,curPos)) # blit just means to render the current image at position (x, y) (in this case, its (0, curPos))

    # render dropdown menu buttons if the menu is actually open
    if CONST.menuOpen:
        # theres only one button so actually all of this is redundant
        # but in the programs earlier stages there were going to be many more
        # which is why the system is still here, in case I want to update the dropdown menu with more buttons to select
        if CONST.curBtn == CONST.SHOP_SEL:
            screen.blit(CONST.shopSel, (365, 400))
            screen.blit(CONST.modBtn, (610, 400))
        else:
            screen.blit(CONST.shopBtn, (365, 400))
            screen.blit(CONST.modSel, (610, 400))
    
# returns dropdown position y value depending on menu state
async def SimulationInputs(): 
    if not CONST.menuOpen:
        return 700 # closed: DOWN
    else:
        return 300 # open: UP

# pretty much the 'User statistics' for the game
# originally i wanted to do smth like cookie clicker with news headlines, but im too lazy 
# but yeah, the fucntion displays the following
# current list size, the max list list, the growth rate, the result of the previous answer
# user TE, user SE
async def StatsRender(screen):
    displayTxt = "List Size: {0} || Max Size: {1} || Growth Rate: {2} || Previous Answer: {3}".format(CONST.length, CONST.MAX_LENGTH, CONST.growthMult, CONST.correct)
    displayTxt2 = "Times Sorted (TS): {0} || Sorted Elements (SE): {1}".format(CONST.timesSorted, CONST.sortedElements)

    # Takes the font stored in constants.py (a system font with size 24) and renders it
    # The first param is the string to be displayed
    # The second param is just whether anti-aliasing is used or not
    # The third parameter is the color of the text (r,g,b,a) or (r,g,b): in this case I made it green
    # The fourth parameter is the color of the background (r,b,g,a) or (r,g,b): I made it black and set the alpha to 0.
    text = CONST.font.render(displayTxt, True, (0, 255, 0), (0, 0, 0, 0))
    # The rect is pretty much the position property of the text on the screen. 
    textRect = text.get_rect()
    # sets the position (x,y) relative to the center
    textRect.center = (1200 // 2, 15)
    # blit just means to render the current image at position (x, y) (in this case, its the textRect)
    screen.blit(text, textRect)

    text = CONST.font.render(displayTxt2, True, (0, 255, 0), (0, 0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1200 // 2, 45)
    screen.blit(text, textRect)

# Renders shop menu and all of the available things to purchase as long as the shop menu is open
async def ShopRender(screen):
    if CONST.shopOpen:
        # draw.rect just draws a rectangle onto the screen, no image file required
        # the first parameter is what display the rect should be drawn to
        # the second parameter is the color of the rectabgle: in this case I made it black
        # the third parameter is the position and scale of the rects in (xPos, yPos, xScale, yScale)
        pygame.draw.rect(screen, pygame.Color(0, 0, 0, 200), (1200 // 4, 150, 1200 // 2, 500))
        # cool title
        screen.blit(CONST.shopTitle, (1200 // 2.5, 90)) # blit just means to render the current image at position (x, y) (in this case, its (middle, 90))
        # to iterate the upgrade names so the texts dont all render on top of each other
        # the base is 200 to make sure that the start of the text renders are actually in the shop rectangle background
        posY = 200 
        for i in range(len(CONST.shopItems)):
            selItem = CONST.shopItems[i]
            displayTxt = "{0} {1}: {2} {3}".format(selItem.count, selItem.name, selItem.upgradePrice, selItem.currencyType)
            # Takes the font stored in constants.py (a system font with size 24) and renders it
            # The first param is the string to be displayed
            # The second param is just whether anti-aliasing is used or not
            # The third parameter is the color of the text (r,g,b,a) or (r,g,b): in this case I made it green
            # The fourth parameter is the color of the background (r,b,g,a) or (r,g,b): I made it black and set the alpha to 0.
            text = CONST.font.render(displayTxt, True, (0, 255, 0), (0, 0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (1200 // 2, posY)
            screen.blit(text, textRect)

            # if condition is met that means that the current iteration is also the user selection
            # so display an arrow next to it showing to the user that this is the currently selected upgrade
            if CONST.curShopSel == i:
                screen.blit(CONST.shopArrowSel, (850, posY-15)) # -15 arrow y offset to line up with the text
            posY += 35
        exitTxt = "ESCAPE to exit"
        text = CONST.font.render(exitTxt, True, (0, 255, 0), (0, 0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1200 // 2, posY + 40)
        screen.blit(text, textRect)
    
# Passive income from upgrades, since thats how the upgrades work (so it runs in the update loop)
# the formula is (count of upgrade i) * (position in shop list+1) + (growth multiplier)
async def MoneyGen():
    for i in range(len(CONST.shopItems)-1):
        selItem = CONST.shopItems[i]
        if i != 0:
            CONST.sortedElements += selItem.count * ((i+1)+CONST.growthMult)

# This is the error popup change
# pretty much, I was inspired by the cookie clicker golden cookies
# made something similar, wheres theres a small change every 40 milliseconds for an error popup to occur
# theyre just questions, to help the user better understand merge sort
# this is the calculation for that 1 in 5000 change every 40 milliseconds
async def ErrorChance():
    rand = int(random.random() * 5000)
    if rand == 1 and CONST.currentState != CONST.ERROR_SCREEN:
        CONST.prevState = CONST.currentState
        CONST.errorUp = True
        randVal = int(random.random() * len(CONST.errors))
        return randVal # so that if the return actually isnt null then the 1/5000 occured so render the error

# Error popup render when the 1 in 5000 hits
async def ErrorRender(screen, val):
    # draw.rect just draws a rectangle onto the screen, no image file required
    # the first parameter is what display the rect should be drawn to
    # the second parameter is the color of the rectabgle: in this case I made it black
    # the third parameter is the position and scale of the rects in (xPos, yPos, xScale, yScale)
    pygame.draw.rect(screen, pygame.Color(0, 0, 0, 200), (1200 // 10, 75, 1200 // 1.25, 700))
    posY = 100 # (for iterating all the question class properties posY, so they dont all render on top of each other)
    CONST.selError = CONST.errors[val] # get the selected class for easier access cause were gonna mess with this alot
    title = "ERROR"
    # Takes the font stored in constants.py (a system font with size 24) and renders it
    # The first param is the string to be displayed
    # The second param is just whether anti-aliasing is used or not
    # The third parameter is the color of the text (r,g,b,a) or (r,g,b): in this case I made it green
    # The fourth parameter is the color of the background (r,b,g,a) or (r,g,b): I made it black and set the alpha to 0.
    titleText = CONST.errorFont.render(title, True, (255, 0, 0), (0, 0, 0, 0))
    # The rect is pretty much the position property of the text on the screen. 
    titleTextRect = titleText.get_rect()
    # sets the position (x,y) relative to the center
    titleTextRect.center = (1200 // 2, posY)
    # blit just means to render the current image at position (x, y) (in this case, its the textRect)
    screen.blit(titleText, titleTextRect)
    posY += 20

    # and then repeat below

    exitTxt = "CORRECT: UPGRADES GENERATE SE FASTER"
    text = CONST.errorFont.render(exitTxt, True, (255, 0, 0), (0, 0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1200 // 2, posY)
    screen.blit(text, textRect)
    posY += 20

    exitTxt = "INCORRECT: LOST 25% SE"
    text = CONST.errorFont.render(exitTxt, True, (255, 0, 0), (0, 0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (1200 // 2, posY)
    screen.blit(text, textRect)
    posY += 20

    question = "QUESTION: {0}".format(CONST.selError.question)
    questionText = CONST.errorFont.render(question, True, (255, 0, 0), (0, 0, 0, 0))
    questionTextRect = questionText.get_rect()
    questionTextRect.center = (1200 // 2, posY)
    screen.blit(questionText, questionTextRect)
    posY += 30

    # so because some of the stuff are arrays of strings: 
    # its the same idea as all the other ones, but now its in a for loop 
    for i in range(len(CONST.selError.codeSnippet)):
        codeSnip = "{0}".format(CONST.selError.codeSnippet[i])
        text = CONST.errorFont.render(codeSnip, True, (255, 0, 0), (0, 0, 0, 0))
        textRect = text.get_rect()
        textRect.midleft = (1200 // 3.5, posY)
        screen.blit(text, textRect)
        posY += 20
    posY += 20
    for i in range(len(CONST.selError.answers)):
        answers = "{0}: {1}".format(i+1, CONST.selError.answers[i])
        text = CONST.errorFont.render(answers, True, (255, 0, 0), (0, 0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1200 // 2, posY)
        screen.blit(text, textRect)
        if CONST.selAns == i:
            screen.blit(CONST.shopArrowSel, (850, posY-15)) #-15 arrow y offset
        posY += 20

# Display the menu for the Array modify screen
# same idea as all the other menus
async def ModifyMenuRender(screen):
    if CONST.currentState == CONST.MODIFY_SCREEN:
        pygame.draw.rect(screen, pygame.Color(0, 0, 0, 200), (1200 // 9, 65, 1200 // 1.25, 700))

        title = "Modify Merge Sort!"
        order = "Ascending?: {0}".format(CONST.AscOrDesc)
        maxVal = "Max Element Value: {0}".format(CONST.maxVal)
        minVal = "Minimum Element Value: {0}".format(CONST.minVal)
        eduMode = "Education Mode: {0}".format(CONST.eduMode)
        warning = "WARNING: its going to take a long time to sort the array if you're in late-game"
        tooltip = "Press LEFT/RIGHT arrows to cycle through values. Hold SHIFT to cycle faster."
        exit = "Press ESCAPE to exit"

        titleTxt = CONST.font.render(title, True, (0, 255, 0), None)
        titleRect = titleTxt.get_rect()
        titleRect.center = (1200 // 2, 115)
        screen.blit(titleTxt, titleRect)

        orderTxt = CONST.font.render(order, True, (0, 255, 0), None)
        orderRect = orderTxt.get_rect()
        orderRect.center = (1200 // 2, 175)
        screen.blit(orderTxt, orderRect)
        if CONST.curMod == CONST.ORDER:
            screen.blit(CONST.shopArrowSel, (850, 160))

        maxValTxt = CONST.font.render(maxVal, True, (0, 255, 0), None)
        maxValRect = maxValTxt.get_rect()
        maxValRect.center = (1200 // 2, 235)
        screen.blit(maxValTxt, maxValRect)
        if CONST.curMod == CONST.MAXIMUM:
            screen.blit(CONST.shopArrowSel, (850, 220))

        minValTxt = CONST.font.render(minVal, True, (0, 255, 0), None)
        minValRect = minValTxt.get_rect()
        minValRect.center = (1200 // 2, 295)
        screen.blit(minValTxt, minValRect)
        if CONST.curMod == CONST.MINIMUM:
            screen.blit(CONST.shopArrowSel, (850, 280))
        
        eduModeTxt = CONST.font.render(eduMode, True, (0, 255, 0), None)
        eduRect = eduModeTxt.get_rect()
        eduRect.center = (1200 // 2, 355)
        screen.blit(eduModeTxt, eduRect)
        if CONST.curMod == CONST.EDUCATION:
            screen.blit(CONST.shopArrowSel, (850, 340))
        
        warningTxt = CONST.font.render(warning, True, (0, 255, 0), None)
        warningRect = warningTxt.get_rect()
        warningRect.center = (1200 // 2, 400)
        screen.blit(warningTxt, warningRect)

        tooltipTxt = CONST.font.render(tooltip, True, (0, 255, 0), None)
        tooltipRect = tooltipTxt.get_rect()
        tooltipRect.center = (1200 // 2, 460)
        screen.blit(tooltipTxt, tooltipRect)

        exitTxt = CONST.font.render(exit, True, (0, 255, 0), None)
        exitRect = exitTxt.get_rect()
        exitRect.center = (1200 // 2, 565)
        screen.blit(exitTxt, exitRect)

# The update loop
async def Update(screen):
    currentFrame = 0
    endFrame = len(CONST.settingsImgList)
    while True:
        # Render loop
        while currentFrame < endFrame:
            # All of these are rendered in a certain order
            # The functions called first means they are rendered first, and below everything else
            # Functions called last are rendered in front of everything
            # If youve ever used drawing software, I like to think of it as image layers.
            await StateManager()
            await Inputs(screen)
            await RenderClickImages(screen, currentFrame, CONST.settingsImgList)
            await StatsRender(screen)
            await RenderBars(screen)
            await SimulationRender(screen)
            await ShopRender(screen)
            await ModifyMenuRender(screen)
            
            # Gameplay loops
            await MoneyGen()
            if not CONST.errorUp:
                CONST.quest = await ErrorChance()
            else:
                await ErrorRender(screen, CONST.quest)

            pygame.display.flip() # Updates the entire screen to account for any new renders needed to be displayed
            pygame.time.wait(40) # Render loop delay (mainly so that the animation plays at a normal speed)
            await asyncio.sleep(0) # Required for async stuff or it will just crash
            currentFrame += 1
        currentFrame = 0 # Reset current frame to the start to loop animation

# The start of the simulation/game/yeah
async def Start(screen):
    await Update(screen)

# Same as RenderBars but takes is slow and step by step
# Renders the bars, the code involved and the control tooltips
async def RenderBarSlow(list, startPoint, screen, displayTxt, codeSnip):
    if list != None:
        display = CONST.font.render(displayTxt, True, (0, 255, 0), None)
        displayRect = display.get_rect()
        displayRect.midleft = (startPoint + 50, 50)
        screen.blit(display, displayRect)
        
        display = CONST.font.render("Press and hold ENTER to slow down", True, (0, 255, 0), None)
        displayRect = display.get_rect()
        displayRect.center = (1200 // 4.5, 600)
        screen.blit(display, displayRect)

        display = CONST.font.render("Press and hold ESCAPE to leave early", True, (0, 255, 0), None)
        displayRect = display.get_rect()
        displayRect.center = (1200 // 4.5, 675)
        screen.blit(display, displayRect)

        yPos = 500
        for i in range(len(codeSnip)):
            txt = CONST.font.render(codeSnip[i], True, (0, 255, 0), None)
            txtRect = txt.get_rect()
            txtRect.midleft = (1200 // 2, yPos)
            screen.blit(txt, txtRect)
            yPos += 30

        pos = startPoint # iterate x so that all the bars dont just render on top of each other
        width = math.ceil(500 / len(CONST.arr)) # bar width
        increment = width # distance between bars
        curSpd = 250
        fast = 250 # delay (in ms) between each iteration
        slow = 1500
        for i in range(len(list)):
            # draw.rect just draws a rectangle onto the screen, no image file required
            # the first parameter is what display the rect should be drawn to
            # the second parameter is the color of the rectabgle: in this case I made it white
            # the third parameter is the position and scale of the rects in (xPos, yPos, xScale, yScale)
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (pos, 75, width, list[i]))
            pos += increment
            keystate = pygame.key.get_pressed() 
            # Exit the tutorial showcase
            if keystate[pygame.K_ESCAPE]:
                CONST.eduMode = False
                break
            # Toggle slowdown/speedup tutorial simulation
            elif keystate[pygame.K_RETURN]:
                if curSpd == fast:
                    curSpd = slow
                else:
                    curSpd = fast
            # The reason why i have a display refresh here is because I want to show a visual step by step process
            # So i need to show each iteration and render it, thus the .flip() refresh
            pygame.display.flip()
            pygame.time.wait(curSpd)
            await asyncio.sleep(0) # Required for async stuff or it will just crash
            # This essentially just makes it so that the program can keep on processing pygame events
            # In this specific case, not having it in this loops makes the inputs not respond (excape key, return key)
            # thus the .pump()
            pygame.event.pump()

# Merge sort
# its not too different from the merge sort in classes
# only modification is the ascending/descending, but thats really it
async def merge(left, right, screen):
    finalList = []
    i, j, = 0, 0
    while i < len(left) and j < len(right):
        # if is ascending
        if CONST.AscOrDesc:
            if left[i] <= right[j]:
                finalList.append(left[i])
                i += 1
            else:
                finalList.append(right[j])
                j += 1
        # if descending
        else:
            if left[i] >= right[j]:
                finalList.append(left[i])
                i += 1
            else:
                finalList.append(right[j])
                j += 1
        # if education mode is on, render each step
        if CONST.eduMode:
            screen.fill((0, 0, 0))
            await RenderBarSlow(finalList, 25, screen, "add the smallest value to the final", CONST.displayMerge2)
    while i < len(left):
        finalList.append(left[i])
        i += 1
        # if education mode is on, render each step
        if CONST.eduMode:
            screen.fill((0, 0, 0))
            await RenderBarSlow(finalList, 25, screen, "add remaining elements from left side", CONST.displayMerge3)
    while j < len(right):
        finalList.append(right[j])
        j += 1
        # if education mode is on, render each step
        if CONST.eduMode:
            screen.fill((0, 0, 0))
            await RenderBarSlow(finalList, 25, screen, "add remaining elements from right side", CONST.displayMerge4)
    return finalList
async def sort(list, screen):
    length = len(list)
    if length < 2:
        return(list)
    else:
        left = list[:length//2]
        right = list[length//2:]
        # if education mode is on, render each step
        if CONST.eduMode:
            screen.fill((0, 0, 0))
            await RenderBarSlow(left, 25, screen, "Split Array: Left", CONST.displayMerge1)
        # The reason why these are seperated into two if conditions is so that the user can actually exit
        # what i mean is, if these were in the same statement then the user would have to wait for left AND right side to finish
        # rendering before being able to exit
        if CONST.eduMode:
            await RenderBarSlow(right, 600, screen, "Split Array: Right", CONST.displayMerge1)
    return await merge(await sort(left, screen), await sort(right, screen), screen)
    