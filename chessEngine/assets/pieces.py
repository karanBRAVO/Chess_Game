import pygame
import sys
from assets.army import pawn, rook, knight, bishop, queen, king
from assets import logger
import json
from assets.socket import SocketClient


def resetStates(boxes: dict, blackArmy: dict, whiteArmy: dict, turn: str, mouseX: float, mouseY: float):
    def resetArmy(army: dict):
        for piece in army:
            army[piece].resetState()

    def resetStateWhenClickedOnEmptyBox(army: dict):
        for piece in army:
            if army[piece].pos.collidepoint(mouseX, mouseY):
                return

        for box in boxes:
            if boxes[box].collidepoint(mouseX, mouseY):
                resetArmy(army)

    if turn == 'w':
        resetArmy(blackArmy)
        resetStateWhenClickedOnEmptyBox(whiteArmy)

    elif turn == 'b':
        resetArmy(whiteArmy)
        resetStateWhenClickedOnEmptyBox(blackArmy)


def checkWin(blackArmy: dict, whiteArmy: dict):
    winflag = False

    if 'Kb' not in list(blackArmy):
        logger.print_success("[*] White Won")
        winflag = True
    elif 'Kw' not in list(whiteArmy):
        logger.print_success("[*] Black Won")
        winflag = True

    if winflag:
        pygame.quit()
        sys.exit()


def piecesMovements(window, colors: dict, boxes: dict, whiteArmy: dict, blackArmy: dict, mouseX: float, mouseY: float, turn: str, army: str):
    if turn == 'b' and army == 'black':
        for piece in list(blackArmy):
            blackArmy[piece].detectClick(
                window, mouseX, mouseY, boxes, whiteArmy, blackArmy, colors)
            moved = blackArmy[piece].Move(
                boxes, mouseX, mouseY, whiteArmy, blackArmy)
            if moved:
                current_turn = "white" if turn == 'b' else "black"
                logger.print_warn(f"Turn: {current_turn}")
                break
        return 'w' if moved else 'b'

    elif turn == 'w' and army == 'white':
        for piece in list(whiteArmy):
            whiteArmy[piece].detectClick(
                window, mouseX, mouseY, boxes, whiteArmy, blackArmy, colors)
            moved = whiteArmy[piece].Move(
                boxes, mouseX, mouseY, whiteArmy, blackArmy)
            if moved:
                current_turn = "white" if turn == 'b' else "black"
                logger.print_warn(f"Turn: {current_turn}")
                break
        return 'b' if moved else 'w'

    return turn


def drawPieces(window, assets: dict, whiteArmy: dict, blackArmy: dict):
    for whitePiece in whiteArmy:
        window.blit(assets[whiteArmy[whitePiece].face],
                    whiteArmy[whitePiece].pos)
    for blackPiece in blackArmy:
        window.blit(assets[blackArmy[blackPiece].face],
                    blackArmy[blackPiece].pos)


