def detectCollision(boxes: dict, army: dict, pos: tuple, successFlag: bool):
    if f"box_{pos[0]}_{pos[1]}" in boxes:
        for piece in army:
            if boxes[f"box_{pos[0]}_{pos[1]}"].colliderect(army[piece].pos):
                return not successFlag
    else:
        return False
    return successFlag
