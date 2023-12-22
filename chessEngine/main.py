# import statements
import pygame
from pygame.locals import *
import sys
from assets import chessboard, pieces, logger


class Game():
    def __init__(self, iconPath: str) -> None:
        pygame.init()
        self.colors = {
            "white": (255, 255, 255),
            "black": (0, 0, 0),
            "red": (255, 0, 0),
            "blue": (0, 0, 255),
            "green": (0, 255, 0),
            "grey": (192, 192, 192),
            "silver": (188, 198, 204),
            "charcoalBlue": (54, 69, 79),
        }
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.windowWidth = 400
        self.windowHeight = 400
        self.window = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight))
        pygame.display.set_caption("Chess Game")
        pygame.display.set_icon(pygame.image.load(iconPath))
        self.run = True
        self.boxWidth = self.windowWidth // 8
        self.boxHeight = self.windowHeight // 8
        self.imageWidth = self.boxWidth
        self.imageHeight = self.boxHeight
        self.boxes = chessboard.getBoxes_rect(self.boxWidth, self.boxHeight)
        self.whiteBoxesPosList, self.blackBoxesPosList = chessboard.getBoxes_posList(
            self.boxes)
        self.piecesImages = pieces.loadAssets(
            "../chessAssets", self.boxWidth, self.boxHeight)
        self.whiteArmyPos, self.blackArmyPos = pieces.getArmy(
            self.imageWidth, self.imageHeight)
        self.mouse_x = -1
        self.mouse_y = -1
        self.turn = 'w'

    def drawGameWindow(self):
        self.window.fill(self.colors["white"])
        self.getMousePosition()
        chessboard.drawChessBoard(
            self.window, self.colors["white"], self.colors["grey"], self.whiteBoxesPosList, self.blackBoxesPosList)
        pieces.drawPieces(self.window, self.piecesImages,
                          self.whiteArmyPos, self.blackArmyPos)
        self.turn = pieces.piecesMovements(self.window, self.colors, self.boxes,
                                           self.whiteArmyPos, self.blackArmyPos, self.mouse_x, self.mouse_y, self.turn)
        pieces.checkWin(self.blackArmyPos, self.whiteArmyPos)
        pieces.resetStates(self.boxes, self.blackArmyPos,
                           self.whiteArmyPos, self.turn, self.mouse_x, self.mouse_y)

    def getMousePosition(self):
        if pygame.mouse.get_pressed(3)[0]:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def startGame(self):
        firstTurn = "white" if self.turn == 'w' else "black"
        logger.print_warn(f"First Turn: {firstTurn}")

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN and (event.key == K_ESCAPE):
                    self.run = False

            self.drawGameWindow()
            pygame.display.update()
            self.clock.tick(self.fps)
        self.quitGame()

    def quitGame(self):
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    logger.print_info("[*] Chess Engine Loading ...")
    game_instance = Game("../chessAssets/chess.png")
    logger.print_success("[*] Game Started")
    game_instance.startGame()
