import pygame
from assets.army.collision import detectCollision
from assets import logger
from assets.army.mappings import piece_mapping
from assets.socket import SocketClient


class Queen:
    def __init__(self, name: str, sio: SocketClient, x: int, y: int, width: int, height: int, face: str = 'Qb' or 'Qw') -> None:
        self.name = name
        self.socket = sio
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.face = face
        self.pos = pygame.Rect(self.x, self.y, width, height)
        self.state = False
        self.movements = [(1, 1), (1, -1), (-1, 1), (-1, -1),
                          (1, 0), (-1, 0), (0, 1), (0, -1)]

    def detectClick(self, window, mouseX: float, mouseY: float, boxes: dict, whiteArmy: dict, blackArmy: dict, colors: dict):
        if self.pos.collidepoint(mouseX, mouseY):
            self.canMove(window, colors, boxes, whiteArmy, blackArmy)

    def canMove(self, window, colors: dict, boxes: dict, whiteArmy: dict, blackArmy: dict):
        def addMarks_helper(same_army: dict, opponent_army: dict):
            for x_direction, y_direction in self.movements:
                if x_direction != 0 and y_direction != 0:
                    x_stop = 8 if x_direction == 1 else -1
                    y_stop = 8 if y_direction == 1 else -1
                    coordinates = list(zip(range(self.x // self.width, x_stop, x_direction),
                                       range(self.y // self.height, y_stop, y_direction)))
                elif x_direction == 0:
                    stop = 8 if y_direction == 1 else -1
                    coordinates = [[self.x // self.width, y]
                                   for y in range(self.y // self.height, stop, y_direction)]
                elif y_direction == 0:
                    stop = 8 if x_direction == 1 else -1
                    coordinates = [[x, self.y // self.height]
                                   for x in range(self.x // self.width, stop, x_direction)]

                for _x, _y in coordinates:
                    if x_direction != 0 and y_direction != 0:
                        if _x == self.x // self.width or _y == self.y // self.height:
                            continue
                    elif x_direction == 0:
                        if _y == self.y // self.height:
                            continue
                    elif y_direction == 0:
                        if _x == self.x // self.width:
                            continue

                    pos = (_x, _y)
                    fromSameArmy = detectCollision(boxes, same_army, pos, True)
                    if fromSameArmy:
                        self.drawRect(
                            window, colors['blue'], boxes[f"box_{pos[0]}_{pos[1]}"], 100)
                        self.state = True
                    else:
                        break
                    fromOpponentArmy = detectCollision(
                        boxes, opponent_army, pos, False)
                    if fromOpponentArmy:
                        self.drawRect(
                            window, colors['red'], boxes[f"box_{pos[0]}_{pos[1]}"], 100)
                        self.state = True
                        break

        if self.face == 'Qb':
            self.resetArmy(blackArmy)
            addMarks_helper(blackArmy, whiteArmy)

        elif self.face == 'Qw':
            self.resetArmy(whiteArmy)
            addMarks_helper(whiteArmy, blackArmy)

    def send_pos(self):
        self.socket.send_message(
            "--client:piece-move", {'name': self.name, 'pos': [self.x, self.y, self.width, self.height]})

    def Move(self, boxes: dict, mouseX: float, mouseY: float, whiteArmy: dict, blackArmy: dict):
        if self.state:
            def move(same_army: dict, opponent_army: dict):
                isPositionUpdated = False

                for x_direction, y_direction in self.movements:
                    if x_direction != 0 and y_direction != 0:
                        x_stop = 8 if x_direction == 1 else -1
                        y_stop = 8 if y_direction == 1 else -1
                        coordinates = list(zip(range(self.x // self.width, x_stop, x_direction), range(
                            self.y // self.height, y_stop, y_direction)))
                    elif x_direction == 0:
                        stop = 8 if y_direction == 1 else -1
                        coordinates = [[self.x // self.width, y]
                                       for y in range(self.y // self.height, stop, y_direction)]
                    elif y_direction == 0:
                        stop = 8 if x_direction == 1 else -1
                        coordinates = [[x, self.y // self.height]
                                       for x in range(self.x // self.width, stop, x_direction)]

                    for _x, _y in coordinates:
                        if x_direction != 0 and y_direction != 0:
                            if _x == self.x // self.width or _y == self.y // self.height:
                                continue
                        elif x_direction == 0:
                            if _y == self.y // self.height:
                                continue
                        elif y_direction == 0:
                            if _x == self.x // self.width:
                                continue

                        pos = (_x, _y)
                        fromSameArmy = detectCollision(
                            boxes, same_army, pos, True)
                        if fromSameArmy:
                            if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                                isPositionUpdated = self.updatePosition(
                                    pos[0] * self.width, pos[1] * self.height)
                                self.resetState()
                        else:
                            break
                        fromOpponentArmy = detectCollision(
                            boxes, opponent_army, pos, False)
                        if fromOpponentArmy:
                            if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                                opponentPlayer = self.getOpponentPlayer(
                                    boxes, opponent_army, pos)
                                opponent_army.pop(opponentPlayer)
                                self.resetState()
                            break

                        if isPositionUpdated:
                            return True

                return False

            if self.face == 'Qb':
                return move(blackArmy, whiteArmy)

            elif self.face == 'Qw':
                return move(whiteArmy, blackArmy)

        return False

    def getOpponentPlayer(self, boxes: dict, army: dict, pos: tuple):
        for piece in army:
            if boxes[f"box_{pos[0]}_{pos[1]}"].colliderect(army[piece].pos):
                logger.print_success(f"Removed {piece_mapping[piece[0]]}")
                return piece
        return ''

    def updatePosition(self, x: int, y: int):
        logger.print_error(
            f"[#] Moved Queen from [{self.x // self.width + 1}, {self.y // self.height + 1}] -> [{x // self.width + 1}, {y // self.height + 1}]")
        self.x = x
        self.y = y
        self.pos.x = self.x
        self.pos.y = self.y
        self.send_pos()
        return True

    def resetArmy(self, army: dict):
        for piece in army:
            if piece != self:
                army[piece].resetState()

    def resetState(self):
        self.state = False

    def drawRect(self, window, color, pos: pygame.Rect, b_rad: int = 100):
        pygame.draw.rect(window, color, pos, border_radius=b_rad)
