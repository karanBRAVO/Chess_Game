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


# checks if black pawns can cuts the white pieces
def check_pawn_black_canCut(which_pawn_clicked, num):
    if pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pw1) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pw2) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pw3) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pw4) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pw5) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pw6) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pw7) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pw8) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.Kw) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.Qw) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.rw1) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.rw2) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.kw1) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.kw2) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.bw1) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.bw2):
        pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num], border_radius=100)
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


# checks if next positions for black pawns are empty or not
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
                if pos.pawnBlack1Clicked_plus8 == 1 or pos.pawnBlack2Clicked_plus8 == 1 or pos.pawnBlack3Clicked_plus8 == 1 or pos.pawnBlack4Clicked_plus8 == 1 or pos.pawnBlack5Clicked_plus8 == 1 \
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
        # check if white pieces are diagonal to black pawn
        if 0 * boxSize <= which_pawn_clicked.x <= 6 * boxSize and which_pawn_clicked.y < pos.box_dict["box57"].y:
            check_pawn_black_canCut(which_pawn_clicked, 8 + 1)
        # check for another diagonal
        if 1 * boxSize <= which_pawn_clicked.x <= 7 * boxSize and which_pawn_clicked.y < pos.box_dict["box57"].y:
            check_pawn_black_canCut(which_pawn_clicked, 8 - 1)


# remove the white pieces if they are at diagonal to black pieces
def check_cut_piece(who_cuts, num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(who_cuts) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw1):
            pos.pw1 = pos.white_deadPieceRect_dict["whiteCutPiece_1"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw2):
            pos.pw2 = pos.white_deadPieceRect_dict["whiteCutPiece_2"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw3):
            pos.pw3 = pos.white_deadPieceRect_dict["whiteCutPiece_3"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw4):
            pos.pw4 = pos.white_deadPieceRect_dict["whiteCutPiece_4"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw5):
            pos.pw5 = pos.white_deadPieceRect_dict["whiteCutPiece_5"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw6):
            pos.pw6 = pos.white_deadPieceRect_dict["whiteCutPiece_6"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw7):
            pos.pw7 = pos.white_deadPieceRect_dict["whiteCutPiece_7"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw8):
            pos.pw8 = pos.white_deadPieceRect_dict["whiteCutPiece_8"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.rw1):
            pos.rw1 = pos.white_deadPieceRect_dict["whiteCutPiece_9"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.rw2):
            pos.rw2 = pos.white_deadPieceRect_dict["whiteCutPiece_10"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.kw1):
            pos.kw1 = pos.white_deadPieceRect_dict["whiteCutPiece_11"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.kw2):
            pos.kw2 = pos.white_deadPieceRect_dict["whiteCutPiece_12"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.bw1):
            pos.bw1 = pos.white_deadPieceRect_dict["whiteCutPiece_13"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.bw2):
            pos.bw2 = pos.white_deadPieceRect_dict["whiteCutPiece_14"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.Kw):
            pos.Kw = pos.white_deadPieceRect_dict["whiteCutPiece_15"]
            pos.KingWhite_isDead = 1
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.Qw):
            pos.Qw = pos.white_deadPieceRect_dict["whiteCutPiece_16"]

        if who_cuts == pos.pb1:
            pos.pb1 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnBlack1Clicked = 0
            pos.pawnBlack1Clicked_cut = 0
        elif who_cuts == pos.pb2:
            pos.pb2 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnBlack2Clicked = 0
            pos.pawnBlack2Clicked_cut = 0
        elif who_cuts == pos.pb3:
            pos.pb3 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnBlack3Clicked = 0
            pos.pawnBlack3Clicked_cut = 0
        elif who_cuts == pos.pb4:
            pos.pb4 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnBlack4Clicked = 0
            pos.pawnBlack4Clicked_cut = 0
        elif who_cuts == pos.pb5:
            pos.pb5 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnBlack5Clicked = 0
            pos.pawnBlack5Clicked_cut = 0
        elif who_cuts == pos.pb6:
            pos.pb6 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnBlack6Clicked = 0
            pos.pawnBlack6Clicked_cut = 0
        elif who_cuts == pos.pb7:
            pos.pb7 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnBlack7Clicked = 0
            pos.pawnBlack7Clicked_cut = 0
        elif who_cuts == pos.pb8:
            pos.pb8 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
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
            if pos.pb1.x < pos.box_dict["box8"].x and pos.pb1.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb1, 8 + 1)
            if pos.box_dict["box1"].x <= pos.pb1.x and pos.pb1.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb1, 8 - 1)
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
            if pos.pb2.x < pos.box_dict["box8"].x and pos.pb2.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb2, 8 + 1)
            if pos.box_dict["box1"].x <= pos.pb2.x and pos.pb2.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb2, 8 - 1)
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
            if pos.pb3.x < pos.box_dict["box8"].x and pos.pb3.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb3, 8 + 1)
            if pos.box_dict["box1"].x <= pos.pb3.x and pos.pb3.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb3, 8 - 1)
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
            if pos.pb4.x < pos.box_dict["box8"].x and pos.pb4.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb4, 8 + 1)
            if pos.box_dict["box1"].x <= pos.pb4.x and pos.pb4.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb4, 8 - 1)
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
            if pos.pb5.x < pos.box_dict["box8"].x and pos.pb5.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb5, 8 + 1)
            if pos.box_dict["box1"].x <= pos.pb5.x and pos.pb5.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb5, 8 - 1)
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
            if pos.pb6.x < pos.box_dict["box8"].x and pos.pb6.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb6, 8 + 1)
            if pos.box_dict["box1"].x <= pos.pb6.x and pos.pb6.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb6, 8 - 1)
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
            if pos.pb7.x < pos.box_dict["box8"].x and pos.pb7.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb7, 8 + 1)
            if pos.box_dict["box1"].x <= pos.pb7.x and pos.pb7.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb7, 8 - 1)
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
            if pos.pb8.x < pos.box_dict["box8"].x and pos.pb8.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb8, 8 + 1)
            if pos.box_dict["box1"].x <= pos.pb8.x and pos.pb8.y < pos.box_dict["box57"].y:
                check_cut_piece(pos.pb8, 8 - 1)
        if pos.pb8.y < pos.box_dict["box49"].y:
            if pos.pawnBlack8Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pb8) + 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pb8 = pos.boxLst[pos.boxLst.index(pos.pb8) + 16]
                    pos.pawnBlack8Clicked = 0
                    pos.pawnBlack8Clicked_twoStep = 0
                    pos.turn = "white"


# checks if white pawns can cuts the black pieces
def check_pawn_white_canCut(which_pawn_clicked, num):
    if pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pb1) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pb2) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pb3) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pb4) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pb5) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pb6) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pb7) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.pb8) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.Kb) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.Qb) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.rb1) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.rb2) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.kb1) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.kb2) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.bb1) or \
            pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num].colliderect(pos.bb2):
        pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(which_pawn_clicked) + num], border_radius=100)
        if which_pawn_clicked == pos.pw1:
            pos.pawnWhite1Clicked = 1
            pos.pawnWhite1Clicked_cut = 1
            pos.pawnWhite2Clicked = 0
            pos.pawnWhite3Clicked = 0
            pos.pawnWhite4Clicked = 0
            pos.pawnWhite5Clicked = 0
            pos.pawnWhite6Clicked = 0
            pos.pawnWhite7Clicked = 0
            pos.pawnWhite8Clicked = 0
            pos.KingWhiteClicked = 0
            pos.knightWhite1Clicked = 0
            pos.knightWhite2Clicked = 0
            pos.rookWhite1Clicked = 0
            pos.rookWhite2Clicked = 0
            pos.bishopWhite1Clicked = 0
            pos.bishopWhite2Clicked = 0
            pos.QueenWhiteClicked = 0
        elif which_pawn_clicked == pos.pw2:
            pos.pawnWhite2Clicked = 1
            pos.pawnWhite2Clicked_cut = 1
            pos.pawnWhite1Clicked = 0
            pos.pawnWhite3Clicked = 0
            pos.pawnWhite4Clicked = 0
            pos.pawnWhite5Clicked = 0
            pos.pawnWhite6Clicked = 0
            pos.pawnWhite7Clicked = 0
            pos.pawnWhite8Clicked = 0
            pos.KingWhiteClicked = 0
            pos.knightWhite1Clicked = 0
            pos.knightWhite2Clicked = 0
            pos.rookWhite1Clicked = 0
            pos.rookWhite2Clicked = 0
            pos.bishopWhite1Clicked = 0
            pos.bishopWhite2Clicked = 0
            pos.QueenWhiteClicked = 0
        elif which_pawn_clicked == pos.pw3:
            pos.pawnWhite3Clicked = 1
            pos.pawnWhite3Clicked_cut = 1
            pos.pawnWhite1Clicked = 0
            pos.pawnWhite2Clicked = 0
            pos.pawnWhite4Clicked = 0
            pos.pawnWhite5Clicked = 0
            pos.pawnWhite6Clicked = 0
            pos.pawnWhite7Clicked = 0
            pos.pawnWhite8Clicked = 0
            pos.KingWhiteClicked = 0
            pos.knightWhite1Clicked = 0
            pos.knightWhite2Clicked = 0
            pos.rookWhite1Clicked = 0
            pos.rookWhite2Clicked = 0
            pos.bishopWhite1Clicked = 0
            pos.bishopWhite2Clicked = 0
            pos.QueenWhiteClicked = 0
        elif which_pawn_clicked == pos.pw4:
            pos.pawnWhite4Clicked = 1
            pos.pawnWhite4Clicked_cut = 1
            pos.pawnWhite1Clicked = 0
            pos.pawnWhite2Clicked = 0
            pos.pawnWhite3Clicked = 0
            pos.pawnWhite5Clicked = 0
            pos.pawnWhite6Clicked = 0
            pos.pawnWhite7Clicked = 0
            pos.pawnWhite8Clicked = 0
            pos.KingWhiteClicked = 0
            pos.knightWhite1Clicked = 0
            pos.knightWhite2Clicked = 0
            pos.rookWhite1Clicked = 0
            pos.rookWhite2Clicked = 0
            pos.bishopWhite1Clicked = 0
            pos.bishopWhite2Clicked = 0
            pos.QueenWhiteClicked = 0
        elif which_pawn_clicked == pos.pw5:
            pos.pawnWhite5Clicked = 1
            pos.pawnWhite5Clicked_cut = 1
            pos.pawnWhite1Clicked = 0
            pos.pawnWhite2Clicked = 0
            pos.pawnWhite3Clicked = 0
            pos.pawnWhite4Clicked = 0
            pos.pawnWhite6Clicked = 0
            pos.pawnWhite7Clicked = 0
            pos.pawnWhite8Clicked = 0
            pos.KingWhiteClicked = 0
            pos.knightWhite1Clicked = 0
            pos.knightWhite2Clicked = 0
            pos.rookWhite1Clicked = 0
            pos.rookWhite2Clicked = 0
            pos.bishopWhite1Clicked = 0
            pos.bishopWhite2Clicked = 0
            pos.QueenWhiteClicked = 0
        elif which_pawn_clicked == pos.pw6:
            pos.pawnWhite6Clicked = 1
            pos.pawnWhite6Clicked_cut = 1
            pos.pawnWhite1Clicked = 0
            pos.pawnWhite2Clicked = 0
            pos.pawnWhite3Clicked = 0
            pos.pawnWhite4Clicked = 0
            pos.pawnWhite5Clicked = 0
            pos.pawnWhite7Clicked = 0
            pos.pawnWhite8Clicked = 0
            pos.KingWhiteClicked = 0
            pos.knightWhite1Clicked = 0
            pos.knightWhite2Clicked = 0
            pos.rookWhite1Clicked = 0
            pos.rookWhite2Clicked = 0
            pos.bishopWhite1Clicked = 0
            pos.bishopWhite2Clicked = 0
            pos.QueenWhiteClicked = 0
        elif which_pawn_clicked == pos.pw7:
            pos.pawnWhite7Clicked = 1
            pos.pawnWhite7Clicked_cut = 1
            pos.pawnWhite1Clicked = 0
            pos.pawnWhite2Clicked = 0
            pos.pawnWhite3Clicked = 0
            pos.pawnWhite4Clicked = 0
            pos.pawnWhite5Clicked = 0
            pos.pawnWhite6Clicked = 0
            pos.pawnWhite8Clicked = 0
            pos.KingWhiteClicked = 0
            pos.knightWhite1Clicked = 0
            pos.knightWhite2Clicked = 0
            pos.rookWhite1Clicked = 0
            pos.rookWhite2Clicked = 0
            pos.bishopWhite1Clicked = 0
            pos.bishopWhite2Clicked = 0
            pos.QueenWhiteClicked = 0
        elif which_pawn_clicked == pos.pw8:
            pos.pawnWhite8Clicked = 1
            pos.pawnWhite8Clicked_cut = 1
            pos.pawnWhite1Clicked = 0
            pos.pawnWhite2Clicked = 0
            pos.pawnWhite3Clicked = 0
            pos.pawnWhite4Clicked = 0
            pos.pawnWhite5Clicked = 0
            pos.pawnWhite6Clicked = 0
            pos.pawnWhite7Clicked = 0
            pos.KingWhiteClicked = 0
            pos.knightWhite1Clicked = 0
            pos.knightWhite2Clicked = 0
            pos.rookWhite1Clicked = 0
            pos.rookWhite2Clicked = 0
            pos.bishopWhite1Clicked = 0
            pos.bishopWhite2Clicked = 0
            pos.QueenWhiteClicked = 0


