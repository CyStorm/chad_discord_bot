import chess

class ChessGame():
    def __init__(self, white, black, *args):
        self.board = chess.Board()
        print(type(white))
        print(type(black))
        self.players = {
            "white": white,
            "black": black,
        }
        self.turn = "white"
        self.ranked = False
        self.blind = False
        self.allow_illegal = False
        self.is_ended = False

        for arg in args:
            if (arg == "ranked"):
                self.ranked = True
            elif (arg == "blind"):
                self.blind = True
            elif (arg == "allow_illegal"):
                self.allow_illegal = True

    def make_move(self, move):
        try:
            self.board.push_san(move)
            self.turn = "white" if self.board.turn == chess.WHITE else "black"
            return True
        except ValueError:
            return False

    def check_result(self):
        '''Check if game is eneded, should call after each successful move.
        '''
        return


def debug():
    print(chess.WHITE)
    print(not chess.WHITE)

if (__name__ == "__main__"):
    debug()
