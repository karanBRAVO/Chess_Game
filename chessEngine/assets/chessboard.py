import pygame


def drawChessBoard(window, color1: str, color2: str, whiteBoxPosList: list, blackBoxPosList: list):
    for whiteBoxPos in whiteBoxPosList:
        pygame.draw.rect(window, color1, whiteBoxPos)

    for blackBoxPos in blackBoxPosList:
        pygame.draw.rect(window, color2, blackBoxPos)


def getBoxes_posList(boxes: dict):
    whiteBoxesPos = []
    blackBoxesPos = []

    flag = True

    for y in range(8):
        if y % 2 == 0:
            start = 0
            end = 8
            step = 1
        else:
            start = 7
            end = -1
            step = -1
        for x in range(start, end, step):
            if flag:
                whiteBoxesPos.append(boxes[f"box_{x}_{y}"])
                flag = False
            else:
                blackBoxesPos.append(boxes[f"box_{x}_{y}"])
                flag = True

    return whiteBoxesPos, blackBoxesPos


def getBoxes_rect(width: int, height: int):
    boxes = {}

    for y in range(8):
        for x in range(8):
            boxes[f"box_{x}_{y}"] = pygame.Rect(
                x * width, y * height, width, height)

    return boxes