# checks if next positions for white pawns are empty or not
def check_pawn_white_next_pos(which_pawn_clicked):
    mouse_pos = get_pos()

    if which_pawn_clicked.collidepoint(mouse_pos[0], mouse_pos[1]):
        if which_pawn_clicked.y > pos.box_dict["box1"].y:
            if not pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw3) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw4) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw5) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw6) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw7) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw8) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.Kw) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.Qw) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.rw1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.rw2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.kw1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.kw2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.bw1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.bw2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb3) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb4) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb5) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb6) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb7) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb8) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.Kb) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.Qb) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.rb1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.rb2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.kb1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.kb2) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.bb1) and not \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.bb2):
                pygame.draw.rect(window, blue, pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8], border_radius=100)
                if which_pawn_clicked == pos.pw1:
                    pos.pawnWhite1Clicked = 1
                    pos.pawnWhite1Clicked_plus8 = 1
                    pos.pawnWhite2Clicked = 0
                    pos.pawnWhite3Clicked = 0
                    pos.pawnWhite4Clicked = 0
                    pos.pawnWhite5Clicked = 0
                    pos.pawnWhite6Clicked = 0
                    pos.pawnWhite7Clicked = 0
                    pos.pawnWhite8Clicked = 0
                    pos.KingWhiteClicked = 0
                    pos.QueenWhiteClicked = 0
                    pos.knightWhite1Clicked = 0
                    pos.knightWhite2Clicked = 0
                    pos.rookWhite1Clicked = 0
                    pos.rookWhite2Clicked = 0
                    pos.bishopWhite1Clicked = 0
                    pos.bishopWhite2Clicked = 0
                elif which_pawn_clicked == pos.pw2:
                    pos.pawnWhite2Clicked = 1
                    pos.pawnWhite2Clicked_plus8 = 1
                    pos.pawnWhite1Clicked = 0
                    pos.pawnWhite3Clicked = 0
                    pos.pawnWhite4Clicked = 0
                    pos.pawnWhite5Clicked = 0
                    pos.pawnWhite6Clicked = 0
                    pos.pawnWhite7Clicked = 0
                    pos.pawnWhite8Clicked = 0
                    pos.KingWhiteClicked = 0
                    pos.knightWhite1Clicked = 0
                    pos.knightWhite2Clicked = 0
                    pos.rookWhite1Clicked = 0
                    pos.rookWhite2Clicked = 0
                    pos.bishopWhite1Clicked = 0
                    pos.bishopWhite2Clicked = 0
                    pos.QueenWhiteClicked = 0
                elif which_pawn_clicked == pos.pw3:
                    pos.pawnWhite3Clicked = 1
                    pos.pawnWhite3Clicked_plus8 = 1
                    pos.pawnWhite1Clicked = 0
                    pos.pawnWhite2Clicked = 0
                    pos.pawnWhite4Clicked = 0
                    pos.pawnWhite5Clicked = 0
                    pos.pawnWhite6Clicked = 0
                    pos.pawnWhite7Clicked = 0
                    pos.pawnWhite8Clicked = 0
                    pos.KingWhiteClicked = 0
                    pos.knightWhite1Clicked = 0
                    pos.knightWhite2Clicked = 0
                    pos.rookWhite1Clicked = 0
                    pos.rookWhite2Clicked = 0
                    pos.bishopWhite1Clicked = 0
                    pos.bishopWhite2Clicked = 0
                    pos.QueenWhiteClicked = 0
                elif which_pawn_clicked == pos.pw4:
                    pos.pawnWhite4Clicked = 1
                    pos.pawnWhite4Clicked_plus8 = 1
                    pos.pawnWhite1Clicked = 0
                    pos.pawnWhite2Clicked = 0
                    pos.pawnWhite3Clicked = 0
                    pos.pawnWhite5Clicked = 0
                    pos.pawnWhite6Clicked = 0
                    pos.pawnWhite7Clicked = 0
                    pos.pawnWhite8Clicked = 0
                    pos.KingWhiteClicked = 0
                    pos.knightWhite1Clicked = 0
                    pos.knightWhite2Clicked = 0
                    pos.rookWhite1Clicked = 0
                    pos.rookWhite2Clicked = 0
                    pos.bishopWhite1Clicked = 0
                    pos.bishopWhite2Clicked = 0
                    pos.QueenWhiteClicked = 0
                elif which_pawn_clicked == pos.pw5:
                    pos.pawnWhite5Clicked = 1
                    pos.pawnWhite5Clicked_plus8 = 1
                    pos.pawnWhite1Clicked = 0
                    pos.pawnWhite2Clicked = 0
                    pos.pawnWhite3Clicked = 0
                    pos.pawnWhite4Clicked = 0
                    pos.pawnWhite6Clicked = 0
                    pos.pawnWhite7Clicked = 0
                    pos.pawnWhite8Clicked = 0
                    pos.KingWhiteClicked = 0
                    pos.knightWhite1Clicked = 0
                    pos.knightWhite2Clicked = 0
                    pos.rookWhite1Clicked = 0
                    pos.rookWhite2Clicked = 0
                    pos.bishopWhite1Clicked = 0
                    pos.bishopWhite2Clicked = 0
                    pos.QueenWhiteClicked = 0
                elif which_pawn_clicked == pos.pw6:
                    pos.pawnWhite6Clicked = 1
                    pos.pawnWhite6Clicked_plus8 = 1
                    pos.pawnWhite1Clicked = 0
                    pos.pawnWhite2Clicked = 0
                    pos.pawnWhite3Clicked = 0
                    pos.pawnWhite4Clicked = 0
                    pos.pawnWhite5Clicked = 0
                    pos.pawnWhite7Clicked = 0
                    pos.pawnWhite8Clicked = 0
                    pos.KingWhiteClicked = 0
                    pos.knightWhite1Clicked = 0
                    pos.knightWhite2Clicked = 0
                    pos.rookWhite1Clicked = 0
                    pos.rookWhite2Clicked = 0
                    pos.bishopWhite1Clicked = 0
                    pos.bishopWhite2Clicked = 0
                    pos.QueenWhiteClicked = 0
                elif which_pawn_clicked == pos.pw7:
                    pos.pawnWhite7Clicked = 1
                    pos.pawnWhite7Clicked_plus8 = 1
                    pos.pawnWhite1Clicked = 0
                    pos.pawnWhite2Clicked = 0
                    pos.pawnWhite3Clicked = 0
                    pos.pawnWhite4Clicked = 0
                    pos.pawnWhite5Clicked = 0
                    pos.pawnWhite6Clicked = 0
                    pos.pawnWhite8Clicked = 0
                    pos.KingWhiteClicked = 0
                    pos.knightWhite1Clicked = 0
                    pos.knightWhite2Clicked = 0
                    pos.rookWhite1Clicked = 0
                    pos.rookWhite2Clicked = 0
                    pos.bishopWhite1Clicked = 0
                    pos.bishopWhite2Clicked = 0
                    pos.QueenWhiteClicked = 0
                elif which_pawn_clicked == pos.pw8:
                    pos.pawnWhite8Clicked = 1
                    pos.pawnWhite8Clicked_plus8 = 1
                    pos.pawnWhite1Clicked = 0
                    pos.pawnWhite2Clicked = 0
                    pos.pawnWhite3Clicked = 0
                    pos.pawnWhite4Clicked = 0
                    pos.pawnWhite5Clicked = 0
                    pos.pawnWhite6Clicked = 0
                    pos.pawnWhite7Clicked = 0
                    pos.KingWhiteClicked = 0
                    pos.knightWhite1Clicked = 0
                    pos.knightWhite2Clicked = 0
                    pos.rookWhite1Clicked = 0
                    pos.rookWhite2Clicked = 0
                    pos.bishopWhite1Clicked = 0
                    pos.bishopWhite2Clicked = 0
                    pos.QueenWhiteClicked = 0
            if which_pawn_clicked.y > pos.box_dict["box41"].y:
                if pos.pawnWhite1Clicked_plus8 == 1 or pos.pawnWhite2Clicked_plus8 == 1 or pos.pawnWhite3Clicked_plus8 == 1 or pos.pawnWhite4Clicked_plus8 == 1 or pos.pawnWhite5Clicked_plus8 == 1 \
                        or pos.pawnWhite6Clicked_plus8 == 1 or pos.pawnWhite7Clicked_plus8 == 1 or pos.pawnWhite8Clicked_plus8 == 1:
                    if not pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw3) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw4) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw5) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw6) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw7) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw8) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.Kw) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.Qw) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.rw1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.rw2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.kw1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.kw2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.bw1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.bw2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb3) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb4) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb5) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb6) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb7) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb8) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.Kb) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.Qb) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.rb1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.rb2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.kb1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.kb2) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.bb1) and not \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.bb2):
                        pygame.draw.rect(window, blue, pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16], border_radius=100)
                        if which_pawn_clicked == pos.pw1:
                            pos.pawnWhite1Clicked = 1
                            pos.pawnWhite1Clicked_twoStep = 1
                            pos.pawnWhite2Clicked = 0
                            pos.pawnWhite3Clicked = 0
                            pos.pawnWhite4Clicked = 0
                            pos.pawnWhite5Clicked = 0
                            pos.pawnWhite6Clicked = 0
                            pos.pawnWhite7Clicked = 0
                            pos.pawnWhite8Clicked = 0
                            pos.KingWhiteClicked = 0
                            pos.QueenWhiteClicked = 0
                            pos.knightWhite1Clicked = 0
                            pos.knightWhite2Clicked = 0
                            pos.rookWhite1Clicked = 0
                            pos.rookWhite2Clicked = 0
                            pos.bishopWhite1Clicked = 0
                            pos.bishopWhite2Clicked = 0
                        elif which_pawn_clicked == pos.pw2:
                            pos.pawnWhite2Clicked = 1
                            pos.pawnWhite2Clicked_twoStep = 1
                            pos.pawnWhite1Clicked = 0
                            pos.pawnWhite3Clicked = 0
                            pos.pawnWhite4Clicked = 0
                            pos.pawnWhite5Clicked = 0
                            pos.pawnWhite6Clicked = 0
                            pos.pawnWhite7Clicked = 0
                            pos.pawnWhite8Clicked = 0
                            pos.KingWhiteClicked = 0
                            pos.QueenWhiteClicked = 0
                            pos.knightWhite1Clicked = 0
                            pos.knightWhite2Clicked = 0
                            pos.rookWhite1Clicked = 0
                            pos.rookWhite2Clicked = 0
                            pos.bishopWhite1Clicked = 0
                            pos.bishopWhite2Clicked = 0
                        elif which_pawn_clicked == pos.pw3:
                            pos.pawnWhite3Clicked = 1
                            pos.pawnWhite3Clicked_twoStep = 1
                            pos.pawnWhite1Clicked = 0
                            pos.pawnWhite2Clicked = 0
                            pos.pawnWhite4Clicked = 0
                            pos.pawnWhite5Clicked = 0
                            pos.pawnWhite6Clicked = 0
                            pos.pawnWhite7Clicked = 0
                            pos.pawnWhite8Clicked = 0
                            pos.KingWhiteClicked = 0
                            pos.QueenWhiteClicked = 0
                            pos.knightWhite1Clicked = 0
                            pos.knightWhite2Clicked = 0
                            pos.rookWhite1Clicked = 0
                            pos.rookWhite2Clicked = 0
                            pos.bishopWhite1Clicked = 0
                            pos.bishopWhite2Clicked = 0
                        elif which_pawn_clicked == pos.pw4:
                            pos.pawnWhite4Clicked = 1
                            pos.pawnWhite4Clicked_twoStep = 1
                            pos.pawnWhite1Clicked = 0
                            pos.pawnWhite2Clicked = 0
                            pos.pawnWhite3Clicked = 0
                            pos.pawnWhite5Clicked = 0
                            pos.pawnWhite6Clicked = 0
                            pos.pawnWhite7Clicked = 0
                            pos.pawnWhite8Clicked = 0
                            pos.KingWhiteClicked = 0
                            pos.QueenWhiteClicked = 0
                            pos.knightWhite1Clicked = 0
                            pos.knightWhite2Clicked = 0
                            pos.rookWhite1Clicked = 0
                            pos.rookWhite2Clicked = 0
                            pos.bishopWhite1Clicked = 0
                            pos.bishopWhite2Clicked = 0
                        elif which_pawn_clicked == pos.pw5:
                            pos.pawnWhite5Clicked = 1
                            pos.pawnWhite5Clicked_twoStep = 1
                            pos.pawnWhite1Clicked = 0
                            pos.pawnWhite2Clicked = 0
                            pos.pawnWhite3Clicked = 0
                            pos.pawnWhite4Clicked = 0
                            pos.pawnWhite6Clicked = 0
                            pos.pawnWhite7Clicked = 0
                            pos.pawnWhite8Clicked = 0
                            pos.KingWhiteClicked = 0
                            pos.QueenWhiteClicked = 0
                            pos.knightWhite1Clicked = 0
                            pos.knightWhite2Clicked = 0
                            pos.rookWhite1Clicked = 0
                            pos.rookWhite2Clicked = 0
                            pos.bishopWhite1Clicked = 0
                            pos.bishopWhite2Clicked = 0
                        elif which_pawn_clicked == pos.pw6:
                            pos.pawnWhite6Clicked = 1
                            pos.pawnWhite6Clicked_twoStep = 1
                            pos.pawnWhite1Clicked = 0
                            pos.pawnWhite2Clicked = 0
                            pos.pawnWhite3Clicked = 0
                            pos.pawnWhite4Clicked = 0
                            pos.pawnWhite5Clicked = 0
                            pos.pawnWhite7Clicked = 0
                            pos.pawnWhite8Clicked = 0
                            pos.KingWhiteClicked = 0
                            pos.QueenWhiteClicked = 0
                            pos.knightWhite1Clicked = 0
                            pos.knightWhite2Clicked = 0
                            pos.rookWhite1Clicked = 0
                            pos.rookWhite2Clicked = 0
                            pos.bishopWhite1Clicked = 0
                            pos.bishopWhite2Clicked = 0
                        elif which_pawn_clicked == pos.pw7:
                            pos.pawnWhite7Clicked = 1
                            pos.pawnWhite7Clicked_twoStep = 1
                            pos.pawnWhite1Clicked = 0
                            pos.pawnWhite2Clicked = 0
                            pos.pawnWhite3Clicked = 0
                            pos.pawnWhite4Clicked = 0
                            pos.pawnWhite5Clicked = 0
                            pos.pawnWhite6Clicked = 0
                            pos.pawnWhite8Clicked = 0
                            pos.KingWhiteClicked = 0
                            pos.QueenWhiteClicked = 0
                            pos.knightWhite1Clicked = 0
                            pos.knightWhite2Clicked = 0
                            pos.rookWhite1Clicked = 0
                            pos.rookWhite2Clicked = 0
                            pos.bishopWhite1Clicked = 0
                            pos.bishopWhite2Clicked = 0
                        elif which_pawn_clicked == pos.pw8:
                            pos.pawnWhite8Clicked = 1
                            pos.pawnWhite8Clicked_twoStep = 1
                            pos.pawnWhite1Clicked = 0
                            pos.pawnWhite2Clicked = 0
                            pos.pawnWhite3Clicked = 0
                            pos.pawnWhite4Clicked = 0
                            pos.pawnWhite5Clicked = 0
                            pos.pawnWhite6Clicked = 0
                            pos.pawnWhite7Clicked = 0
                            pos.KingWhiteClicked = 0
                            pos.QueenWhiteClicked = 0
                            pos.knightWhite1Clicked = 0
                            pos.knightWhite2Clicked = 0
                            pos.rookWhite1Clicked = 0
                            pos.rookWhite2Clicked = 0
                            pos.bishopWhite1Clicked = 0
                            pos.bishopWhite2Clicked = 0
                    elif pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw3) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw4) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw5) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw6) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw7) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pw8) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.Kw) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.Qw) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.rw1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.rw2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.kw1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.kw2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.bw1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.bw2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb3) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb4) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb5) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb6) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb7) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.pb8) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.Kb) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.Qb) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.rb1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.rb2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.kb1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.kb2) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.bb1) or \
                            pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 16].colliderect(pos.bb2):
                        if which_pawn_clicked == pos.pw1:
                            pos.pawnWhite1Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pw2:
                            pos.pawnWhite2Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pw3:
                            pos.pawnWhite3Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pw4:
                            pos.pawnWhite4Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pw5:
                            pos.pawnWhite5Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pw6:
                            pos.pawnWhite6Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pw7:
                            pos.pawnWhite7Clicked_twoStep = 0
                        elif which_pawn_clicked == pos.pw8:
                            pos.pawnWhite8Clicked_twoStep = 0
        if which_pawn_clicked.y > pos.box_dict["box1"].y:
            if pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw3) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw4) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw5) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw6) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw7) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pw8) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.Kw) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.Qw) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.rw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.rw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.kw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.kw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.bw1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.bw2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb3) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb4) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb5) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb6) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb7) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.pb8) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.Kb) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.Qb) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.rb1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.rb2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.kb1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.kb2) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.bb1) or \
                    pos.boxLst[pos.boxLst.index(which_pawn_clicked) - 8].colliderect(pos.bb2):
                if which_pawn_clicked == pos.pw1:
                    pos.pawnWhite1Clicked = 0
                elif which_pawn_clicked == pos.pw2:
                    pos.pawnWhite2Clicked = 0
                elif which_pawn_clicked == pos.pw3:
                    pos.pawnWhite3Clicked = 0
                elif which_pawn_clicked == pos.pw4:
                    pos.pawnWhite4Clicked = 0
                elif which_pawn_clicked == pos.pw5:
                    pos.pawnWhite5Clicked = 0
                elif which_pawn_clicked == pos.pw6:
                    pos.pawnWhite6Clicked = 0
                elif which_pawn_clicked == pos.pw7:
                    pos.pawnWhite7Clicked = 0
                elif which_pawn_clicked == pos.pw8:
                    pos.pawnWhite8Clicked = 0
        if which_pawn_clicked.x < pos.box_dict["box8"].x and which_pawn_clicked.y > pos.box_dict["box1"].y:
            check_pawn_white_canCut(which_pawn_clicked, -8 + 1)
        if which_pawn_clicked.x > pos.box_dict["box1"].x and which_pawn_clicked.y > pos.box_dict["box1"].y:
            check_pawn_white_canCut(which_pawn_clicked, -8 - 1)


# remove the black pieces if they are diagonal to white pieces
def check_white_cut_piece(who_cuts, num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(who_cuts) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb1):
            pos.pb1 = pos.black_deadPieceRect_dict["blackCutPiece_1"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb2):
            pos.pb2 = pos.black_deadPieceRect_dict["blackCutPiece_2"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb3):
            pos.pb3 = pos.black_deadPieceRect_dict["blackCutPiece_3"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb4):
            pos.pb4 = pos.black_deadPieceRect_dict["blackCutPiece_4"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb5):
            pos.pb5 = pos.black_deadPieceRect_dict["blackCutPiece_5"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb6):
            pos.pb6 = pos.black_deadPieceRect_dict["blackCutPiece_6"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb7):
            pos.pb7 = pos.black_deadPieceRect_dict["blackCutPiece_7"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb8):
            pos.pb8 = pos.black_deadPieceRect_dict["blackCutPiece_8"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.rb1):
            pos.rb1 = pos.black_deadPieceRect_dict["blackCutPiece_9"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.rb2):
            pos.rb2 = pos.black_deadPieceRect_dict["blackCutPiece_10"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.kb1):
            pos.kb1 = pos.black_deadPieceRect_dict["blackCutPiece_11"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.kb2):
            pos.kb2 = pos.black_deadPieceRect_dict["blackCutPiece_12"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.bb1):
            pos.bb1 = pos.black_deadPieceRect_dict["blackCutPiece_13"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.bb2):
            pos.bb2 = pos.black_deadPieceRect_dict["blackCutPiece_14"]
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.Kb):
            pos.Kb = pos.black_deadPieceRect_dict["blackCutPiece_15"]
            pos.KingBlack_isDead = 1
        if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.Qb):
            pos.Qb = pos.black_deadPieceRect_dict["blackCutPiece_16"]

        if who_cuts == pos.pw1:
            pos.pw1 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnWhite1Clicked = 0
            pos.pawnWhite1Clicked_cut = 0
        elif who_cuts == pos.pw2:
            pos.pw2 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnWhite2Clicked = 0
            pos.pawnWhite2Clicked_cut = 0
        elif who_cuts == pos.pw3:
            pos.pw3 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnWhite3Clicked = 0
            pos.pawnWhite3Clicked_cut = 0
        elif who_cuts == pos.pw4:
            pos.pw4 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnWhite4Clicked = 0
            pos.pawnWhite4Clicked_cut = 0
        elif who_cuts == pos.pw5:
            pos.pw5 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnWhite5Clicked = 0
            pos.pawnWhite5Clicked_cut = 0
        elif who_cuts == pos.pw6:
            pos.pw6 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnWhite6Clicked = 0
            pos.pawnWhite6Clicked_cut = 0
        elif who_cuts == pos.pw7:
            pos.pw7 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnWhite7Clicked = 0
            pos.pawnWhite7Clicked_cut = 0
        elif who_cuts == pos.pw8:
            pos.pw8 = pos.boxLst[pos.boxLst.index(who_cuts) + num]
            pos.pawnWhite8Clicked = 0
            pos.pawnWhite8Clicked_cut = 0
        pos.turn = "black"


def pawnWMovements():
    mouse_pos = get_pos()

    if pos.turn == "black":
        pos.pawnWhite1Clicked_plus8 = 0
        pos.pawnWhite2Clicked_plus8 = 0
        pos.pawnWhite3Clicked_plus8 = 0
        pos.pawnWhite4Clicked_plus8 = 0
        pos.pawnWhite5Clicked_plus8 = 0
        pos.pawnWhite6Clicked_plus8 = 0
        pos.pawnWhite7Clicked_plus8 = 0
        pos.pawnWhite8Clicked_plus8 = 0

    if pos.turn == "white":
        check_pawn_white_next_pos(pos.pw1)
        check_pawn_white_next_pos(pos.pw2)
        check_pawn_white_next_pos(pos.pw3)
        check_pawn_white_next_pos(pos.pw4)
        check_pawn_white_next_pos(pos.pw5)
        check_pawn_white_next_pos(pos.pw6)
        check_pawn_white_next_pos(pos.pw7)
        check_pawn_white_next_pos(pos.pw8)

    if pos.pawnWhite1Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pw1) - 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pw1 = pos.boxLst[pos.boxLst.index(pos.pw1) - 8]
            pos.pawnWhite1Clicked = 0
            pos.turn = "black"
        if pos.pawnWhite1Clicked_cut == 1:
            if pos.pw1.x < pos.box_dict["box8"].x and pos.pw1.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw1, -8 + 1)
            if pos.box_dict["box1"].x < pos.pw1.x and pos.pw1.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw1, -8 - 1)
        if pos.pw1.y > pos.box_dict["box9"].y:
            if pos.pawnWhite1Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pw1) - 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pw1 = pos.boxLst[pos.boxLst.index(pos.pw1) - 16]
                    pos.pawnWhite1Clicked = 0
                    pos.pawnWhite1Clicked_twoStep = 0
                    pos.turn = "black"

    elif pos.pawnWhite2Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pw2) - 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pw2 = pos.boxLst[pos.boxLst.index(pos.pw2) - 8]
            pos.pawnWhite2Clicked = 0
            pos.turn = "black"
        if pos.pawnWhite2Clicked_cut == 1:
            if pos.pw2.x < pos.box_dict["box8"].x and pos.pw2.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw2, -8 + 1)
            if pos.box_dict["box1"].x < pos.pw2.x and pos.pw2.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw2, -8 - 1)
        if pos.pw2.y > pos.box_dict["box9"].y:
            if pos.pawnWhite2Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pw2) - 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pw2 = pos.boxLst[pos.boxLst.index(pos.pw2) - 16]
                    pos.pawnWhite2Clicked = 0
                    pos.pawnWhiteClicked_twoStep = 0
                    pos.turn = "black"

    elif pos.pawnWhite3Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pw3) - 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pw3 = pos.boxLst[pos.boxLst.index(pos.pw3) - 8]
            pos.pawnWhite3Clicked = 0
            pos.turn = "black"
        if pos.pawnWhite3Clicked_cut == 1:
            if pos.pw3.x < pos.box_dict["box8"].x and pos.pw3.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw3, -8 + 1)
            if pos.box_dict["box1"].x < pos.pw3.x and pos.pw3.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw3, -8 - 1)
        if pos.pw3.y > pos.box_dict["box9"].y:
            if pos.pawnWhite3Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pw3) - 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pw3 = pos.boxLst[pos.boxLst.index(pos.pw3) - 16]
                    pos.pawnWhite3Clicked = 0
                    pos.pawnWhite3Clicked_twoStep = 0
                    pos.turn = "black"

    elif pos.pawnWhite4Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pw4) - 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pw4 = pos.boxLst[pos.boxLst.index(pos.pw4) - 8]
            pos.pawnWhite4Clicked = 0
            pos.turn = "black"
        if pos.pawnWhite4Clicked_cut == 1:
            if pos.pw4.x < pos.box_dict["box8"].x and pos.pw4.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw4, -8 + 1)
            if pos.box_dict["box1"].x < pos.pw4.x and pos.pw4.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw4, -8 - 1)
        if pos.pw4.y > pos.box_dict["box9"].y:
            if pos.pawnWhite4Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pw4) - 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pw4 = pos.boxLst[pos.boxLst.index(pos.pw4) - 16]
                    pos.pawnWhite4Clicked = 0
                    pos.pawnWhite4Clicked_twoStep = 0
                    pos.turn = "black"

    elif pos.pawnWhite5Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pw5) - 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pw5 = pos.boxLst[pos.boxLst.index(pos.pw5) - 8]
            pos.pawnWhite5Clicked = 0
            pos.turn = "black"
        if pos.pawnWhite5Clicked_cut == 1:
            if pos.pw5.x < pos.box_dict["box8"].x and pos.pw5.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw5, -8 + 1)
            if pos.box_dict["box1"].x < pos.pw5.x and pos.pw5.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw5, -8 - 1)
        if pos.pw5.y > pos.box_dict["box9"].y:
            if pos.pawnWhite5Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pw5) - 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pw5 = pos.boxLst[pos.boxLst.index(pos.pw5) - 16]
                    pos.pawnWhite5Clicked = 0
                    pos.pawnWhite5Clicked_twoStep = 0
                    pos.turn = "black"

    elif pos.pawnWhite6Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pw6) - 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pw6 = pos.boxLst[pos.boxLst.index(pos.pw6) - 8]
            pos.pawnWhite6Clicked = 0
            pos.turn = "black"
        if pos.pawnWhite6Clicked_cut == 1:
            if pos.pw6.x < pos.box_dict["box8"].x and pos.pw6.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw6, -8 + 1)
            if pos.box_dict["box1"].x < pos.pw6.x and pos.pw6.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw6, -8 - 1)
        if pos.pw6.y > pos.box_dict["box9"].y:
            if pos.pawnWhite6Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pw6) - 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pw6 = pos.boxLst[pos.boxLst.index(pos.pw6) - 16]
                    pos.pawnWhite6Clicked = 0
                    pos.pawnWhite6Clicked_twoStep = 0
                    pos.turn = "black"

    elif pos.pawnWhite7Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pw7) - 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pw7 = pos.boxLst[pos.boxLst.index(pos.pw7) - 8]
            pos.pawnWhite7Clicked = 0
            pos.turn = "black"
        if pos.pawnWhite7Clicked_cut == 1:
            if pos.pw7.x < pos.box_dict["box8"].x and pos.pw7.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw7, -8 + 1)
            if pos.box_dict["box1"].x < pos.pw7.x and pos.pw7.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw7, -8 - 1)
        if pos.pw7.y > pos.box_dict["box9"].y:
            if pos.pawnWhite7Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pw7) - 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pw7 = pos.boxLst[pos.boxLst.index(pos.pw7) - 16]
                    pos.pawnWhite7Clicked = 0
                    pos.pawnWhite7Clicked_twoStep = 0
                    pos.turn = "black"

    elif pos.pawnWhite8Clicked == 1:
        if pos.boxLst[pos.boxLst.index(pos.pw8) - 8].collidepoint(mouse_pos[0], mouse_pos[1]):
            pos.pw8 = pos.boxLst[pos.boxLst.index(pos.pw8) - 8]
            pos.pawnWhite8Clicked = 0
            pos.turn = "black"
        if pos.pawnWhite8Clicked_cut == 1:
            if pos.pw8.x < pos.box_dict["box8"].x and pos.pw8.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw8, -8 + 1)
            if pos.box_dict["box1"].x < pos.pw8.x and pos.pw8.y > pos.box_dict["box1"].y:
                check_white_cut_piece(pos.pw8, -8 - 1)
        if pos.pw8.y > pos.box_dict["box9"].y:
            if pos.pawnWhite8Clicked_twoStep == 1:
                if pos.boxLst[pos.boxLst.index(pos.pw8) - 16].collidepoint(mouse_pos[0], mouse_pos[1]):
                    pos.pw8 = pos.boxLst[pos.boxLst.index(pos.pw8) - 16]
                    pos.pawnWhite8Clicked = 0
                    pos.pawnWhite8Clicked_twoStep = 0
                    pos.turn = "black"


