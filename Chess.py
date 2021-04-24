# TODO: Unit testing of findoriginatingsquare and findfinalsquare

# Used for rendering the board from a collection of PNGs. 
import PIL

# Mapping of squares to array indices for use in converting coordinates to array indices.
squaremapping = [
["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"] ,
["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"] ,
["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"] ,
["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"] ,
["a3", "b3", "c3", "d3", "e3", "f3", "g3,", "h3"] ,
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



def stripmove(move):
    # TODO strip a move of any illegal characters. This includes capture or check indicators.
    # Iterating through each character.
    strippedMove = "" # Hold stripped move
    
    # May want to return an error here under some circumstances.
    
    for i in range(len(move)):
        # If it's not a legal character.
        if(move[i] in ['=','-','a','b','c','d','e','f','g','h','0','1','2','3','4','5','6','7','8', 'K','Q','R','B','N']):
            # Reconstruct the string around (without) it.
            strippedMove += move[i]
    return strippedMove
        
def checkmovevalid(move):
    # TODO validate if a move is formatted correctly. Does NOT check if a move is possible.
    # Returns True if a move is valid and False otherwise.
    # Moves must be stripped first.
    
    # Valid numbers and letters for locations and pieces.
    LCLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    Numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
    Pieces = ['R', 'N', 'B', 'Q', 'K']
    
    # New Version
    
    # Castling
    if(move[0] == '0'):
        if(move == "0-0" or move == "0-0-0"): # Only valid castling moves.
            return True;
        else:
            return False;
    elif(move[0] in LCLetters): # Pawn move.
        if(len(move) == 2 and move[1] in Numbers): # Simple pawn advancement
            return True
        elif(len(move) == 3 and (move[1] in LCLetters and move[2] in Numbers)): # Simple pawn capture
            return True
        elif(len(move) == 3 and (move[1] in Numbers and move[2] in pieces)): # Pawn advancement and promotion
            return True
        elif (len(move) == 4 and (move[1] in LCLetters and move[2] in Numbers and move[3] in Pieces)): # Pawn capture and promotion
            return True
        else:
            return False
    elif(move[0] in Pieces): # Piece moves
        if(len(move) == 3 and (move[1] in LCLetters and move[2] in Numbers)): # Generic moves
            return True
        elif(len(move) == 4 and move[0] != 'K' and (move[1] in LCLetters or move[1] in Numbers) and move[2] in LCLetters and move[3] in Numbers): # Specifying one piece of information re: originating square
            return True
        # Specifying two pieces of information re: originating square.
        elif(len(move) == 5 and move[0] != 'K' and ((move[1] in LCLetters and move[2] in Numbers) or (move[1] in Numbers and move[2] in LCLetters)) and move[3] in LCLetters and move[4] in Numbers):
            return True
        else:
            return False
    else: # Generic false return in the event that the move can't be validated.
        return False;

def checkmovelegal(move, chessboard, white):
    # TODO check if a move is legal in a given position. 
    # Requires moves to have been run through stripmove() beforehands.
    # This is a computationally-intense function given its internal function calls, so running moves through checkmovevalid() beforehands is highly recommended.
    
    # This does result in calling findoriginatingsquare and findfinalsquare multiple times, but doing it differently would
    # require greatly increasing the complexity of the function calls below, which is no fun for python.
    # Besides, they're not that computationally-intense anyways.
   
   # Holds the resulting position resulting from the move. Ignores all considerations of validity.
    nextboard = executemove(move, chessboard)
 
 
    # Here W stands for white pieces and Z stands for black pieces (conflict with bishops).
    if(white):
        move = "W" + move
    else:
        move = "Z" + move
    
    # Evaluates if a given move of the specificed piece in the given position is legal.
    # Each "piece function" evaluates whether moving the piece as specified is legal, not considering check.
    # Evaluate check then evaluates the resulting position to see if the King is in check (which would make the move illegal).
    
    if(move[1] == "K"):
        if(kingmove(move, chessboard) and not evaluatecheck(nextboard)):
            return True
    elif(move[1] == "Q"):
        if(queenmove(move, chessboard) and not evaluatecheck(nextboard)):
            return True
    elif(move[1] == "R"):
        if(rookmove(move, chessboard) and not evaluatecheck(nextboard)):
            return True
    elif(move[1] == "B"):
        if(bishopmove(move, chessboard) and not evaluatecheck(nextboard)):
            return True
    elif(move[1] == "N"):
        if(knightmove(move, chessboard) and not evaluatecheck(nextboard)):
            return True
    elif(move[1] in ["a", "b", "c", "d", "e", "f", "g", "h"]): # Pawn moves
        if(pawnmove(move, chessboard) and not evaluatecheck(nextboard)):
            return True
    else:
        return False

def findoriginatingsquare(move, chessboard):
    # TODO find the originating square of a given move that has been "stripped." 
    # The originating square is returned as a two-digit integer where the first digit represents the column (i.e. 1 - 8) coordinate
    # and the second digit represents the row (i.e. a - h) coordinate. This is stored as one digit above the actual index as 00
    # would be simplified to 0.
    
    
    # Unfinished. In process of conversion to integer return.
    # FIXME: TEST CASTLING AND PIECE MOVES
    
    originatingPiece = 'W' # The needed information about the originating piece (piece and color)
    if(move[0] == 'Z'): # If the originating piece is black
        originatingPiece = "B" + move[1]
    else:
        originatingPiece = "W" + move[1]
    
    
    # Temporary index tracker for the originating column for pawn captures.
    tempindex = 0
    
    # Track all possible originating locations.
    possibleoriginatinglocations = []
    
    # Special handling of castling.
    if(originatingPiece[1] == '0'):
        return 99
    if(originatingPiece[1] == 'K'): # Can skip originating square logic because max one king.
        # Iterating through all the pieces on the board.
        for i in range(8):
            for j in range(8):
                # If the king is found on the chessboard, then return the corresponding square.
                if(originatingPiece == chessboard[i][j]):
                    return ((10 * (i + 1) + (j+1)))
    # Normal evaluation for major pieces which there could be multiple of. - Untested
    elif(originatingPiece[1] in ['Q','R','B','N']):
        # Iterating through all the pieces on the board.
        for i in range(8):
            for j in range(8):
                # If the piece is found on the chessboard
                if(originatingPiece[1] == (chessboard[i][j])[1] and (chessboard[i][j])[0] == originatingPiece[0]):
                    # Add its square to the possible originating locations.
                    possibleoriginatinglocations.append(((10 * (i + 1) + (j+1))))
        # If there's only one possible originating location then return that.
        if(len(possibleoriginatinglocations) == 1):
            return possibleoriginatinglocations[0]
        # Otherwise iterate through the possible originating locations with different logic for different move formatting / length.
        else:
            # Iterating through the possible originating locations for moves that are specified with a row OR column.
            if(move.len == 5):
                for i in range(len(possibleoriginatinglocations)):
                    if((squaremapping[(int((i / 10)) - 1)][((i % 10) - 1)])[0] == move[2] or (squaremapping[int(i / 10) - 1][(i % 10) - 1])[1] == move[2]):
                        return possibleoriginatinglocations[i]
            # Iterating through the possible originating locations for moves that are specified with a row AND column.
            elif(move.len == 6):
                for i in range(len(possibleoriginatinglocations)):
                    if(( (squaremapping[int(i / 10) - 1][(i % 10) - 1])[0] == move[2]) and ((squaremapping[int(i / 10) - 1][(i % 10) - 1])[1] == move[3])):
                        return possibleoriginatinglocations[i]
            else:
                return "insufficient specification"
    # Pawn moves - tested
    else:
        # Simple advancement.
        if(len(move) == 3):
            for i in range(8):
                for j in range(8):
                    if(squaremapping[i][j] == move[1:3]):
                        if(move[0] == 'W'):
                            return ((10 * (i + 2) + (j+1)))
                        else:
                            return ((10 * (i) + (j+1)))
        # Capture 
        else:
            # Different cases as white pawns advance while capturing while black pawns essentially "regress" one row from an index perspective.
            if(move[0] == 'W'):
                for i in range(8):
                    for j in range(8):
                        if(squaremapping[i][j] == (move[1] + str(int(move[3]) - 1))):
                            return ((10 * (i + 1) + (j+1)))
            else:
                for i in range(8):
                    for j in range(8):
                        if(squaremapping[i][j] == (move[1] + str(int(move[3]) - 1))):
                            return ((10 * (i - 1) + (j+1)))

def findfinalsquare(move):   
    # TODO find the ending square of a given move that has already been stripped by stripmove().
     
    textFinalSquare = ""
    
    move = move[1:] # Stripping color indicator as it is irrelevant.   

    if(move[0] == "0"): # Special handling of castling.
        return 99
    # All other moves.
    else:
        for i in range(len(move)):
            # Dealing with special case of extra information at the end of pawn promotion.
            if(move[i] == "="):
                if(len(move) == 4):
                    textFinalSquare = move[0:2]
                    break
                else:
                    textFinalSquare = move[1:3]
                    break
        # Generally grabbing the last two characters of any other sequence.
        if(textFinalSquare == ""):
            textFinalSquare = move[-2:]
        for i in range(8):
            for j in range(8):
                if(squaremapping[i][j] == textFinalSquare):
                    return ((10 * (i + 1) + (j+1)))
                
def kingmove(move, chessboard):
    # TODO evaluate whether a given king move is legal.
    
    originatingsquare = findoriginatingsquare(move)
    finalsquare = findfinalsquare(move)
    
    
    
    
    return
    
def queenmove(move, chessboard):
    # TODO check if a given queen move is legal.
    # All legal queen moves would be legal for either a bishop or a rook, so evaluation is just passed on to those functions.
    if(rookmove(move, chessboard) or bishopmove(move, chessboard)):
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
                   if(queenmove("Q" + kingsquare, chessboard)):
                       return True
               elif(piece == "BR"):
                   if(rookmove("R" + kingsquare, chessboard)):
                       return True
               elif(piece == "BN"):
                   if(knightmove("N" + kingsquare, chessboard)):
                       return True
               elif(piece == "BB"):
                   if(bishopmove("B" + kingsquare, chessboard)):
                       return True
               elif(piece == "BP"):
                   if(pawnmove((squaremapping[i][j])[0] + kingsquare, chessboard)):
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
                   if(queenmove("Q" + kingsquare, chessboard)):
                       return True
               elif(piece == "WR"):
                   if(rookmove("R" + kingsquare, chessboard)):
                       return True
               elif(piece == "WN"):
                   if(knightmove("N" + kingsquare, chessboard)):
                       return True
               elif(piece == "WB"):
                   if(bishopmove("B" + kingsquare, chessboard)):
                       return True
               elif(piece == "WP"):
                   if(pawnmove((squaremapping[i][j])[0] + kingsquare, chessboard)):
                       return True
               else:
                   return False
   
def executemove(move, chessboard):
    # TODO alter a given chessboard based on a provided move.
    
    nextboard = chessboard
    
    
    return nextboard
    
def renderboard (chessboard):
    # TODO: Create a png of a chessboard from an array in the format defined below.
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


while(game):
    while(impossiblemove):
        move = input("Enter a move: ")
        temp = (findfinalsquare(move))
        print(squaremapping[int(temp / 10) - 1][(temp % 10) - 1])

    
