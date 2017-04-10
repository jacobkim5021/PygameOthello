#OTHELLO - Jacob Kim

import pygame
pygame.init()   # initialize pygame

pygame.font.init()
titleFont = pygame.font.SysFont("Times New Roman", 50)
titleRender = titleFont.render("Othello", False, (0, 0, 0))
whiteTurn = titleFont.render("White's turn", False, (255, 255, 255))
blackTurn = titleFont.render("Black's turn", False, (0, 0, 0))
buttonFont = pygame.font.SysFont("Times New Roman", 20)
buttonRender = buttonFont.render("Skip Turn", False, (0, 0, 0))

displayScreen = pygame.display.set_mode((800, 600))     # object of screen displayed

pygame.display.set_caption('Othello')

pygame.display.update()         

boardColour = (207, 213, 167)
clockClass = pygame.time.Clock()

tilePos = [[10, 10], [70, 10], [130, 10], [190, 10], [250, 10], [310, 10], [370, 10], [430, 10],                #tile pixel positions      
         [10, 70], [70, 70], [130, 70], [190, 70], [250, 70], [310, 70], [370, 70], [430, 70],                  #typed out for 8x8 visibility
         [10, 130], [70, 130], [130, 130], [190, 130], [250, 130], [310, 130], [370, 130], [430, 130],
         [10, 190], [70, 190], [130, 190], [190, 190], [250, 190], [310, 190], [370, 190], [430, 190],
         [10, 250], [70, 250], [130, 250], [190, 250], [250, 250], [310, 250], [370, 250], [430, 250],
         [10, 310], [70, 310], [130, 310], [190, 310], [250, 310], [310, 310], [370, 310], [430, 310],
         [10, 370], [70, 370], [130, 370], [190, 370], [250, 370], [310, 370], [370, 370], [430, 370],
         [10, 430], [70, 430], [130, 430], [190, 430], [250, 430], [310, 430], [370, 430], [430, 430]]

tileCheck = [0, 0, 0, 0, 0, 0, 0, 0,        #0 = EMPTY
             0, 0, 0, 0, 0, 0, 0, 0,        #1 = WHITE
             0, 0, 0, 0, 0, 0, 0, 0,        #2 = BLACK
             0, 0, 0, 1, 2, 0, 0, 0,
             0, 0, 0, 2, 1, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0]

def displayTiles(tilePos, tileCheck, displayScreen):
    for number in range(64):
        if tileCheck[number] == 1:
            pygame.draw.circle(displayScreen, (255, 255, 255), (tilePos[number][0]+30, tilePos[number][1]+30), 28)
        elif tileCheck[number] == 2:
            pygame.draw.circle(displayScreen, (0, 0, 0), (tilePos[number][0]+30, tilePos[number][1]+30), 28)
        else:
            pass
        
####################### Initial Board ##################################     
displayScreen.fill(boardColour)
boardColours = True
counterVar = 0
for tile in tilePos:
    counterVar += 1
    if boardColours == True:
        pygame.draw.rect(displayScreen, (185, 224, 233), [tile[0], tile[1], 60, 60])
        boardColours = False
    elif boardColours == False:
        pygame.draw.rect(displayScreen, (222, 173, 100), [tile[0], tile[1], 60, 60])
        boardColours = True
    if counterVar % 8 == 0:
        if boardColours == True:
            boardColours = False
        elif boardColours == False:
            boardColours = True

displayTiles(tilePos, tileCheck, displayScreen)
displayScreen.blit(titleRender, (520, 10))
nameFont = pygame.font.SysFont("Times New Roman", 13)
nameRender = nameFont.render("by Jacob Kim", False, (0, 0, 0))
displayScreen.blit(nameRender, (700, 26))
displayScreen.blit(whiteTurn, (520, 300))
########################################################################

def checkWinner(tileCheck):
    noWhite = True
    noBlack = True
    noBlanks = True
    for number in tileCheck:
        if number == 1:
            noWhite = False
        elif number == 2:
            noBlack = False
        elif number == 0:
            noBlanks = False
    

