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

debugDropDown = 'Scripts/Sprites/DropDown.png'
buildDropDown = 'Sprites/DropDown.png'

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

#--------------------------Simulation States-----------------------------
menuOpen = False