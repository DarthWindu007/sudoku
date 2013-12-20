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
			return self.get_square_helper(0,j).flatten()
		elif(i<6):
			return self.get_square_helper(3,j).flatten()
		else:
			return self.get_square_helper(6,j).flatten()
	
	def get_possible_values_helper(self,poss,vals):
		for val in vals:
			if val in poss:
				poss.remove(val)

	def get_possible_values(self,i,j):
		if(self.grid[i,j]!=0):
			raise "value already set!"
		poss = [1,2,3,4,5,6,7,8,9]
		vals = self.get_col(j).tolist()+self.get_row(i).tolist()+self.get_square(i,j).tolist()
		self.get_possible_values_helper(poss,vals)
		return poss

	def get_first_unknown(self):
		x = np.where(self.grid == 0)
		#print (x[0][0],x[1][0])
		return (x[0][0],x[1][0])

	def get_copy(self):
		copy = Puzzle()
		copy.grid = np.copy(self.grid)
		copy.is_solved = self.is_solved
		copy.num_unknown = self.num_unknown
		return copy
	
	def set_value(self,i,j,val):
		self.grid[i,j]=val
		self.update_num_unknowns()
	def get_value(self,i,j):
		return self.grid[i,j]

	def __str__(self):
		return self.grid.__str__()


		

filename = "2.txt"

line = open(filename)

puzzle = Puzzle()
num_puzzles = line.readline().split()

lines = line.readlines()
# puzzles = [puzzle]*num_puzzles

for i,line in enumerate(lines):
	puzzle.set_row(line.split(),i)

solutions = []
def solve_puzzle(puz, sol):
	#print puz
	if puz.is_solved:
		print "Found Solution"
		sol.append(puz)
		return
	(i,j) = puz.get_first_unknown()
	#print puz.num_unknown
	poss = puz.get_possible_values(i,j)
	for val in poss:
		puz.set_value(i,j,val)
		solve_puzzle(puz.get_copy(), sol)

solve_puzzle(puzzle, solutions)

print len(solutions)
for i,sol in enumerate(solutions):
	print "solution " + str(i+1)
	print sol
	print "********************************************"


# possible_dic = {}
# current = puzzle.get_copy()
# previous_stack = [None,current]

# print current
# while not current.is_solved:
# 	(i,j) = puzzle.get_first_unknown()
# 	#print i,j

# 	print current
# 	print "///////////////"
# 	if((i,j) not in possible_dic):
# 		possible = puzzle.get_possible_values(i,j)
# 	else:
# 		possible = possible_dic[(i,j)]

# 	if(len(possible)==0):
# 		current=previous_stack.pop()
# 		puzzle = current
# 		if((i,j) in possible_dic):
# 			del possible_dic[(i,j)]
# 		if(current==None):
# 			raise "no solution found"
# 		continue
# 	v = possible[0]
# 	puzzle.set_value(i,j,v)
# 	possible.remove(v)
# 	possible_dic[(i,j)] = possible
# 	previous_stack.append(current)
# 	current=puzzle.get_copy()

# print puzzle


