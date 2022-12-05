width = 800
height = 800
square_size = 640 /9
import pygame
import sudoku_generator
import sys

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.screen = screen
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.board = sudoku_generator.generate_sudoku(9, difficulty)


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

    def drawcells(self, list):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] != 0:
                    val = font.render(str(self.board[i][j]), True, 'black')
                    screen.blit(val, ((110 + i * (640 / 9), 95 + j * 640 / 9)))
                if (i,j) in list:
                    if self.board[i][j] != 0:
                        val = font.render(str(self.board[i][j]), True, 'red')
                        screen.blit(val, ((110 + i * (640 / 9), 95 + j * 640 / 9)))
        pygame.display.update()

    def checkcolums(self,board):
        list = []
        i = 0
        j = 0
        k = []
        while j < 9:
            i = 0
            while i < 9:
                list.append(board[i][j])
                i += 1
            list = set(list)
            if len(list) != 9:
                list = []
                k.append(1)
            else:
                list = []
                k.append(0)
            j += 1
        if sum(k) == 0:
            return True
        else:
            return False

    def checkrows(self,board):
        list = []
        i = 0
        j = 0
        k = []
        while j < 9:
            i = 0
            while i < 9:
                list.append(board[j][i])
                i += 1
            list = set(list)
            if len(list) != 9:
                list = []
                k.append(1)
            else:
                list = []
                k.append(0)
            j += 1
        if sum(k) == 0:
            return True
        else:
            return False

    def checkboxrow1(self,board):
        i = 0
        list = []
        k = 0
        y = []
        while i < 7:
            j = 0
            while j < 3:
                k = 0
                while k < 3:
                    list.append(board[j][i + k])
                    k += 1
                j += 1
            list = set(list)
            if len(list) != 9:
                list = []
                y.append(1)
            else:
                y.append(0)
                list = []
            i += 3
        if sum(y) == 0:
            return True
        else:
            return False

    def checkboxrow2(self,board):
        i = 0
        list = []
        k = 0
        y = []
        while i < 7:
            j = 0
            while j < 3:
                k = 0
                while k < 3:
                    list.append(board[j + 3][i + k])
                    k += 1
                j += 1
            list = set(list)
            if len(list) != 9:
                list = []
                y.append(1)
            else:
                y.append(0)
                list = []
            i += 3
        if sum(y) == 0:
            return True
        else:
            return False

    def checkboxrow3(self,board):
        i = 0
        list = []
        k = 0
        y = []
        while i < 7:
            j = 0
            while j < 3:
                k = 0
                while k < 3:
                    list.append(board[j + 6][i + k])
                    k += 1
                j += 1
            list = set(list)
            if len(list) != 9:
                list = []
                y.append(1)
            else:
                y.append(0)
                list = []
            i += 3
        if sum(y) == 0:
            return True
        else:
            return False

    def zeroes(self,board):
        for i in range(9):
            for j in range(9):
                if board[i][j]== 0:
                    return False
        else:
            return True


    def checkboard(self,board):
        list = []
        if self.zeroes(board) == False:
            return False
        if self.checkcolums(board) == False:
            return False
        if self.checkrows(board) == False:
            return False
        if self.checkboxrow1(board)==False:
            return False
        if self.checkboxrow2(board)==False:
            return False
        if self.checkboxrow3(board)==False:
            return False
        else:
            return True


def draw_you_lost(screen):
    screen.fill('black')
    lostfont = pygame.font.SysFont('Comic Sans MS', 30)
    losttext = lostfont.render("YOU LOST", 0, 'red')
    lostsurface = pygame.Surface((losttext.get_size()[0] + 20, losttext.get_size()[1] + 20))
    lostsurface.fill('white')
    lostsurface.blit(losttext, (10, 10))
    lostrectangle = lostsurface.get_rect(center=((400,400)))
    screen.blit(lostsurface, lostrectangle)

    Restrartfont = pygame.font.SysFont('Comic Sans MS', 30)
    Restrarttext = Restrartfont.render("Restart", 0, 'black')
    Restrartsurface = pygame.Surface((Restrarttext.get_size()[0] + 20, Restrarttext.get_size()[1] + 20))
    Restrartsurface.fill('red')
    Restrartsurface.blit(Restrarttext, (10, 10))
    Restrartrectangle = Restrartsurface.get_rect(center=((400), 500))
    screen.blit(Restrartsurface, Restrartrectangle)
    losingmenu = True

    while losingmenu is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Restrartrectangle.collidepoint(event.pos):
                    screen.fill('white')
                    losingmenu = False
                    return

        pygame.display.update()