# checks if places where king moves are empty or not
def check_king_next_pos(num):
    if not pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw3) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw4) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw5) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw6) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw7) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw8) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.Kw) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.Qw) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.rw1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.rw2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.kw1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.kw2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.bw1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.bw2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pb1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pb2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pb3) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pb4) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pb5) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pb6) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pb7) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pb8) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.Kb) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.Qb) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.rb1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.rb2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.kb1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.kb2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.bb1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.bb2):
        pygame.draw.rect(window, blue, pos.boxLst[pos.boxLst.index(pos.Kb) + num], border_radius=100)
        pos.KingBlackClicked = 1
        pos.pawnBlack1Clicked = 0
        pos.pawnBlack2Clicked = 0
        pos.pawnBlack3Clicked = 0
        pos.pawnBlack4Clicked = 0
        pos.pawnBlack5Clicked = 0
        pos.pawnBlack6Clicked = 0
        pos.pawnBlack7Clicked = 0
        pos.pawnBlack8Clicked = 0
        pos.knightBlack1Clicked = 0
        pos.knightBlack2Clicked = 0
        pos.rookBlack1Clicked = 0
        pos.rookBlack2Clicked = 0
        pos.bishopBlack1Clicked = 0
        pos.bishopBlack2Clicked = 0
        pos.QueenBlackClicked = 0


# checks if white pieces are at position where king moves
def check_king_canCut(num):
    if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw1) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw2) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw3) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw4) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw5) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw6) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw7) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw8) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.Kw) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.Qw) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.rw1) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.rw2) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.kw1) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.kw2) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.bw1) or \
            pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.bw2):
        pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(pos.Kb) + num], border_radius=100)
        pos.KingBlackClicked = 1
        pos.KingBlackClicked_cut = 1
        pos.pawnBlack1Clicked = 0
        pos.pawnBlack2Clicked = 0
        pos.pawnBlack3Clicked = 0
        pos.pawnBlack4Clicked = 0
        pos.pawnBlack5Clicked = 0
        pos.pawnBlack6Clicked = 0
        pos.pawnBlack7Clicked = 0
        pos.pawnBlack8Clicked = 0
        pos.knightBlack1Clicked = 0
        pos.knightBlack2Clicked = 0
        pos.rookBlack1Clicked = 0
        pos.bishopBlack1Clicked = 0
        pos.bishopBlack2Clicked = 0
        pos.QueenBlackClicked = 0


# moves the king
def moveKing(num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(pos.Kb) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        pos.Kb = pos.boxLst[pos.boxLst.index(pos.Kb) + num]
        pos.KingBlackClicked = 0
        pos.turn = "white"


# remove the white pieces which are cut
def KingRemovePieces(num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(pos.Kb) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw1):
            pos.pw1 = pos.white_deadPieceRect_dict["whiteCutPiece_1"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw2):
            pos.pw2 = pos.white_deadPieceRect_dict["whiteCutPiece_2"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw3):
            pos.pw3 = pos.white_deadPieceRect_dict["whiteCutPiece_3"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw4):
            pos.pw4 = pos.white_deadPieceRect_dict["whiteCutPiece_4"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw5):
            pos.pw5 = pos.white_deadPieceRect_dict["whiteCutPiece_5"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw6):
            pos.pw6 = pos.white_deadPieceRect_dict["whiteCutPiece_6"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw7):
            pos.pw7 = pos.white_deadPieceRect_dict["whiteCutPiece_7"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.pw8):
            pos.pw8 = pos.white_deadPieceRect_dict["whiteCutPiece_8"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.rw1):
            pos.rw1 = pos.white_deadPieceRect_dict["whiteCutPiece_9"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.rw2):
            pos.rw2 = pos.white_deadPieceRect_dict["whiteCutPiece_10"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.kw1):
            pos.kw1 = pos.white_deadPieceRect_dict["whiteCutPiece_11"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.kw2):
            pos.kw2 = pos.white_deadPieceRect_dict["whiteCutPiece_12"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.bw1):
            pos.bw1 = pos.white_deadPieceRect_dict["whiteCutPiece_13"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.bw2):
            pos.bw2 = pos.white_deadPieceRect_dict["whiteCutPiece_14"]
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.Kw):
            pos.Kw = pos.white_deadPieceRect_dict["whiteCutPiece_15"]
            pos.KingWhite_isDead = 1
        if pos.boxLst[pos.boxLst.index(pos.Kb) + num].colliderect(pos.Qw):
            pos.Qw = pos.white_deadPieceRect_dict["whiteCutPiece_16"]
        pos.Kb = pos.boxLst[pos.boxLst.index(pos.Kb) + num]
        pos.KingBlackClicked = 0
        pos.KingBlackClicked_cut = 0
        pos.turn = "white"


def kingBMovements():
    mouse_pos = get_pos()

    if pos.turn == "black":
        if pos.Kb.collidepoint(mouse_pos[0], mouse_pos[1]):
            if pos.box_dict["box1"].x < pos.Kb.x < pos.box_dict["box8"].x and pos.box_dict["box1"].y < pos.Kb.y < pos.box_dict["box57"].y:  # boxes except first (row, column) and last (row, column)
                check_king_next_pos(1)
                check_king_next_pos(-1)
                check_king_next_pos(8)
                check_king_next_pos(-8)
                check_king_next_pos(8 + 1)
                check_king_next_pos(8 - 1)
                check_king_next_pos(-8 + 1)
                check_king_next_pos(-8 - 1)
            elif pos.Kb.x == pos.box_dict["box1"].x and pos.box_dict["box1"].y < pos.Kb.y < pos.box_dict["box57"].y:  # first column
                check_king_next_pos(1)
                check_king_next_pos(8)
                check_king_next_pos(8 + 1)
                check_king_next_pos(-8)
                check_king_next_pos(-8 + 1)
            elif pos.Kb.x == pos.box_dict["box8"].x and pos.box_dict["box1"].y < pos.Kb.y < pos.box_dict["box57"].y:  # last column
                check_king_next_pos(-1)
                check_king_next_pos(-8)
                check_king_next_pos(-8 - 1)
                check_king_next_pos(8)
                check_king_next_pos(8 - 1)
            elif pos.box_dict["box1"].x < pos.Kb.x < pos.box_dict["box8"].x and pos.Kb.y == pos.box_dict["box1"].y:  # first row
                check_king_next_pos(1)
                check_king_next_pos(-1)
                check_king_next_pos(8)
                check_king_next_pos(8 + 1)
                check_king_next_pos(8 - 1)
            elif pos.box_dict["box1"].x < pos.Kb.x < pos.box_dict["box8"].x and pos.Kb.y == pos.box_dict["box57"].y:  # last row
                check_king_next_pos(1)
                check_king_next_pos(-1)
                check_king_next_pos(-8)
                check_king_next_pos(-8 + 1)
                check_king_next_pos(-8 - 1)
            elif pos.Kb == pos.box_dict["box1"]:
                check_king_next_pos(1)
                check_king_next_pos(8)
                check_king_next_pos(8 + 1)
            elif pos.Kb == pos.box_dict["box8"]:
                check_king_next_pos(-1)
                check_king_next_pos(8)
                check_king_next_pos(8 - 1)
            elif pos.Kb == pos.box_dict["box57"]:
                check_king_next_pos(1)
                check_king_next_pos(-8)
                check_king_next_pos(-8 + 1)
            elif pos.Kb == pos.box_dict["box64"]:
                check_king_next_pos(-1)
                check_king_next_pos(-8)
                check_king_next_pos(-8 - 1)

            # check if king black can cut the white pieces
            if pos.Kb.x > pos.box_dict["box1"].x:
                check_king_canCut(-1)
            if pos.Kb.x < pos.box_dict["box8"].x:
                check_king_canCut(1)
            if pos.Kb.y < pos.box_dict["box57"].y:
                check_king_canCut(8)
            if pos.Kb.y < pos.box_dict["box57"].y:
                if pos.Kb.x > pos.box_dict["box1"].x:
                    check_king_canCut(8 - 1)
            if pos.Kb.y < pos.box_dict["box57"].y:
                if pos.Kb.x < pos.box_dict["box8"].x:
                    check_king_canCut(8 + 1)
            if pos.Kb.y > pos.box_dict["box1"].y:
                check_king_canCut(-8)
            if pos.Kb.y > pos.box_dict["box1"].y:
                if pos.Kb.x > pos.box_dict["box1"].x:
                    check_king_canCut(-8 - 1)
            if pos.Kb.y > pos.box_dict["box1"].y:
                if pos.Kb.x < pos.box_dict["box8"].x:
                    check_king_canCut(-8 + 1)

    # what should happen if king is clicked
    if pos.KingBlackClicked == 1:

        # cut the pieces
        if pos.KingBlackClicked_cut == 1:
            if pos.Kb.x < pos.box_dict["box8"].x:
                KingRemovePieces(1)
            if pos.Kb.x > pos.box_dict["box1"].x:
                KingRemovePieces(-1)
            if pos.Kb.y < pos.box_dict["box57"].y:
                if pos.Kb.x > pos.box_dict["box1"].x:
                    KingRemovePieces(8 - 1)
                if pos.Kb.y < pos.box_dict["box57"].y:
                    KingRemovePieces(8)
                if pos.Kb.y < pos.box_dict["box57"].y:
                    if pos.Kb.x < pos.box_dict["box8"].x:
                        KingRemovePieces(8 + 1)
            if pos.Kb.y > pos.box_dict["box1"].y:
                if pos.Kb.x > pos.box_dict["box1"].x:
                    KingRemovePieces(-8 - 1)
                KingRemovePieces(-8)
                if pos.Kb.x < pos.box_dict["box8"].x:
                    KingRemovePieces(-8 + 1)

        if pos.Kb.x < pos.box_dict["box8"].x:
            moveKing(1)
        if pos.Kb.x > pos.box_dict["box1"].x:
            moveKing(-1)
        if pos.Kb.y < pos.box_dict["box57"].y:
            if pos.Kb.x > pos.box_dict["box1"].x:
                moveKing(8 - 1)
        if pos.Kb.y < pos.box_dict["box57"].y:
            moveKing(8)
        if pos.Kb.y < pos.box_dict["box57"].y:
            if pos.Kb.x < pos.box_dict["box8"].x:
                moveKing(8 + 1)
        if pos.Kb.y > pos.box_dict["box1"].y:
            if pos.Kb.x > pos.box_dict["box1"].x:
                moveKing(-8 - 1)
            moveKing(-8)
            if pos.Kb.x < pos.box_dict["box8"].x:
                moveKing(-8 + 1)


# checks if places where king moves are empty or not
def check_white_king_next_pos(num):
    if not pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pw1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pw2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pw3) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pw4) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pw5) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pw6) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pw7) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pw8) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.Kw) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.Qw) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.rw1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.rw2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.kw1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.kw2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.bw1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.bw2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb3) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb4) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb5) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb6) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb7) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb8) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.Kb) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.Qb) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.rb1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.rb2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.kb1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.kb2) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.bb1) and not \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.bb2):
        pygame.draw.rect(window, blue, pos.boxLst[pos.boxLst.index(pos.Kw) + num], border_radius=100)
        pos.KingWhiteClicked = 1
        pos.pawnWhite1Clicked = 0
        pos.pawnWhite2Clicked = 0
        pos.pawnWhite3Clicked = 0
        pos.pawnWhite4Clicked = 0
        pos.pawnWhite5Clicked = 0
        pos.pawnWhite6Clicked = 0
        pos.pawnWhite7Clicked = 0
        pos.pawnWhite8Clicked = 0
        pos.knightWhite1Clicked = 0
        pos.knightWhite2Clicked = 0
        pos.rookWhite1Clicked = 0
        pos.rookWhite2Clicked = 0
        pos.bishopWhite1Clicked = 0
        pos.bishopWhite2Clicked = 0
        pos.QueenWhiteClicked = 0


# checks if white pieces are at position where king moves
def check_white_king_canCut(num):
    if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb1) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb2) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb3) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb4) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb5) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb6) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb7) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb8) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.Kb) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.Qb) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.rb1) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.rb2) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.kb1) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.kb2) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.bb1) or \
            pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.bb2):
        pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(pos.Kw) + num], border_radius=100)
        pos.KingWhiteClicked = 1
        pos.KingWhiteClicked_cut = 1
        pos.pawnWhite1Clicked = 0
        pos.pawnWhite2Clicked = 0
        pos.pawnWhite3Clicked = 0
        pos.pawnWhite4Clicked = 0
        pos.pawnWhite5Clicked = 0
        pos.pawnWhite6Clicked = 0
        pos.pawnWhite7Clicked = 0
        pos.pawnWhite8Clicked = 0
        pos.knightWhite1Clicked = 0
        pos.knightWhite2Clicked = 0
        pos.rookWhite1Clicked = 0
        pos.bishopWhite1Clicked = 0
        pos.bishopWhite2Clicked = 0
        pos.QueenWhiteClicked = 0


# moves the king
def moveWhiteKing(num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(pos.Kw) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        pos.Kw = pos.boxLst[pos.boxLst.index(pos.Kw) + num]
        pos.KingWhiteClicked = 0
        pos.turn = "black"


# remove the white pieces which are cut
def WhiteKingRemovePieces(num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(pos.Kw) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb1):
            pos.pb1 = pos.black_deadPieceRect_dict["blackCutPiece_1"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb2):
            pos.pb2 = pos.black_deadPieceRect_dict["blackCutPiece_2"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb3):
            pos.pb3 = pos.black_deadPieceRect_dict["blackCutPiece_3"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb4):
            pos.pb4 = pos.black_deadPieceRect_dict["blackCutPiece_4"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb5):
            pos.pb5 = pos.black_deadPieceRect_dict["blackCutPiece_5"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb6):
            pos.pb6 = pos.black_deadPieceRect_dict["blackCutPiece_6"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb7):
            pos.pb7 = pos.black_deadPieceRect_dict["blackCutPiece_7"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.pb8):
            pos.pb8 = pos.black_deadPieceRect_dict["blackCutPiece_8"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.rb1):
            pos.rb1 = pos.black_deadPieceRect_dict["blackCutPiece_9"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.rb2):
            pos.rb2 = pos.black_deadPieceRect_dict["blackCutPiece_10"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.kb1):
            pos.kb1 = pos.black_deadPieceRect_dict["blackCutPiece_11"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.kb2):
            pos.kb2 = pos.black_deadPieceRect_dict["blackCutPiece_12"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.bb1):
            pos.bb1 = pos.black_deadPieceRect_dict["blackCutPiece_13"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.bb2):
            pos.bb2 = pos.black_deadPieceRect_dict["blackCutPiece_14"]
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.Kb):
            pos.Kb = pos.black_deadPieceRect_dict["blackCutPiece_15"]
            pos.KingBlack_isDead = 1
        if pos.boxLst[pos.boxLst.index(pos.Kw) + num].colliderect(pos.Qb):
            pos.Qb = pos.black_deadPieceRect_dict["blackCutPiece_16"]
        pos.Kw = pos.boxLst[pos.boxLst.index(pos.Kw) + num]
        pos.KingWhiteClicked = 0
        pos.KingWhiteClicked_cut = 0
        pos.turn = "black"


def kingWMovements():
    mouse_pos = get_pos()

    if pos.turn == "white":
        if pos.Kw.collidepoint(mouse_pos[0], mouse_pos[1]):
            if pos.box_dict["box1"].x < pos.Kw.x < pos.box_dict["box8"].x and pos.box_dict["box1"].y < pos.Kw.y < pos.box_dict["box57"].y:  # boxes except first (row, column) and last (row, column)
                check_white_king_next_pos(1)
                check_white_king_next_pos(-1)
                check_white_king_next_pos(8)
                check_white_king_next_pos(-8)
                check_white_king_next_pos(8 + 1)
                check_white_king_next_pos(8 - 1)
                check_white_king_next_pos(-8 + 1)
                check_white_king_next_pos(-8 - 1)
            elif pos.Kw.x == pos.box_dict["box1"].x and pos.box_dict["box1"].y < pos.Kw.y < pos.box_dict["box57"].y:  # first column
                check_white_king_next_pos(1)
                check_white_king_next_pos(8)
                check_white_king_next_pos(8 + 1)
                check_white_king_next_pos(-8)
                check_white_king_next_pos(-8 + 1)
            elif pos.Kw.x == pos.box_dict["box8"].x and pos.box_dict["box1"].y < pos.Kw.y < pos.box_dict["box57"].y:  # last column
                check_white_king_next_pos(-1)
                check_white_king_next_pos(-8)
                check_white_king_next_pos(-8 - 1)
                check_white_king_next_pos(8)
                check_white_king_next_pos(8 - 1)
            elif pos.box_dict["box1"].x < pos.Kw.x < pos.box_dict["box8"].x and pos.Kw.y == pos.box_dict["box1"].y:  # first row
                check_white_king_next_pos(1)
                check_white_king_next_pos(-1)
                check_white_king_next_pos(8)
                check_white_king_next_pos(8 + 1)
                check_white_king_next_pos(8 - 1)
            elif pos.box_dict["box1"].x < pos.Kw.x < pos.box_dict["box8"].x and pos.Kw.y == pos.box_dict["box57"].y:  # last row
                check_white_king_next_pos(1)
                check_white_king_next_pos(-1)
                check_white_king_next_pos(-8)
                check_white_king_next_pos(-8 + 1)
                check_white_king_next_pos(-8 - 1)
            elif pos.Kw == pos.box_dict["box1"]:
                check_white_king_next_pos(1)
                check_white_king_next_pos(8)
                check_white_king_next_pos(8 + 1)
            elif pos.Kw == pos.box_dict["box8"]:
                check_white_king_next_pos(-1)
                check_white_king_next_pos(8)
                check_white_king_next_pos(8 - 1)
            elif pos.Kw == pos.box_dict["box57"]:
                check_white_king_next_pos(1)
                check_white_king_next_pos(-8)
                check_white_king_next_pos(-8 + 1)
            elif pos.Kw == pos.box_dict["box64"]:
                check_white_king_next_pos(-1)
                check_white_king_next_pos(-8)
                check_white_king_next_pos(-8 - 1)

            # check if king black can cut the white pieces
            if pos.Kw.x > pos.box_dict["box1"].x:
                check_white_king_canCut(-1)
            if pos.Kw.x < pos.box_dict["box8"].x:
                check_white_king_canCut(1)
            if pos.Kw.y < pos.box_dict["box57"].y:
                check_white_king_canCut(8)
            if pos.Kw.y < pos.box_dict["box57"].y:
                if pos.Kw.x > pos.box_dict["box1"].x:
                    check_white_king_canCut(8 - 1)
            if pos.Kw.y < pos.box_dict["box57"].y:
                if pos.Kw.x < pos.box_dict["box8"].x:
                    check_white_king_canCut(8 + 1)
            if pos.Kw.y > pos.box_dict["box1"].y:
                check_white_king_canCut(-8)
            if pos.Kw.y > pos.box_dict["box1"].y:
                if pos.Kw.x > pos.box_dict["box1"].x:
                    check_white_king_canCut(-8 - 1)
            if pos.Kw.y > pos.box_dict["box1"].y:
                if pos.Kw.x < pos.box_dict["box8"].x:
                    check_white_king_canCut(-8 + 1)

    # what should happen if king is clicked
    if pos.KingWhiteClicked == 1:

        # cut the pieces
        if pos.KingWhiteClicked_cut == 1:
            if pos.Kw.x < pos.box_dict["box8"].x:
                WhiteKingRemovePieces(1)
            if pos.Kw.x > pos.box_dict["box1"].x:
                WhiteKingRemovePieces(-1)
            if pos.Kw.y < pos.box_dict["box57"].y:
                if pos.Kw.x > pos.box_dict["box1"].x:
                    WhiteKingRemovePieces(8 - 1)
                if pos.Kw.y < pos.box_dict["box57"].y:
                    WhiteKingRemovePieces(8)
                if pos.Kw.y < pos.box_dict["box57"].y:
                    if pos.Kw.x < pos.box_dict["box8"].x:
                        WhiteKingRemovePieces(8 + 1)
            if pos.Kw.y > pos.box_dict["box1"].y:
                if pos.Kw.x > pos.box_dict["box1"].x:
                    WhiteKingRemovePieces(-8 - 1)
                WhiteKingRemovePieces(-8)
                if pos.Kw.x < pos.box_dict["box8"].x:
                    WhiteKingRemovePieces(-8 + 1)

        if pos.Kw.x < pos.box_dict["box8"].x:
            moveWhiteKing(1)
        if pos.Kw.x > pos.box_dict["box1"].x:
            moveWhiteKing(-1)
        if pos.Kw.y < pos.box_dict["box57"].y:
            if pos.Kw.x > pos.box_dict["box1"].x:
                moveWhiteKing(8 - 1)
        if pos.Kw.y < pos.box_dict["box57"].y:
            moveWhiteKing(8)
        if pos.Kw.y < pos.box_dict["box57"].y:
            if pos.Kw.x < pos.box_dict["box8"].x:
                moveWhiteKing(8 + 1)
        if pos.Kw.y > pos.box_dict["box1"].y:
            if pos.Kw.x > pos.box_dict["box1"].x:
                moveWhiteKing(-8 - 1)
            moveWhiteKing(-8)
            if pos.Kw.x < pos.box_dict["box8"].x:
                moveWhiteKing(-8 + 1)


