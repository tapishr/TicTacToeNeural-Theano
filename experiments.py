import TicTacToe.player as Player
import TicTacToe.game as Game
import timeit
import sys

PLAYER1_MARK = 1
PLAYER2_MARK = -1
TRAINING_SET = 10000

if __name__ == '__main__':

	start_time = timeit.default_timer()

	for n_nodes in range(4,20):

		player1 = Player.TicTacToePlayer(PLAYER1_MARK, 1, n_nodes)
		player2 = Player.TicTacToePlayer(PLAYER2_MARK, 1, n_nodes)
		print "Random Training for nodes = ", n_nodes

		for i in range(TRAINING_SET):

			sys.stdout.write ('\rGame %i/%i' %(i, TRAINING_SET))
			sys.stdout.flush()
			game = Game.TicTacToeGame(player1, player2)
			winner = game.play_game()

		end_time = timeit.default_timer()
		
		player1.store_progress()
		player2.store_progress()

		print 'Total Time = ', (end_time-start_time)/60, ' for n_nodes = ', n_nodes