def youwin(screen):
    screen.fill('black')
    lostfont = pygame.font.SysFont('Comic Sans MS', 30)
    losttext = lostfont.render("YOU WIN", 0, 'blue')
    lostsurface = pygame.Surface((losttext.get_size()[0] + 20, losttext.get_size()[1] + 20))
    lostsurface.fill('white')
    lostsurface.blit(losttext, (10, 10))
    lostrectangle = lostsurface.get_rect(center=((400, 400)))
    screen.blit(lostsurface, lostrectangle)

    exitfont = pygame.font.SysFont('Comic Sans MS', 30)
    exittext = exitfont.render("Exit", 0, 'black')
    exitsurface = pygame.Surface((exittext.get_size()[0] + 20, exittext.get_size()[1] + 20))
    exitsurface.fill('red')
    exitsurface.blit(exittext, (10, 10))
    exitrectangle = exitsurface.get_rect(center=((400), 500))
    screen.blit(exitsurface, exitrectangle)
    winningmenu = True

    while winningmenu is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exitrectangle.collidepoint(event.pos):
                    screen.fill('white')
                    sys.exit()
                    return

        pygame.display.update()

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


pygame.init()
screen = pygame.display.set_mode((800,800))
screen.fill('white')
main_menu = True
in_game = False
winningmenu = False
losingmenu = False

while True:

    while main_menu is True:
        m = gamestart(screen)
        main_menu = False
        in_game = True
        pygame.display.update()
        i = 0
    while losingmenu is True:
        draw_you_lost(screen)
        losingmenu = False
        main_menu = True
        pygame.display.update()
    while winningmenu is True:
        youwin(screen)
        pygame.display.update()

    while in_game is True:

        while i < 1:
            list =[]
            emptylist =[]
            screen.fill('white')
            template = Board(800, 800, screen, m)
            template.draw()
            template.drawcells(list)
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
                    template.drawcells(emptylist)
                if (x,y) == (8,9):
                    if template.checkboard(template.board) is True:
                        main_menu = False
                        in_game = False
                        winningmenu = True
                    else:

                        losingmenu = True
                        main_menu = False
                        in_game = False



            if event.type == pygame.KEYDOWN:
                if template.board[x][y] == 0 or (x,y) in emptylist:
                    if event.key == pygame.K_1:
                        template.board[x][y]=1
                        screen.fill('white')
                        template.draw()
                        template.drawcells(emptylist)
                        emptylist.append((x,y))
                    elif event.key == pygame.K_2:
                        template.board[x][y]=2
                        screen.fill('white')
                        template.draw()
                        template.drawcells(emptylist)
                        emptylist.append((x, y))
                    elif event.key == pygame.K_3:
                        template.board[x][y] = 3
                        screen.fill('white')
                        template.draw()
                        template.drawcells(emptylist)
                        emptylist.append((x, y))
                    elif event.key == pygame.K_4:
                        template.board[x][y]= 4
                        screen.fill('white')
                        template.draw()
                        template.drawcells(emptylist)
                        emptylist.append((x, y))
                    elif event.key == pygame.K_5:
                        template.board[x][y]= 5
                        screen.fill('white')
                        template.draw()
                        template.drawcells(emptylist)
                        emptylist.append((x, y))
                    elif event.key == pygame.K_6:
                        template.board[x][y]= 6
                        screen.fill('white')
                        template.draw()
                        template.drawcells(emptylist)
                        emptylist.append((x, y))
                    elif event.key == pygame.K_7:
                        template.board[x][y]= 7
                        screen.fill('white')
                        template.draw()
                        template.drawcells(emptylist)
                        emptylist.append((x, y))
                    elif event.key == pygame.K_8:
                        template.board[x][y]= 8
                        screen.fill('white')
                        template.draw()
                        template.drawcells(emptylist)
                        emptylist.append((x, y))
                    elif event.key == pygame.K_9:
                        template.board[x][y]= 9
                        screen.fill('white')
                        template.draw()
                        template.drawcells(emptylist)
                        emptylist.append((x, y))
        template.drawcells(emptylist)



    pygame.display.update()