# check if knight can move or not
def check_knight_canMove(which_knight_clicked, num):
    if not pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw1) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw2) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw3) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw4) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw5) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw6) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw7) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw8) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.Kw) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.Qw) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.rw1) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.rw2) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.kw1) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.kw2) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.bw1) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.bw2) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb1) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb2) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb3) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb4) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb5) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb6) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb7) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb8) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.Kb) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.Qb) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.rb1) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.rb2) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.kb1) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.kb2) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.bb1) and not \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.bb2):
        pygame.draw.rect(window, blue, pos.boxLst[pos.boxLst.index(which_knight_clicked) + num], border_radius=100)
        if which_knight_clicked == pos.kb1:
            pos.knightBlack1Clicked = 1
            pos.knightBlack2Clicked = 0
        elif which_knight_clicked == pos.kb2:
            pos.knightBlack2Clicked = 1
            pos.knightBlack1Clicked = 0
        if which_knight_clicked == pos.kw1:
            pos.knightWhite1Clicked = 1
            pos.knightWhite2Clicked = 0
        elif which_knight_clicked == pos.kw2:
            pos.knightWhite2Clicked = 1
            pos.knightWhite1Clicked = 0

        if which_knight_clicked == pos.kb1 or which_knight_clicked == pos.kb2:
            pos.pawnBlack1Clicked = 0
            pos.pawnBlack2Clicked = 0
            pos.pawnBlack3Clicked = 0
            pos.pawnBlack4Clicked = 0
            pos.pawnBlack5Clicked = 0
            pos.pawnBlack6Clicked = 0
            pos.pawnBlack7Clicked = 0
            pos.pawnBlack8Clicked = 0
            pos.KingBlackClicked = 0
            pos.QueenBlackClicked = 0
            pos.rookBlack1Clicked = 0
            pos.rookBlack2Clicked = 0
            pos.bishopBlack1Clicked = 0
            pos.bishopBlack2Clicked = 0
        elif which_knight_clicked == pos.kw1 or which_knight_clicked == pos.kw2:
            pos.pawnWhite1Clicked = 0
            pos.pawnWhite2Clicked = 0
            pos.pawnWhite3Clicked = 0
            pos.pawnWhite4Clicked = 0
            pos.pawnWhite5Clicked = 0
            pos.pawnWhite6Clicked = 0
            pos.pawnWhite7Clicked = 0
            pos.pawnWhite8Clicked = 0
            pos.KingWhiteClicked = 0
            pos.QueenWhiteClicked = 0
            pos.rookWhite1Clicked = 0
            pos.rookWhite2Clicked = 0
            pos.bishopWhite1Clicked = 0
            pos.bishopWhite2Clicked = 0


# checks restrictions
def check_knight_restrictions(which_knight_clicked):
    if which_knight_clicked.x < pos.box_dict["box8"].x and which_knight_clicked.y < pos.box_dict["box49"].y:
        check_knight_canMove(which_knight_clicked, 16 + 1)
    if which_knight_clicked.x > pos.box_dict["box1"].x and which_knight_clicked.y < pos.box_dict["box49"].y:
        check_knight_canMove(which_knight_clicked, 16 - 1)
    if which_knight_clicked.x < pos.box_dict["box8"].x and which_knight_clicked.y > pos.box_dict["box9"].y:
        check_knight_canMove(which_knight_clicked, -16 + 1)
    if which_knight_clicked.x > pos.box_dict["box1"].x and which_knight_clicked.y > pos.box_dict["box9"].y:
        check_knight_canMove(which_knight_clicked, -16 - 1)
    if which_knight_clicked.x < pos.box_dict["box7"].x and which_knight_clicked.y < pos.box_dict["box57"].y:
        check_knight_canMove(which_knight_clicked, 8 + 2)
    if which_knight_clicked.x > pos.box_dict["box2"].x and which_knight_clicked.y < pos.box_dict["box57"].y:
        check_knight_canMove(which_knight_clicked, 8 - 2)
    if which_knight_clicked.x < pos.box_dict["box7"].x and which_knight_clicked.y > pos.box_dict["box1"].y:
        check_knight_canMove(which_knight_clicked, -8 + 2)
    if which_knight_clicked.x > pos.box_dict["box2"].x and which_knight_clicked.y > pos.box_dict["box1"].y:
        check_knight_canMove(which_knight_clicked, -8 - 2)


# check knight can cut or not
def check_knight_canCut(which_knight_clicked, num):
    if pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw1) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw2) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw3) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw4) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw5) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw6) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw7) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pw8) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.Kw) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.Qw) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.rw1) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.rw2) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.kw1) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.kw2) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.bw1) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.bw2):
        pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(which_knight_clicked) + num], border_radius=100)
        if which_knight_clicked == pos.kb1:
            pos.knightBlack1Clicked = 1
            pos.knightBlack1Clicked_cut = 1
            pos.knightBlack2Clicked = 0
        elif which_knight_clicked == pos.kb2:
            pos.knightBlack2Clicked = 1
            pos.knightBlack2Clicked_cut = 1
            pos.knightBlack1Clicked = 0
        pos.pawnBlack1Clicked = 0
        pos.pawnBlack2Clicked = 0
        pos.pawnBlack3Clicked = 0
        pos.pawnBlack4Clicked = 0
        pos.pawnBlack5Clicked = 0
        pos.pawnBlack6Clicked = 0
        pos.pawnBlack7Clicked = 0
        pos.pawnBlack8Clicked = 0
        pos.KingBlackClicked = 0
        pos.QueenBlackClicked = 0
        pos.rookBlack1Clicked = 0
        pos.rookBlack2Clicked = 0
        pos.bishopBlack1Clicked = 0
        pos.bishopBlack2Clicked = 0


# check knight cutting restrictions
def check_knight_canCut_restrictions(which_knight_clicked):
    if which_knight_clicked.x < pos.box_dict["box8"].x and which_knight_clicked.y < pos.box_dict["box49"].y:
        check_knight_canCut(which_knight_clicked, 16 + 1)
    if which_knight_clicked.x > pos.box_dict["box1"].x and which_knight_clicked.y < pos.box_dict["box49"].y:
        check_knight_canCut(which_knight_clicked, 16 - 1)
    if which_knight_clicked.x < pos.box_dict["box8"].x and which_knight_clicked.y > pos.box_dict["box9"].y:
        check_knight_canCut(which_knight_clicked, -16 + 1)
    if which_knight_clicked.x > pos.box_dict["box1"].x and which_knight_clicked.y > pos.box_dict["box9"].y:
        check_knight_canCut(which_knight_clicked, -16 - 1)
    if which_knight_clicked.x < pos.box_dict["box7"].x and which_knight_clicked.y < pos.box_dict["box57"].y:
        check_knight_canCut(which_knight_clicked, 8 + 2)
    if which_knight_clicked.x > pos.box_dict["box2"].x and which_knight_clicked.y < pos.box_dict["box57"].y:
        check_knight_canCut(which_knight_clicked, 8 - 2)
    if which_knight_clicked.x < pos.box_dict["box7"].x and which_knight_clicked.y > pos.box_dict["box1"].y:
        check_knight_canCut(which_knight_clicked, -8 + 2)
    if which_knight_clicked.x > pos.box_dict["box2"].x and which_knight_clicked.y > pos.box_dict["box1"].y:
        check_knight_canCut(which_knight_clicked, -8 - 2)


# move knight
def move_knight(which_knight_moves, num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(which_knight_moves) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if which_knight_moves == pos.kb1:
            pos.kb1 = pos.boxLst[pos.boxLst.index(which_knight_moves) + num]
            pos.knightBlack1Clicked = 0
        elif which_knight_moves == pos.kb2:
            pos.kb2 = pos.boxLst[pos.boxLst.index(which_knight_moves) + num]
            pos.knightBlack2Clicked = 0
        pos.turn = "white"


# moving knight restrictions
def moveKnight_restrictions(which_knight_moves):
    # move the knight
    if which_knight_moves.x > pos.box_dict["box1"].x and which_knight_moves.y < pos.box_dict["box49"].y:
        move_knight(which_knight_moves, 16 - 1)
    if which_knight_moves.x < pos.box_dict["box8"].x and which_knight_moves.y < pos.box_dict["box49"].y:
        move_knight(which_knight_moves, 16 + 1)
    if which_knight_moves.x < pos.box_dict["box8"].x and which_knight_moves.y > pos.box_dict["box9"].y:
        move_knight(which_knight_moves, -16 + 1)
    if which_knight_moves.x > pos.box_dict["box1"].x and which_knight_moves.y > pos.box_dict["box9"].y:
        move_knight(which_knight_moves, -16 - 1)
    if which_knight_moves.x < pos.box_dict["box7"].x and which_knight_moves.y < pos.box_dict["box57"].y:
        move_knight(which_knight_moves, 8 + 2)
    if which_knight_moves.x > pos.box_dict["box2"].x and which_knight_moves.y < pos.box_dict["box57"].y:
        move_knight(which_knight_moves, 8 - 2)
    if which_knight_moves.x < pos.box_dict["box7"].x and which_knight_moves.y > pos.box_dict["box1"].y:
        move_knight(which_knight_moves, -8 + 2)
    if which_knight_moves.x > pos.box_dict["box2"].x and which_knight_moves.y > pos.box_dict["box1"].y:
        move_knight(which_knight_moves, -8 - 2)


# remove the white pieces if cut
def knight_remove_pieces(who_removes, num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(who_removes) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw1):
            pos.pw1 = pos.white_deadPieceRect_dict["whiteCutPiece_1"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw2):
            pos.pw2 = pos.white_deadPieceRect_dict["whiteCutPiece_2"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw3):
            pos.pw3 = pos.white_deadPieceRect_dict["whiteCutPiece_3"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw4):
            pos.pw4 = pos.white_deadPieceRect_dict["whiteCutPiece_4"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw5):
            pos.pw5 = pos.white_deadPieceRect_dict["whiteCutPiece_5"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw6):
            pos.pw6 = pos.white_deadPieceRect_dict["whiteCutPiece_6"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw7):
            pos.pw7 = pos.white_deadPieceRect_dict["whiteCutPiece_7"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw8):
            pos.pw8 = pos.white_deadPieceRect_dict["whiteCutPiece_8"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.rw1):
            pos.rw1 = pos.white_deadPieceRect_dict["whiteCutPiece_9"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.rw2):
            pos.rw2 = pos.white_deadPieceRect_dict["whiteCutPiece_10"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.kw1):
            pos.kw1 = pos.white_deadPieceRect_dict["whiteCutPiece_11"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.kw2):
            pos.kw2 = pos.white_deadPieceRect_dict["whiteCutPiece_12"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.bw1):
            pos.bw1 = pos.white_deadPieceRect_dict["whiteCutPiece_13"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.bw2):
            pos.bw2 = pos.white_deadPieceRect_dict["whiteCutPiece_14"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.Kw):
            pos.Kw = pos.white_deadPieceRect_dict["whiteCutPiece_15"]
            pos.KingWhite_isDead = 1
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.Qw):
            pos.Qw = pos.white_deadPieceRect_dict["whiteCutPiece_16"]

        if who_removes == pos.kb1:
            pos.kb1 = pos.boxLst[pos.boxLst.index(who_removes) + num]
            pos.knightBlack1Clicked = 0
            pos.knightBlack1Clicked_cut = 0
        elif who_removes == pos.kb2:
            pos.kb2 = pos.boxLst[pos.boxLst.index(who_removes) + num]
            pos.knightBlack2Clicked = 0
            pos.knightBlack2Clicked_cut = 0
        pos.turn = "white"


# check for restrictions on removing
def knight_remove_pieces_restrictions(who_removes):
    if who_removes.x > pos.box_dict["box1"].x and who_removes.y < pos.box_dict["box49"].y:
        knight_remove_pieces(who_removes, 16 - 1)
    if who_removes.x < pos.box_dict["box8"].x and who_removes.y < pos.box_dict["box49"].y:
        knight_remove_pieces(who_removes, 16 + 1)
    if who_removes.x < pos.box_dict["box8"].x and who_removes.y > pos.box_dict["box9"].y:
        knight_remove_pieces(who_removes, -16 + 1)
    if who_removes.x > pos.box_dict["box1"].x and who_removes.y > pos.box_dict["box9"].y:
        knight_remove_pieces(who_removes, -16 - 1)
    if who_removes.x < pos.box_dict["box7"].x and who_removes.y < pos.box_dict["box57"].y:
        knight_remove_pieces(who_removes, 8 + 2)
    if who_removes.x > pos.box_dict["box2"].x and who_removes.y < pos.box_dict["box57"].y:
        knight_remove_pieces(who_removes, 8 - 2)
    if who_removes.x < pos.box_dict["box7"].x and who_removes.y > pos.box_dict["box1"].y:
        knight_remove_pieces(who_removes, -8 + 2)
    if who_removes.x > pos.box_dict["box2"].x and who_removes.y > pos.box_dict["box1"].y:
        knight_remove_pieces(who_removes, -8 - 2)


def knightBMovements():
    mouse_pos = get_pos()

    if pos.turn == "black":
        if pos.kb1.collidepoint(mouse_pos[0], mouse_pos[1]):
            check_knight_restrictions(pos.kb1)
            check_knight_canCut_restrictions(pos.kb1)
        elif pos.kb2.collidepoint(mouse_pos[0], mouse_pos[1]):
            check_knight_restrictions(pos.kb2)
            check_knight_canCut_restrictions(pos.kb2)

    if pos.knightBlack1Clicked == 1:
        # cut white pieces
        if pos.knightBlack1Clicked_cut == 1:
            knight_remove_pieces_restrictions(pos.kb1)
        moveKnight_restrictions(pos.kb1)
    elif pos.knightBlack2Clicked == 1:
        # cut white pieces
        if pos.knightBlack2Clicked_cut == 1:
            knight_remove_pieces_restrictions(pos.kb2)
        moveKnight_restrictions(pos.kb2)


# check white knight can cut or not
def check_white_knight_canCut(which_knight_clicked, num):
    if pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb1) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb2) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb3) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb4) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb5) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb6) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb7) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.pb8) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.Kb) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.Qb) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.rb1) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.rb2) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.kb1) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.kb2) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.bb1) or \
            pos.boxLst[pos.boxLst.index(which_knight_clicked) + num].colliderect(pos.bb2):
        pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(which_knight_clicked) + num], border_radius=100)
        if which_knight_clicked == pos.kw1:
            pos.knightWhite1Clicked = 1
            pos.knightWhite1Clicked_cut = 1
            pos.knightWhite2Clicked = 0
        elif which_knight_clicked == pos.kw2:
            pos.knightWhite2Clicked = 1
            pos.knightWhite2Clicked_cut = 1
            pos.knightWhite1Clicked = 0
        pos.pawnWhite1Clicked = 0
        pos.pawnWhite2Clicked = 0
        pos.pawnWhite3Clicked = 0
        pos.pawnWhite4Clicked = 0
        pos.pawnWhite5Clicked = 0
        pos.pawnWhite6Clicked = 0
        pos.pawnWhite7Clicked = 0
        pos.pawnWhite8Clicked = 0
        pos.KingWhiteClicked = 0
        pos.QueenWhiteClicked = 0
        pos.rookWhite1Clicked = 0
        pos.rookWhite2Clicked = 0
        pos.bishopWhite1Clicked = 0
        pos.bishopWhite2Clicked = 0


# check white knight cutting restrictions
def check_white_knight_canCut_restrictions(which_knight_clicked):
    if which_knight_clicked.x < pos.box_dict["box8"].x and which_knight_clicked.y < pos.box_dict["box49"].y:
        check_white_knight_canCut(which_knight_clicked, 16 + 1)
    if which_knight_clicked.x > pos.box_dict["box1"].x and which_knight_clicked.y < pos.box_dict["box49"].y:
        check_white_knight_canCut(which_knight_clicked, 16 - 1)
    if which_knight_clicked.x < pos.box_dict["box8"].x and which_knight_clicked.y > pos.box_dict["box9"].y:
        check_white_knight_canCut(which_knight_clicked, -16 + 1)
    if which_knight_clicked.x > pos.box_dict["box1"].x and which_knight_clicked.y > pos.box_dict["box9"].y:
        check_white_knight_canCut(which_knight_clicked, -16 - 1)
    if which_knight_clicked.x < pos.box_dict["box7"].x and which_knight_clicked.y < pos.box_dict["box57"].y:
        check_white_knight_canCut(which_knight_clicked, 8 + 2)
    if which_knight_clicked.x > pos.box_dict["box2"].x and which_knight_clicked.y < pos.box_dict["box57"].y:
        check_white_knight_canCut(which_knight_clicked, 8 - 2)
    if which_knight_clicked.x < pos.box_dict["box7"].x and which_knight_clicked.y > pos.box_dict["box1"].y:
        check_white_knight_canCut(which_knight_clicked, -8 + 2)
    if which_knight_clicked.x > pos.box_dict["box2"].x and which_knight_clicked.y > pos.box_dict["box1"].y:
        check_white_knight_canCut(which_knight_clicked, -8 - 2)


