# import statements
import pygame
from pygame.locals import *
import sys
from assets import chessboard, pieces, logger
import json
from assets.socket import SocketClient
import uuid
import random


def get_uid():
    return str(uuid.uuid4())


class Game():
    def __init__(self, iconPath: str, loadFlag: bool) -> None:
        pygame.init()
        self.socket = SocketClient("http://localhost:8080")
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
        self.user_details = {
            'id': get_uid(),
            'name': '',
            'username': '',
            'army': ''
        }
        self.opponent_details = {
            'id': '',
            'name': '',
            'username': '',
            'army': ''
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
            self.imageWidth, self.imageHeight, loadFlag, self.socket)
        self.mouse_x = -1
        self.mouse_y = -1
        self.turn = self.getFirstTurn(loadFlag)

        @self.socket.sio.on("--server:match")
        def onMatch(data):
            self.opponent_details['id'] = data['id']
            self.opponent_details['name'] = data['name']
            self.opponent_details['username'] = data['username']
            self.opponent_details['army'] = data['army']
            self.user_details['army'] = "black" if data['army'] == "white" else "white"
            self.turn = data['firstTurn']
            logger.print_success(f'[MATCH STARTED]\nYou: {
                                 self.user_details}\nOpponent: {self.opponent_details}')

        @self.socket.sio.on("--server:piece-move")
        def onMove(data):
            name = data['name']
            pos = data['pos']
            logger.print_error(
                f"[#] Moved {name} to {pos}")
            self.turn = 'w' if self.turn == 'b' else 'b'
            logger.print_warn(
                f"Turn: {'white' if self.turn == 'w' else 'black'}")
            # update opponent's army pos
            if self.opponent_details['army'] == 'white':
                self.whiteArmyPos[name].x = pos[0]
                self.whiteArmyPos[name].y = pos[1]
                self.whiteArmyPos[name].pos.x = pos[0]
                self.whiteArmyPos[name].pos.y = pos[1]
            elif self.opponent_details['army'] == 'black':
                self.blackArmyPos[name].x = pos[0]
                self.blackArmyPos[name].y = pos[1]
                self.blackArmyPos[name].pos.x = pos[0]
                self.blackArmyPos[name].pos.y = pos[1]

        @self.socket.sio.on("--server:piece-remove")
        def onRemove(data):
            name = data['name']
            logger.print_error(f"[#] Removed {name}")
            # update opponent's army
            if self.opponent_details['army'] == 'white':
                self.blackArmyPos.pop(name)
            elif self.opponent_details['army'] == 'black':
                self.whiteArmyPos.pop(name)

        @self.socket.sio.on("--server:player-left")
        def onPlayerLeft(data):
            logger.print_success(f'{data['message']}')

    def getFirstTurn(self, loadFlag: bool):
        if loadFlag:
            with open("game_state.json", "r") as f:
                state = json.load(f)
                return state['turn']
        return 'w'

    def drawGameWindow(self):
        self.window.fill(self.colors["white"])
        self.getMousePosition()
        chessboard.drawChessBoard(
            self.window, self.colors["white"], self.colors["grey"], self.whiteBoxesPosList, self.blackBoxesPosList)
        pieces.drawPieces(self.window, self.piecesImages,
                          self.whiteArmyPos, self.blackArmyPos)
        turn = pieces.piecesMovements(self.window, self.colors, self.boxes,
                                      self.whiteArmyPos, self.blackArmyPos, self.mouse_x, self.mouse_y, self.turn, self.user_details['army'])
        if turn is not None:
            self.turn = turn
        pieces.checkWin(self.blackArmyPos, self.whiteArmyPos)
        pieces.resetStates(self.boxes, self.blackArmyPos,
                           self.whiteArmyPos, self.turn, self.mouse_x, self.mouse_y)

    def getMousePosition(self):
        if pygame.mouse.get_pressed(3)[0]:
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def startGame(self):
        self.input_user_details()
        logger.print_warn(self.user_details.__str__())

        self.socket.connect(self.user_details)
        if not self.socket.sio.connected:
            logger.print_error("Unable to connect.")
            return

        while len(self.opponent_details['id']) == 0:
            print("Waiting for other player to join...", end='\r')
        print()

        logger.print_warn(f"Turn: {"white" if self.turn == 'w' else "black"}")

        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                if event.type == pygame.KEYDOWN and (event.key == K_ESCAPE):
                    self.run = False

            self.drawGameWindow()
            self.reconnect_to_socket()
            pygame.display.update()
            self.clock.tick(self.fps)
        self.quitGame()

    def input_user_details(self):
        logger.print_warn("Enter your name:")
        self.user_details['name'] = input()
        logger.print_warn("Enter your username:")
        self.user_details['username'] = input()

    def reconnect_to_socket(self):
        if not self.socket.sio.connected:
            logger.print_info("Reconnecting...")
            self.socket.connect(self.user_details)

    def quitGame(self):
        self.socket.disconnect()
        self.saveGameState()
        pygame.quit()
        sys.exit()

    def saveGameState(self):
        state = {"turn": self.turn, "blackArmyData": {}, "whiteArmyData": {}}

        def addData(armyPos: dict, key: str):
            for piece in armyPos:
                state[key][piece] = [
                    armyPos[piece].x // self.imageWidth, armyPos[piece].y // self.imageHeight]

        addData(self.blackArmyPos, "blackArmyData")
        addData(self.whiteArmyPos, "whiteArmyData")

        with open("game_state.json", "w") as f:
            json.dump(state, f)

        logger.print_info("[*] Game state saved.")


def takeUserResponse():
    try:
        with open("game_state.json", "r") as f:
            state = json.load(f)
            if not state:
                return False
        logger.print_warn(
            "[?] Do you want to load the previous state: (yes|no)")
        flag = input()
        return True if flag.lower() == "yes" else False
    except Exception as e:
        return False


if __name__ == '__main__':
    logger.print_info("[*] Chess Engine Loading ...")
    # loadFlag = takeUserResponse()
    # game_instance = Game("../chessAssets/chess.png", loadFlag)
    game_instance = Game("../chessAssets/chess.png", False)
    logger.print_success("[*] Game Started")
    game_instance.startGame()
