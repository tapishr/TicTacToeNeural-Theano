import TicTacToe.player as Player
import TicTacToe.game as Game
import timeit
import sys


TRAINING_SET = 10000

def experiment1_testing():
	
	for n_nodes in range(1,21):
		print 'Testing for n_nodes = ',n_nodes
		file_name  = 'player' + str(Game.PLAYER1_MARK) + 'QlearnerModelWithNodes' + str(n_nodes)
		player1 = Player.TicTacToePlayer(Game.PLAYER1_MARK, randomness = 0, file_name = file_name)
		player2 = Player.TicTacToePlayer(Game.PLAYER2_MARK, human_player = True)
		response = 'y'
		while response == 'y':
			game = Game.TicTacToeGame(player1, player2, 3, print_every_move_flag = True)
			print 'Winner = Player ',game.play_game()
			response = raw_input('\nContinue?[y/n]')

		file_name  = 'player' + str(Game.PLAYER2_MARK) + 'QlearnerModelWithNodes' + str(n_nodes)
		player2 = Player.TicTacToePlayer(Game.PLAYER2_MARK, randomness = 0, file_name = file_name)
		player1 = Player.TicTacToePlayer(Game.PLAYER1_MARK, human_player = True)
		response = 'y'
		while response == 'y':
			game = Game.TicTacToeGame(player1, player2, 3, print_every_move_flag = True)
			print 'Winner = Player ',game.play_game()
			response = raw_input('\nContinue?[y/n]')

def experiment1_training():

	for n_nodes in range(1,21):

		start_time = timeit.default_timer()
		player1 = Player.TicTacToePlayer(Game.PLAYER1_MARK, randomness = 1, n_nodes = n_nodes, n_in = 9)
		player2 = Player.TicTacToePlayer(Game.PLAYER2_MARK, randomness = 1, n_nodes = n_nodes, n_in = 9)
		print "Random Training for nodes = ", n_nodes

		for i in range(TRAINING_SET):

			sys.stdout.write ('\rGame %i/%i' %(i, TRAINING_SET))
			sys.stdout.flush()
			game = Game.TicTacToeGame(player1, player2, 3)
			game.play_game()

		end_time = timeit.default_timer()
		
		player1.store_progress()
		player2.store_progress()

		print 'Total Time = ', (end_time-start_time)/60, ' for n_nodes = ', n_nodes

if __name__ == '__main__':
	experiment1_testing()