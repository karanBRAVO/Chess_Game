import pygame
from assets.army.collision import detectCollision
from assets import logger
from assets.army.mappings import piece_mapping


class Knight():
    def __init__(self, x: int, y: int, width: int, height: int, face: str = 'kb' or 'kb') -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.face = face
        self.pos = pygame.Rect(self.x, self.y, width, height)
        self.state = False
        self.positions = [[2, -1], [2, 1], [-2, -1],
                          [-2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]

    def detectClick(self, window, mouseX: float, mouseY: float, boxes: dict, whiteArmy: dict, blackArmy: dict, colors: dict):
        if self.pos.collidepoint(mouseX, mouseY):
            self.canMove(window, colors, boxes, whiteArmy, blackArmy)

    def canMove(self, window, colors: dict, boxes: dict, whiteArmy: dict, blackArmy: dict):
        def addMarks_helper(pos: tuple, same_army: dict, opponent_army: dict):
            fromSameArmy = detectCollision(boxes, same_army, pos, True)
            if fromSameArmy:
                self.drawRect(window, colors['blue'],
                              boxes[f"box_{pos[0]}_{pos[1]}"], 100)
                self.state = True
            fromOpponentArmy = detectCollision(
                boxes, opponent_army, pos, False)
            if fromOpponentArmy:
                self.drawRect(window, colors['red'],
                              boxes[f"box_{pos[0]}_{pos[1]}"], 100)
                self.state = True

        if self.face == 'kb':
            self.resetArmy(blackArmy)
            for x_offset, y_offset in self.positions:
                addMarks_helper((self.x // self.width + x_offset, self.y //
                                self.height + y_offset), blackArmy, whiteArmy)

        elif self.face == 'kw':
            self.resetArmy(whiteArmy)
            for x_offset, y_offset in self.positions:
                addMarks_helper((self.x // self.width + x_offset, self.y //
                                self.height + y_offset), whiteArmy, blackArmy)

    def Move(self, boxes: dict, mouseX: float, mouseY: float, whiteArmy: dict, blackArmy: dict):
        if self.state:
            isPositionUpdated = False

            if self.face == 'kb':
                for x_offset, y_offset in self.positions:
                    pos = (self.x // self.width + x_offset,
                           self.y // self.height + y_offset)
                    fromSameArmy = detectCollision(boxes, blackArmy, pos, True)
                    if fromSameArmy:
                        if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                            isPositionUpdated = self.updatePosition(
                                pos[0] * self.width, pos[1] * self.height)
                            self.resetState()
                    fromOpponentArmy = detectCollision(
                        boxes, whiteArmy, pos, False)
                    if fromOpponentArmy:
                        if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                            opponentPlayer = self.getOpponentPlayer(
                                boxes, whiteArmy, pos)
                            whiteArmy.pop(opponentPlayer)
                            self.resetState()

                    if isPositionUpdated:
                        return True

            elif self.face == 'kw':
                for x_offset, y_offset in self.positions:
                    pos = (self.x // self.width + x_offset,
                           self.y // self.height + y_offset)
                    fromSameArmy = detectCollision(boxes, whiteArmy, pos, True)
                    if fromSameArmy:
                        if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                            isPositionUpdated = self.updatePosition(
                                pos[0] * self.width, pos[1] * self.height)
                            self.resetState()
                    fromOpponentArmy = detectCollision(
                        boxes, blackArmy, pos, False)
                    if fromOpponentArmy:
                        if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                            opponentPlayer = self.getOpponentPlayer(
                                boxes, blackArmy, pos)
                            blackArmy.pop(opponentPlayer)
                            self.resetState()

                    if isPositionUpdated:
                        return True

            return isPositionUpdated

        return False

    def getOpponentPlayer(self, boxes: dict, army: dict, pos: tuple):
        for piece in army:
            if boxes[f"box_{pos[0]}_{pos[1]}"].colliderect(army[piece].pos):
                logger.print_success(f"Removed {piece_mapping[piece[0]]}")
                return piece
        return ''

    def updatePosition(self, x: int, y: int):
        logger.print_error(
            f"[#] Moved Knight from [{self.x // self.width + 1}, {self.y // self.height + 1}] -> [{x // self.width + 1}, {y // self.height + 1}]")
        self.x = x
        self.y = y
        self.pos.x = self.x
        self.pos.y = self.y
        return True
    
    def resetArmy(self, army: dict):
        for piece in army:
            if piece != self:
                army[piece].resetState()

    def resetState(self):
        self.state = False

    def drawRect(self, window, color, pos: pygame.Rect, b_rad: int = 100):
        pygame.draw.rect(window, color, pos, border_radius=b_rad)
