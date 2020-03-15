from chessPlayer import *
#import SchessPlayer

def askinput(board, player):
	players=["White", "Black"]
	if player not in (10, 20):
		return False

	
	# get starting location
	currentpos=board.GetPlayerPositions(player)
	print( "It is %s's turn" % players[player//10-1])
	start=int(input("Enter location to move from: "))
	

	while start not in currentpos:
		start=int(input("Invalid location. Please re-enter: "))


	legalmove=board.GetPieceLegalMoves(start)
	end=int(input("Please enter the destination your piece wants to land."))
	while end not in legalmove:	
		end=int(input("Please enter the destination your piece wants to land. Enter -1 to reselect piece to move"))
		if end==-1:
			start=int(input("Enter location to move from: "))
			while start not in currentpos:
				start=int(input("Invalid location. Please re-enter: "))
			legalmove=board.GetPieceLegalMoves(start)


	return (start, end)



def main():
	print ("hello")
	chessboard=board()
	players=["White", "Black"]	
	state=0
	print ("init")
	chessboard.printBoard()
	while state==0:
		print ("current score: ", chessboard.evaluateBoard(10))
		print ("current store: ", chessboard.store)
		chessboard.printBoard()
		print ("White is thinking")
		white_move=SchessPlayer.chessPlayer(chessboard.store, 10)[1]
		#white_move=askinput(chessboard, 10)
		chessboard.setPiece(white_move[0], white_move[1])
		state=chessboard.checkstate()

		if state!=0:
			print("state is", state)
			break
		
		print ("current score: ", chessboard.evaluateBoard(10))
		chessboard.printBoard()
		print("Black is thinking")
		black_move=chessPlayer(chessboard.store, 20)[1]
		chessboard.setPiece(black_move[0], black_move[1])
		state=chessboard.checkstate()

	print(players[state-1], " wins.")

main()
