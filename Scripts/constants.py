import glob

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

#--------------------------Images-----------------------------
titleScreenImgList = []
for image in glob.glob(debugTitle):
    titleScreenImgList.append(image)
titleScreenImgList.sort()

transitionImgList1 = []
for image in glob.glob(debugTrans1):
    transitionImgList1.append(image)
transitionImgList1.sort()