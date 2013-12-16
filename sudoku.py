#sudoku solver
from sys import argv
import numpy as np

class Puzzle(object):
	"""docstring for Puzzle"""
	def __init__(self):
		super(Puzzle, self).__init__()
		self.grid = self.blank_puzzle()
	def blank_puzzle(self):
		self.num_unknown = 81
		self.is_solved=False
		return np.zeros((9,9),dtype=np.int)
	
	def set_row(self,vals,r):
		for i,num in enumerate(vals):
			self.grid[r,i] = (int)(num)
		self.update_num_unknowns()

	def update_num_unknowns(self):
		num = 81-np.count_nonzero(self.grid)
		self.num_unknown = num
		if(self.num_unknown==0):
			self.is_solved = True

	def get_row(self,r):
		return self.grid[r,:]

	def get_col(self,c):
		return self.grid[:,c]

	def get_square_helper(self,i,j):
		if(j<3):
			return self.grid[i:i+3,0:3]
		elif(j<6):
			return self.grid[i:i+3,3:6]
		else:
			return self.grid[i:i+3,6:9]

	def get_square(self,i,j):
		if(i<3):
			return self.get_square_helper(0,j)
		elif(i<6):
			return self.get_square_helper(3,j)
		else:
			return self.get_square_helper(6,j)


filename = "input.txt"

line = open(filename)

puzzle = Puzzle()
num_puzzles = line.readline().split()

lines = line.readlines()

for i,line in enumerate(lines):
	puzzle.set_row(line.split(),i)
print puzzle.grid
print puzzle.get_square(1,1)
print puzzle.get_square(1,2)
print puzzle.get_square(5,5)

print puzzle.num_unknown
