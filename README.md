**Algorithm picked: Merge Sorting Algorithm.**
    **Why?** --> It is the most consistent and fast algorithm, having a worst/average/best time complexity of O(nlogn), and is used
    as the standard in various industries (or so ive heard). Having a fundamental understanding of this algorithm means you understand an algorithm that actually has useful 
    applications (not like bubble sort).

    ## Since my game is inspired by cookie clicker, Idle games like these need a fast way to generate currency (in this case, its Sorted elements (SE)), and merge sort is one of the quickest and the most consistent (out of the main ones), which makes it perfect for a game like this.

**Demo videos and screenshots are on the deployed project link**
### **All code can be found in Scripts folder**

**Computational Thinking**

    Decomposition: Since almost everything is called in an update loop that as long as the program is up, seperate everything into smaller functions
        Things such as:
            - User Inputs (from the keyboard)
            - Program renders background animation, buttons, sorting bars all rendered in a certain order (each have their own function)
            - More specific inputs (like is the user is in the list modification menu/the shop menu, all have thier own functions)
            etc ...

    Pattern Recognition: Reaches values through a script that holds many global variables. Throughout many of the programs processes, it will be referring to these
        global variables and working with/around them.

    Abstraction: The process of merge sort can be toggled on/off through a menu that the user can open with keyboard inputs. Pretty much show whats necessary for 
        displaying the sort (like the unsorted --> sorted list), pre-rendered animations and pixel art to make the UI more visually pleasing, as well as 
        rendering the buttons/sliders to let the user know what values they're modifying and how they're modifying it.

    Algorithm Design: Input is done in various ways,
        - Buttons
        - Dropdown menus
        - Sliders
        These values are stored in a global avariables script as reference for the processing parts of the program
        as for processing, essentially just referring back to those global variables in the global variable script and executing the processes around/with those values.
        output is done through drawing rectangles on the screen (the sorting bars), general idea is just rendering menus and the actual algorithm with premade renders or 
        pygames drawing system. 

    Flow Charts:
        check FlowChartFolder
**OPEN THE FLOWCHARTS IN A NEW TAB, THEY'RE MASSIVE**
        
**Steps to run:**
    Go to my itch.io link
    Click "RUN GAME"

**If you want to run the project through the Scripts instead:**

    Install the Scripts folder

    create a virtual environment

    Install pygame

    Install pygbag


    To run it: Run the main.py file

    If you want to make a build of it: Go into the terminal, and type in "pygbag Scripts"

**Deployed Project link:**
    https://applepielord291.itch.io/idle-merge-sort

**Github Link**
    https://github.com/Applepielord291/SortingPlayground

**Testing and verification**
### test video here: (5 minutes): https://youtu.be/rJjj3ZRxtQs?si=7k7QcQs5_AgusBQU
### as for the images, theres 4, and posted on the deployed link.
### Testing and verification can be viewed here: https://applepielord291.itch.io/idle-merge-sort/devlog/1134689/the-first-and-only-update
### but for clarity, it will also be below.

Idle merge Sort Changes and Features:
- Added a new button to the menu: the Modify button. This allows you to do the following:
    1. Change the sort order
    2. Change the max value
    3. Change the minimum value
    4. Enable Education mode
    1, 2, and 3 are purely cosmetic and for messing around with the merge sort algorithm

- added a new mode, education mode
    - Enable it in the modify menu
    - when enabled, you can view the step-by-step process for merge sort
    - after the showcase, you can still get sorted elements (SE) from it
    - and if you purchased upgrades, SE can generate in the background during the showcase!
The whole point of this project was to be educational, without these features it felt more as a standard idle game with a foreign algorithm, which is why I decided to add these.

- increased the max number of elements in a list from 58 --> 100000
    - Before, the bars wouldn't dynamically scale with how long the list was, so a temporary work around was to keep the limit low. However, keeping it low would limit how much you could mess around with the algorithm, and gameplay wise, would make manually sorting elements completely redundant as early as mid-game. 

- Because of this max list length change, I decided to decrease the price increase of elements from 200 TS --> 20 TS

- Decided to add a song I made for fun (made with LMMS), and a sound effect for clicking (with a phone and a pen)

Bug fixes, Quality of life, and clarity:

- Fixed list bars going off-screen for very specific list-lengths (fixed by just rounding down the width instead of rounding up, then setting the width = 1 if its 0)
- Fixed tutorial being too broad, not explaining enough
- Changed some UI positioning to make it more readable for users
- Fixed education mode UI and text loading off screen and being too fast to read 
- Removed one of the error messages for being too large
- Resized error popup text so that users dont have to squint reading it
- Added some small pixel art in the shop screen
- Fixed min/max value going into the negatives/above 400 when user fast increments/decrements the values (Just added some extra if statements after value changes to check if its in their bounds or not)
- Fixed an issue with upgrades not generating SE properly (e.g. having 5 on one upgrade was only the equivalent of 1, having 100 of an upgrade was still only the equivalent of having 1, turns out it was an issue with my formula for calculating the rate).
- changed the price increase on upgrades from //= 0.95 to //= 0.85
- Not really a huge one, but before all the shop info was being stored in multiple different arrays, finally moved it all into a class
- fixed the stats bar displaying weirder: now its separated into two lines and actually centered.

**Credits:**
### Code written entirely by me (NO AI, only pygame documentation)
### 3D renders (in blender), and pixel art (in pixilart) made by me
### Music made by me (using LMMS)
### Sound effects made by me (using a phone)




