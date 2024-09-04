from dlgo.mcts.mcts import MCTSAgent
from dlgo import goboard_fast as goboard
from dlgo import gotypes
from dlgo.utils import print_board, print_move, point_from_coords


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bot = MCTSAgent(500, temperature=1.4)

    print(chr(27) + "[2J")
    print_board(game.board)

    while not game.is_over():
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')
            point = point_from_coords(human_move.strip())
            move = goboard.Move.play(point)
        else:
            move = bot.select_move(game)

        print(chr(27) + "[2J")
        print_move(game.next_player, move)
        game = game.apply_move(move)
        print_board(game.board)


if __name__ == '__main__':
    main()