def getArmy(width, height, loadFlag: bool, sio: SocketClient):
    # if loadFlag:
    #     with open("game_state.json", 'r') as f:
    #         state = json.load(f)
    #         blackArmyData = state["blackArmyData"]
    #         whiteArmyData = state["whiteArmyData"]
    #         logger.print_info("[*] Previous game state loaded")

    #     blackArmy = {}
    #     whiteArmy = {}

    #     def createArmyFromPreviousState(armyData: dict, _army: dict):
    #         for piece in armyData:
    #             _x, _y = armyData[piece]
    #             _x *= width
    #             _y *= height
    #             if piece[0] == 'p':
    #                 instance = pawn.Pawn(_x, _y, width, height, 'p'+piece[1])
    #             elif piece[0] == 'r':
    #                 instance = rook.Rook(_x, _y, width, height, 'r'+piece[1])
    #             elif piece[0] == 'b':
    #                 instance = bishop.Bishop(
    #                     _x, _y, width, height, 'b'+piece[1])
    #             elif piece[0] == 'k':
    #                 instance = knight.Knight(
    #                     _x, _y, width, height, 'k'+piece[1])
    #             elif piece[0] == 'Q':
    #                 instance = queen.Queen(_x, _y, width, height, 'Q'+piece[1])
    #             elif piece[0] == 'K':
    #                 instance = king.King(_x, _y, width, height, 'K'+piece[1])
    #             _army[piece] = instance

    #     createArmyFromPreviousState(blackArmyData, blackArmy)
    #     createArmyFromPreviousState(whiteArmyData, whiteArmy)

    # else:
    #     blackArmy = {
    #         'pb1': pawn.Pawn('pb1', 0 * width, 1 * height, width, height, 'pb'),
    #         'pb2': pawn.Pawn(1 * width, 1 * height, width, height, 'pb'),
    #         'pb3': pawn.Pawn(2 * width, 1 * height, width, height, 'pb'),
    #         'pb4': pawn.Pawn(3 * width, 1 * height, width, height, 'pb'),
    #         'pb5': pawn.Pawn(4 * width, 1 * height, width, height, 'pb'),
    #         'pb6': pawn.Pawn(5 * width, 1 * height, width, height, 'pb'),
    #         'pb7': pawn.Pawn(6 * width, 1 * height, width, height, 'pb'),
    #         'pb8': pawn.Pawn(7 * width, 1 * height, width, height, 'pb'),
    #         'rb1': rook.Rook(0 * width, 0 * height, width, height, 'rb'),
    #         'rb2': rook.Rook(7 * width, 0 * height, width, height, 'rb'),
    #         'kb1': knight.Knight(1 * width, 0 * height, width, height, 'kb'),
    #         'kb2': knight.Knight(6 * width, 0 * height, width, height, 'kb'),
    #         'bb1': bishop.Bishop(2 * width, 0 * height, width, height, 'bb'),
    #         'bb2': bishop.Bishop(5 * width, 0 * height, width, height, 'bb'),
    #         'Qb': queen.Queen(3 * width, 0 * height, width, height, 'Qb'),
    #         'Kb': king.King(4 * width, 0 * height, width, height, 'Kb'),
    #     }
    #     whiteArmy = {
    #         'pw1': pawn.Pawn(0 * width, 6 * height, width, height, 'pw'),
    #         'pw2': pawn.Pawn(1 * width, 6 * height, width, height, 'pw'),
    #         'pw3': pawn.Pawn(2 * width, 6 * height, width, height, 'pw'),
    #         'pw4': pawn.Pawn(3 * width, 6 * height, width, height, 'pw'),
    #         'pw5': pawn.Pawn(4 * width, 6 * height, width, height, 'pw'),
    #         'pw6': pawn.Pawn(5 * width, 6 * height, width, height, 'pw'),
    #         'pw7': pawn.Pawn(6 * width, 6 * height, width, height, 'pw'),
    #         'pw8': pawn.Pawn(7 * width, 6 * height, width, height, 'pw'),
    #         'rw1': rook.Rook(0 * width, 7 * height, width, height, 'rw'),
    #         'rw2': rook.Rook(7 * width, 7 * height, width, height, 'rw'),
    #         'kw1': knight.Knight(1 * width, 7 * height, width, height, 'kw'),
    #         'kw2': knight.Knight(6 * width, 7 * height, width, height, 'kw'),
    #         'bw1': bishop.Bishop(2 * width, 7 * height, width, height, 'bw'),
    #         'bw2': bishop.Bishop(5 * width, 7 * height, width, height, 'bw'),
    #         'Qw': queen.Queen(3 * width, 7 * height, width, height, 'Qw'),
    #         'Kw': king.King(4 * width, 7 * height, width, height, 'Kw'),
    #     }
    blackArmy = {
        'pb1': pawn.Pawn('pb1', sio, 0 * width, 1 * height, width, height, 'pb'),
        'pb2': pawn.Pawn('pb2', sio, 1 * width, 1 * height, width, height, 'pb'),
        'pb3': pawn.Pawn('pb3', sio, 2 * width, 1 * height, width, height, 'pb'),
        'pb4': pawn.Pawn('pb4', sio, 3 * width, 1 * height, width, height, 'pb'),
        'pb5': pawn.Pawn('pb5', sio, 4 * width, 1 * height, width, height, 'pb'),
        'pb6': pawn.Pawn('pb6', sio, 5 * width, 1 * height, width, height, 'pb'),
        'pb7': pawn.Pawn('pb7', sio, 6 * width, 1 * height, width, height, 'pb'),
        'pb8': pawn.Pawn('pb8', sio, 7 * width, 1 * height, width, height, 'pb'),
        'rb1': rook.Rook('rb1', sio, 0 * width, 0 * height, width, height, 'rb'),
        'rb2': rook.Rook('rb2', sio, 7 * width, 0 * height, width, height, 'rb'),
        'kb1': knight.Knight('kb1', sio, 1 * width, 0 * height, width, height, 'kb'),
        'kb2': knight.Knight('kb2', sio, 6 * width, 0 * height, width, height, 'kb'),
        'bb1': bishop.Bishop('bb1', sio, 2 * width, 0 * height, width, height, 'bb'),
        'bb2': bishop.Bishop('bb2', sio, 5 * width, 0 * height, width, height, 'bb'),
        'Qb': queen.Queen('Qb', sio, 3 * width, 0 * height, width, height, 'Qb'),
        'Kb': king.King('Kb', sio, 4 * width, 0 * height, width, height, 'Kb'),
    }
    whiteArmy = {
        'pw1': pawn.Pawn('pw1', sio, 0 * width, 6 * height, width, height, 'pw'),
        'pw2': pawn.Pawn('pw2', sio, 1 * width, 6 * height, width, height, 'pw'),
        'pw3': pawn.Pawn('pw3', sio, 2 * width, 6 * height, width, height, 'pw'),
        'pw4': pawn.Pawn('pw4', sio, 3 * width, 6 * height, width, height, 'pw'),
        'pw5': pawn.Pawn('pw5', sio, 4 * width, 6 * height, width, height, 'pw'),
        'pw6': pawn.Pawn('pw6', sio, 5 * width, 6 * height, width, height, 'pw'),
        'pw7': pawn.Pawn('pw7', sio, 6 * width, 6 * height, width, height, 'pw'),
        'pw8': pawn.Pawn('pw8', sio, 7 * width, 6 * height, width, height, 'pw'),
        'rw1': rook.Rook('rw1', sio, 0 * width, 7 * height, width, height, 'rw'),
        'rw2': rook.Rook('rw2', sio, 7 * width, 7 * height, width, height, 'rw'),
        'kw1': knight.Knight('kw1', sio, 1 * width, 7 * height, width, height, 'kw'),
        'kw2': knight.Knight('kw2', sio, 6 * width, 7 * height, width, height, 'kw'),
        'bw1': bishop.Bishop('bw1', sio, 2 * width, 7 * height, width, height, 'bw'),
        'bw2': bishop.Bishop('bw2', sio, 5 * width, 7 * height, width, height, 'bw'),
        'Qw': queen.Queen('Qw', sio, 3 * width, 7 * height, width, height, 'Qw'),
        'Kw': king.King('Kw', sio, 4 * width, 7 * height, width, height, 'Kw'),
    }

    return whiteArmy, blackArmy


