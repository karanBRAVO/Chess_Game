# import statements
import pygame
# import time
from pygame.locals import *

# initializing pygame
pygame.init()
# information on terminal
print("*** Chess Engine ***")
print("First Turn: Black")
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
grey = (192, 192, 192)
silver = (188, 198, 204)
charcoalBlue = (54, 69, 79)
# Clock
clock = pygame.time.Clock()
fps = 60
# Window
windowWidth = 400
windowHeight = 400
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption("Chess Game")
pygame.display.set_icon(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/chess.png"))
# Image Resizing variables
boxSize = 50
imageWidth = 50
imageHeight = 50
# images used
assets = {
    'pw': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/pawn-w.png"), (imageWidth, imageHeight)),
    'pb': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/pawn-b.png"), (imageWidth, imageHeight)),
    'rw': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/rook-w.png"), (imageWidth, imageHeight)),
    'rb': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/rook-b.png"), (imageWidth, imageHeight)),
    'kw': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/knight-w.png"), (imageWidth, imageHeight)),
    'kb': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/knight-b.png"), (imageWidth, imageHeight)),
    'bw': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/bishop-w.png"), (imageWidth, imageHeight)),
    'bb': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/bishop-b.png"), (imageWidth, imageHeight)),
    'Kw': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/king-w.png"), (imageWidth, imageHeight)),
    'Kb': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/king-b.png"), (imageWidth, imageHeight)),
    'Qw': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/queen-w.png"), (imageWidth, imageHeight)),
    'Qb': pygame.transform.scale(pygame.image.load("C:/Users/karan-PC/PycharmProjects/chessEngine/chessAssets/queen-b.png"), (imageWidth, imageHeight)),
}
# factors for implementing the logic
x_factor = None
y_factor = None


# main loop
class MainGame:
    def __init__(self):
        self.run = True

    def gameLoop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN and (event.key == K_ESCAPE):
                    self.run = False

            drawGameWindow()
            pygame.display.update()
            clock.tick(fps)
        pygame.quit()


# Contains position of each object in game
class Positions:
    def __init__(self):
        global x_factor, y_factor
        # dictionary for storing box as rect object
        self.box_dict = {}
        # automatically generates all boxes as rect object
        for i in range(1, 65, 1):
            if i <= 8:
                x_factor = i - 1
                y_factor = 0
            elif 8 < i <= 16:
                x_factor = i - 9
                y_factor = 1
            elif 16 < i <= 24:
                x_factor = i - 17
                y_factor = 2
            elif 24 < i <= 32:
                x_factor = i - 25
                y_factor = 3
            elif 32 < i <= 40:
                x_factor = i - 33
                y_factor = 4
            elif 40 < i <= 48:
                x_factor = i - 41
                y_factor = 5
            elif 48 < i <= 56:
                x_factor = i - 49
                y_factor = 6
            elif 56 < i <= 64:
                x_factor = i - 57
                y_factor = 7
            self.box_dict[f"box{i}"] = pygame.Rect(x_factor * boxSize, y_factor * boxSize, boxSize, boxSize)

        # making box list
        self.boxLst = []
        for i in range(1, 65, 1):
            self.boxLst.append(self.box_dict[f"box{i}"])

        # adding colors to the board boxes
        self.whiteBoxLst = [self.box_dict["box1"], self.box_dict["box3"], self.box_dict["box5"], self.box_dict["box7"],
                            self.box_dict["box10"], self.box_dict["box12"], self.box_dict["box14"], self.box_dict["box16"],
                            self.box_dict["box17"], self.box_dict["box19"], self.box_dict["box21"], self.box_dict["box23"],
                            self.box_dict["box26"], self.box_dict["box28"], self.box_dict["box30"], self.box_dict["box32"],
                            self.box_dict["box33"], self.box_dict["box35"], self.box_dict["box37"], self.box_dict["box39"],
                            self.box_dict["box42"], self.box_dict["box44"], self.box_dict["box46"], self.box_dict["box48"],
                            self.box_dict["box49"], self.box_dict["box51"], self.box_dict["box53"], self.box_dict["box55"],
                            self.box_dict["box58"], self.box_dict["box60"], self.box_dict["box62"], self.box_dict["box64"]]
        self.greyBoxLst = [self.box_dict["box2"], self.box_dict["box4"], self.box_dict["box6"], self.box_dict["box8"],
                           self.box_dict["box9"], self.box_dict["box11"], self.box_dict["box13"], self.box_dict["box15"],
                           self.box_dict["box18"], self.box_dict["box20"], self.box_dict["box22"], self.box_dict["box24"],
                           self.box_dict["box25"], self.box_dict["box27"], self.box_dict["box29"], self.box_dict["box31"],
                           self.box_dict["box34"], self.box_dict["box36"], self.box_dict["box38"], self.box_dict["box40"],
                           self.box_dict["box41"], self.box_dict["box43"], self.box_dict["box45"], self.box_dict["box47"],
                           self.box_dict["box50"], self.box_dict["box52"], self.box_dict["box54"], self.box_dict["box56"],
                           self.box_dict["box57"], self.box_dict["box59"], self.box_dict["box61"], self.box_dict["box63"]]

        # dead pieces Rect
        self.white_deadPieceRect_dict = {}
        self.black_deadPieceRect_dict = {}
        for i in range(1, 17, 1):
            if i <= 8:
                x_factor = 8
                y_factor = i - 1
            else:
                x_factor = 9
                y_factor = i - 9
            self.white_deadPieceRect_dict[f"whiteCutPiece_{i}"] = pygame.Rect(x_factor * boxSize, y_factor * boxSize, boxSize, boxSize)
            self.black_deadPieceRect_dict[f"blackCutPiece_{i}"] = pygame.Rect(-x_factor * boxSize, -y_factor * boxSize, boxSize, boxSize)

        # defining piece position
        # black piece position
        self.rb1 = pygame.Rect(0 * boxSize, 0 * boxSize, imageWidth, imageHeight)
        self.pb1 = pygame.Rect(0 * boxSize, 1 * boxSize, imageWidth, imageHeight)
        self.kb1 = pygame.Rect(1 * boxSize, 0 * boxSize, imageWidth, imageHeight)
        self.pb2 = pygame.Rect(1 * boxSize, 1 * boxSize, imageWidth, imageHeight)
        self.bb1 = pygame.Rect(2 * boxSize, 0 * boxSize, imageWidth, imageHeight)
        self.pb3 = pygame.Rect(2 * boxSize, 1 * boxSize, imageWidth, imageHeight)
        self.Qb = pygame.Rect(3 * boxSize, 0 * boxSize, imageWidth, imageHeight)
        self.pb4 = pygame.Rect(3 * boxSize, 1 * boxSize, imageWidth, imageHeight)
        self.Kb = pygame.Rect(4 * boxSize, 0 * boxSize, imageWidth, imageHeight)
        self.pb5 = pygame.Rect(4 * boxSize, 1 * boxSize, imageWidth, imageHeight)
        self.bb2 = pygame.Rect(5 * boxSize, 0 * boxSize, imageWidth, imageHeight)
        self.pb6 = pygame.Rect(5 * boxSize, 1 * boxSize, imageWidth, imageHeight)
        self.kb2 = pygame.Rect(6 * boxSize, 0 * boxSize, imageWidth, imageHeight)
        self.pb7 = pygame.Rect(6 * boxSize, 1 * boxSize, imageWidth, imageHeight)
        self.rb2 = pygame.Rect(7 * boxSize, 0 * boxSize, imageWidth, imageHeight)
        self.pb8 = pygame.Rect(7 * boxSize, 1 * boxSize, imageWidth, imageHeight)
        # white piece position
        self.pw1 = pygame.Rect(0 * boxSize, 6 * boxSize, imageWidth, imageHeight)
        self.rw1 = pygame.Rect(0 * boxSize, 7 * boxSize, imageWidth, imageHeight)
        self.pw2 = pygame.Rect(1 * boxSize, 6 * boxSize, imageWidth, imageHeight)
        self.kw1 = pygame.Rect(1 * boxSize, 7 * boxSize, imageWidth, imageHeight)
        self.pw3 = pygame.Rect(2 * boxSize, 6 * boxSize, imageWidth, imageHeight)
        self.bw1 = pygame.Rect(2 * boxSize, 7 * boxSize, imageWidth, imageHeight)
        self.pw4 = pygame.Rect(3 * boxSize, 6 * boxSize, imageWidth, imageHeight)
        self.Qw = pygame.Rect(3 * boxSize, 7 * boxSize, imageWidth, imageHeight)
        self.pw5 = pygame.Rect(4 * boxSize, 6 * boxSize, imageWidth, imageHeight)
        self.Kw = pygame.Rect(4 * boxSize, 7 * boxSize, imageWidth, imageHeight)
        self.pw6 = pygame.Rect(5 * boxSize, 6 * boxSize, imageWidth, imageHeight)
        self.bw2 = pygame.Rect(5 * boxSize, 7 * boxSize, imageWidth, imageHeight)
        self.pw7 = pygame.Rect(6 * boxSize, 6 * boxSize, imageWidth, imageHeight)
        self.kw2 = pygame.Rect(6 * boxSize, 7 * boxSize, imageWidth, imageHeight)
        self.pw8 = pygame.Rect(7 * boxSize, 6 * boxSize, imageWidth, imageHeight)
        self.rw2 = pygame.Rect(7 * boxSize, 7 * boxSize, imageWidth, imageHeight)

        self.pawnBlack1Clicked = 0
        self.pawnBlack1Clicked_plus8 = 0
        self.pawnBlack1Clicked_twoStep = 0
        self.pawnBlack1Clicked_cut = 0

        self.pawnBlack2Clicked = 0
        self.pawnBlack2Clicked_plus8 = 0
        self.pawnBlack2Clicked_twoStep = 0
        self.pawnBlack2Clicked_cut = 0

        self.pawnBlack3Clicked = 0
        self.pawnBlack3Clicked_plus8 = 0
        self.pawnBlack3Clicked_twoStep = 0
        self.pawnBlack3Clicked_cut = 0

        self.pawnBlack4Clicked = 0
        self.pawnBlack4Clicked_plus8 = 0
        self.pawnBlack4Clicked_twoStep = 0
        self.pawnBlack4Clicked_cut = 0

        self.pawnBlack5Clicked = 0
        self.pawnBlack5Clicked_plus8 = 0
        self.pawnBlack5Clicked_twoStep = 0
        self.pawnBlack5Clicked_cut = 0

        self.pawnBlack6Clicked = 0
        self.pawnBlack6Clicked_plus8 = 0
        self.pawnBlack6Clicked_twoStep = 0
        self.pawnBlack6Clicked_cut = 0

        self.pawnBlack7Clicked = 0
        self.pawnBlack7Clicked_plus8 = 0
        self.pawnBlack7Clicked_twoStep = 0
        self.pawnBlack7Clicked_cut = 0

        self.pawnBlack8Clicked = 0
        self.pawnBlack8Clicked_plus8 = 0
        self.pawnBlack8Clicked_twoStep = 0
        self.pawnBlack8Clicked_cut = 0

        self.KingBlackClicked = 0
        self.KingBlackClicked_cut = 0

        self.knightBlack1Clicked = 0
        self.knightBlack1Clicked_cut = 0

        self.knightBlack2Clicked = 0
        self.knightBlack2Clicked_cut = 0

        self.rookBlack1Clicked = 0
        self.rookBlack1Clicked_plus8 = 0
        self.rookBlack1Clicked_plus16 = 0
        self.rookBlack1Clicked_plus24 = 0
        self.rookBlack1Clicked_plus32 = 0
        self.rookBlack1Clicked_plus40 = 0
        self.rookBlack1Clicked_plus48 = 0
        self.rookBlack1Clicked_plus1 = 0
        self.rookBlack1Clicked_plus2 = 0
        self.rookBlack1Clicked_plus3 = 0
        self.rookBlack1Clicked_plus4 = 0
        self.rookBlack1Clicked_plus5 = 0
        self.rookBlack1Clicked_plus6 = 0
        self.rookBlack1Clicked_minus8 = 0
        self.rookBlack1Clicked_minus16 = 0
        self.rookBlack1Clicked_minus24 = 0
        self.rookBlack1Clicked_minus32 = 0
        self.rookBlack1Clicked_minus40 = 0
        self.rookBlack1Clicked_minus48 = 0
        self.rookBlack1Clicked_minus1 = 0
        self.rookBlack1Clicked_minus2 = 0
        self.rookBlack1Clicked_minus3 = 0
        self.rookBlack1Clicked_minus4 = 0
        self.rookBlack1Clicked_minus5 = 0
        self.rookBlack1Clicked_minus6 = 0
        self.rookBlack1Clicked_cut = 0

        self.rookBlack2Clicked = 0
        self.rookBlack2Clicked_plus8 = 0
        self.rookBlack2Clicked_plus16 = 0
        self.rookBlack2Clicked_plus24 = 0
        self.rookBlack2Clicked_plus32 = 0
        self.rookBlack2Clicked_plus40 = 0
        self.rookBlack2Clicked_plus48 = 0
        self.rookBlack2Clicked_plus1 = 0
        self.rookBlack2Clicked_plus2 = 0
        self.rookBlack2Clicked_plus3 = 0
        self.rookBlack2Clicked_plus4 = 0
        self.rookBlack2Clicked_plus5 = 0
        self.rookBlack2Clicked_plus6 = 0
        self.rookBlack2Clicked_minus8 = 0
        self.rookBlack2Clicked_minus16 = 0
        self.rookBlack2Clicked_minus24 = 0
        self.rookBlack2Clicked_minus32 = 0
        self.rookBlack2Clicked_minus40 = 0
        self.rookBlack2Clicked_minus48 = 0
        self.rookBlack2Clicked_minus1 = 0
        self.rookBlack2Clicked_minus2 = 0
        self.rookBlack2Clicked_minus3 = 0
        self.rookBlack2Clicked_minus4 = 0
        self.rookBlack2Clicked_minus5 = 0
        self.rookBlack2Clicked_minus6 = 0
        self.rookBlack2Clicked_cut = 0

        self.bishopBlack1Clicked = 0
        self.bishopBlack1Clicked_plus8_plus1 = 0
        self.bishopBlack1Clicked_plus16_plus2 = 0
        self.bishopBlack1Clicked_plus24_plus3 = 0
        self.bishopBlack1Clicked_plus32_plus4 = 0
        self.bishopBlack1Clicked_plus40_plus5 = 0
        self.bishopBlack1Clicked_plus48_plus6 = 0
        self.bishopBlack1Clicked_plus8_minus1 = 0
        self.bishopBlack1Clicked_plus16_minus2 = 0
        self.bishopBlack1Clicked_plus24_minus3 = 0
        self.bishopBlack1Clicked_plus32_minus4 = 0
        self.bishopBlack1Clicked_plus40_minus5 = 0
        self.bishopBlack1Clicked_plus48_minus6 = 0
        self.bishopBlack1Clicked_minus8_plus1 = 0
        self.bishopBlack1Clicked_minus16_plus2 = 0
        self.bishopBlack1Clicked_minus24_plus3 = 0
        self.bishopBlack1Clicked_minus32_plus4 = 0
        self.bishopBlack1Clicked_minus40_plus5 = 0
        self.bishopBlack1Clicked_minus48_plus6 = 0
        self.bishopBlack1Clicked_minus8_minus1 = 0
        self.bishopBlack1Clicked_minus16_minus2 = 0
        self.bishopBlack1Clicked_minus24_minus3 = 0
        self.bishopBlack1Clicked_minus32_minus4 = 0
        self.bishopBlack1Clicked_minus40_minus5 = 0
        self.bishopBlack1Clicked_minus48_minus6 = 0
        self.bishopBlack1Clicked_cut = 0

        self.bishopBlack2Clicked = 0
        self.bishopBlack2Clicked_plus8_plus1 = 0
        self.bishopBlack2Clicked_plus16_plus2 = 0
        self.bishopBlack2Clicked_plus24_plus3 = 0
        self.bishopBlack2Clicked_plus32_plus4 = 0
        self.bishopBlack2Clicked_plus40_plus5 = 0
        self.bishopBlack2Clicked_plus48_plus6 = 0
        self.bishopBlack2Clicked_plus8_minus1 = 0
        self.bishopBlack2Clicked_plus16_minus2 = 0
        self.bishopBlack2Clicked_plus24_minus3 = 0
        self.bishopBlack2Clicked_plus32_minus4 = 0
        self.bishopBlack2Clicked_plus40_minus5 = 0
        self.bishopBlack2Clicked_plus48_minus6 = 0
        self.bishopBlack2Clicked_minus8_plus1 = 0
        self.bishopBlack2Clicked_minus16_plus2 = 0
        self.bishopBlack2Clicked_minus24_plus3 = 0
        self.bishopBlack2Clicked_minus32_plus4 = 0
        self.bishopBlack2Clicked_minus40_plus5 = 0
        self.bishopBlack2Clicked_minus48_plus6 = 0
        self.bishopBlack2Clicked_minus8_minus1 = 0
        self.bishopBlack2Clicked_minus16_minus2 = 0
        self.bishopBlack2Clicked_minus24_minus3 = 0
        self.bishopBlack2Clicked_minus32_minus4 = 0
        self.bishopBlack2Clicked_minus40_minus5 = 0
        self.bishopBlack2Clicked_minus48_minus6 = 0
        self.bishopBlack2Clicked_cut = 0

        self.QueenBlackClicked = 0
        self.QueenBlackClicked_plus8 = 0
        self.QueenBlackClicked_plus16 = 0
        self.QueenBlackClicked_plus24 = 0
        self.QueenBlackClicked_plus32 = 0
        self.QueenBlackClicked_plus40 = 0
        self.QueenBlackClicked_plus48 = 0
        self.QueenBlackClicked_plus1 = 0
        self.QueenBlackClicked_plus2 = 0
        self.QueenBlackClicked_plus3 = 0
        self.QueenBlackClicked_plus4 = 0
        self.QueenBlackClicked_plus5 = 0
        self.QueenBlackClicked_plus6 = 0
        self.QueenBlackClicked_minus8 = 0
        self.QueenBlackClicked_minus16 = 0
        self.QueenBlackClicked_minus24 = 0
        self.QueenBlackClicked_minus32 = 0
        self.QueenBlackClicked_minus40 = 0
        self.QueenBlackClicked_minus48 = 0
        self.QueenBlackClicked_minus1 = 0
        self.QueenBlackClicked_minus2 = 0
        self.QueenBlackClicked_minus3 = 0
        self.QueenBlackClicked_minus4 = 0
        self.QueenBlackClicked_minus5 = 0
        self.QueenBlackClicked_minus6 = 0
        self.QueenBlackClicked_plus8_plus1 = 0
        self.QueenBlackClicked_plus16_plus2 = 0
        self.QueenBlackClicked_plus24_plus3 = 0
        self.QueenBlackClicked_plus32_plus4 = 0
        self.QueenBlackClicked_plus40_plus5 = 0
        self.QueenBlackClicked_plus48_plus6 = 0
        self.QueenBlackClicked_plus8_minus1 = 0
        self.QueenBlackClicked_plus16_minus2 = 0
        self.QueenBlackClicked_plus24_minus3 = 0
        self.QueenBlackClicked_plus32_minus4 = 0
        self.QueenBlackClicked_plus40_minus5 = 0
        self.QueenBlackClicked_plus48_minus6 = 0
        self.QueenBlackClicked_minus8_plus1 = 0
        self.QueenBlackClicked_minus16_plus2 = 0
        self.QueenBlackClicked_minus24_plus3 = 0
        self.QueenBlackClicked_minus32_plus4 = 0
        self.QueenBlackClicked_minus40_plus5 = 0
        self.QueenBlackClicked_minus48_plus6 = 0
        self.QueenBlackClicked_minus8_minus1 = 0
        self.QueenBlackClicked_minus16_minus2 = 0
        self.QueenBlackClicked_minus24_minus3 = 0
        self.QueenBlackClicked_minus32_minus4 = 0
        self.QueenBlackClicked_minus40_minus5 = 0
        self.QueenBlackClicked_minus48_minus6 = 0
        self.QueenBlackClicked_cut = 0

        # white pieces variables
        self.pawnWhite1Clicked = 0
        self.pawnWhite1Clicked_plus8 = 0
        self.pawnWhite1Clicked_twoStep = 0
        self.pawnWhite1Clicked_cut = 0

        self.pawnWhite2Clicked = 0
        self.pawnWhite2Clicked_plus8 = 0
        self.pawnWhite2Clicked_twoStep = 0
        self.pawnWhite2Clicked_cut = 0

        self.pawnWhite3Clicked = 0
        self.pawnWhite3Clicked_plus8 = 0
        self.pawnWhite3Clicked_twoStep = 0
        self.pawnWhite3Clicked_cut = 0

        self.pawnWhite4Clicked = 0
        self.pawnWhite4Clicked_plus8 = 0
        self.pawnWhite4Clicked_twoStep = 0
        self.pawnWhite4Clicked_cut = 0

        self.pawnWhite5Clicked = 0
        self.pawnWhite5Clicked_plus8 = 0
        self.pawnWhite5Clicked_twoStep = 0
        self.pawnWhite5Clicked_cut = 0

        self.pawnWhite6Clicked = 0
        self.pawnWhite6Clicked_plus8 = 0
        self.pawnWhite6Clicked_twoStep = 0
        self.pawnWhite6Clicked_cut = 0

        self.pawnWhite7Clicked = 0
        self.pawnWhite7Clicked_plus8 = 0
        self.pawnWhite7Clicked_twoStep = 0
        self.pawnWhite7Clicked_cut = 0

        self.pawnWhite8Clicked = 0
        self.pawnWhite8Clicked_plus8 = 0
        self.pawnWhite8Clicked_twoStep = 0
        self.pawnWhite8Clicked_cut = 0

        self.KingWhiteClicked = 0
        self.KingWhiteClicked_cut = 0

        self.knightWhite1Clicked = 0
        self.knightWhite1Clicked_cut = 0

        self.knightWhite2Clicked = 0
        self.knightWhite2Clicked_cut = 0

        self.rookWhite1Clicked = 0
        self.rookWhite1Clicked_plus8 = 0
        self.rookWhite1Clicked_plus16 = 0
        self.rookWhite1Clicked_plus24 = 0
        self.rookWhite1Clicked_plus32 = 0
        self.rookWhite1Clicked_plus40 = 0
        self.rookWhite1Clicked_plus48 = 0
        self.rookWhite1Clicked_plus1 = 0
        self.rookWhite1Clicked_plus2 = 0
        self.rookWhite1Clicked_plus3 = 0
        self.rookWhite1Clicked_plus4 = 0
        self.rookWhite1Clicked_plus5 = 0
        self.rookWhite1Clicked_plus6 = 0
        self.rookWhite1Clicked_minus8 = 0
        self.rookWhite1Clicked_minus16 = 0
        self.rookWhite1Clicked_minus24 = 0
        self.rookWhite1Clicked_minus32 = 0
        self.rookWhite1Clicked_minus40 = 0
        self.rookWhite1Clicked_minus48 = 0
        self.rookWhite1Clicked_minus1 = 0
        self.rookWhite1Clicked_minus2 = 0
        self.rookWhite1Clicked_minus3 = 0
        self.rookWhite1Clicked_minus4 = 0
        self.rookWhite1Clicked_minus5 = 0
        self.rookWhite1Clicked_minus6 = 0
        self.rookWhite1Clicked_cut = 0

        self.rookWhite2Clicked = 0
        self.rookWhite2Clicked_plus8 = 0
        self.rookWhite2Clicked_plus16 = 0
        self.rookWhite2Clicked_plus24 = 0
        self.rookWhite2Clicked_plus32 = 0
        self.rookWhite2Clicked_plus40 = 0
        self.rookWhite2Clicked_plus48 = 0
        self.rookWhite2Clicked_plus1 = 0
        self.rookWhite2Clicked_plus2 = 0
        self.rookWhite2Clicked_plus3 = 0
        self.rookWhite2Clicked_plus4 = 0
        self.rookWhite2Clicked_plus5 = 0
        self.rookWhite2Clicked_plus6 = 0
        self.rookWhite2Clicked_minus8 = 0
        self.rookWhite2Clicked_minus16 = 0
        self.rookWhite2Clicked_minus24 = 0
        self.rookWhite2Clicked_minus32 = 0
        self.rookWhite2Clicked_minus40 = 0
        self.rookWhite2Clicked_minus48 = 0
        self.rookWhite2Clicked_minus1 = 0
        self.rookWhite2Clicked_minus2 = 0
        self.rookWhite2Clicked_minus3 = 0
        self.rookWhite2Clicked_minus4 = 0
        self.rookWhite2Clicked_minus5 = 0
        self.rookWhite2Clicked_minus6 = 0
        self.rookWhite2Clicked_cut = 0

        self.bishopWhite1Clicked = 0
        self.bishopWhite1Clicked_plus8_plus1 = 0
        self.bishopWhite1Clicked_plus16_plus2 = 0
        self.bishopWhite1Clicked_plus24_plus3 = 0
        self.bishopWhite1Clicked_plus32_plus4 = 0
        self.bishopWhite1Clicked_plus40_plus5 = 0
        self.bishopWhite1Clicked_plus48_plus6 = 0
        self.bishopWhite1Clicked_plus8_minus1 = 0
        self.bishopWhite1Clicked_plus16_minus2 = 0
        self.bishopWhite1Clicked_plus24_minus3 = 0
        self.bishopWhite1Clicked_plus32_minus4 = 0
        self.bishopWhite1Clicked_plus40_minus5 = 0
        self.bishopWhite1Clicked_plus48_minus6 = 0
        self.bishopWhite1Clicked_minus8_plus1 = 0
        self.bishopWhite1Clicked_minus16_plus2 = 0
        self.bishopWhite1Clicked_minus24_plus3 = 0
        self.bishopWhite1Clicked_minus32_plus4 = 0
        self.bishopWhite1Clicked_minus40_plus5 = 0
        self.bishopWhite1Clicked_minus48_plus6 = 0
        self.bishopWhite1Clicked_minus8_minus1 = 0
        self.bishopWhite1Clicked_minus16_minus2 = 0
        self.bishopWhite1Clicked_minus24_minus3 = 0
        self.bishopWhite1Clicked_minus32_minus4 = 0
        self.bishopWhite1Clicked_minus40_minus5 = 0
        self.bishopWhite1Clicked_minus48_minus6 = 0
        self.bishopWhite1Clicked_cut = 0

        self.bishopWhite2Clicked = 0
        self.bishopWhite2Clicked_plus8_plus1 = 0
        self.bishopWhite2Clicked_plus16_plus2 = 0
        self.bishopWhite2Clicked_plus24_plus3 = 0
        self.bishopWhite2Clicked_plus32_plus4 = 0
        self.bishopWhite2Clicked_plus40_plus5 = 0
        self.bishopWhite2Clicked_plus48_plus6 = 0
        self.bishopWhite2Clicked_plus8_minus1 = 0
        self.bishopWhite2Clicked_plus16_minus2 = 0
        self.bishopWhite2Clicked_plus24_minus3 = 0
        self.bishopWhite2Clicked_plus32_minus4 = 0
        self.bishopWhite2Clicked_plus40_minus5 = 0
        self.bishopWhite2Clicked_plus48_minus6 = 0
        self.bishopWhite2Clicked_minus8_plus1 = 0
        self.bishopWhite2Clicked_minus16_plus2 = 0
        self.bishopWhite2Clicked_minus24_plus3 = 0
        self.bishopWhite2Clicked_minus32_plus4 = 0
        self.bishopWhite2Clicked_minus40_plus5 = 0
        self.bishopWhite2Clicked_minus48_plus6 = 0
        self.bishopWhite2Clicked_minus8_minus1 = 0
        self.bishopWhite2Clicked_minus16_minus2 = 0
        self.bishopWhite2Clicked_minus24_minus3 = 0
        self.bishopWhite2Clicked_minus32_minus4 = 0
        self.bishopWhite2Clicked_minus40_minus5 = 0
        self.bishopWhite2Clicked_minus48_minus6 = 0
        self.bishopWhite2Clicked_cut = 0

        self.QueenWhiteClicked = 0
        self.QueenWhiteClicked_plus8 = 0
        self.QueenWhiteClicked_plus16 = 0
        self.QueenWhiteClicked_plus24 = 0
        self.QueenWhiteClicked_plus32 = 0
        self.QueenWhiteClicked_plus40 = 0
        self.QueenWhiteClicked_plus48 = 0
        self.QueenWhiteClicked_plus1 = 0
        self.QueenWhiteClicked_plus2 = 0
        self.QueenWhiteClicked_plus3 = 0
        self.QueenWhiteClicked_plus4 = 0
        self.QueenWhiteClicked_plus5 = 0
        self.QueenWhiteClicked_plus6 = 0
        self.QueenWhiteClicked_minus8 = 0
        self.QueenWhiteClicked_minus16 = 0
        self.QueenWhiteClicked_minus24 = 0
        self.QueenWhiteClicked_minus32 = 0
        self.QueenWhiteClicked_minus40 = 0
        self.QueenWhiteClicked_minus48 = 0
        self.QueenWhiteClicked_minus1 = 0
        self.QueenWhiteClicked_minus2 = 0
        self.QueenWhiteClicked_minus3 = 0
        self.QueenWhiteClicked_minus4 = 0
        self.QueenWhiteClicked_minus5 = 0
        self.QueenWhiteClicked_minus6 = 0
        self.QueenWhiteClicked_plus8_plus1 = 0
        self.QueenWhiteClicked_plus16_plus2 = 0
        self.QueenWhiteClicked_plus24_plus3 = 0
        self.QueenWhiteClicked_plus32_plus4 = 0
        self.QueenWhiteClicked_plus40_plus5 = 0
        self.QueenWhiteClicked_plus48_plus6 = 0
        self.QueenWhiteClicked_plus8_minus1 = 0
        self.QueenWhiteClicked_plus16_minus2 = 0
        self.QueenWhiteClicked_plus24_minus3 = 0
        self.QueenWhiteClicked_plus32_minus4 = 0
        self.QueenWhiteClicked_plus40_minus5 = 0
        self.QueenWhiteClicked_plus48_minus6 = 0
        self.QueenWhiteClicked_minus8_plus1 = 0
        self.QueenWhiteClicked_minus16_plus2 = 0
        self.QueenWhiteClicked_minus24_plus3 = 0
        self.QueenWhiteClicked_minus32_plus4 = 0
        self.QueenWhiteClicked_minus40_plus5 = 0
        self.QueenWhiteClicked_minus48_plus6 = 0
        self.QueenWhiteClicked_minus8_minus1 = 0
        self.QueenWhiteClicked_minus16_minus2 = 0
        self.QueenWhiteClicked_minus24_minus3 = 0
        self.QueenWhiteClicked_minus32_minus4 = 0
        self.QueenWhiteClicked_minus40_minus5 = 0
        self.QueenWhiteClicked_minus48_minus6 = 0
        self.QueenWhiteClicked_cut = 0

        self.turn = "black"


pos = Positions()


# draw the chess board
def drawChessBoard():
    for whiteBoxPos in pos.whiteBoxLst:
        pygame.draw.rect(window, white, whiteBoxPos)
    for greyBoxPos in pos.greyBoxLst:
        pygame.draw.rect(window, grey, greyBoxPos)


# draw the pieces on board
def drawPieces():
    window.blit(assets['rb'], pos.rb1)
    window.blit(assets['rb'], pos.rb2)
    window.blit(assets['kb'], pos.kb1)
    window.blit(assets['kb'], pos.kb2)
    window.blit(assets['bb'], pos.bb1)
    window.blit(assets['bb'], pos.bb2)
    window.blit(assets['Kb'], pos.Kb)
    window.blit(assets['Qb'], pos.Qb)

    window.blit(assets['pb'], pos.pb1)
    window.blit(assets['pb'], pos.pb2)
    window.blit(assets['pb'], pos.pb3)
    window.blit(assets['pb'], pos.pb4)
    window.blit(assets['pb'], pos.pb5)
    window.blit(assets['pb'], pos.pb6)
    window.blit(assets['pb'], pos.pb7)
    window.blit(assets['pb'], pos.pb8)

    window.blit(assets['pw'], pos.pw1)
    window.blit(assets['pw'], pos.pw2)
    window.blit(assets['pw'], pos.pw3)
    window.blit(assets['pw'], pos.pw4)
    window.blit(assets['pw'], pos.pw5)
    window.blit(assets['pw'], pos.pw6)
    window.blit(assets['pw'], pos.pw7)
    window.blit(assets['pw'], pos.pw8)

    window.blit(assets['rw'], pos.rw1)
    window.blit(assets['rw'], pos.rw2)
    window.blit(assets['kw'], pos.kw1)
    window.blit(assets['kw'], pos.kw2)
    window.blit(assets['bw'], pos.bw1)
    window.blit(assets['bw'], pos.bw2)
    window.blit(assets['Kw'], pos.Kw)
    window.blit(assets['Qw'], pos.Qw)


# variables for addressing mouse position -> (x, y)
mouse_x = -1
mouse_y = -1


# returns mouse x, y co-ordinates
def get_pos():
    global mouse_x, mouse_y

    if pygame.mouse.get_pressed(3)[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
    return [mouse_x, mouse_y]


# checks if next positions are empty or not
def check_pawn_next_pos(which_pawn_clicked):
    mouse_pos = get_pos()

    if which_pawn_clicked.collidepoint(mouse_pos[0], mouse_pos[1]):
        if which_pawn_clicked.y < pos.box_dict["box57"].y:
            if not pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw3) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw4) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw5) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw6) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw7) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw8) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.Kw) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.Qw) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.rw1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.rw2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.kw1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.kw2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.bw1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.bw2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb3) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb4) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb5) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb6) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb7) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb8) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.Kb) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.Qb) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.rb1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.rb2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.kb1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.kb2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.bb1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.bb2):
                pygame.draw.rect(window, blue, pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8], border_radius=100)
                if which_pawn_clicked == pos.pb1:
                    pos.pawnBlack1Clicked = 1
                    pos.pawnBlack1Clicked_plus8 = 1
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.QueenBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                elif which_pawn_clicked == pos.pb2:
                    pos.pawnBlack2Clicked = 1
                    pos.pawnBlack2Clicked_plus8 = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb3:
                    pos.pawnBlack3Clicked = 1
                    pos.pawnBlack3Clicked_plus8 = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb4:
                    pos.pawnBlack4Clicked = 1
                    pos.pawnBlack4Clicked_plus8 = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb5:
                    pos.pawnBlack5Clicked = 1
                    pos.pawnBlack5Clicked_plus8 = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb6:
                    pos.pawnBlack6Clicked = 1
                    pos.pawnBlack6Clicked_plus8 = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb7:
                    pos.pawnBlack7Clicked = 1
                    pos.pawnBlack7Clicked_plus8 = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb8:
                    pos.pawnBlack8Clicked = 1
                    pos.pawnBlack8Clicked_plus8 = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
            if which_pawn_clicked.y < pos.box_dict["box17"].y:
                if pos.pawnBlack1Clicked_plus8 == 1 or pos.pawnBlack2Clicked_plus8 == 1 or pos.pawnBlack3Clicked_plus8 == 1 or pos.pawnBlack4Clicked_plus8 == 1 or pos.pawnBlack3Clicked_plus8 == 1 \
                        or pos.pawnBlack6Clicked_plus8 == 1 or pos.pawnBlack7Clicked_plus8 == 1 or pos.pawnBlack8Clicked_plus8 == 1:
                    if not pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw3) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw4) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw5) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw6) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw7) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw8) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.Kw) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.Qw) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.rw1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.rw2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.kw1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.kw2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.bw1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.bw2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb3) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb4) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb5) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb6) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb7) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb8) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.Kb) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.Qb) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.rb1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.rb2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.kb1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.kb2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.bb1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.bb2):
                        pygame.draw.rect(window, blue, pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16], border_radius=100)
                        if which_pawn_clicked == pos.pb1:
                            pos.pawnBlack1Clicked = 1
                            pos.pawnBlack1Clicked_twoStep = 1
                            pos.pawnBlack2Clicked = 0
                            pos.pawnBlack3Clicked = 0
                            pos.pawnBlack4Clicked = 0
                            pos.pawnBlack5Clicked = 0
                            pos.pawnBlack6Clicked = 0
                            pos.pawnBlack7Clicked = 0
                            pos.pawnBlack8Clicked = 0
                            pos.KingBlackClicked = 0
                            pos.QueenBlackClicked = 0
                            pos.knightBlack1Clicked = 0
                            pos.knightBlack2Clicked = 0
                            pos.rookBlack1Clicked = 0
                            pos.rookBlack2Clicked = 0
                            pos.bishopBlack1Clicked = 0
                            pos.bishopBlack2Clicked = 0
                        elif which_pawn_clicked == pos.pb2:
                            pos.pawnBlack2Clicked = 1
                            pos.pawnBlack2Clicked_twoStep = 1
                            pos.pawnBlack1Clicked = 0
                            pos.pawnBlack3Clicked = 0
                            pos.pawnBlack4Clicked = 0
                            pos.pawnBlack5Clicked = 0
                            pos.pawnBlack6Clicked = 0
                            pos.pawnBlack7Clicked = 0
                            pos.pawnBlack8Clicked = 0
                            pos.KingBlackClicked = 0
                            pos.QueenBlackClicked = 0
                            pos.knightBlack1Clicked = 0
                            pos.knightBlack2Clicked = 0
                            pos.rookBlack1Clicked = 0
                            pos.rookBlack2Clicked = 0
                            pos.bishopBlack1Clicked = 0
                            pos.bishopBlack2Clicked = 0
                        elif which_pawn_clicked == pos.pb3:
                            pos.pawnBlack3Clicked = 1
                            pos.pawnBlack3Clicked_twoStep = 1
                            pos.pawnBlack1Clicked = 0
                            pos.pawnBlack2Clicked = 0
                            pos.pawnBlack4Clicked = 0
                            pos.pawnBlack5Clicked = 0
                            pos.pawnBlack6Clicked = 0
                            pos.pawnBlack7Clicked = 0
                            pos.pawnBlack8Clicked = 0
                            pos.KingBlackClicked = 0
                            pos.QueenBlackClicked = 0
                            pos.knightBlack1Clicked = 0
                            pos.knightBlack2Clicked = 0
                            pos.rookBlack1Clicked = 0
                            pos.rookBlack2Clicked = 0
                            pos.bishopBlack1Clicked = 0
                            pos.bishopBlack2Clicked = 0
                        elif which_pawn_clicked == pos.pb4:
                            pos.pawnBlack4Clicked = 1
                            pos.pawnBlack4Clicked_twoStep = 1
                            pos.pawnBlack1Clicked = 0
                            pos.pawnBlack2Clicked = 0
                            pos.pawnBlack3Clicked = 0
                            pos.pawnBlack5Clicked = 0
                            pos.pawnBlack6Clicked = 0
                            pos.pawnBlack7Clicked = 0
                            pos.pawnBlack8Clicked = 0
                            pos.KingBlackClicked = 0
                            pos.QueenBlackClicked = 0
                            pos.knightBlack1Clicked = 0
                            pos.knightBlack2Clicked = 0
                            pos.rookBlack1Clicked = 0
                            pos.rookBlack2Clicked = 0
                            pos.bishopBlack1Clicked = 0
                            pos.bishopBlack2Clicked = 0
                        elif which_pawn_clicked == pos.pb5:
                            pos.pawnBlack5Clicked = 1
                            pos.pawnBlack5Clicked_twoStep = 1
                            pos.pawnBlack1Clicked = 0
                            pos.pawnBlack2Clicked = 0
                            pos.pawnBlack3Clicked = 0
                            pos.pawnBlack4Clicked = 0
                            pos.pawnBlack6Clicked = 0
                            pos.pawnBlack7Clicked = 0
                            pos.pawnBlack8Clicked = 0
                            pos.KingBlackClicked = 0
                            pos.QueenBlackClicked = 0
                            pos.knightBlack1Clicked = 0
                            pos.knightBlack2Clicked = 0
                            pos.rookBlack1Clicked = 0
                            pos.rookBlack2Clicked = 0
                            pos.bishopBlack1Clicked = 0
                            pos.bishopBlack2Clicked = 0
                        elif which_pawn_clicked == pos.pb6:
                            pos.pawnBlack6Clicked = 1
                            pos.pawnBlack6Clicked_twoStep = 1
                            pos.pawnBlack1Clicked = 0
                            pos.pawnBlack2Clicked = 0
                            pos.pawnBlack3Clicked = 0
                            pos.pawnBlack4Clicked = 0
                            pos.pawnBlack5Clicked = 0
                            pos.pawnBlack7Clicked = 0
                            pos.pawnBlack8Clicked = 0
                            pos.KingBlackClicked = 0
                            pos.QueenBlackClicked = 0
                            pos.knightBlack1Clicked = 0
                            pos.knightBlack2Clicked = 0
                            pos.rookBlack1Clicked = 0
                            pos.rookBlack2Clicked = 0
                            pos.bishopBlack1Clicked = 0
                            pos.bishopBlack2Clicked = 0
                        elif which_pawn_clicked == pos.pb7:
                            pos.pawnBlack7Clicked = 1
                            pos.pawnBlack7Clicked_twoStep = 1
                            pos.pawnBlack1Clicked = 0
                            pos.pawnBlack2Clicked = 0
                            pos.pawnBlack3Clicked = 0
                            pos.pawnBlack4Clicked = 0
                            pos.pawnBlack5Clicked = 0
                            pos.pawnBlack6Clicked = 0
                            pos.pawnBlack8Clicked = 0
                            pos.KingBlackClicked = 0
                            pos.QueenBlackClicked = 0
                            pos.knightBlack1Clicked = 0
                            pos.knightBlack2Clicked = 0
                            pos.rookBlack1Clicked = 0
                            pos.rookBlack2Clicked = 0
                            pos.bishopBlack1Clicked = 0
                            pos.bishopBlack2Clicked = 0
                        elif which_pawn_clicked == pos.pb8:
                            pos.pawnBlack8Clicked = 1
                            pos.pawnBlack8Clicked_twoStep = 1
                            pos.pawnBlack1Clicked = 0
                            pos.pawnBlack2Clicked = 0
                            pos.pawnBlack3Clicked = 0
                            pos.pawnBlack4Clicked = 0
                            pos.pawnBlack5Clicked = 0
                            pos.pawnBlack6Clicked = 0
                            pos.pawnBlack7Clicked = 0
                            pos.KingBlackClicked = 0
                            pos.QueenBlackClicked = 0
                            pos.knightBlack1Clicked = 0
                            pos.knightBlack2Clicked = 0
                            pos.rookBlack1Clicked = 0
                            pos.rookBlack2Clicked = 0
                            pos.bishopBlack1Clicked = 0
                            pos.bishopBlack2Clicked = 0
                    elif pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw3) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw4) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw5) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw6) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw7) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pw8) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.Kw) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.Qw) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.rw1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.rw2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.kw1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.kw2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.bw1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.bw2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb3) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb4) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb5) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb6) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb7) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.pb8) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.Kb) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.Qb) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.rb1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.rb2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.kb1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.kb2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.bb1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 16].colliderect(pos.bb2):
                        if which_pawn_clicked == pos.pb1:
                            pos.pawnBlack1Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pb2:
                            pos.pawnBlack2Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pb3:
                            pos.pawnBlack3Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pb4:
                            pos.pawnBlack4Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pb5:
                            pos.pawnBlack5Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pb6:
                            pos.pawnBlack6Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pb7:
                            pos.pawnBlack7Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pb8:
                            pos.pawnBlack8Clicked_twoStep = 0
        if which_pawn_clicked.y < pos.box_dict["box57"].y:
            if pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw3) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw4) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw5) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw6) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw7) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pw8) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.Kw) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.Qw) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.rw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.rw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.kw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.kw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.bw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.bw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb3) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb4) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb5) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb6) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb7) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.pb8) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.Kb) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.Qb) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.rb1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.rb2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.kb1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.kb2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.bb1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8].colliderect(pos.bb2):
                if which_pawn_clicked == pos.pb1:
                    pos.pawnBlack1Clicked = 0
                elif which_pawn_clicked == pos.pb2:
                    pos.pawnBlack2Clicked = 0
                elif which_pawn_clicked == pos.pb3:
                    pos.pawnBlack3Clicked = 0
                elif which_pawn_clicked == pos.pb4:
                    pos.pawnBlack4Clicked = 0
                elif which_pawn_clicked == pos.pb5:
                    pos.pawnBlack5Clicked = 0
                elif which_pawn_clicked == pos.pb6:
                    pos.pawnBlack6Clicked = 0
                elif which_pawn_clicked == pos.pb7:
                    pos.pawnBlack7Clicked = 0
                elif which_pawn_clicked == pos.pb8:
                    pos.pawnBlack8Clicked = 0
        if 0 * boxSize <= which_pawn_clicked.x <= 6 * boxSize and which_pawn_clicked.y < pos.box_dict["box57"].y:
            if pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.pw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.pw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.pw3) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.pw4) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.pw5) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.pw6) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.pw7) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.pw8) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.Kw) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.Qw) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.rw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.rw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.kw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.kw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.bw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1].colliderect(pos.bw2):
                pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 + 1], border_radius=100)
                if which_pawn_clicked == pos.pb1:
                    pos.pawnBlack1Clicked = 1
                    pos.pawnBlack1Clicked_cut = 1
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb2:
                    pos.pawnBlack2Clicked = 1
                    pos.pawnBlack2Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb3:
                    pos.pawnBlack3Clicked = 1
                    pos.pawnBlack3Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb4:
                    pos.pawnBlack4Clicked = 1
                    pos.pawnBlack4Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb5:
                    pos.pawnBlack5Clicked = 1
                    pos.pawnBlack5Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb6:
                    pos.pawnBlack6Clicked = 1
                    pos.pawnBlack6Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb7:
                    pos.pawnBlack7Clicked = 1
                    pos.pawnBlack7Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb8:
                    pos.pawnBlack8Clicked = 1
                    pos.pawnBlack8Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
        if 1 * boxSize <= which_pawn_clicked.x <= 7 * boxSize and which_pawn_clicked.y < pos.box_dict["box57"].y:
            if pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.pw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.pw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.pw3) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.pw4) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.pw5) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.pw6) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.pw7) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.pw8) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.Kw) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.Qw) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.rw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.rw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.kw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.kw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.bw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1].colliderect(pos.bw2):
                pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(which_pawn_clicked) + 8 - 1], border_radius=100)
                if which_pawn_clicked == pos.pb1:
                    pos.pawnBlack1Clicked = 1
                    pos.pawnBlack1Clicked_cut = 1
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb2:
                    pos.pawnBlack2Clicked = 1
                    pos.pawnBlack2Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb3:
                    pos.pawnBlack3Clicked = 1
                    pos.pawnBlack3Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb4:
                    pos.pawnBlack4Clicked = 1
                    pos.pawnBlack4Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb5:
                    pos.pawnBlack5Clicked = 1
                    pos.pawnBlack5Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb6:
                    pos.pawnBlack6Clicked = 1
                    pos.pawnBlack6Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                    pos.QueenBlackClicked = 0
                elif which_pawn_clicked == pos.pb7:
                    pos.pawnBlack7Clicked = 1
                    pos.pawnBlack7Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack8Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.QueenBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0
                elif which_pawn_clicked == pos.pb8:
                    pos.pawnBlack8Clicked = 1
                    pos.pawnBlack8Clicked_cut = 1
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack7Clicked = 0
                    pos.KingBlackClicked = 0
                    pos.QueenBlackClicked = 0
                    pos.knightBlack1Clicked = 0
                    pos.knightBlack2Clicked = 0
                    pos.rookBlack1Clicked = 0
                    pos.rookBlack2Clicked = 0
                    pos.bishopBlack1Clicked = 0
                    pos.bishopBlack2Clicked = 0


