import glob
import pygame
from pygame import mixer

# NO AI USED, only documentation, and code examples in their documentation
# Documentation used:
#   https://www.pygame.org/docs/

# Nigel Garcia
# constants.py
# Many variables that needs to be accessed globally are stored here.

#----------------------SIMULATION STATES--------------------------------
CLICK_SCREEN = 0
MENU_SCREEN = 1
SHOP_SCREEN = 2
ERROR_SCREEN = 3
RESULT_SCREEN = 4
MODIFY_SCREEN = 5

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

# Sprites
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

debugModBtn = 'Scripts/Sprites/ModBtn.png'
buildModBtn = 'Sprites/ModBtn.png'

debugModSel = 'Scripts/Sprites/ModSelect.png'
buildModSel = 'Sprites/ModSelect.png'

debugArrowSel = 'Scripts/Sprites/ArrowSelect.png'
buildArrowSel = 'Sprites/ArrowSelect.png'

debugShopTitle = 'Scripts/Sprites/ShopTitle.png'
buildShopTitle = 'Sprites/ShopTitle.png'

# music
debugSong = 'Scripts/Music/IdleMergeBG.ogg'
buildSong = 'Music/IdleMergeBG.ogg'

debugClickSound = 'Scripts/Music/ClickSound.ogg'
buildClickSound = 'Music/ClickSound.ogg'

#--------------------------ANIMATIONS-----------------------------
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
shopTitle = pygame.image.load(debugShopTitle)

randBtn = pygame.image.load(debugRandBtn)
startBtn = pygame.image.load(debugStartBtn)
shopBtn = pygame.image.load(debugShopBtn)
readyBtn = pygame.image.load(debugReadyBtn)
modBtn = pygame.image.load(debugModBtn)

randSel = pygame.image.load(debugRandSelect)
startSel = pygame.image.load(debugStartSelect)
shopSel = pygame.image.load(debugShopSel)
modSel = pygame.image.load(debugModSel)

#---------------------------MUSIC-------------------------------------------------
mixer.init()
mixer.music.load(debugSong)
click = pygame.mixer.Sound(debugClickSound)

mixer.music.set_volume(0.3)
click.set_volume(0.05)

mixer.music.play(-1)

#--------------------------Menu button States----------------------------
menuOpen = False
SHOP_SEL = 0
MODIFY_SEL = 1
curBtn = SHOP_SEL


#---------------------LIST MODIFICATION SELECTION-------------------------------
ORDER = 0
MAXIMUM = 1
MINIMUM = 2
EDUCATION = 3

curMod = ORDER

modOpen = False

AscOrDesc = True # True is ascending, False is descending

#-----------------------UPGRADE SHOP SELECTION-----------------------------------   
shopOpen = False

ELEMENT = 0
SCRIPT = 1
SCHOOL = 2
FACTORY = 3
FRACTAL = 4
PORTAL = 5
UNIVERSE = 6
SUPERCOMPUTER = 7

curShopSel = SCRIPT

class ShopItem:
    name = ""
    count = 0
    upgradePrice = 0
    currencyType = ""
    def __init__(self, name, count, upgradePrice, currencyType):
        self.name = name
        self.count = count
        self.upgradePrice = upgradePrice
        self.currencyType = currencyType

mergeSortScript = ShopItem("MergeSort Scripts", 0, 500, "SE")
mergeSortSchool = ShopItem("MergeSort School", 0, 2500, "SE")
mergeSortFactory = ShopItem("MergeSort Factories", 0, 10000, "SE")
mergeSortFractal = ShopItem("MergeSort Fractals", 0, 50000, "SE")
mergeSortPortal = ShopItem("MergeSort Portals", 0, 100000, "SE")
mergeSortUniverse = ShopItem("MergeSort Universes", 0, 1000000, "SE")
mergeSortComputer = ShopItem("SuperComputers", 0, 5000000, "SE")
mergeSortElements = ShopItem("Increase Elements", 0, 25, "TS")

shopItems = [mergeSortElements, mergeSortScript, mergeSortSchool, mergeSortFactory, mergeSortFractal, mergeSortPortal, mergeSortUniverse, mergeSortComputer]


#----------------------------LIST UPGRADES/MODIFICATIONS------------------------------------------
length = 3
MAX_LENGTH = 100000
maxVal = 300
minVal = 0
arr = [0] * length

canSort = False

#------------------------------------FONTS------------------------------------
pygame.font.init()
font = pygame.font.SysFont('freesansbold', 24)
errorFont = pygame.font.SysFont('freesansbold', 15)

#----------------------------CURRENCY------------------------------------
timesSorted = 0
sortedElements = 0

#---------------------------ERROR POPUP-----------------------------------
# refer to questions.py
errorUp = False
selAns = 0
selError = None
quest = 0
correct = False

growthMult = 1

class Question:
    question = ""
    codeSnippet = ""
    answers = []
    correctAnswer = 0
    def __init__(self, question, codeSnippet, answers, correctAnswer):
        self.question = question
        self.codeSnippet = codeSnippet
        self.answers = answers
        self.correctAnswer = correctAnswer

