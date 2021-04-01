import pygame
import random
import array
import sys
import os


#Set things
while True:

    WIDTH = 1280
    gridcalcx = 1152
    gridcalcy = 648
    printedmap = False
    HEIGHT = 720
    TILESIZE = 20
    zoom = 1
    pressed_down = False
    pressed_up = False
    pressed_left = False
    pressed_right = False
    x_speed = 6
    y_speed = 6
    GRIDWIDTH = int((gridcalcx / TILESIZE))
    GRIDHEIGHT = int((gridcalcy / TILESIZE))
    display = pygame.Surface((int(WIDTH), int(HEIGHT)))
    GRID = []
    for i in range(GRIDHEIGHT):
        GRID.append([0] * GRIDWIDTH)
    RED = (255,0,0)
    PURPLE = (128,0,128)
    YELLOW = (250,218,94)
    WHITE = (255,255,255)
    GREEN = (46,139,87)
    BROWN = (176,140,108)
    cube_gposX = []
    cube_gposY = []
    #walkers = int(input("\n \n \n \nNumber of Walkers[8] : ") or 8 )
    #steps = int(input("Number of Steps[150] : ") or 150)
    walkers = int(8)
    steps = int(150)

    for x in range(walkers):
        cube_gposX.append(GRIDWIDTH / 2 + random.randint(-2, 2))
        cube_gposY.append(GRIDHEIGHT / 2 + random.randint(-2, 2))
    GEN_LIMIT = steps
    generated = False
    floormarkerX = array.array("i")
    floormarkerY = array.array("i")


    #init
    pygame.init()
    clock = pygame.time.Clock()
    #set screem
    screen = pygame.display.set_mode((int(WIDTH),int(HEIGHT)),pygame.RESIZABLE)
    w, h = pygame.display.get_surface().get_size()
    playercorx = w / 2
    playercory = h / 2

    running = True

    #Icon + title
    pygame.display.set_caption("Window")

    #Set images
    empty = pygame.image.load("empty.png")
    wall = pygame.image.load("Wall.png")
    Ground1 = pygame.image.load("Ground1.png")
    fwall = pygame.image.load("FloorWall.png")
    #def thimgs
    def walkers(index):
        #pygame.draw.rect(screen,WHITE,(cube_gposX[index] * TILESIZE,cube_gposY[index] * TILESIZE,TILESIZE,TILESIZE))
        floormarkerX.append(int(cube_gposX[index]))
        floormarkerY.append(int(cube_gposY[index]))
        count = 0
        for x in range(0,len(floormarkerX)):
            try:
                GRID[floormarkerY[x]][floormarkerX[x]] = 1
            except IndexError:
                pass


    def printgrid():
        for x in range(0,WIDTH,TILESIZE):
            pygame.draw.line(screen,WHITE,(x,0),(x,HEIGHT))

        for y in range(0,HEIGHT,TILESIZE):
            pygame.draw.line(screen,WHITE,(0,y),(WIDTH,y))



    def random_walk():

        global cube_gposX
        global cube_gposY
        global generated

        for x in range(0, len(cube_gposX)):

            DOWN = cube_gposY[x] + 1
            UP = cube_gposY[x] - 1
            LEFT = cube_gposX[x] - 1
            RIGHT = cube_gposX[x] + 1
            select_dir = random.random()
            if generated == False:

                if select_dir > 0 and select_dir < 0.25:

                    if cube_gposX[x] <= 1:
                        pass
                    else:
                        cube_gposX[x] = LEFT

                if select_dir > 0.26 and select_dir < 0.5:

                    if cube_gposX[x] >= GRIDWIDTH - 1:
                        pass
                    else:
                        cube_gposX[x] = RIGHT

                if select_dir > 0.51 and select_dir < 0.75:

                    if cube_gposY[x] == GRIDHEIGHT - 2:
                        pass
                    else:
                        cube_gposY[x] = DOWN

                if select_dir > 0.76 and select_dir < 1:

                    if cube_gposY[x] == 2:
                        pass
                    else:
                        cube_gposY[x] = UP

    def borders():
        for j in range(0, len(GRID)):
            for u in range(len(GRID[j])):
                    if  GRID[j][u] == 1:
                        try:
                            if GRID[j][u+1] == 0:
                                GRID[j][u+1] = 2
                        except IndexError:
                            GRID[j][u] = 2
                        try:
                            if GRID[j][u-1] == 0:
                                GRID[j][u-1] = 2
                        except IndexError:
                            GRID[j][u] = 2
                        try:
                            if GRID[j+1][u] == 0:
                                GRID[j+1][u] = 2
                        except IndexError:
                            GRID[j][u] = 2
                        try:
                            if GRID[j-1][u] == 0:
                                GRID[j-1][u] = 2
                        except IndexError:
                            GRID[j][u] = 2
                        try:
                            if GRID[0][u] == 2:
                                GRID[0][u] = 2

                            if GRID[GRIDHEIGHT][u] == 2:
                                GRID[GRIDHEIGHT][u] = 2

                            if GRID[j][0] == 2:
                                GRID[j][0] = 2

                            if GRID[j][GRIDWIDTH - 1] == 2:
                                GRID[j][GRIDWIDTH - 1] = 2
                        except IndexError:
                            pass

                        if GRID[j][u] == 2:
                            try:
                                if GRID[j][u+1] == 1 and GRID[j][u-1] == 1 and GRID[j+1][u] == 1 and GRID[j-1][u] == 1:
                                    GRID[j][u] = 1
                            except IndexError:
                                GRID[j][u] = 2


    def drawfromgrid():
        for j in range(0, len(GRID)):
            for u in range(len(GRID[j])):
                if GRID[j][u] == 1:

                    pygame.Surface.blit(display,Ground1,(u * TILESIZE,j * TILESIZE))
                elif GRID[j][u] == 2:

                    pygame.Surface.blit(display,wall,(u * TILESIZE,j * TILESIZE))
                elif GRID[j][u] == 0:

                    pygame.draw.rect(display,BROWN,(u * TILESIZE,j * TILESIZE,TILESIZE,TILESIZE))
                else:

                    pygame.draw.rect(display,BROWN,(u * TILESIZE,j * TILESIZE,TILESIZE,TILESIZE))
                try:
                    if GRID[j-1][u] == 2 and GRID[j][u] == 1:

                        pygame.Surface.blit(display,fwall,(u * TILESIZE-1,j * TILESIZE))
                    if GRID[j][u] == 2 and GRID[j][u-1] == 1:

                        pygame.draw.line(display, BROWN, (u * TILESIZE-1 , j * TILESIZE), (u * TILESIZE - 1, j * TILESIZE + TILESIZE))
                    if GRID[j][u] == 2 and GRID[j][u+1] == 1:

                        pygame.draw.line(display, BROWN, (u * TILESIZE + TILESIZE - 1 , j * TILESIZE), (u * TILESIZE  + TILESIZE - 1, j * TILESIZE + TILESIZE))
                except IndexError:
                    pass


    #game loop
    while running == True:
        fps = str(int(clock.get_fps()))
        display.fill(BROWN)
    #    printgrid()
        random_walk()

        for x in range(0, len(cube_gposX)):
            walkers(x)
        if GEN_LIMIT == 0:
            generated = True
            borders()

            if printedmap == False:
                for i in range(GRIDHEIGHT):
                    print(GRID[i])
                    pass


            printedmap = True
        GEN_LIMIT -= 1

        if generated == True:
            drawfromgrid()


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

                if event.key == pygame.K_ESCAPE:
                    sys.exit()


        screen.blit(pygame.transform.scale(display, screen.get_rect().size), (0, 0))
        #screen.blit(display,(0,0))
        pygame.display.update()
