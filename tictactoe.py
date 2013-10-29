class TicTacToeGame(object):

	def __init__(self):
		self.board = [ '-' for i in range(0,9) ]
		self.lastmoves = []
		self.winner = None
		self.wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
		

		
	def print_board(self):
	
		print "\nBoard\n"
		
		for j in range(0,9,3):
			print "%s | %s | %s" % (self.board[j], self.board[j+1], self.board[j+2])

			
	def list_free_spots(self):
		moves = [i for i,v in enumerate(self.board) if v == '-']
		return moves
		
	def mark_move(self, letter, space):
		self.board[space] = letter
		self.lastmoves.append(space)
		
	def undo_move(self):
		self.board[self.lastmoves.pop()] = '-'
		self.winner = None
		
	def is_gameover(self):
	
		for i,j,k in self.wins:
			if self.board[i] == self.board[j] == self.board[k] and self.board[i] != '-':
				self.winner = self.board[i]
				return True				
			elif '-' not in self.board:
				self.winner = '-'
				return True

		return False
		
			
	def play(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		
		for i in range(9):
		
			self.print_board()
			
			if i%2 == 0:
				print "Player 1 (%s)'s move" % self.p1.type
				self.p1.move(self)
			else:
				print "Player 2 (%s)'s move" % self.p2.type
				self.p2.move(self)
			if self.is_gameover():
				self.print_board()
				if self.winner == '-':
					print "Draw"
				else:
					print "\nWinner: %s" % self.winner
				return
				
class Human(object):
	def __init__(self, letter):
		self.letter = letter
		self.type = 'H'
		
	def move(self, gameinstance):
		while True:
			m = raw_input("Input position:")
			try:
				m = int(m)
			except:
				m = -1

			if m not in gameinstance.list_free_spots():
				print "invalid move"
			else:
				break
		
		gameinstance.mark_move(self.letter, m)
		
class Computer(object):
	def __init__(self, letter):
		self.letter = letter
		self.type = 'C'
		
		if self.letter == 'X':
			self.opponentletter = 'O'
		else:
			self.opponentletter = 'X'
						
	def move(self, gameinstance):

		m,score,mx= self.max_move_two(gameinstance, 1)
	#	m, score = self.max_move(gameinstance)
		gameinstance.mark_move(self.letter, m)
		
	def max_move(self, gameinstance):
		bestscore = None
		bestmove = None
		
		for m in gameinstance.list_free_spots():
			gameinstance.mark_move(self.letter, m)
			
			if gameinstance.is_gameover():
				score = self.get_score(gameinstance)
			else:
				move_pos, score = self.min_move(gameinstance)
			gameinstance.undo_move()
			
			if bestscore == None or score > bestscore:
				bestscore = score
				bestmove = m
		return bestmove, bestscore
				
	def min_move(self, gameinstance):
		bestscore = None
		bestmove = None
		
		for m in gameinstance.list_free_spots():
			gameinstance.mark_move(self.opponentletter, m)
			
			if gameinstance.is_gameover():
				score = self.get_score(gameinstance)
			else:
				move_pos, score = self.max_move(gameinstance)
			gameinstance.undo_move()
			
			if bestscore == None or score < bestscore:
				bestscore = score
				bestmove = m
		return bestmove, bestscore
	
		
 	def max_move_two(self, gameinstance, maxmin):
		bestscore = None
		bestmove = None

		for m in gameinstance.list_free_spots():
			if maxmin > 0:
				gameinstance.mark_move(self.letter, m)
			else:
				gameinstance.mark_move(self.opponentletter,m)
			if gameinstance.is_gameover():
				score = self.get_score(gameinstance)
			else:
				move_pos, score, maxmin = self.max_move_two(gameinstance, -maxmin)
			
			gameinstance.undo_move()
			
			if maxmin > 0:
				cond = score > bestscore
			else:
				cond = score < bestscore
			
			if bestscore == None or cond:
				bestscore = score
				bestmove = m
				
		return bestmove, bestscore, -maxmin
	
	def get_score(self, gameinstance):
		if gameinstance.is_gameover():
			if gameinstance.winner == self.letter:
				return 1
			elif gameinstance.winner == self.opponentletter:
				return -1
		return 0
		
		
if __name__ == '__main__':
	game = TicTacToeGame()
	player1 = Human("X")
	player2 = Computer("O")
	game.play(player1, player2)