def loadAssets(dirName: str, imageWidth: int, imageHeight: int):
    assets = {
        'pw': pygame.transform.scale(pygame.image.load(f"{dirName}/pawn-w.png"), (imageWidth, imageHeight)),
        'pb': pygame.transform.scale(pygame.image.load(f"{dirName}/pawn-b.png"), (imageWidth, imageHeight)),
        'rw': pygame.transform.scale(pygame.image.load(f"{dirName}/rook-w.png"), (imageWidth, imageHeight)),
        'rb': pygame.transform.scale(pygame.image.load(f"{dirName}/rook-b.png"), (imageWidth, imageHeight)),
        'kw': pygame.transform.scale(pygame.image.load(f"{dirName}/knight-w.png"), (imageWidth, imageHeight)),
        'kb': pygame.transform.scale(pygame.image.load(f"{dirName}/knight-b.png"), (imageWidth, imageHeight)),
        'bw': pygame.transform.scale(pygame.image.load(f"{dirName}/bishop-w.png"), (imageWidth, imageHeight)),
        'bb': pygame.transform.scale(pygame.image.load(f"{dirName}/bishop-b.png"), (imageWidth, imageHeight)),
        'Kw': pygame.transform.scale(pygame.image.load(f"{dirName}/king-w.png"), (imageWidth, imageHeight)),
        'Kb': pygame.transform.scale(pygame.image.load(f"{dirName}/king-b.png"), (imageWidth, imageHeight)),
        'Qw': pygame.transform.scale(pygame.image.load(f"{dirName}/queen-w.png"), (imageWidth, imageHeight)),
        'Qb': pygame.transform.scale(pygame.image.load(f"{dirName}/queen-b.png"), (imageWidth, imageHeight)),
    }
    return assets
