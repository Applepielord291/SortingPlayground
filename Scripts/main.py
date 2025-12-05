import pygame
import asyncio
from pygame.locals import *

# NO AI USED, only documentation, and code examples in their documentation
# Documentation used:
#   https://www.pygame.org/docs/

# Nigel Garcia
# main.py
# Main script, run this to run the program.
# This is the title screen, the start of the program.

# it goes: main.py --> tutorial.py --> simulation.py
# questions.py and constants.py are global variables/classes stored in there for convenience

# Also im going to be copy-pasting the same comments alot throughout all the scripts, just for clarity.

# Throughout all these scripts, you're gonna see functions defined with "async def" and functions called with "await function()"
# A library im using (pygbag), allows web builds of pygame applications, which is what im using
# however, since this programs gonna be on the web, it needs something like async IO to handle the high-performance stuff on the web
# Thus the async and the awaits.

# Other Scripts 
import constants as CONST
import tutorial as TRANSITION

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
    if keystate[pygame.K_SPACE]:
        await TRANSITION.Start(screen)

# renders the animation frames on screen, called in the update loop
async def RenderImages(screen, currentFrame): 
    titleScreenImg = pygame.image.load(CONST.titleScreenImgList[currentFrame]) # retrieve the image from the animation sheet
    screen.blit(titleScreenImg,(0,0)) # blit just means to render the current image at position (x, y) (in this case, its (0, 0))

# The update loop
async def Update(screen):
    # animation frames
    currentFrame = 0
    endFrame = len(CONST.titleScreenImgList)   

    # Render loop
    while True:
        while currentFrame < endFrame: 
            await Inputs(screen) 
            await RenderImages(screen, currentFrame)

            pygame.display.flip() # Updates the entire screen to account for any new renders needed to be displayed
            pygame.time.wait(30) # Render loop delay (mainly so that the animation plays at a normal speed)
            await asyncio.sleep(0) # Required for async stuff or it will just crash
            currentFrame += 1
        currentFrame = 0 # Reset current frame to the start to loop animation

# START OF THE PROGRAM
async def main():
    pygame.init() # always needs to be initialized so it can actually be used
    pygame.display.set_caption('Merge Sort Simulation') # Window title (also the tab name on the web)
    display = (1200, 800)
    screen = pygame.display.set_mode(display) # initializes the display window with whatever size
    await Update(screen)

if __name__ == "__main__":
    asyncio.run(main())