# move knight
def move_white_knight(which_knight_moves, num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(which_knight_moves) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if which_knight_moves == pos.kw1:
            pos.kw1 = pos.boxLst[pos.boxLst.index(which_knight_moves) + num]
            pos.knightWhite1Clicked = 0
        elif which_knight_moves == pos.kw2:
            pos.kw2 = pos.boxLst[pos.boxLst.index(which_knight_moves) + num]
            pos.knightWhite2Clicked = 0
        pos.turn = "black"


# moving knight restrictions
def moveWhiteKnight_restrictions(which_knight_moves):
    # move the knight
    if which_knight_moves.x > pos.box_dict["box1"].x and which_knight_moves.y < pos.box_dict["box49"].y:
        move_white_knight(which_knight_moves, 16 - 1)
    if which_knight_moves.x < pos.box_dict["box8"].x and which_knight_moves.y < pos.box_dict["box49"].y:
        move_white_knight(which_knight_moves, 16 + 1)
    if which_knight_moves.x < pos.box_dict["box8"].x and which_knight_moves.y > pos.box_dict["box9"].y:
        move_white_knight(which_knight_moves, -16 + 1)
    if which_knight_moves.x > pos.box_dict["box1"].x and which_knight_moves.y > pos.box_dict["box9"].y:
        move_white_knight(which_knight_moves, -16 - 1)
    if which_knight_moves.x < pos.box_dict["box7"].x and which_knight_moves.y < pos.box_dict["box57"].y:
        move_white_knight(which_knight_moves, 8 + 2)
    if which_knight_moves.x > pos.box_dict["box2"].x and which_knight_moves.y < pos.box_dict["box57"].y:
        move_white_knight(which_knight_moves, 8 - 2)
    if which_knight_moves.x < pos.box_dict["box7"].x and which_knight_moves.y > pos.box_dict["box1"].y:
        move_white_knight(which_knight_moves, -8 + 2)
    if which_knight_moves.x > pos.box_dict["box2"].x and which_knight_moves.y > pos.box_dict["box1"].y:
        move_white_knight(which_knight_moves, -8 - 2)


# remove the white pieces if cut
def white_knight_remove_pieces(who_removes, num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(who_removes) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb1):
            pos.pb1 = pos.black_deadPieceRect_dict["blackCutPiece_1"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb2):
            pos.pb2 = pos.black_deadPieceRect_dict["blackCutPiece_2"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb3):
            pos.pb3 = pos.black_deadPieceRect_dict["blackCutPiece_3"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb4):
            pos.pb4 = pos.black_deadPieceRect_dict["blackCutPiece_4"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb5):
            pos.pb5 = pos.black_deadPieceRect_dict["blackCutPiece_5"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb6):
            pos.pb6 = pos.black_deadPieceRect_dict["blackCutPiece_6"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb7):
            pos.pb7 = pos.black_deadPieceRect_dict["blackCutPiece_7"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb8):
            pos.pb8 = pos.black_deadPieceRect_dict["blackCutPiece_8"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.rb1):
            pos.rb1 = pos.black_deadPieceRect_dict["blackCutPiece_9"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.rb2):
            pos.rb2 = pos.black_deadPieceRect_dict["blackCutPiece_10"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.kb1):
            pos.kb1 = pos.black_deadPieceRect_dict["blackCutPiece_11"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.kb2):
            pos.kb2 = pos.black_deadPieceRect_dict["blackCutPiece_12"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.bb1):
            pos.bb1 = pos.black_deadPieceRect_dict["blackCutPiece_13"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.bb2):
            pos.bb2 = pos.black_deadPieceRect_dict["blackCutPiece_14"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.Kb):
            pos.Kb = pos.black_deadPieceRect_dict["blackCutPiece_15"]
            pos.KingBlack_isDead = 1
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.Qb):
            pos.Qb = pos.black_deadPieceRect_dict["blackCutPiece_16"]

        if who_removes == pos.kw1:
            pos.kw1 = pos.boxLst[pos.boxLst.index(who_removes) + num]
            pos.knightWhite1Clicked = 0
            pos.knightWhite1Clicked_cut = 0
        elif who_removes == pos.kw2:
            pos.kw2 = pos.boxLst[pos.boxLst.index(who_removes) + num]
            pos.knightWhite2Clicked = 0
            pos.knightWhite2Clicked_cut = 0
        pos.turn = "black"


# check for restrictions on removing
def white_knight_remove_pieces_restrictions(who_removes):
    if who_removes.x > pos.box_dict["box1"].x and who_removes.y < pos.box_dict["box49"].y:
        white_knight_remove_pieces(who_removes, 16 - 1)
    if who_removes.x < pos.box_dict["box8"].x and who_removes.y < pos.box_dict["box49"].y:
        white_knight_remove_pieces(who_removes, 16 + 1)
    if who_removes.x < pos.box_dict["box8"].x and who_removes.y > pos.box_dict["box9"].y:
        white_knight_remove_pieces(who_removes, -16 + 1)
    if who_removes.x > pos.box_dict["box1"].x and who_removes.y > pos.box_dict["box9"].y:
        white_knight_remove_pieces(who_removes, -16 - 1)
    if who_removes.x < pos.box_dict["box7"].x and who_removes.y < pos.box_dict["box57"].y:
        white_knight_remove_pieces(who_removes, 8 + 2)
    if who_removes.x > pos.box_dict["box2"].x and who_removes.y < pos.box_dict["box57"].y:
        white_knight_remove_pieces(who_removes, 8 - 2)
    if who_removes.x < pos.box_dict["box7"].x and who_removes.y > pos.box_dict["box1"].y:
        white_knight_remove_pieces(who_removes, -8 + 2)
    if who_removes.x > pos.box_dict["box2"].x and who_removes.y > pos.box_dict["box1"].y:
        white_knight_remove_pieces(who_removes, -8 - 2)


def knightWMovements():
    mouse_pos = get_pos()

    if pos.turn == "white":
        if pos.kw1.collidepoint(mouse_pos[0], mouse_pos[1]):
            check_knight_restrictions(pos.kw1)
            check_white_knight_canCut_restrictions(pos.kw1)
        elif pos.kw2.collidepoint(mouse_pos[0], mouse_pos[1]):
            check_knight_restrictions(pos.kw2)
            check_white_knight_canCut_restrictions(pos.kw2)

    if pos.knightWhite1Clicked == 1:
        # cut white pieces
        if pos.knightWhite1Clicked_cut == 1:
            white_knight_remove_pieces_restrictions(pos.kw1)
        moveWhiteKnight_restrictions(pos.kw1)
    elif pos.knightWhite2Clicked == 1:
        # cut white pieces
        if pos.knightWhite2Clicked_cut == 1:
            white_knight_remove_pieces_restrictions(pos.kw2)
        moveWhiteKnight_restrictions(pos.kw2)


# check rook can move
def check_rook_canMove(which_rook_clicked, num):
    if not pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pw1) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pw2) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pw3) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pw4) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pw5) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pw6) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pw7) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pw8) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.Kw) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.Qw) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.rw1) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.rw2) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.kw1) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.kw2) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.bw1) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.bw2) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pb1) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pb2) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pb3) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pb4) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pb5) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pb6) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pb7) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.pb8) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.Kb) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.Qb) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.kb1) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.kb2) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.rb1) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.rb2) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.bb1) and not \
            pos.boxLst[pos.boxLst.index(which_rook_clicked) + num].colliderect(pos.bb2):
        pygame.draw.rect(window, blue, pos.boxLst[pos.boxLst.index(which_rook_clicked) + num], border_radius=100)

        if which_rook_clicked == pos.rb1:
            if num == 8:
                pos.rookBlack1Clicked_plus8 = 1
            if num == 16:
                pos.rookBlack1Clicked_plus16 = 1
            if num == 24:
                pos.rookBlack1Clicked_plus24 = 1
            if num == 32:
                pos.rookBlack1Clicked_plus32 = 1
            if num == 40:
                pos.rookBlack1Clicked_plus40 = 1
            if num == 48:
                pos.rookBlack1Clicked_plus48 = 1
            if num == 1:
                pos.rookBlack1Clicked_plus1 = 1
            if num == 2:
                pos.rookBlack1Clicked_plus2 = 1
            if num == 3:
                pos.rookBlack1Clicked_plus3 = 1
            if num == 4:
                pos.rookBlack1Clicked_plus4 = 1
            if num == 5:
                pos.rookBlack1Clicked_plus5 = 1
            if num == 6:
                pos.rookBlack1Clicked_plus6 = 1
            if num == -8:
                pos.rookBlack1Clicked_minus8 = 1
            if num == -16:
                pos.rookBlack1Clicked_minus16 = 1
            if num == -24:
                pos.rookBlack1Clicked_minus24 = 1
            if num == -32:
                pos.rookBlack1Clicked_minus32 = 1
            if num == -40:
                pos.rookBlack1Clicked_minus40 = 1
            if num == -48:
                pos.rookBlack1Clicked_minus48 = 1
            if num == -1:
                pos.rookBlack1Clicked_minus1 = 1
            if num == -2:
                pos.rookBlack1Clicked_minus2 = 1
            if num == -3:
                pos.rookBlack1Clicked_minus3 = 1
            if num == -4:
                pos.rookBlack1Clicked_minus4 = 1
            if num == -5:
                pos.rookBlack1Clicked_minus5 = 1
            if num == -6:
                pos.rookBlack1Clicked_minus6 = 1

        elif which_rook_clicked == pos.rb2:
            if num == 8:
                pos.rookBlack2Clicked_plus8 = 1
            if num == 16:
                pos.rookBlack2Clicked_plus16 = 1
            if num == 24:
                pos.rookBlack2Clicked_plus24 = 1
            if num == 32:
                pos.rookBlack2Clicked_plus32 = 1
            if num == 40:
                pos.rookBlack2Clicked_plus40 = 1
            if num == 48:
                pos.rookBlack2Clicked_plus48 = 1
            if num == 1:
                pos.rookBlack2Clicked_plus1 = 1
            if num == 2:
                pos.rookBlack2Clicked_plus2 = 1
            if num == 3:
                pos.rookBlack2Clicked_plus3 = 1
            if num == 4:
                pos.rookBlack2Clicked_plus4 = 1
            if num == 5:
                pos.rookBlack2Clicked_plus5 = 1
            if num == 6:
                pos.rookBlack2Clicked_plus6 = 1
            if num == -8:
                pos.rookBlack2Clicked_minus8 = 1
            if num == -16:
                pos.rookBlack2Clicked_minus16 = 1
            if num == -24:
                pos.rookBlack2Clicked_minus24 = 1
            if num == -32:
                pos.rookBlack2Clicked_minus32 = 1
            if num == -40:
                pos.rookBlack2Clicked_minus40 = 1
            if num == -48:
                pos.rookBlack2Clicked_minus48 = 1
            if num == -1:
                pos.rookBlack2Clicked_minus1 = 1
            if num == -2:
                pos.rookBlack2Clicked_minus2 = 1
            if num == -3:
                pos.rookBlack2Clicked_minus3 = 1
            if num == -4:
                pos.rookBlack2Clicked_minus4 = 1
            if num == -5:
                pos.rookBlack2Clicked_minus5 = 1
            if num == -6:
                pos.rookBlack2Clicked_minus6 = 1

        if which_rook_clicked == pos.rw1:
            if num == 8:
                pos.rookWhite2Clicked_plus8 = 1
            if num == 16:
                pos.rookWhite2Clicked_plus16 = 1
            if num == 24:
                pos.rookWhite2Clicked_plus24 = 1
            if num == 32:
                pos.rookWhite2Clicked_plus32 = 1
            if num == 40:
                pos.rookWhite2Clicked_plus40 = 1
            if num == 48:
                pos.rookWhite2Clicked_plus48 = 1
            if num == 1:
                pos.rookWhite2Clicked_plus1 = 1
            if num == 2:
                pos.rookWhite2Clicked_plus2 = 1
            if num == 3:
                pos.rookWhite2Clicked_plus3 = 1
            if num == 4:
                pos.rookWhite2Clicked_plus4 = 1
            if num == 5:
                pos.rookWhite2Clicked_plus5 = 1
            if num == 6:
                pos.rookWhite2Clicked_plus6 = 1
            if num == -8:
                pos.rookWhite2Clicked_minus8 = 1
            if num == -16:
                pos.rookWhite2Clicked_minus16 = 1
            if num == -24:
                pos.rookWhite2Clicked_minus24 = 1
            if num == -32:
                pos.rookWhite2Clicked_minus32 = 1
            if num == -40:
                pos.rookWhite2Clicked_minus40 = 1
            if num == -48:
                pos.rookWhite2Clicked_minus48 = 1
            if num == -1:
                pos.rookWhite2Clicked_minus1 = 1
            if num == -2:
                pos.rookWhite2Clicked_minus2 = 1
            if num == -3:
                pos.rookWhite2Clicked_minus3 = 1
            if num == -4:
                pos.rookWhite2Clicked_minus4 = 1
            if num == -5:
                pos.rookWhite2Clicked_minus5 = 1
            if num == -6:
                pos.rookWhite2Clicked_minus6 = 1

        elif which_rook_clicked == pos.rw2:
            if num == 8:
                pos.rookWhite2Clicked_plus8 = 1
            if num == 16:
                pos.rookWhite2Clicked_plus16 = 1
            if num == 24:
                pos.rookWhite2Clicked_plus24 = 1
            if num == 32:
                pos.rookWhite2Clicked_plus32 = 1
            if num == 40:
                pos.rookWhite2Clicked_plus40 = 1
            if num == 48:
                pos.rookWhite2Clicked_plus48 = 1
            if num == 1:
                pos.rookWhite2Clicked_plus1 = 1
            if num == 2:
                pos.rookWhite2Clicked_plus2 = 1
            if num == 3:
                pos.rookWhite2Clicked_plus3 = 1
            if num == 4:
                pos.rookWhite2Clicked_plus4 = 1
            if num == 5:
                pos.rookWhite2Clicked_plus5 = 1
            if num == 6:
                pos.rookWhite2Clicked_plus6 = 1
            if num == -8:
                pos.rookWhite2Clicked_minus8 = 1
            if num == -16:
                pos.rookWhite2Clicked_minus16 = 1
            if num == -24:
                pos.rookWhite2Clicked_minus24 = 1
            if num == -32:
                pos.rookWhite2Clicked_minus32 = 1
            if num == -40:
                pos.rookWhite2Clicked_minus40 = 1
            if num == -48:
                pos.rookWhite2Clicked_minus48 = 1
            if num == -1:
                pos.rookWhite2Clicked_minus1 = 1
            if num == -2:
                pos.rookWhite2Clicked_minus2 = 1
            if num == -3:
                pos.rookWhite2Clicked_minus3 = 1
            if num == -4:
                pos.rookWhite2Clicked_minus4 = 1
            if num == -5:
                pos.rookWhite2Clicked_minus5 = 1
            if num == -6:
                pos.rookWhite2Clicked_minus6 = 1


def rook_conditions(which_rook_clicked):
    if which_rook_clicked == pos.rb1:
        pos.rookBlack1Clicked = 1
        pos.rookBlack2Clicked = 0
        pos.pawnBlack1Clicked = 0
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
        pos.bishopBlack1Clicked = 0
        pos.bishopBlack2Clicked = 0
    elif which_rook_clicked == pos.rb2:
        pos.rookBlack2Clicked = 1
        pos.rookBlack1Clicked = 0
        pos.pawnBlack1Clicked = 0
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
        pos.bishopBlack1Clicked = 0
        pos.bishopBlack2Clicked = 0
    if which_rook_clicked == pos.rw1:
        pos.rookWhite1Clicked = 1
        pos.rookWhite2Clicked = 0
        pos.pawnWhite1Clicked = 0
        pos.pawnWhite2Clicked = 0
        pos.pawnWhite3Clicked = 0
        pos.pawnWhite4Clicked = 0
        pos.pawnWhite5Clicked = 0
        pos.pawnWhite6Clicked = 0
        pos.pawnWhite7Clicked = 0
        pos.pawnWhite8Clicked = 0
        pos.KingWhiteClicked = 0
        pos.QueenWhiteClicked = 0
        pos.knightWhite1Clicked = 0
        pos.knightWhite2Clicked = 0
        pos.bishopWhite1Clicked = 0
        pos.bishopWhite2Clicked = 0
    elif which_rook_clicked == pos.rw2:
        pos.rookWhite2Clicked = 1
        pos.rookWhite1Clicked = 0
        pos.pawnWhite1Clicked = 0
        pos.pawnWhite2Clicked = 0
        pos.pawnWhite3Clicked = 0
        pos.pawnWhite4Clicked = 0
        pos.pawnWhite5Clicked = 0
        pos.pawnWhite6Clicked = 0
        pos.pawnWhite7Clicked = 0
        pos.pawnWhite8Clicked = 0
        pos.KingWhiteClicked = 0
        pos.QueenWhiteClicked = 0
        pos.knightWhite1Clicked = 0
        pos.knightWhite2Clicked = 0
        pos.bishopWhite1Clicked = 0
        pos.bishopWhite2Clicked = 0


def check_rook_canMove_restrictions(which_rook_clicked):
    # along y-axis
    if which_rook_clicked.y < pos.box_dict["box57"].y:
        check_rook_canMove(which_rook_clicked, 8)
        rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box49"].y:
        if pos.rookBlack1Clicked_plus8 == 1 or \
                pos.rookBlack2Clicked_plus8 == 1:
            check_rook_canMove(which_rook_clicked, 16)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box41"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1) or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1):
            check_rook_canMove(which_rook_clicked, 24)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box33"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1) or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1 and pos.rookBlack2Clicked_plus24 == 1):
            check_rook_canMove(which_rook_clicked, 32)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box25"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1 and pos.rookBlack1Clicked_plus32 == 1) or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1 and pos.rookBlack2Clicked_plus24 == 1 and pos.rookBlack2Clicked_plus32 == 1):
            check_rook_canMove(which_rook_clicked, 40)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box17"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1 and pos.rookBlack1Clicked_plus32 == 1 and pos.rookBlack1Clicked_plus40 == 1) \
                or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1 and pos.rookBlack2Clicked_plus24 == 1 and pos.rookBlack2Clicked_plus32 == 1 and
                 pos.rookBlack2Clicked_plus40 == 1):
            check_rook_canMove(which_rook_clicked, 48)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box9"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1 and pos.rookBlack1Clicked_plus32 == 1 and pos.rookBlack1Clicked_plus40 == 1
            and pos.rookBlack1Clicked_plus48 == 1) or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1 and pos.rookBlack2Clicked_plus24 == 1 and pos.rookBlack2Clicked_plus32 == 1 and
                 pos.rookBlack2Clicked_plus40 == 1 and pos.rookBlack2Clicked_plus48 == 1):
            check_rook_canMove(which_rook_clicked, 56)
            rook_conditions(which_rook_clicked)

    if which_rook_clicked.y > pos.box_dict["box1"].y:
        check_rook_canMove(which_rook_clicked, -8)
        rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box9"].y:
        if pos.rookBlack1Clicked_minus8 == 1 or pos.rookBlack2Clicked_minus8 == 1:
            check_rook_canMove(which_rook_clicked, -16)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box17"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1) or (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1):
            check_rook_canMove(which_rook_clicked, -24)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box25"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1) or (
                pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1 and pos.rookBlack2Clicked_minus24 == 1):
            check_rook_canMove(which_rook_clicked, -32)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box33"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1 and pos.rookBlack1Clicked_minus32 == 1) or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1 and pos.rookBlack2Clicked_minus24 == 1 and pos.rookBlack2Clicked_minus32 == 1):
            check_rook_canMove(which_rook_clicked, -40)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box41"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1 and pos.rookBlack1Clicked_minus32 == 1 and
            pos.rookBlack1Clicked_minus40 == 1) or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1 and pos.rookBlack2Clicked_minus24 == 1 and pos.rookBlack2Clicked_minus32 == 1 and
                 pos.rookBlack2Clicked_minus40 == 1):
            check_rook_canMove(which_rook_clicked, -48)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box49"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1 and pos.rookBlack1Clicked_minus32 == 1 and
            pos.rookBlack1Clicked_minus40 and pos.rookBlack1Clicked_minus48 == 1) or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1 and pos.rookBlack2Clicked_minus24 == 1 and pos.rookBlack2Clicked_minus32 == 1 and
                 pos.rookBlack2Clicked_minus40 and pos.rookBlack2Clicked_minus48 == 1):
            check_rook_canMove(which_rook_clicked, -56)
            rook_conditions(which_rook_clicked)

    # along x-axis
    if which_rook_clicked.x < pos.box_dict["box8"].x:
        check_rook_canMove(which_rook_clicked, 1)
        rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box7"].x:
        if pos.rookBlack1Clicked_plus1 == 1 or pos.rookBlack2Clicked_plus1 == 1:
            check_rook_canMove(which_rook_clicked, 2)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box6"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1):
            check_rook_canMove(which_rook_clicked, 3)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box5"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1):
            check_rook_canMove(which_rook_clicked, 4)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box4"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1 and pos.rookBlack1Clicked_plus4 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1 and pos.rookBlack2Clicked_plus4 == 1):
            check_rook_canMove(which_rook_clicked, 5)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box3"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1 and pos.rookBlack1Clicked_plus4 == 1 and
            pos.rookBlack1Clicked_plus5 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1 and pos.rookBlack2Clicked_plus4 == 1 and pos.rookBlack2Clicked_plus5 == 1):
            check_rook_canMove(which_rook_clicked, 6)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box2"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1 and pos.rookBlack1Clicked_plus4 == 1 and
            pos.rookBlack1Clicked_plus5 == 1 and pos.rookBlack1Clicked_plus6 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1 and pos.rookBlack2Clicked_plus4 == 1 and pos.rookBlack2Clicked_plus5 == 1
                 and pos.rookBlack2Clicked_plus6 == 1):
            check_rook_canMove(which_rook_clicked, 7)
            rook_conditions(which_rook_clicked)

    if which_rook_clicked.x > pos.box_dict["box1"].x:
        check_rook_canMove(which_rook_clicked, -1)
        rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box2"].x:
        if pos.rookBlack1Clicked_minus1 == 1 or pos.rookBlack2Clicked_minus1 == 1:
            check_rook_canMove(which_rook_clicked, -2)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box3"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1):
            check_rook_canMove(which_rook_clicked, -3)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box4"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1):
            check_rook_canMove(which_rook_clicked, -4)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box5"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1 and pos.rookBlack1Clicked_minus4 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1 and pos.rookBlack2Clicked_minus4 == 1):
            check_rook_canMove(which_rook_clicked, -5)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box6"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1 and pos.rookBlack1Clicked_minus4 == 1 and
            pos.rookBlack1Clicked_minus5 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1 and pos.rookBlack2Clicked_minus4 == 1 and pos.rookBlack2Clicked_minus5
                 == 1):
            check_rook_canMove(which_rook_clicked, -6)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box7"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1 and pos.rookBlack1Clicked_minus4 == 1 and
            pos.rookBlack1Clicked_minus5 == 1 and pos.rookBlack1Clicked_minus6 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1 and pos.rookBlack2Clicked_minus4 == 1 and
                 pos.rookBlack2Clicked_minus5 == 1 and pos.rookBlack2Clicked_minus6 == 1):
            check_rook_canMove(which_rook_clicked, -7)
            rook_conditions(which_rook_clicked)


