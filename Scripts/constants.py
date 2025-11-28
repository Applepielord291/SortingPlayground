import glob
import pygame

# Nigel Garcia
# constants.py
# Many variables that needs to be accessed globally are stored here.

# Window States
currentState = 0

# Constant States
TITLE_SCREEN = 0
SETTINGS_SCREEN = 1
SIMULATION_SCREEN = 2
INFO_SCREEN = 3

#--------------------------Paths-----------------------------
debugTitle = 'Scripts/TitleScreen/*.bmp'
buildTitle = 'TitleScreen/*.bmp'

debugTrans1 = 'Scripts/Transition1/*.bmp'
buildTrans1 = 'Transition1/*.bmp'

debugTrans2 = 'Scripts/Transition2/*.bmp'
buildTrans2 = 'Transition2/*.bmp'

debugSettings = 'Scripts/SettingsScreen/*.bmp'
buildSettings = 'SettingsScreen/*.bmp'

#Sprites
debugDropDown = 'Scripts/Sprites/DropDown.png'
buildDropDown = 'Sprites/DropDown.png'

debugSizeBtn = 'Scripts/Sprites/SizeBtn.png'
buildSizeBtn = 'Sprites/SizeBtn.png'

debugSizeSelect = 'Scripts/Sprites/SizeSelect.png'
buildSizeSelect = 'Sprites/SizeSelect.png'

debugOrderBtn = 'Scripts/Sprites/OrderBtn.png'
buildOrderBtn = 'Sprites/OrderBtn.png'

debugOrderSelect = 'Scripts/Sprites/OrderSelect.png'
buildOrderSelect = 'Sprites/OrderSelect.png'

debugRandBtn = 'Scripts/Sprites/RandomBtn.png'
buildRandBtn = 'Sprites/RandomBtn.png'

debugRandSelect = 'Scripts/Sprites/RandomSelect.png'
buildRandSelect = 'Sprites/RandomSelect.png'

debugStartBtn = 'Scripts/Sprites/StartBtn.png'
buildStartBtn = 'Sprites/StartBtn.png'

debugStartSelect = 'Scripts/Sprites/StartSelect.png'
buildStartSelect = 'Sprites/StartSelect.png'

#--------------------------Images-----------------------------
titleScreenImgList = []
for image in glob.glob(debugTitle):
    titleScreenImgList.append(image)
titleScreenImgList.sort()

transitionImgList1 = []
for image in glob.glob(debugTrans1):
    transitionImgList1.append(image)
transitionImgList1.sort()

transitionImgList2 = []
for image in glob.glob(debugTrans2):
    transitionImgList2.append(image)
transitionImgList2.sort()

settingsImgList = []
for image in glob.glob(debugSettings):
    settingsImgList.append(image)
settingsImgList.sort()

#--------------------------Simulation Images-----------------------------
dropDown = pygame.image.load(debugDropDown)
sizeBtn = pygame.image.load(debugSizeBtn)
orderBtn = pygame.image.load(debugOrderBtn)
randBtn = pygame.image.load(debugRandBtn)
startBtn = pygame.image.load(debugStartBtn)

sizeSel = pygame.image.load(debugSizeSelect)
orderSel = pygame.image.load(debugOrderSelect)
randSel = pygame.image.load(debugRandSelect)
startSel = pygame.image.load(debugStartSelect)

#--------------------------Simulation States-----------------------------
menuOpen = False

#--------------------------Menu button States----------------------------

CHANGE_SIZE = 1
CHANGE_DIR = 2
SELECT_RAND = 3
SELECT_START = 4
curBtn = CHANGE_SIZE
AscOrDesc = True # True is ascending, False is descending
RenderInput = False
pickMaxVal = False
pickMaxElem = False

#----------------------------List------------------------------------------

length = 6
maxVal = 300
arr = [0] * length

# Debugging bool
x = False

#------------------------------------text------------------------------------
pygame.font.init()
font = pygame.font.SysFont('timesnewroman', 30)