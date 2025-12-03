import pygame
import asyncio
import random
from pygame.locals import *

# NO AI USED

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
import questions as QUEST

# State manager
# Too many bool values for a single state, decided to make it more readable and assign a set of bools to a single int
async def StateManager():
    # user is at dropdown menu
    if CONST.menuOpen and not CONST.shopOpen and not CONST.errorUp: 
        CONST.currentState = CONST.MENU_SCREEN

    # user is in the shop 
    elif CONST.shopOpen and not CONST.errorUp: 
        CONST.currentState = CONST.SHOP_SCREEN

    # user is in the base state, clicking and merge-sorting
    elif not CONST.menuOpen and not CONST.shopOpen and not CONST.errorUp: 
        CONST.currentState = CONST.CLICK_SCREEN

    # user has a suprise error pop-up
    elif CONST.errorUp: 
        CONST.currentState = CONST.ERROR_SCREEN

# Generates a list with a dynamic length and a constant max value
async def GenerateList():
    arr = [0] * CONST.length
    for i in range(CONST.length):
        randVal = int(random.random() * CONST.maxVal)
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

# Buying shop upgrades system, function called when the user buys an item from the shop
# sel item is the selected upgrade (int)
async def BuyItem(selItem):
    # if its not buying extra list length then that means its an upgrade taht will cost SE
    # similar to buying things irl, you get thing and money gets subtracted
    # but it also gets more expensive, because game design.
    if CONST.shopItems[selItem] != "Elements":
        if CONST.sortedElements >= CONST.shopItemPrice[selItem]: # if you even have enough SE
            CONST.shopItemCount[selItem] += 1
            CONST.sortedElements -= CONST.shopItemPrice[selItem]
            CONST.shopItemPrice[selItem] //= 0.90
    
    # if it is buying extra list length then its an upgrade that will cost TS
    # TS is less of a currency and more of a milestone in this game, so you cant lose TS
    # similar to rewards, you show of your achievement, you get extra reward, and aim for greater!
    else:
        if CONST.timesSorted >= CONST.shopItemPrice[selItem] and CONST.length < CONST.MAX_LENGTH: # if you even have enough TS and it wont go past the max
            CONST.shopItemCount[selItem] += 1
            CONST.length += 1
            CONST.shopItemPrice[selItem] += 200

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
        CONST.sortedElements //= 1.25
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
            CONST.timesSorted += 1
            CONST.sortedElements += CONST.length
            arr = await sort(CONST.arr)
            CONST.arr = arr
            CONST.canSort = False
        # Sort
        elif keystate[K_s] and not CONST.canSort: 
            await GenerateList()
            CONST.canSort = True

        # Open the dropdwon menu (up arrow) and change the user state because now theyre on the dropdown menu
        if keystate[pygame.K_UP] and not CONST.menuOpen:
            CONST.menuOpen = True
    
    # Menu Navigation with arrow keys
    if CONST.currentState == CONST.MENU_SCREEN: 
        # Close the dropdown menu (down arrow)
        if keystate[pygame.K_DOWN] and CONST.menuOpen:
            CONST.menuOpen = False
        
        # theres only one button so actually all of this is redundant
        # but in the programs earlier stages there were going to be many more
        # which is why the system is still here, in case I want to update the dropdown menu with more buttons to select
        if keystate[pygame.K_RIGHT] and CONST.curBtn < CONST.SHOP_SEL:
            CONST.curBtn += 1
        elif keystate[pygame.K_LEFT] and CONST.curBtn > CONST.SHOP_SEL:
            CONST.curBtn -= 1
        
        # Selecting a button from the dropdown menu
        if keystate[pygame.K_RETURN]: 
            await MenuOperations(CONST.curBtn)
    
    # Shop navigation (same keybinds as dropdown menu)
    if CONST.currentState == CONST.SHOP_SCREEN:
        if keystate[pygame.K_DOWN] and CONST.curShopSel < CONST.ELEMENT:
            CONST.curShopSel += 1
        elif keystate[pygame.K_UP] and CONST.curShopSel > CONST.SCRIPT:
            CONST.curShopSel -= 1
        
        # Buy an upgrade
        if keystate[pygame.K_RETURN]:
            await BuyItem(CONST.curShopSel)
        # exit the shop menu with escape
        elif keystate[pygame.K_ESCAPE]:
            CONST.shopOpen = False

    # Error screen navigation (same as all the other menus)
    if CONST.currentState == CONST.ERROR_SCREEN:
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
        pos = 20 # iterate x so that all the bars dont just render on top of each other
        for i in range(len(CONST.arr)):
            # draw.rect just draws a rectangle onto the screen, no image file required
            # the first parameter is what display the rect should be drawn to
            # the second parameter is the color of the rectabgle: in this case I made it white
            # the third parameter is the position and scale of the rects in (xPos, yPos, xScale, yScale)
            pygame.draw.rect(screen, pygame.Color(255, 255, 255, 255), (pos, 75, 15, CONST.arr[i]))
            pos += 20
        