# check white pieces can cut or not
def check_rook_canCut(who_cuts, num):
    if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw1) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw2) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw3) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw4) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw5) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw6) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw7) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pw8) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.Kw) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.Qw) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.rw1) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.rw2) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.kw1) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.kw2) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.bw1) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.bw2):
        pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(who_cuts) + num], border_radius=100)
        if who_cuts == pos.rb1:
            pos.rookBlack1Clicked = 1
            pos.rookBlack1Clicked_cut = 1
            pos.rookBlack2Clicked = 0
        elif who_cuts == pos.rb2:
            pos.rookBlack2Clicked = 1
            pos.rookBlack2Clicked_cut = 1
            pos.rookBlack1Clicked = 0
        pos.pawnBlack1Clicked = 0
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
        pos.bishopBlack1Clicked = 0
        pos.bishopBlack2Clicked = 0
        pos.QueenBlackClicked = 0


# restrictions on cutting
def check_rook_canCut_restrictions(who_cuts):
    if who_cuts.y < pos.box_dict["box57"].y:
        check_rook_canCut(who_cuts, 8)
    if who_cuts.y < pos.box_dict["box49"].y:
        if pos.rookBlack1Clicked_plus8 == 1 or \
                pos.rookBlack2Clicked_plus8 == 1:
            check_rook_canCut(who_cuts, 16)
    if who_cuts.y < pos.box_dict["box41"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1) or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1):
            check_rook_canCut(who_cuts, 24)
    if who_cuts.y < pos.box_dict["box33"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1) or \
               (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1 and pos.rookBlack2Clicked_plus24 == 1):
            check_rook_canCut(who_cuts, 32)
    if who_cuts.y < pos.box_dict["box25"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1 and pos.rookBlack1Clicked_plus32 == 1) or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1 and pos.rookBlack2Clicked_plus24 == 1 and pos.rookBlack2Clicked_plus32 == 1):
            check_rook_canCut(who_cuts, 40)
    if who_cuts.y < pos.box_dict["box17"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1 and pos.rookBlack1Clicked_plus32 == 1 and
                pos.rookBlack1Clicked_plus40 == 1) \
                or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1 and pos.rookBlack2Clicked_plus24 == 1 and pos.rookBlack2Clicked_plus32 == 1 and pos.rookBlack2Clicked_plus40
                 == 1):
            check_rook_canCut(who_cuts, 48)
    if who_cuts.y < pos.box_dict["box9"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1 and pos.rookBlack1Clicked_plus32 == 1 and
                pos.rookBlack1Clicked_plus40 == 1 and pos.rookBlack1Clicked_plus48 == 1) \
                or\
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1 and pos.rookBlack2Clicked_plus24 == 1 and pos.rookBlack2Clicked_plus32 == 1 and pos.rookBlack2Clicked_plus40
                 == 1 and pos.rookBlack2Clicked_plus48 == 1):
            check_rook_canCut(who_cuts, 56)

    if who_cuts.y > pos.box_dict["box1"].y:
        check_rook_canCut(who_cuts, -8)
    if who_cuts.y > pos.box_dict["box9"].y:
        if pos.rookBlack1Clicked_minus8 == 1 or \
                pos.rookBlack2Clicked_minus8 == 1:
            check_rook_canCut(who_cuts, -16)
    if who_cuts.y > pos.box_dict["box17"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1) or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1):
            check_rook_canCut(who_cuts, -24)
    if who_cuts.y > pos.box_dict["box25"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1) or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1 and pos.rookBlack2Clicked_minus24 == 1):
            check_rook_canCut(who_cuts, -32)
    if who_cuts.y > pos.box_dict["box33"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1 and pos.rookBlack1Clicked_minus32 == 1) or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1 and pos.rookBlack2Clicked_minus24 == 1 and pos.rookBlack2Clicked_minus32 == 1):
            check_rook_canCut(who_cuts, -40)
    if who_cuts.y > pos.box_dict["box41"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1 and pos.rookBlack1Clicked_minus32 == 1 and
                pos.rookBlack1Clicked_minus40 == 1) \
                or\
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1 and pos.rookBlack2Clicked_minus24 == 1 and pos.rookBlack2Clicked_minus32 == 1 and
                 pos.rookBlack2Clicked_minus40 == 1):
            check_rook_canCut(who_cuts, -48)
    if who_cuts.y > pos.box_dict["box49"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1 and pos.rookBlack1Clicked_minus32 == 1 and
                pos.rookBlack1Clicked_minus40 == 1 and pos.rookBlack1Clicked_minus48 == 1) \
                or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1 and pos.rookBlack2Clicked_minus24 == 1 and pos.rookBlack2Clicked_minus32 == 1 and
                 pos.rookBlack2Clicked_minus40 == 1 and pos.rookBlack2Clicked_minus48 == 1):
            check_rook_canCut(who_cuts, -56)

    if who_cuts.x < pos.box_dict["box8"].x:
        check_rook_canCut(who_cuts, 1)
    if who_cuts.x < pos.box_dict["box7"].x:
        if pos.rookBlack1Clicked_plus1 == 1 or \
                pos.rookBlack2Clicked_plus1 == 1:
            check_rook_canCut(who_cuts, 2)
    if who_cuts.x < pos.box_dict["box6"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1):
            check_rook_canCut(who_cuts, 3)
    if who_cuts.x < pos.box_dict["box5"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1):
            check_rook_canCut(who_cuts, 4)
    if who_cuts.x < pos.box_dict["box4"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1 and pos.rookBlack1Clicked_plus4 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1 and pos.rookBlack2Clicked_plus4 == 1):
            check_rook_canCut(who_cuts, 5)
    if who_cuts.x < pos.box_dict["box3"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1 and pos.rookBlack1Clicked_plus4 == 1 and
                pos.rookBlack1Clicked_plus5 == 1) \
                or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1 and pos.rookBlack2Clicked_plus4 == 1 and pos.rookBlack2Clicked_plus5 == 1):
            check_rook_canCut(who_cuts, 6)
    if who_cuts.x < pos.box_dict["box2"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1 and pos.rookBlack1Clicked_plus4 == 1 and
                pos.rookBlack1Clicked_plus5 == 1 and pos.rookBlack1Clicked_plus6 == 1) \
                or\
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1 and pos.rookBlack2Clicked_plus4 == 1 and pos.rookBlack2Clicked_plus5 == 1
                 and pos.rookBlack2Clicked_plus6 == 1):
            check_rook_canCut(who_cuts, 7)

    if who_cuts.x > pos.box_dict["box1"].x:
        check_rook_canCut(who_cuts, -1)
    if who_cuts.x > pos.box_dict["box2"].x:
        if pos.rookBlack1Clicked_minus1 == 1 or \
                pos.rookBlack2Clicked_minus1 == 1:
            check_rook_canCut(who_cuts, -2)
    if who_cuts.x > pos.box_dict["box3"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1):
            check_rook_canCut(who_cuts, -3)
    if who_cuts.x > pos.box_dict["box4"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1):
            check_rook_canCut(who_cuts, -4)
    if who_cuts.x > pos.box_dict["box5"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1 and pos.rookBlack1Clicked_minus4 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1 and pos.rookBlack2Clicked_minus4 == 1):
            check_rook_canCut(who_cuts, -5)
    if who_cuts.x > pos.box_dict["box6"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1 and pos.rookBlack1Clicked_minus4 == 1 and
                pos.rookBlack1Clicked_minus5 == 1) \
                or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1 and pos.rookBlack2Clicked_minus4 == 1 and pos.rookBlack2Clicked_minus5
                 == 1):
            check_rook_canCut(who_cuts, -6)
    if who_cuts.x > pos.box_dict["box7"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1 and pos.rookBlack1Clicked_minus4 == 1 and
                pos.rookBlack1Clicked_minus5 == 1 and pos.rookBlack1Clicked_minus6 == 1) \
                or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1 and pos.rookBlack2Clicked_minus4 == 1 and pos.rookBlack2Clicked_minus5
                 == 1 and pos.rookBlack2Clicked_minus6 == 1):
            check_rook_canCut(who_cuts, -7)


# move the rook
def move_rook(who_moves, num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(who_moves) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if who_moves == pos.rb1:
            pos.rb1 = pos.boxLst[pos.boxLst.index(who_moves) + num]
            pos.rookBlack1Clicked = 0
            pos.turn = "white"
        elif who_moves == pos.rb2:
            pos.rb2 = pos.boxLst[pos.boxLst.index(who_moves) + num]
            pos.rookBlack2Clicked = 0
            pos.turn = "white"
        if who_moves == pos.rw1:
            pos.rw1 = pos.boxLst[pos.boxLst.index(who_moves) + num]
            pos.rookWhite1Clicked = 0
            pos.turn = "black"
        elif who_moves == pos.rw2:
            pos.rw2 = pos.boxLst[pos.boxLst.index(who_moves) + num]
            pos.rookWhite2Clicked = 0
            pos.turn = "black"


# restrictions on movements
def move_rook_restrictions(who_moves):
    # along y-axis(+)
    if who_moves.y < pos.box_dict["box57"].y:
        move_rook(who_moves, 8)
    if who_moves.y < pos.box_dict["box49"].y:
        if pos.rookBlack1Clicked_plus8 == 1 or \
                pos.rookBlack2Clicked_plus8 == 1:
            move_rook(who_moves, 16)
    if who_moves.y < pos.box_dict["box41"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1) or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1):
            move_rook(who_moves, 24)
    if who_moves.y < pos.box_dict["box33"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1) or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus16 == 1 and pos.rookBlack2Clicked_plus24 == 1):
            move_rook(who_moves, 32)
    if who_moves.y < pos.box_dict["box25"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1 and pos.rookBlack1Clicked_plus32 == 1) or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus24 == 1 and pos.rookBlack2Clicked_plus32 == 1):
            move_rook(who_moves, 40)
    if who_moves.y < pos.box_dict["box17"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1 and pos.rookBlack1Clicked_plus32 == 1 and pos.rookBlack1Clicked_plus40 == 1) \
                or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus24 == 1 and pos.rookBlack2Clicked_plus32 == 1 and pos.rookBlack2Clicked_plus40 == 1):
            move_rook(who_moves, 48)
    if who_moves.y < pos.box_dict["box9"].y:
        if (pos.rookBlack1Clicked_plus8 == 1 and pos.rookBlack1Clicked_plus16 == 1 and pos.rookBlack1Clicked_plus24 == 1 and pos.rookBlack1Clicked_plus32 == 1 and pos.rookBlack1Clicked_plus40 == 1
            and pos.rookBlack1Clicked_plus48 == 1) \
                or \
                (pos.rookBlack2Clicked_plus8 == 1 and pos.rookBlack2Clicked_plus24 == 1 and pos.rookBlack2Clicked_plus32 == 1 and pos.rookBlack2Clicked_plus40 == 1 and pos.rookBlack2Clicked_plus48
                 == 1):
            move_rook(who_moves, 56)

    # along y-axis(-)
    if who_moves.y > pos.box_dict["box1"].y:
        move_rook(who_moves, -8)
    if who_moves.y > pos.box_dict["box9"].y:
        if pos.rookBlack1Clicked_minus8 == 1 or \
                pos.rookBlack2Clicked_minus8 == 1:
            move_rook(who_moves, -16)
    if who_moves.y > pos.box_dict["box17"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1) or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1):
            move_rook(who_moves, -24)
    if who_moves.y > pos.box_dict["box25"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1) or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus16 == 1 and pos.rookBlack2Clicked_minus24 == 1):
            move_rook(who_moves, -32)
    if who_moves.y > pos.box_dict["box33"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1 and pos.rookBlack1Clicked_minus32 == 1) or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus24 == 1 and pos.rookBlack2Clicked_minus32 == 1):
            move_rook(who_moves, -40)
    if who_moves.y > pos.box_dict["box41"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1 and pos.rookBlack1Clicked_minus32 == 1 and
            pos.rookBlack1Clicked_minus40 == 1) \
                or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus24 == 1 and pos.rookBlack2Clicked_minus32 == 1 and pos.rookBlack2Clicked_minus40 == 1):
            move_rook(who_moves, -48)
    if who_moves.y > pos.box_dict["box49"].y:
        if (pos.rookBlack1Clicked_minus8 == 1 and pos.rookBlack1Clicked_minus16 == 1 and pos.rookBlack1Clicked_minus24 == 1 and pos.rookBlack1Clicked_minus32 == 1 and pos.rookBlack1Clicked_minus40
            == 1 and pos.rookBlack1Clicked_minus48 == 1) \
                or \
                (pos.rookBlack2Clicked_minus8 == 1 and pos.rookBlack2Clicked_minus24 == 1 and pos.rookBlack2Clicked_minus32 == 1 and pos.rookBlack2Clicked_minus40 == 1 and
                 pos.rookBlack2Clicked_minus48 == 1):
            move_rook(who_moves, -56)

    # along x-axis(+)
    if who_moves.x < pos.box_dict["box8"].x:
        move_rook(who_moves, 1)
    if who_moves.x < pos.box_dict["box7"].x:
        if pos.rookBlack1Clicked_plus1 == 1 or \
                pos.rookBlack2Clicked_plus1 == 1:
            move_rook(who_moves, 2)
    if who_moves.x < pos.box_dict["box6"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1):
            move_rook(who_moves, 3)
    if who_moves.x < pos.box_dict["box5"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1):
            move_rook(who_moves, 4)
    if who_moves.x < pos.box_dict["box4"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1 and pos.rookBlack1Clicked_plus4 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1 and pos.rookBlack2Clicked_plus4 == 1):
            move_rook(who_moves, 5)
    if who_moves.x < pos.box_dict["box3"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1 and pos.rookBlack1Clicked_plus4 == 1 and pos.rookBlack1Clicked_plus5 == 1) or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1 and pos.rookBlack2Clicked_plus4 == 1 and pos.rookBlack2Clicked_plus5 == 1):
            move_rook(who_moves, 6)
    if who_moves.x < pos.box_dict["box2"].x:
        if (pos.rookBlack1Clicked_plus1 == 1 and pos.rookBlack1Clicked_plus2 == 1 and pos.rookBlack1Clicked_plus3 == 1 and pos.rookBlack1Clicked_plus4 == 1 and pos.rookBlack1Clicked_plus5 == 1 and
            pos.rookBlack1Clicked_plus6 == 1) \
                or \
                (pos.rookBlack2Clicked_plus1 == 1 and pos.rookBlack2Clicked_plus2 == 1 and pos.rookBlack2Clicked_plus3 == 1 and pos.rookBlack2Clicked_plus4 == 1 and pos.rookBlack2Clicked_plus5 == 1
                 and pos.rookBlack2Clicked_plus6 == 1):
            move_rook(who_moves, 7)

    # along x-axis(-)
    if who_moves.x > pos.box_dict["box1"].x:
        move_rook(who_moves, -1)
    if who_moves.x > pos.box_dict["box2"].x:
        if pos.rookBlack1Clicked_minus1 == 1 or \
                pos.rookBlack2Clicked_minus1 == 1:
            move_rook(who_moves, -2)
    if who_moves.x > pos.box_dict["box3"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1):
            move_rook(who_moves, -3)
    if who_moves.x > pos.box_dict["box4"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1):
            move_rook(who_moves, -4)
    if who_moves.x > pos.box_dict["box5"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1 and pos.rookBlack1Clicked_minus4 == 1) or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1 and pos.rookBlack2Clicked_minus4 == 1):
            move_rook(who_moves, -5)
    if who_moves.x > pos.box_dict["box6"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1 and pos.rookBlack1Clicked_minus4 == 1 and pos.rookBlack1Clicked_minus5 ==
            1) or \
              (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1 and pos.rookBlack2Clicked_minus4 == 1 and pos.rookBlack2Clicked_minus5
               == 1):
            move_rook(who_moves, -6)
    if who_moves.x > pos.box_dict["box7"].x:
        if (pos.rookBlack1Clicked_minus1 == 1 and pos.rookBlack1Clicked_minus2 == 1 and pos.rookBlack1Clicked_minus3 == 1 and pos.rookBlack1Clicked_minus4 == 1 and pos.rookBlack1Clicked_minus5 == 1
            and pos.rookBlack1Clicked_minus6 == 1) \
                or \
                (pos.rookBlack2Clicked_minus1 == 1 and pos.rookBlack2Clicked_minus2 == 1 and pos.rookBlack2Clicked_minus3 == 1 and pos.rookBlack2Clicked_minus4 == 1 and pos.rookBlack2Clicked_minus5
                 == 1 and pos.rookBlack2Clicked_minus6 == 1):
            move_rook(who_moves, -7)


# remove white pieces
def rook_remove(who_removes, num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(who_removes) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw1):
            pos.pw1 = pos.white_deadPieceRect_dict["whiteCutPiece_1"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw2):
            pos.pw2 = pos.white_deadPieceRect_dict["whiteCutPiece_2"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw3):
            pos.pw3 = pos.white_deadPieceRect_dict["whiteCutPiece_3"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw4):
            pos.pw4 = pos.white_deadPieceRect_dict["whiteCutPiece_4"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw5):
            pos.pw5 = pos.white_deadPieceRect_dict["whiteCutPiece_5"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw6):
            pos.pw6 = pos.white_deadPieceRect_dict["whiteCutPiece_6"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw7):
            pos.pw7 = pos.white_deadPieceRect_dict["whiteCutPiece_7"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pw8):
            pos.pw8 = pos.white_deadPieceRect_dict["whiteCutPiece_8"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.rw1):
            pos.rw1 = pos.white_deadPieceRect_dict["whiteCutPiece_9"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.rw2):
            pos.rw2 = pos.white_deadPieceRect_dict["whiteCutPiece_10"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.kw1):
            pos.kw1 = pos.white_deadPieceRect_dict["whiteCutPiece_11"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.kw2):
            pos.kw2 = pos.white_deadPieceRect_dict["whiteCutPiece_12"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.bw1):
            pos.bw1 = pos.white_deadPieceRect_dict["whiteCutPiece_13"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.bw2):
            pos.bw2 = pos.white_deadPieceRect_dict["whiteCutPiece_14"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.Kw):
            pos.Kw = pos.white_deadPieceRect_dict["whiteCutPiece_15"]
            pos.KingWhite_isDead = 1
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.Qw):
            pos.Qw = pos.white_deadPieceRect_dict["whiteCutPiece_16"]

        if who_removes == pos.rb1:
            pos.rb1 = pos.boxLst[pos.boxLst.index(who_removes) + num]
            pos.rookBlack1Clicked = 0
            pos.rookBlack1Clicked_cut = 0
        elif who_removes == pos.rb2:
            pos.rb2 = pos.boxLst[pos.boxLst.index(who_removes) + num]
            pos.rookBlack2Clicked = 0
            pos.rookBlack2Clicked_cut = 0
        pos.turn = "white"


