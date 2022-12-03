width = 800
height = 800
square_size = 640 /9
import pygame
import sudoku_generator
import sys
import pygame



class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.width = 640 / 9
        self.height = 640 / 9
        self.screen = screen
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def draw(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        val = font.render(str(self.value), True, 'Black')
        valrectangle = val.get_rect(center = ((640/9)*self.row + (640/9)//2,
                                    (640 / 9) * self.col + (640 / 9) // 2))

        self.screen.blit(val,valrectangle)



class Board:
    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.board = sudoku_generator.generate_sudoku(9, difficulty)
        self.cells = [
            [Cell(self.board[i][j], i,j, screen) for j in range(0,9)]

        for i in range(0,9)

        ]
        self.replaced = 0

    def emptycells(self):
        list = []
        for j in range(9):
            for i in range(9):
                if self.board[i][j] == 0:
                    self.list.append((i,j))

    def replacecheck(self, x, y):
        if self.board[x][y] == 0:
            return True
        else:
            return False

    def clearemptycells(self, list):
        for j in range(9):
            for i in range(9):
                if (i,j) in list:
                    self.board[i][j] = 0

    def draw(self):
        pygame.draw.line(self.screen, 'black', (80, 720), (720, 720), 4)
        pygame.draw.line(self.screen, 'black', (80, 80), (80, 720), 4)
        pygame.draw.line(self.screen, 'black', (720, 720), (720, 80), 4)
        pygame.draw.line(self.screen, 'black', (720, 80), (80, 80), 4)
        for i in range(1, 9):
            if i % 3 == 0:
                pygame.draw.line(self.screen, 'black', (80, 720 - i * 640 / 9), (720, 720 - i * 640 / 9), 4)
                pygame.draw.line(self.screen, 'black', (720 - i * 640 / 9, 80), (720 - i * 640 / 9, 720), 4)
            else:
                pygame.draw.line(self.screen, 'black', (80, 720 - i * 640 / 9), (720, 720 - i * 640 / 9), 2)
                pygame.draw.line(self.screen, 'black', (720 - i * 640 / 9, 80), (720 - i * 640 / 9, 720), 2)
        exitfont = pygame.font.SysFont('Comic Sans MS', 30)
        exittext = exitfont.render("Exit", 0, 'white')
        exitsurface = pygame.Surface((exittext.get_size()[0] + 20, exittext.get_size()[1] + 20))
        exitsurface.fill('black')
        exitsurface.blit(exittext, (10, 10))
        exitrectangle = exitsurface.get_rect(center=((720 - 5 * 640 / 9) / 3, 760))
        screen.blit(exitsurface, exitrectangle)

        resetfont = pygame.font.SysFont('Comic Sans MS', 30)
        resettext = resetfont.render("Reset", 0, 'white')
        resetsurface = pygame.Surface((resettext.get_size()[0] + 20, resettext.get_size()[1] + 20))
        resetsurface.fill('black')
        resetsurface.blit(resettext, (10, 10))
        resetrectangle = resetsurface.get_rect(center=((720 - 1 * 640 / 9) / 3, 760))
        screen.blit(resetsurface, resetrectangle)

        Restrartfont = pygame.font.SysFont('Comic Sans MS', 30)
        Restrarttext = Restrartfont.render("Restart", 0, 'white')
        Restrartsurface = pygame.Surface((Restrarttext.get_size()[0] + 20, Restrarttext.get_size()[1] + 20))
        Restrartsurface.fill('black')
        Restrartsurface.blit(Restrarttext, (10, 10))
        Restrartrectangle = Restrartsurface.get_rect(center=((720 - (-4) * 640 / 9) / 3, 760))
        screen.blit(Restrartsurface, Restrartrectangle)
        pygame.display.update()

        Donefont = pygame.font.SysFont('Comic Sans MS', 30)
        Donetext = Donefont.render("Done", 0, 'white')
        Donesurface = pygame.Surface((Donetext.get_size()[0] + 20, Donetext.get_size()[1] + 20))
        Donesurface.fill('black')
        Donesurface.blit(Donetext, (10, 10))
        Donerectangle = Donesurface.get_rect(center=((720 - (-18) * 640 / 9) / 3, 760))
        screen.blit(Donesurface, Donerectangle)
        pygame.display.update()

    def drawcells(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] != 0:
                    val = font.render(str(self.board[i][j]), True, 'black')
                    screen.blit(val, ((110 + i * (640 / 9), 95 + j * 640 / 9)))
        pygame.display.update()





#return true if
    def check_if_full(self):
        if 0 in self.board:
            return False
        else:
            return True

'''    def checkifboardvalid(self):
        if self.board
'''





pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill('white')

def gamestart(screen):

    titlefont = pygame.font.Font(None, 100)
    buttonfont = pygame.font.Font(None, 100)

    screen.fill('white')

    titlesurface = titlefont.render("Sudoku", 0, 'Black')
    buttonsurface = titlesurface.get_rect( center = (800 // 2, 800 //2 - 200))
    screen.blit(titlesurface, buttonsurface)

    easytext = buttonfont.render("Easy", 0, 'white')
    mediumtext = buttonfont.render("Medium", 0, 'white')
    hardtext = buttonfont.render("Hard", 0, 'white')

    easysurface = pygame.Surface((easytext.get_size()[0]+20,
                                  easytext.get_size()[1]+20))
    easysurface.fill('black')
    easysurface.blit(easytext,(10,10))

    mediumsurface = pygame.Surface((mediumtext.get_size()[0]
                                    + 20, mediumtext.get_size()[1] + 20))
    mediumsurface.fill('black')
    mediumsurface.blit(mediumtext, (10, 10))

    hardsurface = pygame.Surface((hardtext.get_size()[0] + 20,
                                  hardtext.get_size()[1] + 20))
    hardsurface.fill('black')
    hardsurface.blit(hardtext, (10, 10))

    easyrectangle = easysurface.get_rect(center = (800//2, (800/2) +100))
    mediumrectangle = mediumsurface.get_rect(center=(800//2, 800/2 + 200))
    hardrectangle = hardsurface.get_rect(center=(800//2, 800/2 + 300))

    screen.blit(easysurface, easyrectangle)
    screen.blit(mediumsurface, mediumrectangle)
    screen.blit(hardsurface, hardrectangle)
    main_menu= True
    while main_menu is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easyrectangle.collidepoint(event.pos):
                    main_menu = False
                    screen.fill('white')
                    return 30
                if mediumrectangle.collidepoint(event.pos):
                    main_menu = False
                    screen.fill('white')
                    return 40
                if hardrectangle.collidepoint(event.pos):
                    main_menu = False
                    screen.fill('white')
                    return 50
        pygame.display.update()

main_menu = True
in_game = False

while True:
    while main_menu is True:
        m = gamestart(screen)
        main_menu = False
        in_game = True
        pygame.display.update()
        i = 0
    while in_game is True:

        while i < 1:
            emptylist =[]
            screen.fill('white')
            template = Board(800, 800, screen, m)
            template.draw()
            template.drawcells()
            i +=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                x = int(x / (640 / 9)) - 1
                y = int(y / (640 / 9)) - 1
                if (x,y) == (0,9):
                    sys.exit()
                if (x,y) == (3,9):
                    in_game  = False
                    main_menu = True
                if (x,y) == (1,9):
                    for j in range(9):
                        for i in range(9):
                            if (i, j) in emptylist:
                                template.board[i][j] = 0
                    screen.fill('white')
                    template.draw()
                    template.drawcells()
###check if board is right
                if (x,y) == (8,9):
                    pass

            if event.type == pygame.KEYDOWN:
                if template.board[x][y] == 0 or (x,y) in emptylist:
                    if event.key == pygame.K_1:
                        template.board[x][y]=1
                        screen.fill('white')
                        template.draw()
                        template.drawcells()
                        emptylist.append((x,y))
                    elif event.key == pygame.K_2:
                        template.board[x][y]=2
                        screen.fill('white')
                        template.draw()
                        template.drawcells()
                        emptylist.append((x, y))
                    elif event.key == pygame.K_3:
                        template.board[x][y] = 3
                        screen.fill('white')
                        template.draw()
                        template.drawcells()
                        emptylist.append((x, y))
                    elif event.key == pygame.K_4:
                        template.board[x][y]= 4
                        screen.fill('white')
                        template.draw()
                        template.drawcells()
                        emptylist.append((x, y))
                    elif event.key == pygame.K_5:
                        template.board[x][y]= 5
                        screen.fill('white')
                        template.draw()
                        template.drawcells()
                        emptylist.append((x, y))
                    elif event.key == pygame.K_6:
                        template.board[x][y]= 6
                        screen.fill('white')
                        template.draw()
                        template.drawcells()
                        emptylist.append((x, y))
                    elif event.key == pygame.K_7:
                        template.board[x][y]= 7
                        screen.fill('white')
                        template.draw()
                        template.drawcells()
                        emptylist.append((x, y))
                    elif event.key == pygame.K_8:
                        template.board[x][y]= 8
                        screen.fill('white')
                        template.draw()
                        template.drawcells()
                        emptylist.append((x, y))
                    elif event.key == pygame.K_9:
                        template.board[x][y]= 9
                        screen.fill('white')
                        template.draw()
                        template.drawcells()
                        emptylist.append((x, y))










        template.drawcells()
        pygame.display.update()








