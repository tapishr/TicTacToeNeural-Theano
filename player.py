import numpy as np
import random
from learner import DeepLearner

class TicTacToePlayer:

	def __init__(self, player_mark, randomness = 0.5, load_params_flag = False, human_player = False, strategy = None):
		self.player_mark = player_mark
		self.randomness = randomness
		self.gamesWon = 0
		self.gamesPlayed = 0
		self.human_player = human_player
		self.strategy = strategy

		if load_params_flag:
			self.load_progress()
		else:
			self.playerNetwork = DeepLearner()
		

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
		
		return (selected_cell/shape[1],selected_cell%shape[1])


	def trained_move (self, board):
		new_board = np.copy(board)
		q_values = []
		for index, x in np.ndenumerate(board):
			if x!= 0:
				continue
			new_board[index] = self.player_mark
			q_values = q_values + [(self.playerNetwork.get_q_value(new_board), index)]
			new_board[index] = 0

		max_q_value, required_index = max(q_values)
		# print 'q_values = ', q_values
		print 'max_q_value = ', max_q_value
		print 'required_index', required_index
		return required_index


	def pass_rewards(self, board, reward):
		self.playerNetwork.assign_reward(reward, board)
		#print 'Player',self.player_mark, ' cost = ',self.playerNetwork.assign_reward(reward, board)

	def store_progress(self):
		filename = 'player'+str(self.player_mark)
		np.save(filename, self.playerNetwork.get_all_params())

	def load_progress(self):
		filename = 'player' + str(self.player_mark) + '.npy'
		self.playerNetwork = DeepLearner(np.load(filename))

def testing_with_random(board):
	player = TicTacToePlayer(1,1.0)
	
	return player.make_a_move(board)

if __name__ == '__main__':
	board = np.array([
		[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
		[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
		[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
		[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
		[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
		[ 1 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 ],
		[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
		[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
		[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 ],
		[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 , 0 ]
		])
	print testing_with_random(board)