# remove white pieces restrictions
def rook_remove_restrictions(who_removes):
    # along y-axis
    if who_removes.y < pos.box_dict["box57"].y:
        rook_remove(who_removes, 8)
    if who_removes.y < pos.box_dict["box49"].y:
        rook_remove(who_removes, 16)
    if who_removes.y < pos.box_dict["box41"].y:
        rook_remove(who_removes, 24)
    if who_removes.y < pos.box_dict["box33"].y:
        rook_remove(who_removes, 32)
    if who_removes.y < pos.box_dict["box25"].y:
        rook_remove(who_removes, 40)
    if who_removes.y < pos.box_dict["box17"].y:
        rook_remove(who_removes, 48)
    if who_removes.y < pos.box_dict["box9"].y:
        rook_remove(who_removes, 56)

    if who_removes.y > pos.box_dict["box1"].y:
        rook_remove(who_removes, -8)
    if who_removes.y > pos.box_dict["box9"].y:
        rook_remove(who_removes, -16)
    if who_removes.y > pos.box_dict["box17"].y:
        rook_remove(who_removes, -24)
    if who_removes.y > pos.box_dict["box25"].y:
        rook_remove(who_removes, -32)
    if who_removes.y > pos.box_dict["box33"].y:
        rook_remove(who_removes, -40)
    if who_removes.y > pos.box_dict["box41"].y:
        rook_remove(who_removes, -48)
    if who_removes.y > pos.box_dict["box49"].y:
        rook_remove(who_removes, -56)

    # along x-axis
    if who_removes.x < pos.box_dict["box8"].x:
        rook_remove(who_removes, 1)
    if who_removes.x < pos.box_dict["box7"].x:
        rook_remove(who_removes, 2)
    if who_removes.x < pos.box_dict["box6"].x:
        rook_remove(who_removes, 3)
    if who_removes.x < pos.box_dict["box5"].x:
        rook_remove(who_removes, 4)
    if who_removes.x < pos.box_dict["box4"].x:
        rook_remove(who_removes, 5)
    if who_removes.x < pos.box_dict["box3"].x:
        rook_remove(who_removes, 6)
    if who_removes.x < pos.box_dict["box2"].x:
        rook_remove(who_removes, 7)

    if who_removes.x > pos.box_dict["box1"].x:
        rook_remove(who_removes, -1)
    if who_removes.x > pos.box_dict["box2"].x:
        rook_remove(who_removes, -2)
    if who_removes.x > pos.box_dict["box3"].x:
        rook_remove(who_removes, -3)
    if who_removes.x > pos.box_dict["box4"].x:
        rook_remove(who_removes, -4)
    if who_removes.x > pos.box_dict["box5"].x:
        rook_remove(who_removes, -5)
    if who_removes.x > pos.box_dict["box6"].x:
        rook_remove(who_removes, -6)
    if who_removes.x > pos.box_dict["box7"].x:
        rook_remove(who_removes, -7)


def rookBMovements():
    mouse_pos = get_pos()

    if pos.turn == "white":
        pos.rookBlack1Clicked_plus8 = 0
        pos.rookBlack1Clicked_plus16 = 0
        pos.rookBlack1Clicked_plus24 = 0
        pos.rookBlack1Clicked_plus32 = 0
        pos.rookBlack1Clicked_plus40 = 0
        pos.rookBlack1Clicked_plus48 = 0
        pos.rookBlack1Clicked_plus1 = 0
        pos.rookBlack1Clicked_plus2 = 0
        pos.rookBlack1Clicked_plus3 = 0
        pos.rookBlack1Clicked_plus4 = 0
        pos.rookBlack1Clicked_plus5 = 0
        pos.rookBlack1Clicked_plus6 = 0
        pos.rookBlack1Clicked_minus8 = 0
        pos.rookBlack1Clicked_minus16 = 0
        pos.rookBlack1Clicked_minus24 = 0
        pos.rookBlack1Clicked_minus32 = 0
        pos.rookBlack1Clicked_minus40 = 0
        pos.rookBlack1Clicked_minus48 = 0
        pos.rookBlack1Clicked_minus1 = 0
        pos.rookBlack1Clicked_minus2 = 0
        pos.rookBlack1Clicked_minus3 = 0
        pos.rookBlack1Clicked_minus4 = 0
        pos.rookBlack1Clicked_minus5 = 0
        pos.rookBlack1Clicked_minus6 = 0

        pos.rookBlack2Clicked_plus8 = 0
        pos.rookBlack2Clicked_plus16 = 0
        pos.rookBlack2Clicked_plus24 = 0
        pos.rookBlack2Clicked_plus32 = 0
        pos.rookBlack2Clicked_plus40 = 0
        pos.rookBlack2Clicked_plus48 = 0
        pos.rookBlack2Clicked_plus1 = 0
        pos.rookBlack2Clicked_plus2 = 0
        pos.rookBlack2Clicked_plus3 = 0
        pos.rookBlack2Clicked_plus4 = 0
        pos.rookBlack2Clicked_plus5 = 0
        pos.rookBlack2Clicked_plus6 = 0
        pos.rookBlack2Clicked_minus8 = 0
        pos.rookBlack2Clicked_minus16 = 0
        pos.rookBlack2Clicked_minus24 = 0
        pos.rookBlack2Clicked_minus32 = 0
        pos.rookBlack2Clicked_minus40 = 0
        pos.rookBlack2Clicked_minus48 = 0
        pos.rookBlack2Clicked_minus1 = 0
        pos.rookBlack2Clicked_minus2 = 0
        pos.rookBlack2Clicked_minus3 = 0
        pos.rookBlack2Clicked_minus4 = 0
        pos.rookBlack2Clicked_minus5 = 0
        pos.rookBlack2Clicked_minus6 = 0

    if pos.turn == "black":
        if pos.rb1.collidepoint(mouse_pos[0], mouse_pos[1]):
            check_rook_canMove_restrictions(pos.rb1)
            check_rook_canCut_restrictions(pos.rb1)
        elif pos.rb2.collidepoint(mouse_pos[0], mouse_pos[1]):
            check_rook_canMove_restrictions(pos.rb2)
            check_rook_canCut_restrictions(pos.rb2)

    if pos.rookBlack1Clicked == 1:
        if pos.rookBlack1Clicked_cut == 1:
            rook_remove_restrictions(pos.rb1)
        move_rook_restrictions(pos.rb1)
    elif pos.rookBlack2Clicked == 1:
        if pos.rookBlack2Clicked_cut == 1:
            rook_remove_restrictions(pos.rb2)
        move_rook_restrictions(pos.rb2)


# restrictions on white rook movements
def check_white_rook_canMove_restrictions(which_rook_clicked):
    # along y-axis
    if which_rook_clicked.y < pos.box_dict["box57"].y:
        check_rook_canMove(which_rook_clicked, 8)
        rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box49"].y:
        if pos.rookWhite1Clicked_plus8 == 1 or \
                pos.rookWhite2Clicked_plus8 == 1:
            check_rook_canMove(which_rook_clicked, 16)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box41"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1) or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1):
            check_rook_canMove(which_rook_clicked, 24)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box33"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1) or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1 and pos.rookWhite2Clicked_plus24 == 1):
            check_rook_canMove(which_rook_clicked, 32)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box25"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 and pos.rookWhite1Clicked_plus32 == 1) or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1 and pos.rookWhite2Clicked_plus24 == 1 and pos.rookWhite2Clicked_plus32 == 1):
            check_rook_canMove(which_rook_clicked, 40)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box17"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 and pos.rookWhite1Clicked_plus32 == 1 and pos.rookWhite1Clicked_plus40 == 1) \
                or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1 and pos.rookWhite2Clicked_plus24 == 1 and pos.rookWhite2Clicked_plus32 == 1 and
                 pos.rookWhite2Clicked_plus40 == 1):
            check_rook_canMove(which_rook_clicked, 48)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y < pos.box_dict["box9"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 and pos.rookWhite1Clicked_plus32 == 1 and pos.rookWhite1Clicked_plus40 == 1
            and pos.rookWhite1Clicked_plus48 == 1) or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1 and pos.rookWhite2Clicked_plus24 == 1 and pos.rookWhite2Clicked_plus32 == 1 and
                 pos.rookWhite2Clicked_plus40 == 1 and pos.rookWhite2Clicked_plus48 == 1):
            check_rook_canMove(which_rook_clicked, 56)
            rook_conditions(which_rook_clicked)

    if which_rook_clicked.y > pos.box_dict["box1"].y:
        check_rook_canMove(which_rook_clicked, -8)
        rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box9"].y:
        if pos.rookWhite1Clicked_minus8 == 1 or pos.rookWhite2Clicked_minus8 == 1:
            check_rook_canMove(which_rook_clicked, -16)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box17"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1) or (pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1):
            check_rook_canMove(which_rook_clicked, -24)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box25"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1) or (
                pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1 and pos.rookWhite2Clicked_minus24 == 1):
            check_rook_canMove(which_rook_clicked, -32)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box33"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 and pos.rookWhite1Clicked_minus32 == 1) or \
                (pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1 and pos.rookWhite2Clicked_minus24 == 1 and pos.rookWhite2Clicked_minus32 == 1):
            check_rook_canMove(which_rook_clicked, -40)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box41"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 and pos.rookWhite1Clicked_minus32 == 1 and
            pos.rookWhite1Clicked_minus40 == 1) or \
                (pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1 and pos.rookWhite2Clicked_minus24 == 1 and pos.rookWhite2Clicked_minus32 == 1 and
                 pos.rookWhite2Clicked_minus40 == 1):
            check_rook_canMove(which_rook_clicked, -48)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.y > pos.box_dict["box49"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 and pos.rookWhite1Clicked_minus32 == 1 and
            pos.rookWhite1Clicked_minus40 and pos.rookWhite1Clicked_minus48 == 1) or \
                (pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1 and pos.rookWhite2Clicked_minus24 == 1 and pos.rookWhite2Clicked_minus32 == 1 and
                 pos.rookWhite2Clicked_minus40 and pos.rookWhite2Clicked_minus48 == 1):
            check_rook_canMove(which_rook_clicked, -56)
            rook_conditions(which_rook_clicked)

    # along x-axis
    if which_rook_clicked.x < pos.box_dict["box8"].x:
        check_rook_canMove(which_rook_clicked, 1)
        rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box7"].x:
        if pos.rookWhite1Clicked_plus1 == 1 or pos.rookWhite2Clicked_plus1 == 1:
            check_rook_canMove(which_rook_clicked, 2)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box6"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1) or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1):
            check_rook_canMove(which_rook_clicked, 3)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box5"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1) or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1):
            check_rook_canMove(which_rook_clicked, 4)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box4"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 and pos.rookWhite1Clicked_plus4 == 1) or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1 and pos.rookWhite2Clicked_plus4 == 1):
            check_rook_canMove(which_rook_clicked, 5)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box3"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 and pos.rookWhite1Clicked_plus4 == 1 and
            pos.rookWhite1Clicked_plus5 == 1) or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1 and pos.rookWhite2Clicked_plus4 == 1 and pos.rookWhite2Clicked_plus5 == 1):
            check_rook_canMove(which_rook_clicked, 6)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x < pos.box_dict["box2"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 and pos.rookWhite1Clicked_plus4 == 1 and
            pos.rookWhite1Clicked_plus5 == 1 and pos.rookWhite1Clicked_plus6 == 1) or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1 and pos.rookWhite2Clicked_plus4 == 1 and pos.rookWhite2Clicked_plus5 == 1
                 and pos.rookWhite2Clicked_plus6 == 1):
            check_rook_canMove(which_rook_clicked, 7)
            rook_conditions(which_rook_clicked)

    if which_rook_clicked.x > pos.box_dict["box1"].x:
        check_rook_canMove(which_rook_clicked, -1)
        rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box2"].x:
        if pos.rookWhite1Clicked_minus1 == 1 or pos.rookWhite2Clicked_minus1 == 1:
            check_rook_canMove(which_rook_clicked, -2)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box3"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1) or \
                (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1):
            check_rook_canMove(which_rook_clicked, -3)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box4"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1) or \
                (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1):
            check_rook_canMove(which_rook_clicked, -4)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box5"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 and pos.rookWhite1Clicked_minus4 == 1) or \
                (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1 and pos.rookWhite2Clicked_minus4 == 1):
            check_rook_canMove(which_rook_clicked, -5)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box6"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 and pos.rookWhite1Clicked_minus4 == 1 and
            pos.rookWhite1Clicked_minus5 == 1) or \
                (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1 and pos.rookWhite2Clicked_minus4 == 1 and pos.rookWhite2Clicked_minus5
                 == 1):
            check_rook_canMove(which_rook_clicked, -6)
            rook_conditions(which_rook_clicked)
    if which_rook_clicked.x > pos.box_dict["box7"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 and pos.rookWhite1Clicked_minus4 == 1 and
            pos.rookWhite1Clicked_minus5 == 1 and pos.rookWhite1Clicked_minus6 == 1) or \
                (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1 and pos.rookWhite2Clicked_minus4 == 1 and
                 pos.rookWhite2Clicked_minus5 == 1 and pos.rookWhite2Clicked_minus6 == 1):
            check_rook_canMove(which_rook_clicked, -7)
            rook_conditions(which_rook_clicked)


# check white rooks can cut or not
def check_white_rook_canCut(who_cuts, num):
    if pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb1) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb2) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb3) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb4) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb5) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb6) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb7) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.pb8) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.Kb) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.Qb) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.rb1) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.rb2) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.kb1) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.kb2) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.bb1) or \
            pos.boxLst[pos.boxLst.index(who_cuts) + num].colliderect(pos.bb2):
        pygame.draw.rect(window, red, pos.boxLst[pos.boxLst.index(who_cuts) + num], border_radius=100)
        if who_cuts == pos.rw1:
            pos.rookWhite1Clicked = 1
            pos.rookWhite1Clicked_cut = 1
            pos.rookWhite2Clicked = 0
        elif who_cuts == pos.rw2:
            pos.rookWhite2Clicked = 1
            pos.rookWhite2Clicked_cut = 1
            pos.rookWhite1Clicked = 0
        pos.pawnWhite1Clicked = 0
        pos.pawnWhite2Clicked = 0
        pos.pawnWhite3Clicked = 0
        pos.pawnWhite4Clicked = 0
        pos.pawnWhite5Clicked = 0
        pos.pawnWhite6Clicked = 0
        pos.pawnWhite7Clicked = 0
        pos.pawnWhite8Clicked = 0
        pos.KingWhiteClicked = 0
        pos.knightWhite1Clicked = 0
        pos.knightWhite2Clicked = 0
        pos.bishopWhite1Clicked = 0
        pos.bishopWhite2Clicked = 0
        pos.QueenWhiteClicked = 0


# restrictions on checking
def check_white_rook_canCut_restrictions(who_cuts):
    if who_cuts.y < pos.box_dict["box57"].y:
        check_white_rook_canCut(who_cuts, 8)
    if who_cuts.y < pos.box_dict["box49"].y:
        if pos.rookWhite1Clicked_plus8 == 1 or pos.rookWhite2Clicked_plus8 == 1:
            check_white_rook_canCut(who_cuts, 16)
    if who_cuts.y < pos.box_dict["box41"].y:
        if pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 or pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1:
            check_white_rook_canCut(who_cuts, 24)
    if who_cuts.y < pos.box_dict["box33"].y:
        if pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 or pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1 and \
                pos.rookWhite2Clicked_plus24 == 1:
            check_white_rook_canCut(who_cuts, 32)
    if who_cuts.y < pos.box_dict["box25"].y:
        if pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 and pos.rookWhite1Clicked_plus32 == 1 or pos.rookWhite2Clicked_plus8 == 1 and \
                pos.rookWhite2Clicked_plus16 == 1 and pos.rookWhite2Clicked_plus24 == 1 and pos.rookWhite2Clicked_plus32 == 1:
            check_white_rook_canCut(who_cuts, 40)
    if who_cuts.y < pos.box_dict["box17"].y:
        if pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 and pos.rookWhite1Clicked_plus32 == 1 and \
                pos.rookWhite1Clicked_plus40 == 1 or pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1 and pos.rookWhite2Clicked_plus24 == 1 and pos.rookWhite2Clicked_plus32 == 1\
                and pos.rookWhite2Clicked_plus40 == 1:
            check_white_rook_canCut(who_cuts, 48)
    if who_cuts.y < pos.box_dict["box9"].y:
        if pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 and pos.rookWhite1Clicked_plus32 == 1 and \
                pos.rookWhite1Clicked_plus40 == 1 and pos.rookWhite1Clicked_plus48 == 1 or pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1 and pos.rookWhite2Clicked_plus24 == 1\
                and pos.rookWhite2Clicked_plus32 == 1 and pos.rookWhite2Clicked_plus40 == 1 and pos.rookWhite2Clicked_plus48 == 1:
            check_white_rook_canCut(who_cuts, 56)

    if who_cuts.y > pos.box_dict["box1"].y:
        check_white_rook_canCut(who_cuts, -8)
    if who_cuts.y > pos.box_dict["box9"].y:
        if pos.rookWhite1Clicked_minus8 == 1 or pos.rookWhite2Clicked_minus8 == 1:
            check_white_rook_canCut(who_cuts, -16)
    if who_cuts.y > pos.box_dict["box17"].y:
        if pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 or pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1:
            check_white_rook_canCut(who_cuts, -24)
    if who_cuts.y > pos.box_dict["box25"].y:
        if pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 or pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1 \
                and pos.rookWhite2Clicked_minus24 == 1:
            check_white_rook_canCut(who_cuts, -32)
    if who_cuts.y > pos.box_dict["box33"].y:
        if pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 and pos.rookWhite1Clicked_minus32 == 1 or pos.rookWhite2Clicked_minus8 == 1 \
                and pos.rookWhite2Clicked_minus16 == 1 and pos.rookWhite2Clicked_minus24 == 1 and pos.rookWhite2Clicked_minus32 == 1:
            check_white_rook_canCut(who_cuts, -40)
    if who_cuts.y > pos.box_dict["box41"].y:
        if pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 and pos.rookWhite1Clicked_minus32 == 1 and \
                pos.rookWhite1Clicked_minus40 == 1 or pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1 and pos.rookWhite2Clicked_minus24 == 1 and pos.rookWhite2Clicked_minus32\
                == 1 and pos.rookWhite2Clicked_minus40 == 1:
            check_white_rook_canCut(who_cuts, -48)
    if who_cuts.y > pos.box_dict["box49"].y:
        if pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 and pos.rookWhite1Clicked_minus32 == 1 and \
                pos.rookWhite1Clicked_minus40 == 1 and pos.rookWhite1Clicked_minus48 == 1 or pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1 and pos.rookWhite2Clicked_minus24\
                == 1 and pos.rookWhite2Clicked_minus32 == 1 and pos.rookWhite2Clicked_minus40 == 1 and pos.rookWhite2Clicked_minus48 == 1:
            check_white_rook_canCut(who_cuts, -56)

    if who_cuts.x < pos.box_dict["box8"].x:
        check_white_rook_canCut(who_cuts, 1)
    if who_cuts.x < pos.box_dict["box7"].x:
        if pos.rookWhite1Clicked_plus1 == 1 or pos.rookWhite2Clicked_plus1 == 1:
            check_white_rook_canCut(who_cuts, 2)
    if who_cuts.x < pos.box_dict["box6"].x:
        if pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 or pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1:
            check_white_rook_canCut(who_cuts, 3)
    if who_cuts.x < pos.box_dict["box5"].x:
        if pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 or pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and \
                pos.rookWhite2Clicked_plus3 == 1:
            check_white_rook_canCut(who_cuts, 4)
    if who_cuts.x < pos.box_dict["box4"].x:
        if pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 and pos.rookWhite1Clicked_plus4 == 1 or pos.rookWhite2Clicked_plus1 == 1 and \
                pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1 and pos.rookWhite2Clicked_plus4 == 1:
            check_white_rook_canCut(who_cuts, 5)
    if who_cuts.x < pos.box_dict["box3"].x:
        if pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 and pos.rookWhite1Clicked_plus4 == 1 and \
                pos.rookWhite1Clicked_plus5 == 1 or pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1 and pos.rookWhite2Clicked_plus4 == 1 \
                and pos.rookWhite2Clicked_plus5 == 1:
            check_white_rook_canCut(who_cuts, 6)
    if who_cuts.x < pos.box_dict["box2"].x:
        if pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 and pos.rookWhite1Clicked_plus4 == 1 and \
                pos.rookWhite1Clicked_plus5 == 1 and pos.rookWhite1Clicked_plus6 == 1 or pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1 and\
                pos.rookWhite2Clicked_plus4 == 1 and pos.rookWhite2Clicked_plus5 == 1 and pos.rookWhite2Clicked_plus6 == 1:
            check_white_rook_canCut(who_cuts, 7)

    if who_cuts.x > pos.box_dict["box1"].x:
        check_white_rook_canCut(who_cuts, -1)
    if who_cuts.x > pos.box_dict["box2"].x:
        if pos.rookWhite1Clicked_minus1 == 1 or pos.rookWhite2Clicked_minus1 == 1:
            check_white_rook_canCut(who_cuts, -2)
    if who_cuts.x > pos.box_dict["box3"].x:
        if pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 or pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1:
            check_white_rook_canCut(who_cuts, -3)
    if who_cuts.x > pos.box_dict["box4"].x:
        if pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 or pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and\
                pos.rookWhite2Clicked_minus3 == 1:
            check_white_rook_canCut(who_cuts, -4)
    if who_cuts.x > pos.box_dict["box5"].x:
        if pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 and pos.rookWhite1Clicked_minus4 == 1 or pos.rookWhite2Clicked_minus1 == 1 and\
                pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1 and pos.rookWhite2Clicked_minus4 == 1:
            check_white_rook_canCut(who_cuts, -5)
    if who_cuts.x > pos.box_dict["box6"].x:
        if pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 and pos.rookWhite1Clicked_minus4 == 1 and \
                pos.rookWhite1Clicked_minus5 == 1 or pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1 and pos.rookWhite2Clicked_minus4 == \
                1 and pos.rookWhite2Clicked_minus5 == 1:
            check_white_rook_canCut(who_cuts, -6)
    if who_cuts.x > pos.box_dict["box7"].x:
        if pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 and pos.rookWhite1Clicked_minus4 == 1 and \
                pos.rookWhite1Clicked_minus5 == 1 and pos.rookWhite1Clicked_minus6 == 1 or pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == \
                1 and pos.rookWhite2Clicked_minus4 == 1 and pos.rookWhite2Clicked_minus5 == 1 and pos.rookWhite2Clicked_minus6 == 1:
            check_white_rook_canCut(who_cuts, -7)


