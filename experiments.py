import TicTacToe.player as Player
import TicTacToe.game as Game
import timeit
import sys


TRAINING_SET = 10000

if __name__ == '__main__':


	for n_nodes in range(1,20):

		start_time = timeit.default_timer()
		player1 = Player.TicTacToePlayer(Game.PLAYER1_MARK, 1, n_nodes)
		player2 = Player.TicTacToePlayer(Game.PLAYER2_MARK, 1, n_nodes)
		print "Random Training for nodes = ", n_nodes

		for i in range(TRAINING_SET):

			sys.stdout.write ('\rGame %i/%i' %(i, TRAINING_SET))
			sys.stdout.flush()
			game = Game.TicTacToeGame(player1, player2, 3)

		end_time = timeit.default_timer()
		
		player1.store_progress()
		player2.store_progress()

		print 'Total Time = ', (end_time-start_time)/60, ' for n_nodes = ', n_nodes