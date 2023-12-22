import pygame
import sys
from assets.army import pawn, rook, knight, bishop, queen, king
from assets import logger


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


def piecesMovements(window, colors: dict, boxes: dict, whiteArmy: dict, blackArmy: dict, mouseX: float, mouseY: float, turn: str):
    if turn == 'b':
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

    elif turn == 'w':
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


def drawPieces(window, assets: dict, whiteArmy: dict, blackArmy: dict):
    for whitePiece in whiteArmy:
        window.blit(assets[whiteArmy[whitePiece].face],
                    whiteArmy[whitePiece].pos)
    for blackPiece in blackArmy:
        window.blit(assets[blackArmy[blackPiece].face],
                    blackArmy[blackPiece].pos)


def getArmy(width, height):
    blackArmy = {
        'pb1': pawn.Pawn(0 * width, 1 * height, width, height, 'pb'),
        'pb2': pawn.Pawn(1 * width, 1 * height, width, height, 'pb'),
        'pb3': pawn.Pawn(2 * width, 1 * height, width, height, 'pb'),
        'pb4': pawn.Pawn(3 * width, 1 * height, width, height, 'pb'),
        'pb5': pawn.Pawn(4 * width, 1 * height, width, height, 'pb'),
        'pb6': pawn.Pawn(5 * width, 1 * height, width, height, 'pb'),
        'pb7': pawn.Pawn(6 * width, 1 * height, width, height, 'pb'),
        'pb8': pawn.Pawn(7 * width, 1 * height, width, height, 'pb'),
        'rb1': rook.Rook(0 * width, 0 * height, width, height, 'rb'),
        'rb2': rook.Rook(7 * width, 0 * height, width, height, 'rb'),
        'kb1': knight.Knight(1 * width, 0 * height, width, height, 'kb'),
        'kb2': knight.Knight(6 * width, 0 * height, width, height, 'kb'),
        'bb1': bishop.Bishop(2 * width, 0 * height, width, height, 'bb'),
        'bb2': bishop.Bishop(5 * width, 0 * height, width, height, 'bb'),
        'Qb': queen.Queen(3 * width, 0 * height, width, height, 'Qb'),
        'Kb': king.King(4 * width, 0 * height, width, height, 'Kb'),
    }
    whiteArmy = {
        'pw1': pawn.Pawn(0 * width, 6 * height, width, height, 'pw'),
        'pw2': pawn.Pawn(1 * width, 6 * height, width, height, 'pw'),
        'pw3': pawn.Pawn(2 * width, 6 * height, width, height, 'pw'),
        'pw4': pawn.Pawn(3 * width, 6 * height, width, height, 'pw'),
        'pw5': pawn.Pawn(4 * width, 6 * height, width, height, 'pw'),
        'pw6': pawn.Pawn(5 * width, 6 * height, width, height, 'pw'),
        'pw7': pawn.Pawn(6 * width, 6 * height, width, height, 'pw'),
        'pw8': pawn.Pawn(7 * width, 6 * height, width, height, 'pw'),
        'rw1': rook.Rook(0 * width, 7 * height, width, height, 'rw'),
        'rw2': rook.Rook(7 * width, 7 * height, width, height, 'rw'),
        'kw1': knight.Knight(1 * width, 7 * height, width, height, 'kw'),
        'kw2': knight.Knight(6 * width, 7 * height, width, height, 'kw'),
        'bw1': bishop.Bishop(2 * width, 7 * height, width, height, 'bw'),
        'bw2': bishop.Bishop(5 * width, 7 * height, width, height, 'bw'),
        'Qw': queen.Queen(3 * width, 7 * height, width, height, 'Qw'),
        'Kw': king.King(4 * width, 7 * height, width, height, 'Kw'),
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