mergeSort=[ "1  def merge(firstHalf, secondHalf):",
            "2     finalList = []",
            "3     i, j = 0",
            "4     while i < len(firstHalf) and j < len(secondHalf):",
            "5         if firstHalf[i] <= secondHalf[j]:",
            "6             finalList.append(firstHalf[i])",
            "7             i += 1",
            "8         else:",
            "9             finalList.append(secondHalf[j])",
            "10            j += 1",
            "11    while i < len(firstHalf):",
            "12        finalList.append(firstHalf[i])",
            "13        i += 1",
            "14    while j < len(secondHalf):",
            "15        finalList.append(secondHalf[j])",
            "16        j += 1",
            "17    return finalList",
            "18 def sort(list):",
            "19    length = len(list)",
            "20    if length < 2:",
            "21        return list",
            "22    else:",
            "23        firstHalf = list[:length//2]",
            "24        secondHalf = list[length//2:]",
            "25    return merge(sort(firstHalf), sort(secondHalf))" ]
errorsor3=[ "1  def merge(firstHalf, secondHalf):",
            "2     finalList = firstHalf + secondHalf",
            "3     i, j = 0",
            "4     while i < len(firstHalf) and j < len(secondHalf):",
            "5         if firstHalf[i] <= secondHalf[j]:",
            "6             finalList.append(firstHalf[i])",
            "7             i += 1",
            "8         else:",
            "9             finalList.append(secondHalf[j])",
            "10            j += 1",
            "11    while i < len(firstHalf):",
            "12        finalList.append(firstHalf[i])",
            "13        i += 1",
            "14    while j < len(secondHalf):",
            "15        finalList.append(secondHalf[j])",
            "16        j += 1",
            "17    return finalList"]
errorsor5=[ "1  def merge(firstHalf, secondHalf):",
            "2     finalList = []",
            "3     i, j = 0",
            "4     while i < len(firstHalf) and j < len(secondHalf):",
            "5         if firstHalf[i] >= secondHalf[j]:",
            "6             finalList.append(firstHalf[i])",
            "7             i += 1",
            "8         else:",
            "9             finalList.append(secondHalf[j])",
            "10            j += 1",
            "11    while i < len(firstHalf):",
            "12       finalList.append(firstHalf[i])",
            "13       i += 1",
            "14    while j < len(secondHalf):",
            "15        finalList.append(secondHalf[j])",
            "16        j += 1",
            "17    return finalList",
            "18 def sort(list):",
            "19    length = len(list)",
            "20    if length < 2:",
            "21        return list",
            "22    else:",
            "23        firstHalf = list[:length//2]",
            "24        secondHalf = list[length//2:]",
            "25    return merge(sort(firstHalf), sort(secondHalf))" ]
errorsor6=[ "18 def sort(list):",
            "19    length = len(list)",
            "20    if length < 2:",
            "21        return list",
            "22    else:",
            "23        firstHalf = list[:length//2]",
            "24        secondHalf = list[length//2:]",
            "25    return merge(firstHalf, secondHalf)" ]

error1 = Question("Merge Sort worst case TIME complexity", mergeSort, ["O(logn)", "O(nlogn)", "O(n)", "O(n^2)"], 1)
error2 = Question("Merge Sort SPACE complexity", mergeSort, ["O(logn)", "O(nlogn)", "O(n)", "O(n^2)"], 2)
error3 = Question("Identify the error:", errorsor3, ["Line 1", "Line 4", "Line 5", "Line 2"], 3)
error4 = Question("Change one line to make this ascending:", mergeSort, ["Line 11", "Line 5", "Line 25", "Line 4"], 1)
error5 = Question("Change one line to make this descending:", errorsor5, ["Line 11", "Line 5", "Line 25", "Line 4"], 1)
error6 = Question("Identify the error:", errorsor6, ["Line 20", "Line 24", "Line 25", "Line 23"], 2)

errors = [error1, error2, error3, error4, error5, error6]

#------------------------EDUCATION MODE------------------------------------
eduMode = False

displayMerge1 = ["18 def sort(list):",
                 "19    length = len(list)",
                 "20    if length < 2:",
                 "21        return list",
                 "22    else:",
                 "23        firstHalf = list[:length//2]",
                 "24        secondHalf = list[length//2:]"]
displayMerge2 = ["1  def merge(firstHalf, secondHalf):",
                 "2     finalList = []",
                 "3     i, j = 0",
                 "4     while i < len(firstHalf) and j < len(secondHalf):",
                 "5         if firstHalf[i] <= secondHalf[j]:",
                 "6             finalList.append(firstHalf[i])",
                 "7             i += 1",
                 "8         else:",
                 "9             finalList.append(secondHalf[j])",
                 "10            j += 1"]
displayMerge3 = ["11    while i < len(firstHalf):",
                 "12        finalList.append(firstHalf[i])",
                 "13        i += 1"]
displayMerge4 = ["14    while j < len(secondHalf):",
                 "15        finalList.append(secondHalf[j])",
                 "16        j += 1",
                 "17    return finalList"]
