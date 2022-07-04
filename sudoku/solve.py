from colors import TerminalColors as tc
import requests as r
import json

class Sudoku:
	"""
	Sudoku solver (and eventually generator)
	Can use an api or filesystem to get sudokus to solve
	"""

	def __init__(self, board="api", api_url="https://sugoku.herokuapp.com"):
		self.URL = api_url
		
		if board.lower()=="api":
			self.a = self.load_board_from_api()
		elif board.lower()=="file":
			filename = input("Enter file to read from: ").strip()
			# error check
			self.a = self.load_board_from_file(filename)

	# TO-DO
	def generate_puzzles(self):
		return None

	def is_valid_solution(self):
		for row in range(9):
			if any([i not in self.a[row] for i in range(1, 10)]):
				print(f"Not a valid row {row+1, self.a[row]}")
				return False

		for col in range(9):
			if any([i not in [self.a[row][col] for row in range(9)] for i in range(1, 10)]):
				print(f"Not a valid column {col+1, [self.a[row][col] for row in range(9)]}")
				return False

		print("Valid solution")
		return True

	def print_board(self):
		for li in self.a:
			for val in li:
				if val==0:
					print(f"{tc.RED}", end="")
				else:
					print(f"{tc.GREEN}", end="")

				print(val, end=f"{tc.ENDC} ")
			print()

	def val_in_row(self, row, val):
		return False if val not in self.a[row] else True

	def val_in_column(self, col, val):
		return False if val not in [self.a[x][col] for x in range(9)] else True

	def val_in_square(self, row, col, val):
		r = (row//3)*3
		c = (col//3)*3

		return False if val not in [self.a[i][j] for i in range(r, r+3) for j in range(c, c+3)] else True

	def valid(self, row, col, val):
		return False if any([self.val_in_row(row, val), self.val_in_column(col, val), self.val_in_square(row, col, val)]) else True

	def empty_square(self):
		for i in range(9):
			for j in range(9):
				if self.a[i][j] == 0:
					return i,j

		return None

	def solve_sudoku(self):
		print("Unsolved".center(17))
		self.print_board()
		print(f"{tc.CYAN}{'-'*((9*2)-1)}{tc.ENDC}")
		self.__solve()
		print("Solved".center(17))
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
		board = []
		try:
			with open(filename) as f:
				for li in f.readlines():
					board.append(list(map(int, li.strip().split(" "))))
		except FileNotFoundError:
			print(f"No such file as {filename}...")

		return board

	# for future reference
	# https://github.com/bertoort/sugoku
	def load_board_from_api(self, difficulty='easy'):
		resp = r.get(f"{self.URL}/board?difficulty={difficulty}")
		return json.loads(resp.content.decode('UTF-8'))['board']
	

if __name__=='__main__':

	s = Sudoku()
	s.solve_sudoku()
	s.is_valid_solution()

