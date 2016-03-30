import numpy as np
import random
#from learner import DeepLearner
from learner3X3 import QScoreLearner

#need to add global vars

class TicTacToePlayer(object):

	def __init__(self, player_mark, randomness = None, n_nodes = None, n_in = None, file_name = None, human_player = False, strategy = None):
		self.player_mark = player_mark
		self.randomness = randomness
		self.gamesWon = 0
		self.gamesPlayed = 0
		self.human_player = human_player
		self.strategy = strategy
		self.playerNetwork = None
		if not randomness is None:
			if file_name == None:
				self.playerNetwork = QScoreLearner(self.player_mark, n_nodes = n_nodes, n_in = n_in)
			else :
				self.playerNetwork = QScoreLearner(self.player_mark, file_name = file_name)
		

	def make_a_move (self, board):
		new_board = np.copy(board)
		move = ()
		if self.human_player:
			response = input("Enter Board Cell Number ") - 1
			shape = board.shape
			move = (response/shape[1], response%shape[1])

		elif self.strategy != None:
			move = self.strategy.pop()


		else:

			p = random.random()
						
			if p < self.randomness:
				move = self.random_move(board)
			else :
				move = self.trained_move(board)

		if board[move] != 0:
			raise Exception('Illegal Move')
		else :
			new_board[move] = self.player_mark

		return new_board


	def random_move (self, board):
		shape = board.shape
		total_cells = shape[0]*shape[1]
		empty_cell = False
		selected_cell = -1
		while not empty_cell:
			selected_cell = random.randint(0,total_cells-1)
			if board[selected_cell/shape[1],selected_cell%shape[1]] == 0:
				empty_cell = True
		
		return (selected_cell/shape[0],selected_cell%shape[1])


	def trained_move (self, board):
		
		index = self.playerNetwork.predict(board)
		return index


	def pass_rewards(self, board, reward):
		if not self.playerNetwork is None:
			return self.playerNetwork.give_reward(reward, board)
		#print 'Player',self.player_mark, ' cost = ',self.playerNetwork.assign_reward(reward, board)

	def store_progress(self):
		self.playerNetwork.save_model()




