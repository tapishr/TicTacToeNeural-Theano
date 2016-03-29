import numpy as np
import random
#from learner import DeepLearner
from learner3X3 import QScoreLearner

#need to add global vars

class TicTacToePlayer(object):

	def __init__(self, player_mark, randomness = 0.5, n_nodes = 20, load_params_flag = False, human_player = False, strategy = None):
		self.player_mark = player_mark
		self.randomness = randomness
		self.gamesWon = 0
		self.gamesPlayed = 0
		self.human_player = human_player
		self.strategy = strategy

		if load_params_flag:
			self.load_progress()
		else:
			self.playerNetwork = QScoreLearner(self.player_mark, n_nodes, 3*3)
		

	def make_a_move (self, board):
		new_board = np.copy(board)
		move = ()
		if self.human_player:
			response = input("Enter Board Cell Number ")
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
		
		index1d = self.playerNetwork.predict(board)
		return (index1d/board.shape[1], index1d%board.shape[1])


	def pass_rewards(self, board, reward):
		return self.playerNetwork.give_reward(reward, board)
		#print 'Player',self.player_mark, ' cost = ',self.playerNetwork.assign_reward(reward, board)

	def store_progress(self):
		self.playerNetwork.save_model()




