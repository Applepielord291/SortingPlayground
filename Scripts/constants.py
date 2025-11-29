import glob
import pygame

# Nigel Garcia
# constants.py
# Many variables that needs to be accessed globally are stored here.

# Window States


# Constant States
CLICK_SCREEN = 0
MENU_SCREEN = 1
SHOP_SCREEN = 2

currentState = CLICK_SCREEN

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

debugMaxBtn = 'Scripts/Sprites/MaxValBtn.png'
buildMaxBtn = 'Sprites/MaxValBtn.png'

debugMaxSelect = 'Scripts/Sprites/MaxValSelect.png'
buildMaxSelect = 'Sprites/MaxValSelect.png'

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

debugShopBtn = 'Scripts/Sprites/ShopBtn.png'
buildShopBtn = 'Sprites/ShopBtn.png'

debugShopSel = 'Scripts/Sprites/ShopSel.png'
buildShopSel = 'Sprites/ShopSel.png'

debugArrowSel = 'Scripts/Sprites/ArrowSelect.png'
buildArrowSel = 'Sprites/ArrowSelect.png'

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

shopArrowSel = pygame.image.load(debugArrowSel)

sizeBtn = pygame.image.load(debugSizeBtn)
maxBtn = pygame.image.load(debugMaxBtn)
orderBtn = pygame.image.load(debugOrderBtn)
randBtn = pygame.image.load(debugRandBtn)
startBtn = pygame.image.load(debugStartBtn)
shopBtn = pygame.image.load(debugShopBtn)

sizeSel = pygame.image.load(debugSizeSelect)
maxSel = pygame.image.load(debugMaxSelect)
orderSel = pygame.image.load(debugOrderSelect)
randSel = pygame.image.load(debugRandSelect)
startSel = pygame.image.load(debugStartSelect)
shopSel = pygame.image.load(debugShopSel)

#--------------------------Simulation States-----------------------------
menuOpen = False

#--------------------------Menu button States----------------------------

CHANGE_SIZE = 1
CHANGE_MAX = 2
CHANGE_DIR = 3
SHOP_SEL = 4
curBtn = CHANGE_SIZE
AscOrDesc = True # True is ascending, False is descending
RenderInput = False
pickMaxVal = False
pickMaxElem = False
shopOpen = False

#----------------------------List------------------------------------------

length = 3
maxVal = 300
arr = [0] * length

canSort = False

#------------------------------------text------------------------------------
pygame.font.init()
font = pygame.font.SysFont('timesnewroman', 24)

#----------------------------game variables------------------------------------
timesSorted = 0
sortedElements = 0

shopItems = ["MergeSort Script", 
             "MergeSort School",
             "MergeSort Factory",
             "MergeSort Fractal",
             "MergeSort Portal",
             "MergeSort Universe",
             "SuperComputer",
             "Elements"]

shopItemCount = [0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0,
                 0]

shopItemPrice = [500,
                 2500,
                 10000,
                 50000,
                 100000,
                 1000000,
                 1500000,
                 25]

shopItemCurrency = ["SE",
                    "SE",
                    "SE",
                    "SE",
                    "SE",
                    "SE",
                    "SE",
                    "TS"]


SCRIPT = 0
SCHOOL = 1
FACTORY = 2
FRACTAL = 3
PORTAL = 4
UNIVERSE = 5
SUPERCOMPUTER = 6
ELEMENT = 7
BACK = 8
curShopSel = BACK