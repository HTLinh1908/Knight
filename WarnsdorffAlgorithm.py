# Python program to for Knight's tour problem using Warnsdorff's algorithm
import random
import pygame


class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y


dimension = 8

# Move pattern on basis of the change of x coordinates and y coordinates respectively
cx = [1, 1, 2, 2, -1, -1, -2, -2]
cy = [2, -2, 1, -1, 2, -2, 1, -1]


# Restricts the knight to remain within the 8x8 chessboard
def limits(x_coordinate, y_coordinate):
	return (x_coordinate >= 0 and y_coordinate >= 0) and (x_coordinate < dimension and y_coordinate < dimension)


# Checks whether a square is valid and empty or not
def is_empty(board, x_coordinate, y_coordinate):
	return (limits(x_coordinate, y_coordinate)) and (board[y_coordinate * dimension + x_coordinate] < 0)


# Returns the number of empty squares adjacent to (x, y) aka degree of the vertex
def get_degree(board, x_coordinate, y_coordinate):
	count = 0
	for i in range(dimension):
		if is_empty(board, (x_coordinate + cx[i]), (y_coordinate + cy[i])):
			count += 1
	return count


# Picks next point, returns false if it is not possible to pick next point.
def next_move(board, current_cell):
	min_deg_idx = -1
	min_deg = (dimension + 1)

	# Try all N adjacent of (*x, *y) starting from a random adjacent. Find the adjacent with minimum degree.
	start = random.randint(0, 1000) % dimension

	for count in range(0, dimension):
		i = (start + count) % dimension
		next_x = current_cell.x + cx[i]
		next_y = current_cell.y + cy[i]
		degree = get_degree(board, next_x, next_y)
		if (is_empty(board, next_x, next_y)) and degree < min_deg:
			min_deg_idx = i
			min_deg = degree

	# IF we could not find a next cell
	if min_deg_idx == -1:
		return None

	# Store coordinates of next point
	next_x = current_cell.x + cx[min_deg_idx]
	next_y = current_cell.y + cy[min_deg_idx]

	# Mark next move
	board[next_y * dimension + next_x] = board[current_cell.y * dimension + current_cell.x] + 1

	# Update next point
	current_cell.x = next_x
	current_cell.y = next_y

	return current_cell


# Displays the chessboard with all the legal knight's moves
def print_board(board):
	for i in range(dimension):
		for j in range(dimension):
			print("%d\t" % board[j+ dimension * i], end="")
		print()


# Checks if the knight ends on a square that is one move from the beginning square,then tour is closed
def neighbour(x_coordinate, y_coordinate, start_coordinate_x, start_coordinate_y):
	for i in range(dimension):
		if ((x_coordinate + cx[i]) == start_coordinate_x) and ((y_coordinate + cy[i]) == start_coordinate_y):
			return True
	return False


# Generates the legal moves. Returns false if not possible
def find_closed_hamilton_path():
	# Filling up the chessboard matrix with -1's
	board = [-1] * dimension * dimension

	# initial position
	start_coordinate_x = 5
	start_coordinate_y = 1

	# Current points are same as initial points
	current_cell = Cell(start_coordinate_x, start_coordinate_y)

	board[current_cell.y * dimension + current_cell.x] = 1  # Mark first move.

	# Keep picking next points using Warnsdorff's heuristic
	next_move_coordinate = None
	for i in range(dimension * dimension - 1):
		next_move_coordinate = next_move(board, current_cell)
		if next_move_coordinate is None:
			return False

	# Check if tour is closed (Can end at starting point)
	if not neighbour(next_move_coordinate.x, next_move_coordinate.y, start_coordinate_x, start_coordinate_y):
		return False
	print_board(board)

	input("Press any key to continue")

	# Pygame implementation
	pygame.init()
	width, height = 800, 800
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption("Knight's Tour Warnsdorff's Algorithm")
	clock = pygame.time.Clock()
	fps = 60
	current_position = 1
	x, y = 0, 0
	filled_position = []
	knight = pygame.image.load("knight.png")
	knight = pygame.transform.scale(knight, (80, 80))

	def draw_board():
		for i in range(32):
			column = i % 4
			row = i // 4
			if row % 2 == 0:
				pygame.draw.rect(screen, 'light gray', [600 - (column * 200), row * 100, 100, 100])
			else:
				pygame.draw.rect(screen, 'light gray', [700 - (column * 200), row * 100, 100, 100])
			for index in range(9):
				pygame.draw.line(screen, 'black', (0, 100 * i), (800, 100 * i), 2)
				pygame.draw.line(screen, 'black', (100 * i, 0), (100 * i, 800), 2)

	def draw_knight(x, y):
		screen.blit(knight, (x * 100, y * 100))

	run = True
	while run:
		clock.tick(fps)
		screen.fill("black")
		draw_board()
		pygame.transform.flip(screen, False, True)
		for i in board:
			if i == current_position:
				x = board.index(i) % 8
				y = board.index(i) // 8

		draw_knight(x, y)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		for item in filled_position:
			pygame.draw.circle(screen, 'red', (item[0] * 100 + 50, item[1] * 100 + 50), 30)

		filled_position.append((x, y))

		current_position += 1
		pygame.time.delay(1000)
		pygame.display.update()
	pygame.quit()

	return True


if __name__ == '__main__':
	# While no solution is found
	while not find_closed_hamilton_path():
		pass