# deals with image renders in the clicking screen (base state)
# so the main animation, and click buttons are here
async def RenderImages(screen, currentFrame, currentAnim): 
    titleScreenImg = pygame.image.load(currentAnim[currentFrame]) # retrieve the image from the animation sheet
    screen.blit(titleScreenImg, (0,0)) # blit just means to render the current image at position (x, y) (in this case, its (0, 0))

    # So each button has two states: selected and unselected
    # This part is just to visually show the user which button is selected and which one isnt, since i made two diff sprites for each button
    # In this case, random and sort cant be selected at the same time
    if not CONST.canSort:
        screen.blit(CONST.randBtn, (365, 550))
        screen.blit(CONST.startSel, (610, 550))
    elif CONST.canSort:
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
            screen.blit(CONST.shopSel, (1200 // 2.5, 400))
        else:
            screen.blit(CONST.shopBtn, (1200 // 2.5, 400))
    
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
async def SideBarRender(screen):
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
            displayTxt = "{0} {1}: {2} {3}".format(CONST.shopItemCount[i], CONST.shopItems[i], CONST.shopItemPrice[i], CONST.shopItemCurrency[i])
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
    for i in range(len(CONST.shopItemCount)-1):
        if CONST.shopItemCount[i] != 0:
            CONST.sortedElements += CONST.shopItemCount[i] * ((i+1)+CONST.growthMult)

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
        randVal = int(random.random() * len(QUEST.errors))
        return randVal # so that if the return actually isnt null then the 1/5000 occured so render the error

# Error popup render when the 1 in 5000 hits
async def ErrorRender(screen, val):
    # draw.rect just draws a rectangle onto the screen, no image file required
    # the first parameter is what display the rect should be drawn to
    # the second parameter is the color of the rectabgle: in this case I made it black
    # the third parameter is the position and scale of the rects in (xPos, yPos, xScale, yScale)
    pygame.draw.rect(screen, pygame.Color(0, 0, 0, 200), (1200 // 10, 75, 1200 // 1.25, 700))
    posY = 100 # (for iterating all the question class properties posY, so they dont all render on top of each other)
    CONST.selError = QUEST.errors[val] # get the selected class for easier access cause were gonna mess with this alot
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
            await RenderImages(screen, currentFrame, CONST.settingsImgList)
            await SideBarRender(screen)
            await RenderBars(screen)
            await SimulationRender(screen)
            await ShopRender(screen)
            
            # Gameplay loops
            await MoneyGen()
            if not CONST.errorUp:
                CONST.quest = await ErrorChance()
            elif CONST.errorUp:
                await ErrorRender(screen, CONST.quest)

            pygame.display.flip() # Updates the entire screen to account for any new renders needed to be displayed
            pygame.time.wait(40) # Render loop delay (mainly so that the animation plays at a normal speed)
            await asyncio.sleep(0) # Required for async stuff or it will just crash
            currentFrame += 1
        currentFrame = 0 # Reset current frame to the start to loop animation

# The start of the simulation/game/yeah
async def Start(screen):
    await Update(screen)

# Merge sort
# its not too different from the merge sort in classes
# only modification is the ascending/descending, but thats really it
async def merge(left, right):
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
        return(list)
    else:
        left = list[:length//2]
        right = list[length//2:]
    return await merge(await sort(left), await sort(right))
    