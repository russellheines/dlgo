import time

from dlgo.agent.naive import RandomBot
from dlgo import goboard
from dlgo.gotypes import Player
from dlgo.utils import print_board, print_move


def main():
    board_size = 9
    game = goboard.GameState.new_game(board_size)
    bots = {
        Player.black: RandomBot(),
        Player.white: RandomBot(),
    }
    while not game.is_over():
        time.sleep(0.5)

        bot_move = bots[game.next_player].select_move(game)
        print(chr(27) + "[2J")
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)
        print_board(game.board)


if __name__ == '__main__':
    main()