def checkPlacement(tileCheck, clickedTileNumber, playerWhite, integer):
    c = clickedTileNumber
    oppTile = 2
    oriTile = 1
    if playerWhite == False:
        oppTile = 1
        oriTile = 2
    approved = False

    if c == 0:
        while (c+integer) < 64 and (c+integer) % 8 != 7:
            if tileCheck[c + integer] == oppTile:
                approved = True
            elif tileCheck[c + integer] == oriTile:
                if approved == True:
                    return True
                else:
                    return False
            elif tileCheck[c + integer] == 0:
                return False
            c += integer
    elif c == 7:
        while (c+integer) < 64 and (c+integer) % 8 != 0:
            if tileCheck[c + integer] == oppTile:
                approved = True
            elif tileCheck[c + integer] == oriTile:
                if approved == True:
                    return True
                else:
                    return False
            elif tileCheck[c + integer] == 0:
                return False
            c += integer
    elif c == 56:
        while (c+integer) > -1 and (c+integer) % 8 != 7:
            if tileCheck[c + integer] == oppTile:
                approved = True
            elif tileCheck[c + integer] == oriTile:
                if approved == True:
                    return True
                else:
                    return False
            elif tileCheck[c + integer] == 0:
                return False
            c += integer
    elif c == 63:
        while (c+integer) > -1 and (c+integer) % 8 != 0:
            if tileCheck[c + integer] == oppTile:
                approved = True
            elif tileCheck[c + integer] == oriTile:
                if approved == True:
                    return True
                else:
                    return False
            elif tileCheck[c + integer] == 0:
                return False
            c += integer
    elif c > 0 and c < 7:
        while (c+integer) < 64 and (c+integer) % 8 != 0 and (c+integer) % 8 != 7:
            if tileCheck[c + integer] == oppTile:
                approved = True
            elif tileCheck[c + integer] == oriTile:
                if approved == True:
                    return True
                else:
                    return False
            elif tileCheck[c + integer] == 0:
                return False
            c += integer
    elif c > 56 and c < 63:
        while (c+integer) > -1 and (c+integer) % 8 != 0 and (c+integer) % 8 != 7:
            if tileCheck[c + integer] == oppTile:
                approved = True
            elif tileCheck[c + integer] == oriTile:
                if approved == True:
                    return True
                else:
                    return False
            elif tileCheck[c + integer] == 0:
                return False
            c += integer
    elif c % 8 == 0 and c != 0 and c != 56:
        while (c+integer) > -1 and (c+integer) % 8 != 7 and (c+integer) < 64:
            if tileCheck[c + integer] == oppTile:
                approved = True
            elif tileCheck[c + integer] == oriTile:
                if approved == True:
                    return True
                else:
                    return False
            elif tileCheck[c + integer] == 0:
                return False
            c += integer
    elif c % 8 == 7 and c != 7 and c != 63:
        while (c+integer) > -1 and (c+integer) % 8 != 0 and (c+integer) < 64:
            if tileCheck[c + integer] == oppTile:
                approved = True
            elif tileCheck[c + integer] == oriTile:
                if approved == True:
                    return True
                else:
                    return False
            elif tileCheck[c + integer] == 0:
                return False
            c += integer
    else:
        while (c + integer) % 8 != 0 and (c + integer) % 8 != 7 and (c + integer) > -1 and (c + integer) < 64:
            if tileCheck[c + integer] == oppTile:
                approved = True
            elif tileCheck[c + integer] == oriTile:
                if approved == True:
                    return True
                else:
                    return False
            elif tileCheck[c + integer] == 0:
                return False
            c += integer

    return False
        

def checkBoard(tileCheck, clickedTileNumber, playerWhite):
                                                                                                    #   Surrounding tiles
    if clickedTileNumber == 0:                                                                      #   |_x-9_|_x-8_|_x-7_|
        validTiles = [1, 8, 9]                                                                      #   |_x-1_|__x__|_x+1_|
    elif clickedTileNumber > 0 and clickedTileNumber < 7:                                           #   |_x+7_|_x+8_|_x+9_|
        validTiles = [-1, 1, 7, 8, 9]
    elif clickedTileNumber == 7:
        validTiles = [-1, 7, 8]
    elif clickedTileNumber % 8 == 0 and clickedTileNumber != 0 and clickedTileNumber != 56:
        validTiles = [-8, -7, 1, 8, 9]
    elif clickedTileNumber % 8 == 7 and clickedTileNumber != 7 and clickedTileNumber != 63:
        validTiles = [-9, -8, -1, 7, 8]
    elif clickedTileNumber == 56:
        validTiles = [-8, -7, 1]
    elif clickedTileNumber > 56 and clickedTileNumber < 63:
        validTiles = [-9, -8, -7, -1, 1]
    elif clickedTileNumber == 63:
        validTiles = [-9, -8, -1]
    else:
        validTiles = [-9, -8, -7, -1, 1, 7, 8, 9]
    flipLine = []
    valid = 0
    for number in validTiles:
        if checkPlacement(tileCheck, clickedTileNumber, playerWhite, number) == True:
            flipLine.append(number)
            valid += 1

    if valid > 0:
        return flipLine
    else:
        return [0]

