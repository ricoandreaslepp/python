import requests as r
import json

class term_colors:
	GREEN = '\033[92m'
	RED = '\033[91m'
	CYAN = '\033[96m'
	ENDC = '\033[0m'

class Sudoku:

	URL = "https://sugoku.herokuapp.com"

	def __init__(self):
		pass

	# TO-DO
	def check_solution(self):
		return None

	# TO-DO
	def generate_puzzles(self):
		return None

	def print_board(self):
		for li in self.a:
			for val in li:
				if val==0:
					print(f"{term_colors.RED}", end="")
				else:
					print(f"{term_colors.GREEN}", end="")

				print(val, end=" ")
			print()

	def valid_row(self, row, col, val):
		return True if val not in self.a[row] else False

	def valid_column(self, row, col, val):
		return True if val not in [self.a[x][col] for x in range(9)] else False

	def valid_square(self, row, col, val):
		r = (row//3)*3
		c = (col//3)*3

		return True if val not in [self.a[i][j] for i in range(r, r+3) for j in range(c, c+3)] else False

	def valid(self, row, col, val):
		return True if all([self.valid_row(row, col, val), self.valid_column(row, col, val), self.valid_square(row, col, val)]) else False

	def empty_square(self):
		for i in range(9):
			for j in range(9):
				if self.a[i][j] == 0:
					return i,j

		return None

	def solve_sudoku(self):
		self.print_board()
		print(f"{term_colors.CYAN}" + "-"*((9*2)-1))
		self.__solve()
		self.print_board()

	# Backtracking algorithm
	def __solve(self):

		if self.empty_square():
			row, col = self.empty_square()
		else: # solved
			return True

		for i in range(1, 10):
			
			if self.valid(row, col ,i):
				self.a[row][col] = i

				if self.__solve():
					return True

				# backtrack
				self.a[row][col] = 0

		return False

	def load_board_from_file(self, filename):
		try:
			with open(filename) as f:
				for li in f.readlines():
					self.a.append(list(map(int, li.strip().split(" "))))
		except FileNotFoundError:
			print(f"No such file as {filename}...")

	# same api offers solution as well, for future reference
	# https://github.com/bertoort/sugoku
	def get_board_from_api(self, difficulty='easy'):
		resp = r.get(f"{self.URL}/board?difficulty={difficulty}")
		self.a = json.loads(resp.content.decode('UTF-8'))['board']
	

if __name__=='__main__':

	s = Sudoku()
	s.get_board_from_api()
	s.solve_sudoku()
	"""
	if action.strip().lower()=='file':
		filename = input("Enter the name of the file to open: ")
	elif action.strip().lower()=='api':
		difficulty = input("Enter the difficulty to test: ")
	"""
