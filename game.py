from player import TicTacToePlayer as TTTPlayer
from judge import TicTacToeJudge as TTTJudge
import numpy as np
import timeit
import sys

REWARD_WIN = 1
REWARD_LOSE = 0
REWARD_TIE = 0

TIE_MARK = -2
PLAYER1_MARK = 1
PLAYER2_MARK = -1
NO_WINNER_MARK = 0

BOARD_DIMENSION = 3#10
GAME_MARKS = 3#5

TRAINING_SET = 10000

class TicTacToeGame(object):

	def __init__(self, player1, player2 ,print_every_move_flag=False):
		self.players = [player1 , player2]
		self.board = np.zeros((BOARD_DIMENSION, BOARD_DIMENSION),np.int8)
		self.judge = TTTJudge(GAME_MARKS)
		self.print_every_move_flag = print_every_move_flag

	def play_game(self):
		game_over = False
		winner = 0
		count = 0
		while not game_over :
			count += 1
			for player in self.players :
				new_board = player.make_a_move(self.board)
				if self.judge.check_move(new_board, self.board, player.player_mark):
					self.board = new_board
					if self.print_every_move_flag:
						print '\nPlayer ', player.player_mark
						print self.board
				else :
					raise Exception ('Wrong Move')
				winner = self.judge.get_result(self.board)
				if winner != NO_WINNER_MARK :
					game_over = True
					break
		self.reward_winner(winner)
		return winner
	
	def reward_winner(self, winner):
		
		self.players[0].gamesPlayed += 1
		self.players[1].gamesPlayed += 1
		if winner == TIE_MARK:
			self.players[0].pass_rewards(self.board, REWARD_TIE)
			self.players[1].pass_rewards(self.board, REWARD_TIE)
		else:
			
			if winner == self.players[1].player_mark:
				winning_player = self.players[1]
				losing_player = self.players[0]
			else :
				winning_player = self.players[0]
				losing_player = self.players[1]
			winning_player.pass_rewards(self.board, REWARD_WIN)
			losing_player.pass_rewards(self.board, REWARD_LOSE)
			winning_player.gamesWon += 1


if __name__ == '__main__':

	start_time = timeit.default_timer()

	for n_nodes in range(2,20):

		player1 = TTTPlayer(PLAYER1_MARK, 1, n_nodes)
		player2 = TTTPlayer(PLAYER2_MARK, 1, n_nodes)
		print "Random Training for nodes = ", n_nodes

		for i in range(TRAINING_SET):

			sys.stdout.write ('\rGame %i/%i' %(i, TRAINING_SET))
			sys.stdout.flush()
			game = TicTacToeGame(player1, player2)
			winner = game.play_game()

		end_time = timeit.default_timer()
		
		player1.store_progress()
		player2.store_progress()

		print 'Total Time = ', (end_time-start_time)/60, ' for n_nodes = ', n_nodes

