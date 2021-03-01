import numpy as np

starting_board = [5, 3, 0, 0, 7, 0, 0, 0, 0,
					6, 0, 0, 1, 9, 5, 0, 0, 0,
					0, 9, 8, 0, 0, 0, 0, 6, 0,
					8, 0, 0, 0, 6, 0, 0, 0, 3,
					4, 0, 0, 8, 0, 3, 0, 0, 1,
					7, 0, 0, 0, 2, 0, 0, 0, 6,
					0, 6, 0, 0, 0, 0, 2, 8, 0,
					0, 0, 0, 4, 1, 9, 0, 0, 5,
					0, 0, 0, 0, 8, 0, 0, 7, 9]

def potential_candidates(board):
	board_array = np.array(board)

	board_shaped = np.reshape(board_array, (9,9))
	num_board = np.arange(81).reshape((9,9))

	num_sub_boards = np.array([num_board[0:3, 0:3], num_board[0:3, 3:6], num_board[0:3, 6:9],
								num_board[3:6, 0:3], num_board[3:6, 3:6], num_board[3:6, 6:9],
								num_board[6:9, 0:3], num_board[6:9, 3:6], num_board[6:9, 6:9]])

	sub_boards = np.array([board_shaped[0:3, 0:3], board_shaped[0:3, 3:6], board_shaped[0:3, 6:9],
							board_shaped[3:6, 0:3], board_shaped[3:6, 3:6], board_shaped[3:6, 6:9],
							board_shaped[6:9, 0:3], board_shaped[6:9, 3:6], board_shaped[6:9, 6:9]])

	x, y = np.where(board_shaped == 0)

	if len(x) == 0:
		print('done')
		return None

	else:
		row = x[0] #0
		col = y[0] #2

		nums_in_row = board_shaped[row]
		nums_in_col = board_shaped[:,col:col+1]

		target = num_board[row:row+1,col:col+1]

		for num, sub_board in enumerate(num_sub_boards):
			if target in sub_board:
				target_board = num
				break

		sub_board_nums = sub_boards[target_board]

		flat_a = nums_in_row.flatten()
		flat_b = nums_in_col.flatten()
		flat_c = sub_board_nums.flatten()

		numbers = np.concatenate((flat_a, flat_b, flat_c))

		opposing_candidates = np.unique(numbers[numbers != 0])

		candidates = list()

		for i in range(1, 10):
			if i not in opposing_candidates:
				candidates.append(i)

		return (candidates, (row, col))


def solve_it(starting_board):
	board = np.array(starting_board).reshape((9, 9))
	return_tuple = potential_candidates(board)

	if return_tuple is None: 
		print(board)
		return None

	else:
		candidates, pos = return_tuple

		for candidate in candidates:
			board[pos[0]:pos[0]+1,pos[1]:pos[1]+1] = candidate
			solve_it(board)
		

solve_it(starting_board)





