import glob
import pygame

# Nigel Garcia
# constants.py
# Many variables that needs to be accessed globally are stored here.

# Constant States
CLICK_SCREEN = 0
MENU_SCREEN = 1
SHOP_SCREEN = 2
ERROR_SCREEN = 3
RESULT_SCREEN = 4

currentState = CLICK_SCREEN
prevState = CLICK_SCREEN

#--------------------------Paths-----------------------------
debugTitle = 'Scripts/TitleScreen/*.jpg'
buildTitle = 'TitleScreen/*.jpg'

debugTrans1 = 'Scripts/Transition1/*.jpg'
buildTrans1 = 'Transition1/*.jpg'

debugTrans2 = 'Scripts/Transition2/*.jpg'
buildTrans2 = 'Transition2/*.jpg'

debugSettings = 'Scripts/SettingsScreen/*.jpg'
buildSettings = 'SettingsScreen/*.jpg'

#Sprites
debugDropDown = 'Scripts/Sprites/DropDown.png'
buildDropDown = 'Sprites/DropDown.png'

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

debugReadyBtn = 'Scripts/Sprites/ReadyBtn.png'
buildReadyBtn = 'Sprites/ReadyBtn.png'

debugShopSel = 'Scripts/Sprites/ShopSel.png'
buildShopSel = 'Sprites/ShopSel.png'

debugArrowSel = 'Scripts/Sprites/ArrowSelect.png'
buildArrowSel = 'Sprites/ArrowSelect.png'

debugShopTitle = 'Scripts/Sprites/ShopTitle.png'
buildShopTitle = 'Sprites/ShopTitle.png'

#--------------------------Images-----------------------------
titleScreenImgList = []
for image in glob.glob(buildTitle):
    titleScreenImgList.append(image)
titleScreenImgList.sort()

transitionImgList1 = []
for image in glob.glob(buildTrans1):
    transitionImgList1.append(image)
transitionImgList1.sort()

transitionImgList2 = []
for image in glob.glob(buildTrans2):
    transitionImgList2.append(image)
transitionImgList2.sort()

settingsImgList = []
for image in glob.glob(buildSettings):
    settingsImgList.append(image)
settingsImgList.sort()

#--------------------------Simulation Images-----------------------------
dropDown = pygame.image.load(buildDropDown)

shopArrowSel = pygame.image.load(buildArrowSel)
shopTitle = pygame.image.load(buildShopTitle)

randBtn = pygame.image.load(buildRandBtn)
startBtn = pygame.image.load(buildStartBtn)
shopBtn = pygame.image.load(buildShopBtn)
readyBtn = pygame.image.load(buildReadyBtn)

randSel = pygame.image.load(buildRandSelect)
startSel = pygame.image.load(buildStartSelect)
shopSel = pygame.image.load(buildShopSel)

#--------------------------Simulation States-----------------------------
menuOpen = False

#--------------------------Menu button States----------------------------
SHOP_SEL = 0
curBtn = SHOP_SEL
AscOrDesc = True # True is ascending, False is descending
RenderInput = False
pickMaxVal = False
pickMaxElem = False
shopOpen = False

#----------------------------List------------------------------------------

length = 3
MAX_LENGTH = 58
maxVal = 300
arr = [0] * length

canSort = False

#------------------------------------text------------------------------------
pygame.font.init()
font = pygame.font.SysFont('freesansbold', 24)
errorFont = pygame.font.SysFont('freesansbold', 15)

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
curShopSel = SCRIPT

errorUp = False
selAns = 0
selError = None
quest = 0
correct = False

growthMult = 1