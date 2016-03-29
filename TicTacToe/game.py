from player import TicTacToePlayer as TTTPlayer
from judge import TicTacToeJudge as TTTJudge
import numpy as np


class TicTacToeGame(object):

	PLAYER1_MARK = 1
	PLAYER2_MARK = -1

	REWARD_WIN = 1
	REWARD_LOSE = 0
	REWARD_TIE = 0


	def __init__(self, player1, player2 , type_of_game, print_every_move_flag=False):
		self.players = [player1 , player2]
		if type_of_game == 5:
			board_dimension = (10,10)
		else :
			board_dimension = (type_of_game, type_of_game)
		self.board = np.zeros((board_dimension[0], board_dimension[1]),np.int8)
		self.judge = TTTJudge(type_of_game)
		self.print_every_move_flag = print_every_move_flag

	def play_game(self):
		game_over = False
		winner = 0
		count = 0
		while not game_over :
			count += 1
			for player in self.players :
				new_board = player.make_a_move(self.board)
				if self.judge.is_move_legal(new_board, self.board, player.player_mark):
					self.board = new_board
					if self.print_every_move_flag:
						print '\nPlayer ', player.player_mark
						print self.board
				else :
					winner = TTTJudge.ILLEGAL_MOVE_MARK
					game_over = True
					break
				winner = self.judge.get_result(self.board)
				if winner != TTTJudge.NO_WINNER_MARK :
					game_over = True
					break
		self.reward_winner(winner)
		return winner
	
	def reward_winner(self, winner):
		
		self.players[0].gamesPlayed += 1
		self.players[1].gamesPlayed += 1
		if winner == TTTJudge.TIE_MARK:
			self.players[0].pass_rewards(self.board, REWARD_TIE)
			self.players[1].pass_rewards(self.board, REWARD_TIE)
		elif winner == PLAYER1_MARK or PLAYER2_MARK:
			
			if winner == self.players[1].player_mark:
				winning_player = self.players[1]
				losing_player = self.players[0]
			else :
				winning_player = self.players[0]
				losing_player = self.players[1]
			winning_player.pass_rewards(self.board, REWARD_WIN)
			losing_player.pass_rewards(self.board, REWARD_LOSE)
			winning_player.gamesWon += 1




