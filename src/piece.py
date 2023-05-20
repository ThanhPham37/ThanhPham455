import os


class Piece:

    def __init__(self, name, color, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        color = 'b' if self.color == 'black' else 'w'
        if self.name == "knight":
            piece = 'N'
        elif self.name == "pawn":
            piece = 'p'
        else:
            piece = self.name[:1].upper()
            # print(piece)
        self.texture = os.path.join(
            f'../assets/images/imgs-{size}px/{color}{piece}.png')

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []


class Pawn(Piece):

    def __init__(self, color):
        super().__init__('pawn', color)


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color)


class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color)


class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color)


class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color)


class King(Piece):

    def __init__(self, color):
        super().__init__('king', color)