# movement restrictions
def move_white_rook_restrictions(who_moves):
    # along y-axis(+)
    if who_moves.y < pos.box_dict["box57"].y:
        move_rook(who_moves, 8)
    if who_moves.y < pos.box_dict["box49"].y:
        if pos.rookWhite1Clicked_plus8 == 1 or \
                pos.rookWhite2Clicked_plus8 == 1:
            move_rook(who_moves, 16)
    if who_moves.y < pos.box_dict["box41"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1) or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1):
            move_rook(who_moves, 24)
    if who_moves.y < pos.box_dict["box33"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1) or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus16 == 1 and pos.rookWhite2Clicked_plus24 == 1):
            move_rook(who_moves, 32)
    if who_moves.y < pos.box_dict["box25"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 and pos.rookWhite1Clicked_plus32 == 1) or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus24 == 1 and pos.rookWhite2Clicked_plus32 == 1):
            move_rook(who_moves, 40)
    if who_moves.y < pos.box_dict["box17"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 and pos.rookWhite1Clicked_plus32 == 1 and pos.rookWhite1Clicked_plus40 == 1) \
                or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus24 == 1 and pos.rookWhite2Clicked_plus32 == 1 and pos.rookWhite2Clicked_plus40 == 1):
            move_rook(who_moves, 48)
    if who_moves.y < pos.box_dict["box9"].y:
        if (pos.rookWhite1Clicked_plus8 == 1 and pos.rookWhite1Clicked_plus16 == 1 and pos.rookWhite1Clicked_plus24 == 1 and pos.rookWhite1Clicked_plus32 == 1 and pos.rookWhite1Clicked_plus40 == 1
            and pos.rookWhite1Clicked_plus48 == 1) \
                or \
                (pos.rookWhite2Clicked_plus8 == 1 and pos.rookWhite2Clicked_plus24 == 1 and pos.rookWhite2Clicked_plus32 == 1 and pos.rookWhite2Clicked_plus40 == 1 and pos.rookWhite2Clicked_plus48
                 == 1):
            move_rook(who_moves, 56)

    # along y-axis(-)
    if who_moves.y > pos.box_dict["box1"].y:
        move_rook(who_moves, -8)
    if who_moves.y > pos.box_dict["box9"].y:
        if pos.rookWhite1Clicked_minus8 == 1 or \
                pos.rookWhite2Clicked_minus8 == 1:
            move_rook(who_moves, -16)
    if who_moves.y > pos.box_dict["box17"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1) or \
                (pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1):
            move_rook(who_moves, -24)
    if who_moves.y > pos.box_dict["box25"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1) or \
                (pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus16 == 1 and pos.rookWhite2Clicked_minus24 == 1):
            move_rook(who_moves, -32)
    if who_moves.y > pos.box_dict["box33"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 and pos.rookWhite1Clicked_minus32 == 1) or \
                (pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus24 == 1 and pos.rookWhite2Clicked_minus32 == 1):
            move_rook(who_moves, -40)
    if who_moves.y > pos.box_dict["box41"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 and pos.rookWhite1Clicked_minus32 == 1 and
            pos.rookWhite1Clicked_minus40 == 1) \
                or \
                (pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus24 == 1 and pos.rookWhite2Clicked_minus32 == 1 and pos.rookWhite2Clicked_minus40 == 1):
            move_rook(who_moves, -48)
    if who_moves.y > pos.box_dict["box49"].y:
        if (pos.rookWhite1Clicked_minus8 == 1 and pos.rookWhite1Clicked_minus16 == 1 and pos.rookWhite1Clicked_minus24 == 1 and pos.rookWhite1Clicked_minus32 == 1 and pos.rookWhite1Clicked_minus40
            == 1 and pos.rookWhite1Clicked_minus48 == 1) \
                or \
                (pos.rookWhite2Clicked_minus8 == 1 and pos.rookWhite2Clicked_minus24 == 1 and pos.rookWhite2Clicked_minus32 == 1 and pos.rookWhite2Clicked_minus40 == 1 and
                 pos.rookWhite2Clicked_minus48 == 1):
            move_rook(who_moves, -56)

    # along x-axis(+)
    if who_moves.x < pos.box_dict["box8"].x:
        move_rook(who_moves, 1)
    if who_moves.x < pos.box_dict["box7"].x:
        if pos.rookWhite1Clicked_plus1 == 1 or \
                pos.rookWhite2Clicked_plus1 == 1:
            move_rook(who_moves, 2)
    if who_moves.x < pos.box_dict["box6"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1) or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1):
            move_rook(who_moves, 3)
    if who_moves.x < pos.box_dict["box5"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1) or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1):
            move_rook(who_moves, 4)
    if who_moves.x < pos.box_dict["box4"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 and pos.rookWhite1Clicked_plus4 == 1) or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1 and pos.rookWhite2Clicked_plus4 == 1):
            move_rook(who_moves, 5)
    if who_moves.x < pos.box_dict["box3"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 and pos.rookWhite1Clicked_plus4 == 1 and pos.rookWhite1Clicked_plus5 == 1) or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1 and pos.rookWhite2Clicked_plus4 == 1 and pos.rookWhite2Clicked_plus5 == 1):
            move_rook(who_moves, 6)
    if who_moves.x < pos.box_dict["box2"].x:
        if (pos.rookWhite1Clicked_plus1 == 1 and pos.rookWhite1Clicked_plus2 == 1 and pos.rookWhite1Clicked_plus3 == 1 and pos.rookWhite1Clicked_plus4 == 1 and pos.rookWhite1Clicked_plus5 == 1 and
            pos.rookWhite1Clicked_plus6 == 1) \
                or \
                (pos.rookWhite2Clicked_plus1 == 1 and pos.rookWhite2Clicked_plus2 == 1 and pos.rookWhite2Clicked_plus3 == 1 and pos.rookWhite2Clicked_plus4 == 1 and pos.rookWhite2Clicked_plus5 == 1
                 and pos.rookWhite2Clicked_plus6 == 1):
            move_rook(who_moves, 7)

    # along x-axis(-)
    if who_moves.x > pos.box_dict["box1"].x:
        move_rook(who_moves, -1)
    if who_moves.x > pos.box_dict["box2"].x:
        if pos.rookWhite1Clicked_minus1 == 1 or \
                pos.rookWhite2Clicked_minus1 == 1:
            move_rook(who_moves, -2)
    if who_moves.x > pos.box_dict["box3"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1) or \
                (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1):
            move_rook(who_moves, -3)
    if who_moves.x > pos.box_dict["box4"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1) or \
                (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1):
            move_rook(who_moves, -4)
    if who_moves.x > pos.box_dict["box5"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 and pos.rookWhite1Clicked_minus4 == 1) or \
                (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1 and pos.rookWhite2Clicked_minus4 == 1):
            move_rook(who_moves, -5)
    if who_moves.x > pos.box_dict["box6"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 and pos.rookWhite1Clicked_minus4 == 1 and pos.rookWhite1Clicked_minus5 ==
            1) or \
              (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1 and pos.rookWhite2Clicked_minus4 == 1 and pos.rookWhite2Clicked_minus5
               == 1):
            move_rook(who_moves, -6)
    if who_moves.x > pos.box_dict["box7"].x:
        if (pos.rookWhite1Clicked_minus1 == 1 and pos.rookWhite1Clicked_minus2 == 1 and pos.rookWhite1Clicked_minus3 == 1 and pos.rookWhite1Clicked_minus4 == 1 and pos.rookWhite1Clicked_minus5 == 1
            and pos.rookWhite1Clicked_minus6 == 1) \
                or \
                (pos.rookWhite2Clicked_minus1 == 1 and pos.rookWhite2Clicked_minus2 == 1 and pos.rookWhite2Clicked_minus3 == 1 and pos.rookWhite2Clicked_minus4 == 1 and pos.rookWhite2Clicked_minus5
                 == 1 and pos.rookWhite2Clicked_minus6 == 1):
            move_rook(who_moves, -7)


# remove the black pieces
def white_rook_remove(who_removes, num):
    mouse_pos = get_pos()

    if pos.boxLst[pos.boxLst.index(who_removes) + num].collidepoint(mouse_pos[0], mouse_pos[1]):
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb1):
            pos.pb1 = pos.black_deadPieceRect_dict["blackCutPiece_1"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb2):
            pos.pb2 = pos.black_deadPieceRect_dict["blackCutPiece_2"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb3):
            pos.pb3 = pos.black_deadPieceRect_dict["blackCutPiece_3"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb4):
            pos.pb4 = pos.black_deadPieceRect_dict["blackCutPiece_4"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb5):
            pos.pb5 = pos.black_deadPieceRect_dict["blackCutPiece_5"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb6):
            pos.pb6 = pos.black_deadPieceRect_dict["blackCutPiece_6"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb7):
            pos.pb7 = pos.black_deadPieceRect_dict["blackCutPiece_7"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.pb8):
            pos.pb8 = pos.black_deadPieceRect_dict["blackCutPiece_8"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.rb1):
            pos.rb1 = pos.black_deadPieceRect_dict["blackCutPiece_9"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.rb2):
            pos.rb2 = pos.black_deadPieceRect_dict["blackCutPiece_10"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.kb1):
            pos.kb1 = pos.black_deadPieceRect_dict["blackCutPiece_11"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.kb2):
            pos.kb2 = pos.black_deadPieceRect_dict["blackCutPiece_12"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.bb1):
            pos.bb1 = pos.black_deadPieceRect_dict["blackCutPiece_13"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.bb2):
            pos.bb2 = pos.black_deadPieceRect_dict["blackCutPiece_14"]
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.Kb):
            pos.Kb = pos.black_deadPieceRect_dict["blackCutPiece_15"]
            pos.KingBlack_isDead = 1
        if pos.boxLst[pos.boxLst.index(who_removes) + num].colliderect(pos.Qb):
            pos.Qb = pos.black_deadPieceRect_dict["blackCutPiece_16"]

        if who_removes == pos.rw1:
            pos.rw1 = pos.boxLst[pos.boxLst.index(who_removes) + num]
            pos.rookWhite1Clicked = 0
            pos.rookWhite1Clicked_cut = 0
        elif who_removes == pos.rw2:
            pos.rw2 = pos.boxLst[pos.boxLst.index(who_removes) + num]
            pos.rookWhite2Clicked = 0
            pos.rookWhite2Clicked_cut = 0
        pos.turn = "black"


# removing restrictions
def white_rook_remove_restrictions(who_removes):
    # along y-axis
    if who_removes.y < pos.box_dict["box57"].y:
        white_rook_remove(who_removes, 8)
    if who_removes.y < pos.box_dict["box49"].y:
        white_rook_remove(who_removes, 16)
    if who_removes.y < pos.box_dict["box41"].y:
        white_rook_remove(who_removes, 24)
    if who_removes.y < pos.box_dict["box33"].y:
        white_rook_remove(who_removes, 32)
    if who_removes.y < pos.box_dict["box25"].y:
        white_rook_remove(who_removes, 40)
    if who_removes.y < pos.box_dict["box17"].y:
        white_rook_remove(who_removes, 48)
    if who_removes.y < pos.box_dict["box9"].y:
        white_rook_remove(who_removes, 56)

    if who_removes.y > pos.box_dict["box1"].y:
        white_rook_remove(who_removes, -8)
    if who_removes.y > pos.box_dict["box9"].y:
        white_rook_remove(who_removes, -16)
    if who_removes.y > pos.box_dict["box17"].y:
        white_rook_remove(who_removes, -24)
    if who_removes.y > pos.box_dict["box25"].y:
        white_rook_remove(who_removes, -32)
    if who_removes.y > pos.box_dict["box33"].y:
        white_rook_remove(who_removes, -40)
    if who_removes.y > pos.box_dict["box41"].y:
        white_rook_remove(who_removes, -48)
    if who_removes.y > pos.box_dict["box49"].y:
        white_rook_remove(who_removes, -56)

    # along x-axis
    if who_removes.x < pos.box_dict["box8"].x:
        white_rook_remove(who_removes, 1)
    if who_removes.x < pos.box_dict["box7"].x:
        white_rook_remove(who_removes, 2)
    if who_removes.x < pos.box_dict["box6"].x:
        white_rook_remove(who_removes, 3)
    if who_removes.x < pos.box_dict["box5"].x:
        white_rook_remove(who_removes, 4)
    if who_removes.x < pos.box_dict["box4"].x:
        white_rook_remove(who_removes, 5)
    if who_removes.x < pos.box_dict["box3"].x:
        white_rook_remove(who_removes, 6)
    if who_removes.x < pos.box_dict["box2"].x:
        white_rook_remove(who_removes, 7)

    if who_removes.x > pos.box_dict["box1"].x:
        white_rook_remove(who_removes, -1)
    if who_removes.x > pos.box_dict["box2"].x:
        white_rook_remove(who_removes, -2)
    if who_removes.x > pos.box_dict["box3"].x:
        white_rook_remove(who_removes, -3)
    if who_removes.x > pos.box_dict["box4"].x:
        white_rook_remove(who_removes, -4)
    if who_removes.x > pos.box_dict["box5"].x:
        white_rook_remove(who_removes, -5)
    if who_removes.x > pos.box_dict["box6"].x:
        white_rook_remove(who_removes, -6)
    if who_removes.x > pos.box_dict["box7"].x:
        white_rook_remove(who_removes, -7)


def rookWMovements():
    mouse_pos = get_pos()

    if pos.turn == "black":
        pos.rookWhite1Clicked_plus8 = 0
        pos.rookWhite1Clicked_plus16 = 0
        pos.rookWhite1Clicked_plus24 = 0
        pos.rookWhite1Clicked_plus32 = 0
        pos.rookWhite1Clicked_plus40 = 0
        pos.rookWhite1Clicked_plus48 = 0
        pos.rookWhite1Clicked_plus1 = 0
        pos.rookWhite1Clicked_plus2 = 0
        pos.rookWhite1Clicked_plus3 = 0
        pos.rookWhite1Clicked_plus4 = 0
        pos.rookWhite1Clicked_plus5 = 0
        pos.rookWhite1Clicked_plus6 = 0
        pos.rookWhite1Clicked_minus8 = 0
        pos.rookWhite1Clicked_minus16 = 0
        pos.rookWhite1Clicked_minus24 = 0
        pos.rookWhite1Clicked_minus32 = 0
        pos.rookWhite1Clicked_minus40 = 0
        pos.rookWhite1Clicked_minus48 = 0
        pos.rookWhite1Clicked_minus1 = 0
        pos.rookWhite1Clicked_minus2 = 0
        pos.rookWhite1Clicked_minus3 = 0
        pos.rookWhite1Clicked_minus4 = 0
        pos.rookWhite1Clicked_minus5 = 0
        pos.rookWhite1Clicked_minus6 = 0

        pos.rookWhite2Clicked_plus8 = 0
        pos.rookWhite2Clicked_plus16 = 0
        pos.rookWhite2Clicked_plus24 = 0
        pos.rookWhite2Clicked_plus32 = 0
        pos.rookWhite2Clicked_plus40 = 0
        pos.rookWhite2Clicked_plus48 = 0
        pos.rookWhite2Clicked_plus1 = 0
        pos.rookWhite2Clicked_plus2 = 0
        pos.rookWhite2Clicked_plus3 = 0
        pos.rookWhite2Clicked_plus4 = 0
        pos.rookWhite2Clicked_plus5 = 0
        pos.rookWhite2Clicked_plus6 = 0
        pos.rookWhite2Clicked_minus8 = 0
        pos.rookWhite2Clicked_minus16 = 0
        pos.rookWhite2Clicked_minus24 = 0
        pos.rookWhite2Clicked_minus32 = 0
        pos.rookWhite2Clicked_minus40 = 0
        pos.rookWhite2Clicked_minus48 = 0
        pos.rookWhite2Clicked_minus1 = 0
        pos.rookWhite2Clicked_minus2 = 0
        pos.rookWhite2Clicked_minus3 = 0
        pos.rookWhite2Clicked_minus4 = 0
        pos.rookWhite2Clicked_minus5 = 0
        pos.rookWhite2Clicked_minus6 = 0

    if pos.turn == "white":
        if pos.rw1.collidepoint(mouse_pos[0], mouse_pos[1]):
            check_white_rook_canMove_restrictions(pos.rw1)
            check_white_rook_canCut_restrictions(pos.rw1)
        elif pos.rw2.collidepoint(mouse_pos[0], mouse_pos[1]):
            check_white_rook_canMove_restrictions(pos.rw2)
            check_white_rook_canCut_restrictions(pos.rw2)

    if pos.rookWhite1Clicked == 1:
        if pos.rookWhite1Clicked_cut == 1:
            white_rook_remove_restrictions(pos.rw1)
        move_white_rook_restrictions(pos.rw1)
    elif pos.rookWhite2Clicked == 1:
        if pos.rookWhite2Clicked_cut == 1:
            white_rook_remove_restrictions(pos.rw2)
        move_white_rook_restrictions(pos.rw2)


def bishopBMovements():
    pass


def bishopWMovements():
    pass


# contains the functions to be run inside while loop
def drawGameWindow():
    window.fill(white)
    drawChessBoard()
    drawPieces()
    pawnBMovements()
    pawnWMovements()
    kingBMovements()
    kingWMovements()
    knightBMovements()
    knightWMovements()
    rookBMovements()
    rookWMovements()
    bishopBMovements()
    bishopWMovements()


game = MainGame()
# run the game
game.gameLoop()
