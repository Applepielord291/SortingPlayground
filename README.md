**Algorithm picked: Merge Sorting Algorithm**
    **Why?** --> It is the most consistent and fast algorithm, having a worst/average/best time complexity of O(nlogn), and is used
    as the standard in various industries (or so ive heard). Having a fundamental understanding of this algorithm means you understand an algorithm that actually has useful 
    applications (not like bubble sort).

    ## Since my game is inspired by cookie clicker, Idle games like these need a fast way to generate currency (in this case, its Sorted elements (SE)), and merge sort is one of the quickest and the most consistent (out of the main ones)

**Demo videos and screenshots are on the deployed project link**
**All code can be found in Scripts/**

**Computational Thinking**

    ## Decomposition: Since almost everything is called in an update loop that as long as the program is up, seperate everything into smaller functions
        Things such as:
            - User Inputs (from the keyboard)
            - Program renders background animation, buttons, sorting bars all rendered in a certain order (each have their own function)
            - More specific inputs (like is the user is in the list modification menu/the shop menu, all have thier own functions)
            etc ...

    ## Pattern Recognition: Reaches values through a script that holds many global variables. Throughout many of the programs processes, it will be referring to these
        global variables and working with/around them.

    ## Abstraction: The process of merge sort can be toggled on/off through a menu that the user can open with keyboard inputs. Pretty much show whats necessary for 
        displaying the sort (like the unsorted --> sorted list), pre-rendered animations and pixel art to make the UI more visually pleasing, as well as 
        rendering the buttons/sliders to let the user know what values they're modifying and how they're modifying it.

    ## Algorithm Design: Input is done in various ways,
        - Buttons
        - Dropdown menus
        - Sliders
        These values are stored in a global avariables script as reference for the processing parts of the program
        as for processing, essentially just referring back to those global variables in the global variable script and executing the processes around/with those values.
        output is done through drawing rectangles on the screen (the sorting bars), general idea is just rendering menus and the actual algorithm with premade renders or 
        pygames drawing system. 

    ## Flow Chart:
        check FlowChartFolder
        **OPEN THE IMAGE IN A NEW TAB, THEY'RE MASSIVE**
        
**Steps to run:**
    Go to my itch.io link
    Click "RUN GAME"

**Deployed Project link:**
    https://applepielord291.itch.io/idle-merge-sort

**Github Link**
    https://github.com/Applepielord291/SortingPlayground

**Credits:**
    Code written entirely by me (NO AI, only pygame documentation)
    3D renders (in blender), and pixel art (in pixilart) made by me
    Music made by me (using LMMS)
    Sound effects made by me (using a phone)