# remove the pieces if cut
def check_cut_piece(who_cuts):
    mouse_pos = get_pos()

    if who_cuts.x < pos.box_dict["box8"].x and who_cuts.y < pos.box_dict["box57"].y:
        if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].collidepoint(mouse_pos[0], mouse_pos[1]):
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.pw1):
                pos.pw1 = pos.white_deadPieceRect_dict["whiteCutPiece_1"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.pw2):
                pos.pw2 = pos.white_deadPieceRect_dict["whiteCutPiece_2"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.pw3):
                pos.pw3 = pos.white_deadPieceRect_dict["whiteCutPiece_3"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.pw4):
                pos.pw4 = pos.white_deadPieceRect_dict["whiteCutPiece_4"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.pw5):
                pos.pw5 = pos.white_deadPieceRect_dict["whiteCutPiece_5"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.pw6):
                pos.pw6 = pos.white_deadPieceRect_dict["whiteCutPiece_6"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.pw7):
                pos.pw7 = pos.white_deadPieceRect_dict["whiteCutPiece_7"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.pw8):
                pos.pw8 = pos.white_deadPieceRect_dict["whiteCutPiece_8"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.rw1):
                pos.rw1 = pos.white_deadPieceRect_dict["whiteCutPiece_9"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.rw2):
                pos.rw2 = pos.white_deadPieceRect_dict["whiteCutPiece_10"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.kw1):
                pos.kw1 = pos.white_deadPieceRect_dict["whiteCutPiece_11"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.kw2):
                pos.kw2 = pos.white_deadPieceRect_dict["whiteCutPiece_12"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.bw1):
                pos.bw1 = pos.white_deadPieceRect_dict["whiteCutPiece_13"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.bw2):
                pos.bw2 = pos.white_deadPieceRect_dict["whiteCutPiece_14"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.Kw):
                pos.Kw = pos.white_deadPieceRect_dict["whiteCutPiece_15"]
                pos.KingWhite_isDead = 1
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1].colliderect(pos.Qw):
                pos.Qw = pos.white_deadPieceRect_dict["whiteCutPiece_16"]

            if who_cuts == pos.pb1:
                pos.pb1 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1]
                pos.pawnBlack1Clicked = 0
                pos.pawnBlack1Clicked_cut = 0
            elif who_cuts == pos.pb2:
                pos.pb2 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1]
                pos.pawnBlack2Clicked = 0
                pos.pawnBlack2Clicked_cut = 0
            elif who_cuts == pos.pb3:
                pos.pb3 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1]
                pos.pawnBlack3Clicked = 0
                pos.pawnBlack3Clicked_cut = 0
            elif who_cuts == pos.pb4:
                pos.pb4 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1]
                pos.pawnBlack4Clicked = 0
                pos.pawnBlack4Clicked_cut = 0
            elif who_cuts == pos.pb5:
                pos.pb5 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1]
                pos.pawnBlack5Clicked = 0
                pos.pawnBlack5Clicked_cut = 0
            elif who_cuts == pos.pb6:
                pos.pb6 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1]
                pos.pawnBlack6Clicked = 0
                pos.pawnBlack6Clicked_cut = 0
            elif who_cuts == pos.pb7:
                pos.pb7 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1]
                pos.pawnBlack7Clicked = 0
                pos.pawnBlack7Clicked_cut = 0
            elif who_cuts == pos.pb8:
                pos.pb8 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 + 1]
                pos.pawnBlack8Clicked = 0
                pos.pawnBlack8Clicked_cut = 0
            pos.turn = "white"

    if pos.box_dict["box1"].x <= who_cuts.x and who_cuts.y < pos.box_dict["box57"].y:
        if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].collidepoint(mouse_pos[0], mouse_pos[1]):
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.pw1):
                pos.pw1 = pos.white_deadPieceRect_dict["whiteCutPiece_1"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.pw2):
                pos.pw2 = pos.white_deadPieceRect_dict["whiteCutPiece_2"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.pw3):
                pos.pw3 = pos.white_deadPieceRect_dict["whiteCutPiece_3"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.pw4):
                pos.pw4 = pos.white_deadPieceRect_dict["whiteCutPiece_4"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.pw5):
                pos.pw5 = pos.white_deadPieceRect_dict["whiteCutPiece_5"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.pw6):
                pos.pw6 = pos.white_deadPieceRect_dict["whiteCutPiece_6"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.pw7):
                pos.pw7 = pos.white_deadPieceRect_dict["whiteCutPiece_7"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.pw8):
                pos.pw8 = pos.white_deadPieceRect_dict["whiteCutPiece_8"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.rw1):
                pos.rw1 = pos.white_deadPieceRect_dict["whiteCutPiece_9"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.rw2):
                pos.rw2 = pos.white_deadPieceRect_dict["whiteCutPiece_10"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.kw1):
                pos.kw1 = pos.white_deadPieceRect_dict["whiteCutPiece_11"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.kw2):
                pos.kw2 = pos.white_deadPieceRect_dict["whiteCutPiece_12"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.bw1):
                pos.bw1 = pos.white_deadPieceRect_dict["whiteCutPiece_13"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.bw2):
                pos.bw2 = pos.white_deadPieceRect_dict["whiteCutPiece_14"]
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.Kw):
                pos.Kw = pos.white_deadPieceRect_dict["whiteCutPiece_15"]
                pos.KingWhite_isDead = 1
            if pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1].colliderect(pos.Qw):
                pos.Qw = pos.white_deadPieceRect_dict["whiteCutPiece_16"]

            if who_cuts == pos.pb1:
                pos.pb1 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1]
                pos.pawnBlack1Clicked = 0
                pos.pawnBlack1Clicked_cut = 0
            elif who_cuts == pos.pb2:
                pos.pb2 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1]
                pos.pawnBlack2Clicked = 0
                pos.pawnBlack2Clicked_cut = 0
            elif who_cuts == pos.pb3:
                pos.pb3 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1]
                pos.pawnBlack3Clicked = 0
                pos.pawnBlack3Clicked_cut = 0
            elif who_cuts == pos.pb4:
                pos.pb4 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1]
                pos.pawnBlack4Clicked = 0
                pos.pawnBlack4Clicked_cut = 0
            elif who_cuts == pos.pb5:
                pos.pb5 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1]
                pos.pawnBlack5Clicked = 0
                pos.pawnBlack5Clicked_cut = 0
            elif who_cuts == pos.pb6:
                pos.pb6 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1]
                pos.pawnBlack6Clicked = 0
                pos.pawnBlack6Clicked_cut = 0
            elif who_cuts == pos.pb7:
                pos.pb7 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1]
                pos.pawnBlack7Clicked = 0
                pos.pawnBlack7Clicked_cut = 0
            elif who_cuts == pos.pb8:
                pos.pb8 = pos.boxLst[pos.boxLst.index(who_cuts) + 8 - 1]
                pos.pawnBlack8Clicked = 0
                pos.pawnBlack8Clicked_cut = 0
            pos.turn = "white"


