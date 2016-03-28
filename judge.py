import numpy as np

TIE_MARK = -2
PLAYER1_MARK = 1
PLAYER2_MARK = -1
NO_WINNER_MARK = 0

class TicTacToeJudge(object):
	
	def __init__ (self, num_contigous_marks_to_win = 3):
		self.board = []
		self.n_winmarks = num_contigous_marks_to_win

	def check_move (self, new_board, old_board, player_mark):
		count = 0
		legal_move = True
		for index, x in np.ndenumerate(new_board):
			if x != old_board[index]:
				if x == player_mark:
					count += 1
				else :
					legal_move = False
		
		if count != 1:
			legal_move = False
		
		return legal_move


	def get_result(self, board):
		self.board = board
		winner = NO_WINNER_MARK
		for index, x in np.ndenumerate(self.board):
			if x == PLAYER1_MARK or x == PLAYER2_MARK :
				winner = self.get_winner(index)
				if winner != NO_WINNER_MARK:
					break
		
		# Tie Condition
		if sum(sum(board == 0)) == 0 and winner == NO_WINNER_MARK:  
			winner = TIE_MARK

		return winner

	def check_index(self, i,j,shape_array):
		if i < 0 or j < 0:
			return False
		if i >= shape_array[0] or j >= shape_array[1]:
			return False
		return True


	def get_winner(self, index):
		x = self.board[index]
		i, j = index
		winner = 0
		shape = self.board.shape

		if not self.check_index(i-1, j-1, shape) or self.board[i-1,j-1] != x :
			winner = self.check_right_diagonal(index)
			if winner != 0:
				return winner
		if not self.check_index(i-1, j, shape) or self.board[i-1,j] != x :
			winner = self.check_vertical( index)
			if winner != 0:
				return winner
		if not self.check_index(i-1, j+1, shape) or self.board[i-1,j+1] != x :
			winner = self.check_left_diagonal(index)
			if winner != 0:
				return winner 
		if not self.check_index(i, j-1, shape) or self.board[i,j-1] != x :
			winner = self.check_horizontal(index)

		return winner

	def check_right_diagonal(self, index):
		winner = 0
		i,j = index
		x = self.board[index]
		shape = self.board.shape
		for k in range(4):
			if self.check_index(i+k+1, j+k+1, shape) and self.board[i+k+1, j+k+1] == x :
				if k == self.n_winmarks-2:
					winner = x
			else :
				break
		return winner

	def check_vertical(self, index):
		winner = 0
		i,j = index
		x = self.board[index]
		shape = self.board.shape

		for k in range(4):
			if self.check_index(i+k+1, j, shape) and self.board[i+k+1, j] == x :
				if k == self.n_winmarks - 2:
					winner = x
			else :
				break

		return winner

	def check_left_diagonal(self, index):
		winner = 0
		i,j = index
		x = self.board[index]
		shape = self.board.shape

		for k in range(4):
			if self.check_index(i+k+1, j-k-1, shape) and self.board[i+k+1, j-k-1] == x :
				if k == self.n_winmarks-2:
					winner = x
			else :
				break

		return winner

	def check_horizontal(self, index):
		winner = 0
		i,j = index
		x = self.board[index]
		shape = self.board.shape

		for k in range(4):
			if self.check_index(i, j+k+1, shape) and self.board[i, j+k+1] == x :
				if k == self.n_winmarks-2:
					winner = x
			else :
				break

		return winner
if __name__ == '__main__':
	board = np.array([
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
		])
	board1diag = np.array([
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
		])
	board2hor = np.array([
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 ,-1 ,-1 ,-1 ,-1 ,-1 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
		])
	board1vert = np.array([
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
		[ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
		])
	tttJ = TicTacToeJudge()
	print tttJ.get_result(board)
	print tttJ.get_result(board1diag)
	print tttJ.get_result(board2hor)
	print tttJ.get_result(board1vert)
