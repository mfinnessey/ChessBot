# Used for rendering the board from a collection of PNGs. 
import PIL

# Mapping of squares to array indices for use in converting coordinates to array indices.
squaremapping = [
["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"] ,
["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"] ,
["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"] ,
["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"] ,
["a3", "b3", "c3", "d3", "e3", "f3", "g3," "h3"] ,
["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"] ,
["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]

# Array with each position representing one square on the chessboard.
# Snakes from left to right going from A to H and from top to bottom from 8 to 1.
# Pieces are designated with w / b indicating white or black and then a letter representing the piece.
chessboard = [ 
["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR",],
["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP",] ,
["", "", "", "", "", "", "", "", ],
["", "", "", "", "", "", "", "", ],
["", "", "", "", "", "", "", "", ],
["", "", "", "", "", "", "", "", ],
["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP",],
["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR",]
]

# Tracks whether castling is possible for white and black, kingside and queenside (in that order).
castling = [True, True, True, True]

# Create an array to track en passant options.

# Tracks whether white or black is in check.
inCheck = [False, False]

# Tracks whether the game has ended, whether through a resignation, an accepted draw, or a checkmate.
game = True
# Tracks whether the entered move is impossible.
impossiblemove = True

def checkmovevalid(move):
    # TODO validate if a move is formatted correctly. Does NOT check if a move is possible.
    # Moves must be provided in algeBRaic notation.
    # Consider expanding for weird three queens type crap with needing to spec out both letter and number for originating square.
    
    
    # Valid numbers and letters for locations.
    LCLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    Numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    
    # Pawn moves
    # Pawn advancement.
    if(len(move) == 2 and move[0] in LCLetters and move[1] in [1,2,3,4,5,6,7]):
        return True
    # Pawn promotion.
    elif(len(move)==4 and move[2]=='=' and move[3] in ['Q','B','R','N']):
            return True
    # Pawn Captures
    elif(len(move) == 4 and move[1]=='x' and move[2] in LCLetters and move[3] in [1,2,3,4,5,6,7]):
        return True
    # Pawn Capture and Promotion
    elif(len(move) == 6 and move[1]=='x' and move[2] in LCLetters and move[3] == 8 and move[4]=='=' and move[5] in ['Q','B','R','N']):
        return True
    
    # Castling
    if(move[0] == '0'):
        if(move == "0-0" or move == "0-0-0" or move == "0-0+" or move == "0-0-0+"):
            return True
        else:
            return False
    
    
    # King or Queen moves.
    if(move[0] in ['Q', 'B', 'K']):
        if(len(move) == 4 and move[1]=='x' and move[2] in LCLetters and move[3] in Numbers):
            return True
        elif(len(move)==3 and move[1] in LCLetters and move[2] in Numbers):
            return True
        else:
            return False
    
    
    # Rook, Bishop, or Knight moves separated out due to multiple potential originating locations.
    if(move[0] in ['R', 'N']):
        if(len(move) == 4 and move[1]=='x' and move[2] in LCLetters and move[3] in Numbers):
            return True
        elif(len(move) == 3 and move[1] in LCLetters and move[2] in Numbers):
            return True
        elif(move[1] in LCLetters or move[1] in Numbers):
            if(len(move) == 5 and move[2]=='x' and move[3] in LCLetters and move[4] in Numbers):
                return True
            else:
                return False
        else:
            return False
    
    # Generic invalid return.
    return False

def findoriginatingsquare(move, chessboard, white):
    # TODO find the originating square of a given move that has been "stripped"
    # ADD IN OTHER FUNCTION: stripping of moves.
    
    # Temporary index tracker for the originating column for pawn captures.
    tempindex = 0
    
    # Track all possible originating locations.
    possibleoriginatinglocations = []
    
    # Special handling of castling.
    if(move == "0-0" or move == "0-0-0"):
        return "castling"
    if(white):
        # Only one possible king - can skip evaluation of potential multiple pieces.
        elif(move[0] == 'K'):
            # Iterating through all the pieces on the board.
            for i in range(len(chessboard)):
                for j in range (len(chessboard[i]):
                    # If the king is found on the chessboard, then return the corresponding square.
                    if('WK' == chessboard[i][j]):
                        return squaremapping[i][j]
        # Normal evaluation for major pieces which there could be multiple of.
        elif(move[0] in ['Q','R','B','N']):
            # Iterating through all the pieces on the board.
            for i in range(len(chessboard)):
                for j in range (len(chessboard[i]):
                    # If the piece is found on the chessboard
                    if(move[0] == (chessboard[i][j])[1] and (chessboard[i][j])[0] == 'W'):
                        # Add its square to the possible originating locations.
                        possibleoriginatinglocations.append(squaremapping[i][j])
            # If there's only one possible originating location then return that.
            if(len(possibleoriginatinglocations) = 1):
                return possibleoriginatinglocations[0]
            # Otherwise iterate through the possible originating locations with different logic for different move formatting / length.
            else:
                # Iterating through the possible originating locations for moves that are specified with a row OR column.
                if(move.len == 4):
                    for i in range(len(possibleoriginatinglocations)):
                        if(move[1] == (possibleoriginatinglocations[i])[0] or move[1] == (possibleoriginatinglocations[i])[1]):
                            return possibleoriginatinglocations[i]
                # Iterating through the possible originating locations for moves that are specified with a row AND column.
                elif(move.len == 5):
                    if(move[1:2] == possibleoriginatinglocations[i]):
                        return possibleoriginatinglocations[i]
                else:
                    return "insufficient specification"
        # Pawn moves
        else:
            # Simple advancement.
            if(len(move) == 2):
            # Capture 
            else:
                # White pawns advance one row while capturing, and the originating column must be indicated by definition.
                return (move[0] + str(int(move[2]--)))     
    # Black pieces.            
    else:
    # Only one possible king - can skip evaluation of potential multiple pieces.
        elif(move[0] == 'K'):
            # Iterating through all the pieces on the board.
            for i in range(len(chessboard)):
                for j in range (len(chessboard[i]):
                    # If the king is found on the chessboard, then return the corresponding square.
                    if('BK' == chessboard[i][j]):
                        return squaremapping[i][j]
        # Normal evaluation for major pieces which there could be multiple of.
        elif(move[0] in ['Q','R','B','N']):
            # Iterating through all the pieces on the board.
            for i in range(len(chessboard)):
                for j in range (len(chessboard[i]):
                    # If the piece is found on the chessboard
                    if(move[0] == (chessboard[i][j])[1] and (chessboard[i][j])[0] == 'B'):
                        # Add its square to the possible originating locations.
                        possibleoriginatinglocations.append(squaremapping[i][j])
            # If there's only one possible originating location then return that.
            if(len(possibleoriginatinglocations) = 1):
                return possibleoriginatinglocations[0]
            # Otherwise iterate through the possible originating locations with different logic for different move formatting / length.
            else:
                # Iterating through the possible originating locations for moves that are specified with a row OR column.
                if(move.len == 4):
                    for i in range(len(possibleoriginatinglocations)):
                        if(move[1] == (possibleoriginatinglocations[i])[0] or move[1] == (possibleoriginatinglocations[i])[1]):
                            return possibleoriginatinglocations[i]
                # Iterating through the possible originating locations for moves that are specified with a row AND column.
                elif(move.len == 5):
                    if(move[1:2] == possibleoriginatinglocations[i]):
                        return possibleoriginatinglocations[i]
                else:
                    return "insufficient specification"
        # Pawn moves
        else:
            # Simple advancement.
            if(len(move) == 2):
            # Capture 
            else:
                # Black pawns regress (in terms of linear progression) one row while capturing, and the originating column must be indicated by definition.
                return (move[0] + str(int(move[2]++)))
    return "error"

def kingmove(move, chessboard):
    print("king move")
    return
    
def queenmove(move, chessboard):
    # TODO check if a given queen move is legal.
    # All legal queen moves would be legal for either a bishop or a rook, so evaluation is just passed on to those functions.
    if(rookmove(move, chessboard) or bishopmove(move, chessboard):
        return True
    else:
        return False
        
def rookmove(move, chessboard):
    
    print("rook move")
    return
    
def bishopmove(move, chessboard):
    print("bishop move")
    return

def knightmove(move, chessboard):
    print("knight move")
    return

def pawnmove(move, chessboard):
    print("pawn move")
    return

def evaluatecheck(chessboard, white):
    # TODO evaluate if the king of a given color is in check in a given position. True is white and false is black.
    # Returns True if the King is in check and Fasle if the King is not in check.
    
    # Stores the square that the king in question is located on.
    kingsquare = ""
    `
   # Symmetric construction for black king so not commenting that part.
   # Finding the square that the king is on. 
   if(white):
       for i in range(len(chessboard)):
           for j in range(len(chessboard[i])):
               if(piece == "WK"):
                  # Saving the square that the king is on so that the potential legality of moving another piece to that square can be evaluated.
                  kingsqure = squaremapping[i][j]
       # Iterating through all potential locations for enemy pieces.
       for i in range(len(chessboard)):
           for j in range(len(chessboard[i])):
               # If an enemy piece is found, the legality of "capturing" the king is evaluated via the functions for checking the legality of any individual move.
               if(piece == "BK"):
                   if(kingmove("K" + kingsqure, chessboard)):
                       return True
               elif(piece == "BQ"):
                   if(queenmove("Q" + kingsquare, chessboard):
                       return True
               elif(piece == "BR"):
                   if(rookmove("R" + kingsquare, chessboard):
                       return True
               elif(piece == "BN"):
                   if(knightmove("N" + kingsquare, chessboard):
                       return True
               elif(piece == "BB"):
                   if(bishopmove("B" + kingsquare, chessboard):
                       return True
               elif(piece == "BP"):
                   if(pawnmove((squaremapping[i][j])[0] + kingsquare, chessboard):
                       return True
               else:
                   return False
   else:
       for i in range(len(chessboard)):
           for j in range(len(chessboard[i])):
               if(piece == "BK"):
                  kingsqure = squaremapping[i][j]
      for i in range(len(chessboard)):
           for j in range(len(chessboard[i])):
               if(piece == "WK"):
                   if(kingmove("K" + kingsqure, chessboard)):
                       return True
               elif(piece == "WQ"):
                   if(queenmove("Q" + kingsquare, chessboard):
                       return True
               elif(piece == "WR"):
                   if(rookmove("R" + kingsquare, chessboard):
                       return True
               elif(piece == "WN"):
                   if(knightmove("N" + kingsquare, chessboard):
                       return True
               elif(piece == "WB"):
                   if(bishopmove("B" + kingsquare, chessboard):
                       return True
               elif(piece == "WP"):
                   if(pawnmove((squaremapping[i][j])[0] + kingsquare, chessboard):
                       return True
               else:
                   return False

def checkmovelegal(move, chessboard, white):
    # TODO check if a move is legal in a given position. Moves must have already been validated through checkmovevalid as there is no internal error-handling.
    # Unfinished lmao.
   
   # Holds the potential resulting position resulting from the move.
   nextboard = executemove(move, chessboard)
 
    
    # Evaluates if a given move of the specificed piece in the given position is legal. Separated out for readability and ease of evaluating check to assess legality of other moves. Does not handle check considerations.
    
   if(move[0] == "K"):
        if(kingmove(move, chessboard) and evaluatecheck(nextboard)):
            return True
        else:
            return False
   elif(move[0] == "Q"):
        if(queenmove(move, chessboard) and evaluatecheck(nextboard)):
            return True
        else:
            return False
   elif(move[0] == "R"):
        if(rookmove(move, chessboard) and evaluatecheck(nextboard)):
            return True
        else:
            return False
   elif(move[0] == "B"):
        if(bishopmove(move, chessboard) and evaluatecheck(nextboard)):
            return True
        else:
            return False
   elif(move[0] == "N"):
        if(knightmove(move, chessboard) and evaluatecheck(nextboard)):
            return True
        else:
            return False
   elif(move[0] in ["a", "b", "c", "d", "e", "f", "g", "h"]):
        if(pawnmove(move, chessboard) and evaluatecheck(nextboard)):
            return True
        else:
            return False
   else:
        return False

   
       
def executemove(move, chessboard):
    # TODO alter a given chessboard based on a provided move.
    
    nextboard = chessboard
    
    
    return nextboard
    
def renderboard (chessboard):
    # TODO: Create a png of a chessboard from an array in the format defined below.
    # Borked because of switch to 2D array.
    from PIL import Image
    
    # Importing / Creating Images
    # The base image on which everything else is built.
    builder = Image.new('RGB', (1000,1000))
    # Board + Pieces
    board = Image.open("Chessboard.png")
    WP = Image.open("WP.png")
    BP = Image.open("BP.png")
    WK = Image.open("WK.png")
    BK = Image.open("BK.png")
    WQ = Image.open("WQ.png")
    BQ = Image.open("BQ.png")
    WR = Image.open("WR.png")
    BR = Image.open("BR.png")
    WN = Image.open("WN.png")
    BN = Image.open("BN.png")
    WB = Image.open("WB.png")
    BB = Image.open("BB.png")
    
    # Adding the base board to the builder image.
    builder.paste(board)
    
    # Dictionary because python doesn't have switch statements :(
    # Serves to map different pieces stored in chessboard to their respective images for the for loop below.
    fakeswitch = {
        "WP": WP,
        "BP": BP,
        "WK": WK,
        "BK": BK,
        "WQ": WQ,
        "BQ": BQ,
        "WR": WR,
        "BR": BR,
        "WN": WN,
        "BN": BN,
        "WB": WB,
        "BB": BB
    }
    
    # Iterate through the list of squares, pasting the appropriate piece on the square. Quick maths.
    for i in range(len(chessboard)):
        for j in range(len(chessboard[i])):
            # Skipping null strings which represent empty squares.
            if(piece==""):
                pass
            else:
                # This one gets a little complicated.
                # First argument is the image to be pasted, which is fetched via the dictionary defined above.
                # Second argument is the left, upper, right, and lower pixel coordinates. The only weird thing is the lower coordinate which needs a little bump up because math.ceil rounds 0 to 0.
                # Third argument tells PIL to use the transparency on the image as its oWN mask when pasting it onto the board.
                builder.paste(fakeswitch.get(piece), ((125*(j)),(125*(i)),(125*(j+1)),(125*(i+1))), mask = fakeswitch.get(piece))
        # Saving the final image as a PNG
        builder.save("test", format="PNG")
        return


# Taking move inputs.

# Random test code.
checkmovelegal("Na5", chessboard, True)

while(game):
    while(impossiblemove):
        move = input("Enter a move: ")
        if(checkmovevalid(move)):
            print('valid')
        else:
            print('invalid')
    

    
