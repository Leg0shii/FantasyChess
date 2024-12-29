from util import parse_notation
from engine import ChessEngine
from color import ColorType
from board import ChessBoard


class ChessGame:

    def __init__(self, player_white, player_black) -> None:
        self.chess_board = ChessBoard()
        self.engine = ChessEngine(self.chess_board)
        self.turn = ColorType.WHITE
        self.players = [player_white, player_black]
        self.current_player = player_white
        self.history = []
        self.move_count = 0
    

    def step(self) -> None:
        self.show_game()

        self.move_count += 1
        self.current_player = [p for p in self.players if p.color == self.turn][0]

        user_input = None
        first_input = True
        while not self.is_move_allowed(user_input):
            message = f'{self.move_count}. Move: Its now your turn {self.current_player.name}! Type in your next move: \n'
            if not first_input:
                message = f'{user_input} is not a valid notation. Please use a valid notation. For example: a5a6 \n'

            raw_input = input(message)
            user_input = parse_notation(raw_input)
            first_input = False

        self.apply_move(user_input)
        self.history.append(raw_input)
        self.switch_state()


    def switch_state(self) -> None:
        if self.turn == ColorType.WHITE:
            self.turn = ColorType.BLACK
        else:
            self.turn = ColorType.WHITE

    
    def is_move_allowed(self, user_input: str) -> bool:
        return self.engine.is_move_allowed(user_input)


    def has_won(self) -> None:
        return self.engine.has_won()
    

    def apply_move(self, from_to: list) -> None:
        print(from_to)
        from_pos, to_pos = from_to[0], from_to[1]
        field = self.chess_board.board

        temp = field[from_pos[1]][from_pos[0]]
        field[from_pos[1]][from_pos[0]] = field[to_pos[1]][to_pos[0]]
        field[to_pos[1]][to_pos[0]] = temp


    def show_game(self) -> None:
        print(chr(27) + "[2J")
        print(f'Previous moves: {str(self.history)}')
        print(str(self.chess_board))