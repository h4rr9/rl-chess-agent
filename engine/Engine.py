"""Chess engine object
"""
import chess
import chess.svg as render


class Chess:

    """Chess wrapper for easy use of chess module

    Attributes:
        board (TYPE): chess board object
        turn (bool): boolean value denoting player turn
    """

    def __init__(self, fen_string=chess.STARTING_FEN):
        """init function

        Args:
            fen_string (TYPE, optional): FEN representation of board state
        """
        self.board = chess.Board(fen_string)
        self.turn = True

    def __str__(self):
        """print function

        Returns:
            TYPE: string representation of the class instance
        """
        return self.board.__str__()

    def __repr__(self):
        """Summary

        Returns:
            TYPE: object representation of the class instance
        """
        return self.board

    def is_legal(self, move):
        """checks validity of move

        Args:
            move (TYPE): san format move

        Returns:
            TYPE: boolean denoting validity of move
        """
        try:
            self.board.parse_san(move)
        except ValueError:
            return False
        else:
            return True

    def move(self, move):
        """function to move pieces

        Args:
            move (TYPE): san format move

        Raises:
            Exception: Description

        No Longer Raises:
            error: illegal move error
        """
        if self.is_legal(move):
            self.board.push_san(move)
            self.turn = not self.turn
        else:
            raise Exception('IllegalMove')

    def get_turn(self):
        """function to find player's turn

        Returns:
            TYPE: string denoting players turn
        """
        return 'White' if self.turn else 'Black'

    def game_over(self):
        return self.board.is_game_over()

    def get_result(self):
        if self.game_over():
            if self.board.is_checkmate():
                return self.get_turn()
            else:
                return 'Draw'

    def reset(self):
        """resets board
        """
        self.board.reset()

    def get_image(self, size=400):
        """function to return svg of game

        Args:
            size (int, optional): size of svg

        Returns:
            TYPE: svg string
        """
        return str(render.board(board=self.board, size=size))