def flipTiles(tileCheck, clickedTileNumber, PlayerWhite, validTileList):
    
    oppTile = 2
    oriTile = 1
    if PlayerWhite == False:
        oppTile = 1
        oriTile = 2
    for number in validTileList:
        c = clickedTileNumber
        if c == 0:
            while (c+number) < 64 and (c+number) % 8 != 7 and tileCheck[c+number] == oppTile:
                tileCheck[c+number] = oriTile
                c += number
        elif c == 7:
            while (c+number) < 64 and (c+number) % 8 != 0 and tileCheck[c+number] == oppTile:
                tileCheck[c+number] = oriTile
                c += number
        elif c == 56:
            while (c+number) > -1 and (c+number) % 8 != 7 and tileCheck[c+number] == oppTile:
                tileCheck[c+number] = oriTile
                c += number
        elif c == 63:
            while (c+number) > -1 and (c+number) % 8 != 0 and tileCheck[c+number] == oppTile:
                tileCheck[c+number] = oriTile
                c += number
        elif c > 0 and c < 7:
            while (c+number) < 64 and (c+number) % 8 != 0 and (c+number) % 8 != 7 and tileCheck[c+number] == oppTile:
                tileCheck[c+number] = oriTile
                c += number
        elif c > 56 and c < 63:
            while (c+number) > -1 and (c+number) % 8 != 0 and (c+number) % 8 != 7 and tileCheck[c+number] == oppTile:
                tileCheck[c+number] = oriTile
                c += number
        elif c % 8 == 0 and c != 0 and c != 56:
            while (c+number) < 64 and (c+number) % 8 != 7 and (c+number) > -1 and tileCheck[c+number] == oppTile:
                tileCheck[c+number] = oriTile
                c += number
        elif c % 8 == 7 and c != 7 and c != 63:
            while (c+number) < 64 and (c+number) % 8 != 0 and (c+number) > -1 and tileCheck[c+number] == oppTile:
                tileCheck[c+number] = oriTile
                c += number
        else:
            while (c + number) % 8 != 0 and (c + number) % 8 != 7 and (c + number) > -1 and (c + number) < 64 and tileCheck[c+number] == oppTile:
                tileCheck[c+number] = oriTile
                c += number
        

exitGame = False
PlayerWhite = True

while not exitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
        if event.type == pygame.MOUSEBUTTONUP:
            mousePos = pygame.mouse.get_pos()
            if mousePos[0] > 10 and mousePos[0] < 490 and mousePos[1] > 10 and mousePos[1] < 490:
                tempX = (mousePos[0]-10)/60
                tempY = (mousePos[1]-10)/60
                clickedTileNumber = tempX + tempY*8
                validTileList = checkBoard(tileCheck, clickedTileNumber, PlayerWhite)
                if PlayerWhite == True:
                    if tileCheck[clickedTileNumber] == 0 and validTileList[0] != 0:
                        tileCheck[clickedTileNumber] = 1
                        flipTiles(tileCheck, clickedTileNumber, PlayerWhite, validTileList)
                        PlayerWhite = False
                        displayScreen.fill((207, 213, 167), (520, 300, 260, 200))
                        displayScreen.blit(blackTurn, (520, 300))
                elif PlayerWhite == False:
                    if tileCheck[clickedTileNumber] == 0 and validTileList[0] != 0:
                        tileCheck[clickedTileNumber] = 2
                        flipTiles(tileCheck, clickedTileNumber, PlayerWhite, validTileList)
                        PlayerWhite = True
                        displayScreen.fill((207, 213, 167), (520, 300, 260, 200))
                        displayScreen.blit(whiteTurn, (520, 300))
            elif mousePos[0] > 595 and mousePos[0] < 700 and mousePos[1] > 430 and mousePos[1] < 480:
                if PlayerWhite == True:
                    displayScreen.fill((207, 213, 167), (520, 300, 260, 200))
                    displayScreen.blit(blackTurn, (520, 300))
                    PlayerWhite = False
                elif PlayerWhite == False:
                    displayScreen.fill((207, 213, 167), (520, 300, 260, 200))
                    displayScreen.blit(whiteTurn, (520, 300))
                    PlayerWhite = True
    displayTiles(tilePos, tileCheck, displayScreen)
    pygame.draw.rect(displayScreen, (222, 222, 222), [595, 430, 100, 50])
    displayScreen.blit(buttonRender, (605, 445))
    pygame.display.update()
    clockClass.tick(60) # limit to 60 fps



pygame.quit()   # de-initialize pygame
quit()          
