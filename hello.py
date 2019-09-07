def display_board(board):
	
	#clear_output()
	print(board[7]+ '|' +board[8]+ '|' +board[9])
	print(board[4]+ '|' +board[5]+ '|' +board[6])
	print(board[3]+ '|' +board[2]+ '|' +board[1])

test_board = ['#','X','O','X','O','X','O','X','O','X']

display_board(test_board)

def player_input():

	marker = ''
	while marker != 'X' and marker != 'O':
		marker = input('Player1: Choose X or O').upper()

	if marker == 'X':
		return ('X','O')
	else:
		return('O','X')

player_input()

def place_marker(board,marker,position):
	
	board[position] = marker

place_marker(test_board,'@',9)
display_board(test_board)

def win_check(board,  mark):
	
	print((board[7] == board[8] == board[9] == mark))
	return ((board[7] == board[8] == board[9] == mark) or
		(board[4] == board[5] == board[6] == mark) or
		(board[3] == board[2] == board[1] == mark) or
		(board[7] == board[4] == board[1] == mark) or
		(board[8] == board[5] == board[2] == mark) or
		(board[9] == board[6] == board[3] == mark) or
		(board[7] == board[5] == board[3] == mark) or
		(board[9] == board[5] == board[1] == mark))



win_check(test_board,'X')