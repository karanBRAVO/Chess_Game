import pygame
from assets.army.collision import detectCollision
from assets.army import queen, bishop, knight, rook
from assets import logger
from assets.army.mappings import piece_mapping
from assets.socket import SocketClient


class Pawn():
    def __init__(self, name: str, sio: SocketClient, x: int, y: int, width: int, height: int, face: str = 'pb' or 'pw') -> None:
        self.name = name
        self.socket = sio
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.face = face
        self.pos = pygame.Rect(self.x, self.y, width, height)
        self.state = False
        self.movements = 1 if self.face == 'pb' else -1
        self.upgrades = {'Queen': 1, 'bishop': 2, 'knight': 3, 'rook': 4}

    def detectClick(self, window, mouseX: float, mouseY: float, boxes: dict, whiteArmy: dict, blackArmy: dict, colors: dict):
        if self.pos.collidepoint(mouseX, mouseY):
            self.canMove(window, colors, boxes, whiteArmy, blackArmy)

    def canMove(self, window, colors, boxes: dict, whiteArmy: dict, blackArmy: dict):
        def addMarks_helper(same_army: dict, opponent_army: dict, base: int):
            pos = (self.x // self.width, self.y //
                   self.height + 1 * self.movements)
            flag = detectCollision(boxes, opponent_army, pos, True) and detectCollision(
                boxes, same_army, pos, True)
            if flag:
                self.drawRect(window, colors['blue'],
                              boxes[f"box_{pos[0]}_{pos[1]}"], 100)
                self.state = True

            if self.y == base * self.height:
                pos = (self.x // self.width, self.y //
                       self.height + 2 * self.movements)
                flag = detectCollision(boxes, opponent_army, pos, True) and detectCollision(
                    boxes, same_army, pos, True)
                if flag:
                    self.drawRect(
                        window, colors['blue'], boxes[f"box_{pos[0]}_{pos[1]}"], 100)
                    self.state = True

            pos = (self.x // self.width - 1, self.y //
                   self.height + 1 * self.movements)
            flag = detectCollision(boxes, opponent_army, pos, False)
            if flag:
                self.drawRect(window, colors['red'],
                              boxes[f"box_{pos[0]}_{pos[1]}"], 100)
                self.state = True

            pos = (self.x // self.width + 1, self.y //
                   self.height + 1 * self.movements)
            flag = detectCollision(boxes, opponent_army, pos, False)
            if flag:
                self.drawRect(window, colors['red'],
                              boxes[f"box_{pos[0]}_{pos[1]}"], 100)
                self.state = True

        if self.face == 'pb':
            self.resetArmy(blackArmy)
            addMarks_helper(blackArmy, whiteArmy, 1)

        elif self.face == 'pw':
            self.resetArmy(whiteArmy)
            addMarks_helper(whiteArmy, blackArmy, 6)

    def send_pos(self):
        self.socket.send_message(
            "--client:piece-move", {'name': self.name, 'pos': [self.x, self.y, self.width, self.height]})

    def send_remove_player(self, name: str):
        self.socket.send_message(
            "--client:piece-remove", {'name': name})

    def Move(self, boxes: dict, mouseX: float, mouseY: float, whiteArmy: dict, blackArmy: dict):
        if self.state:
            def move(same_army: dict, opponent_army: dict, base: int):
                pos = (self.x // self.width, self.y //
                       self.height + 1 * self.movements)
                flag = detectCollision(boxes, opponent_army, pos, True) and detectCollision(
                    boxes, same_army, pos, True)
                if flag:
                    if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                        self.updatePosition(
                            pos[0] * self.width, pos[1] * self.height)
                        self.upgradePawn(boxes, same_army)
                        self.resetState()
                        return True

                if self.y == base * self.height:
                    pos = (self.x // self.width, self.y //
                           self.height + 2 * self.movements)
                    flag = detectCollision(boxes, opponent_army, pos, True) and detectCollision(
                        boxes, same_army, pos, True)
                    if flag:
                        if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                            self.updatePosition(
                                pos[0] * self.width, pos[1] * self.height)
                            self.resetState()
                            return True

                pos = (self.x // self.width - 1, self.y //
                       self.height + 1 * self.movements)
                flag = detectCollision(boxes, opponent_army, pos, False)
                if flag:
                    if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                        self.updatePosition(
                            pos[0] * self.width, pos[1] * self.height)
                        opponentPlayer = self.getOpponentPlayer(
                            boxes, opponent_army, pos)
                        opponent_army.pop(opponentPlayer)
                        self.send_remove_player(opponentPlayer)
                        self.upgradePawn(boxes, same_army)
                        self.resetState()
                        return True

                pos = (self.x // self.width + 1, self.y //
                       self.height + 1 * self.movements)
                flag = detectCollision(boxes, opponent_army, pos, False)
                if flag:
                    if boxes[f"box_{pos[0]}_{pos[1]}"].collidepoint(mouseX, mouseY):
                        self.updatePosition(
                            pos[0] * self.width, pos[1] * self.height)
                        opponentPlayer = self.getOpponentPlayer(
                            boxes, opponent_army, pos)
                        opponent_army.pop(opponentPlayer)
                        self.send_remove_player(opponentPlayer)
                        self.upgradePawn(boxes, same_army)
                        self.resetState()
                        return True

                return False

            if self.face == 'pb':
                return move(blackArmy, whiteArmy, 1)

            elif self.face == 'pw':
                return move(whiteArmy, blackArmy, 6)

        return False

    def upgradePawn(self, boxes: dict, same_army: dict):
        def getUpgradePiece():
            logger.print_info(f"Upgrade options: {self.upgrades}")
            flag = False
            while not flag:
                new_piece = int(input("[?] upgrade your pawn to: "))
                for upgradeOption in self.upgrades:
                    if new_piece == self.upgrades[upgradeOption]:
                        flag = True
                        return new_piece, upgradeOption
                if not flag:
                    logger.print_error("[!] Invalid upgrade")

        def getNewPieceName(start: str):
            count = 1
            new_name = f"{start}{self.face[1]}{count}"
            while new_name in same_army:
                count += 1
                new_name = f"{start}{self.face[1]}{count}"
            return new_name

        def upgrade(base: int):
            if self.y // self.height == base:
                new_piece, upgradeTo = getUpgradePiece()
                new_name = getNewPieceName(upgradeTo[0])

                # remove the pawn
                pos = (self.x // self.width, self.y // self.height)
                remove_piece_name = ""
                for piece in same_army:
                    if boxes[f"box_{pos[0]}_{pos[1]}"].colliderect(same_army[piece].pos):
                        same_army.pop(piece)
                        remove_piece_name = piece
                        break

                # add the new piece
                face = ""
                if new_piece == 1:
                    face = f'Q{self.face[1]}'
                    same_army[new_name] = queen.Queen(
                        new_name, self.socket, self.x, self.y, self.width, self.height, f'Q{self.face[1]}')
                elif new_piece == 2:
                    face = f'b{self.face[1]}'
                    same_army[new_name] = bishop.Bishop(
                        new_name, self.socket, self.x, self.y, self.width, self.height, f'b{self.face[1]}')
                elif new_piece == 3:
                    face = f'k{self.face[1]}'
                    same_army[new_name] = knight.Knight(
                        new_name, self.socket, self.x, self.y, self.width, self.height, f'k{self.face[1]}')
                elif new_piece == 4:
                    face = f'r{self.face[1]}'
                    same_army[new_name] = rook.Rook(
                        new_name, self.socket, self.x, self.y, self.width, self.height, f'r{self.face[1]}')

                logger.print_success("[+] pawn upgraded to " + upgradeTo)
                self.socket.send_message("--client:pawn-upgrade", {
                                         'removePieceName': remove_piece_name, 'newPieceName': new_name, 'pos': [self.x, self.y, self.width, self.height], 'face': face, 'newPiece': new_piece})

        if self.face == 'pb':
            upgrade(7)

        elif self.face == 'pw':
            upgrade(0)

    def getOpponentPlayer(self, boxes: dict, army: dict, pos: tuple):
        for piece in army:
            if boxes[f"box_{pos[0]}_{pos[1]}"].colliderect(army[piece].pos):
                logger.print_success(f"Removed {piece_mapping[piece[0]]}")
                return piece
        return ''

    def updatePosition(self, x: int, y: int):
        logger.print_error(
            f"[#] Moved Pawn from [{self.x // self.width + 1}, {self.y // self.height + 1}] -> [{x // self.width + 1}, {y // self.height + 1}]")
        self.x = x
        self.y = y
        self.pos.x = x
        self.pos.y = y
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
