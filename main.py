import pygame
import random
import array
import sys


#Set things
while True:
    WIDTH = 1216
    printedmap = False
    HEIGHT = 720
    TILESIZE = 32
    GRIDWIDTH = int(WIDTH / TILESIZE)
    GRIDHEIGHT = int(HEIGHT / TILESIZE)
    GRID = []
    for i in range(GRIDHEIGHT):
        GRID.append([0] * GRIDWIDTH)

    WHITE = (255,255,255)
    RED = (255,0,0)
    cube_gposX = []
    cube_gposY = []
    walkers = int(input("\n \n \n \nNumber of Walkers[4] : ") or 4 )
    steps = int(input("Number of Steps[90] : ") or 90)
    for x in range(walkers):
        cube_gposX.append(GRIDWIDTH / 2)
        cube_gposY.append(GRIDHEIGHT / 2)
    GEN_LIMIT = steps
    generated = False
    floormarkerX = array.array("i")
    floormarkerY = array.array("i")
    #initº1º1
    pygame.init()
    clock = pygame.time.Clock()
    #set screem
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    running = True

    #Icon + title
    pygame.display.set_caption("Window")

    #Set images
    testCube_img = pygame.image.load("empty.png")

    #def thimgs
    def walkers(index):
        screen.blit(testCube_img,(cube_gposX[index] * TILESIZE,cube_gposY[index] * TILESIZE))
        floormarkerX.append(int(cube_gposX[index]))
        floormarkerY.append(int(cube_gposY[index]))
        count = 0

        for x in range(0,len(floormarkerX)):
            pygame.draw.rect(screen,RED,(floormarkerX[x] * TILESIZE,floormarkerY[x] * TILESIZE,32,32))
            #print(floormarkerX[count],floormarkerY[count])

            try:
                GRID[floormarkerY[x]][floormarkerX[x]] = 1
            except IndexError:
                pass


    def drawgrid():
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
                    print("LEFT")
                    if cube_gposX[x] <= 2:
                        pass
                    else:
                        cube_gposX[x] = LEFT

                if select_dir > 0.26 and select_dir < 0.5:
                    print("RIGHT")
                    if cube_gposX[x] >= GRIDWIDTH - 2:
                        pass
                    else:
                        cube_gposX[x] = RIGHT

                if select_dir > 0.51 and select_dir < 0.75:
                    print("UP")
                    if cube_gposY[x] == GRIDHEIGHT - 2:
                        pass
                    else:
                        cube_gposY[x] = UP

                if select_dir > 0.76 and select_dir < 1:
                    print("DOWN")
                    if cube_gposY[x] == 2:
                        pass
                    else:
                        cube_gposY[x] = DOWN

    def drawfromgrid():
        pass


    #game loop
    while running == True:
        clock.tick(30)
        screen.fill((0,0,0))
        drawgrid()
        random_walk()
        for x in range(0, len(cube_gposX)):
            walkers(x)
        if GEN_LIMIT == 0:
            generated = True
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

                            if GRID[0][u] == 1:
                                GRID[0][u] = 2
                            try:
                                if GRID[GRIDHEIGHT][u] == 1:
                                    GRID[GRIDHEIGHT][u] = 2
                                if GRID[j][0] == 1:
                                    GRID[j][0] = 2
                                if GRID[j][GRIDWIDTH - 1] == 1:
                                    GRID[j][GRIDWIDTH - 1] = 2
                            except IndexError:
                                pass

            if printedmap == False:
                for i in range(GRIDHEIGHT):
                    print(GRID[i])
                    pass

            printedmap = True
        GEN_LIMIT -= 1

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        pygame.display.update()