def pawnBMovements():
    mouse_pos = get_pos()

    if pos.turn == "white":
        pos.pawnBlack1Clicked_plus8 = 0
        pos.pawnBlack2Clicked_plus8 = 0
        pos.pawnBlack3Clicked_plus8 = 0
        pos.pawnBlack4Clicked_plus8 = 0
        pos.pawnBlack5Clicked_plus8 = 0
        pos.pawnBlack6Clicked_plus8 = 0
        pos.pawnBlack7Clicked_plus8 = 0
        pos.pawnBlack8Clicked_plus8 = 0
        
    if pos.turn == "black":
        check_pawn_next_pos(pos.pb1)
        check_pawn_next_pos(pos.pb2)
        check_pawn_next_pos(pos.pb3)
        check_pawn_next_pos(pos.pb4)
        check_pawn_next_pos(pos.pb5)
        check_pawn_next_pos(pos.pb6)
        check_pawn_next_pos(pos.pb7)
        check_pawn_next_pos(pos.pb8)

    if pos.pawnBlack1Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pb1) + 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pb1 = pos.boxLst[pos.boxLst.index(pos.pb1) + 8]
            pos.pawnBlack1Clicked = 0
            pos.turn = "white"
        if pos.pawnBlack1Clicked_cut == 1:
            check_cut_piece(pos.pb1)
        if pos.pb1.y < pos.box_dict["box49"].y:
            if pos.pawnBlack1Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pb1) + 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pb1 = pos.boxLst[pos.boxLst.index(pos.pb1) + 16]
                    pos.pawnBlack1Clicked = 0
                    pos.pawnBlack1Clicked_twoStep = 0
                    pos.turn = "white"

    elif pos.pawnBlack2Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pb2) + 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pb2 = pos.boxLst[pos.boxLst.index(pos.pb2) + 8]
            pos.pawnBlack2Clicked = 0
            pos.turn = "white"
        if pos.pawnBlack2Clicked_cut == 1:
            check_cut_piece(pos.pb2)
        if pos.pb2.y < pos.box_dict["box49"].y:
            if pos.pawnBlack2Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pb2) + 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pb2 = pos.boxLst[pos.boxLst.index(pos.pb2) + 16]
                    pos.pawnBlack2Clicked = 0
                    pos.pawnBlack2Clicked_twoStep = 0
                    pos.turn = "white"

    elif pos.pawnBlack3Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pb3) + 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pb3 = pos.boxLst[pos.boxLst.index(pos.pb3) + 8]
            pos.pawnBlack3Clicked = 0
            pos.turn = "white"
        if pos.pawnBlack3Clicked_cut == 1:
            check_cut_piece(pos.pb3)
        if pos.pb3.y < pos.box_dict["box49"].y:
            if pos.pawnBlack3Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pb3) + 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pb3 = pos.boxLst[pos.boxLst.index(pos.pb3) + 16]
                    pos.pawnBlack3Clicked = 0
                    pos.pawnBlack3Clicked_twoStep = 0
                    pos.turn = "white"

    elif pos.pawnBlack4Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pb4) + 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pb4 = pos.boxLst[pos.boxLst.index(pos.pb4) + 8]
            pos.pawnBlack4Clicked = 0
            pos.turn = "white"
        if pos.pawnBlack4Clicked_cut == 1:
            check_cut_piece(pos.pb4)
        if pos.pb4.y < pos.box_dict["box49"].y:
            if pos.pawnBlack4Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pb4) + 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pb4 = pos.boxLst[pos.boxLst.index(pos.pb4) + 16]
                    pos.pawnBlack4Clicked = 0
                    pos.pawnBlack4Clicked_twoStep = 0
                    pos.turn = "white"

    elif pos.pawnBlack5Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pb5) + 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pb5 = pos.boxLst[pos.boxLst.index(pos.pb5) + 8]
            pos.pawnBlack5Clicked = 0
            pos.turn = "white"
        if pos.pawnBlack5Clicked_cut == 1:
            check_cut_piece(pos.pb5)
        if pos.pb5.y < pos.box_dict["box49"].y:
            if pos.pawnBlack5Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pb5) + 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pb5 = pos.boxLst[pos.boxLst.index(pos.pb5) + 16]
                    pos.pawnBlack5Clicked = 0
                    pos.pawnBlack5Clicked_twoStep = 0
                    pos.turn = "white"

    elif pos.pawnBlack6Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pb6) + 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pb6 = pos.boxLst[pos.boxLst.index(pos.pb6) + 8]
            pos.pawnBlack6Clicked = 0
            pos.turn = "white"
        if pos.pawnBlack6Clicked_cut == 1:
            check_cut_piece(pos.pb6)
        if pos.pb6.y < pos.box_dict["box49"].y:
            if pos.pawnBlack6Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pb6) + 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pb6 = pos.boxLst[pos.boxLst.index(pos.pb6) + 16]
                    pos.pawnBlack6Clicked = 0
                    pos.pawnBlack6Clicked_twoStep = 0
                    pos.turn = "white"

    elif pos.pawnBlack7Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pb7) + 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pb7 = pos.boxLst[pos.boxLst.index(pos.pb7) + 8]
            pos.pawnBlack7Clicked = 0
            pos.turn = "white"
        if pos.pawnBlack7Clicked_cut == 1:
            check_cut_piece(pos.pb7)
        if pos.pb7.y < pos.box_dict["box49"].y:
            if pos.pawnBlack7Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pb7) + 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pb7 = pos.boxLst[pos.boxLst.index(pos.pb7) + 16]
                    pos.pawnBlack7Clicked = 0
                    pos.pawnBlack7Clicked_twoStep = 0
                    pos.turn = "white"

    elif pos.pawnBlack8Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pb8) + 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pb8 = pos.boxLst[pos.boxLst.index(pos.pb8) + 8]
            pos.pawnBlack8Clicked = 0
            pos.turn = "white"
        if pos.pawnBlack8Clicked_cut == 1:
            check_cut_piece(pos.pb8)
        if pos.pb8.y < pos.box_dict["box49"].y:
            if pos.pawnBlack8Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pb8) + 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pb8 = pos.boxLst[pos.boxLst.index(pos.pb8) + 16]
                    pos.pawnBlack8Clicked = 0
                    pos.pawnBlack8Clicked_twoStep = 0
                    pos.turn = "white"


# contains the functions to be run inside while loop
def drawGameWindow():
    window.fill(white)
    drawChessBoard()
    drawPieces()
    pawnBMovements()


game = MainGame()
# run the game
game.gameLoop()
