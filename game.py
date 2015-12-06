from player import TicTacToePlayer as TTTPlayer
from judge import TicTacToeJudge as TTTJudge
import numpy as np

class TicTacToeGame:

	def __init__(self, player1, player2 ,print_every_move_flag=False):
		self.players = [player1 , player2]
		self.board = np.zeros((8,8),np.int8)
		self.judge = TTTJudge()
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
				if winner != 0 :
					game_over = True
					# if self.print_every_move_flag:
					print 'count = ',count
					if winner == -2:
						print 'Game Tied'
					else :
						if self.print_every_move_flag:
							print 'Winner = ', player.player_mark
					break
		self.reward_winner(winner)
		return winner
	
	def reward_winner(self, winner):
		
		self.players[0].gamesPlayed += 1
		self.players[1].gamesPlayed += 1
		if winner == -2:
			self.players[0].pass_rewards(self.board,0)
			self.players[1].pass_rewards(self.board,0)
		else:
			
			if winner == self.players[1].player_mark:
				winning_player = self.players[1]
				losing_player = self.players[0]
			else :
				winning_player = self.players[0]
				losing_player = self.players[1]
			winning_player.pass_rewards(self.board,1)
			losing_player.pass_rewards(self.board,-1)
			winning_player.gamesWon += 1


if __name__ == '__main__':
	player1 = TTTPlayer(1, 0.2)


	player2 = TTTPlayer(-1, 0.2)

	
	#print 'Random Training'
	i = 0
	response = 'y'
	# player1.load_progress()
	# player2.load_progress()
	while response == 'y':
		# player2.strategy = [(1,0),(1,2),(1,1)]
		
		i += 1
		print 'Game ',i
		game = TicTacToeGame(player1, player2)
		winner = game.play_game()
		print 'Winner = Player ', winner
		# print 'Player 1 Wins = ', player1.gamesWon
		# print 'Player 2 Wins = ', player2.gamesWon
		
		# if winner != -1:
		# 	response = 'y'
		response = raw_input("Continue?[y/n]")
		# if i%100 == 0:
		# 	player1.store_progress()
		# 	player2.store_progress()


