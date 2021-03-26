import PIL
import math
# Move to 2D Array
def checkmovevalid(move):
    # TODO validate if a move is formatted correctly. Does NOT check if a move is possible.
    # Moves must be provided in algebraic notation.
    
    # Consider removing x from move notation.
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
    if(move[0] in ['Q', 'K']):
        if(len(move) == 4 and move[1]=='x' and move[2] in LCLetters and move[3] in Numbers):
            return True
        elif(len(move)==3 and move[1] in LCLetters and move[2] in Numbers):
            return True
        else:
            return False
    
    
    # Rook, Bishop, or Knight moves separated out due to multiple potential originating locations.
    if(move[0] in ['R', 'B', 'N']):
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

def kingmove(move, chessboard):
        print("king move")
        return
def queenmove(move, chessboard):
    print("queen move")
    return
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
        # Mapping of squares to array indices for use in locating the king in relation to other moves.
        squaremapping = [
        ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"] ,
        ["a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7"],
        ["a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6"] ,
        ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"] ,
        ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"] ,
        ["a3", "b3", "c3", "d3", "e3", "f3", "g3," "h3"] ,
        ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"] ,
        ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]]
       # Symmetric construction for black king so not commenting that part.
       # Finding the square that the king is on. 
       if(white):
           for i in range(len(chessboard)):
               for j in range(len(chessboard[i])):
                   if(piece == "wk"):
                      # Saving the square that the king is on so that the potential legality of moving another piece to that square can be evaluated.
                      kingsqure = squaremapping[i][j]
           # Iterating through all potential locations for enemy pieces.
           for i in range(len(chessboard)):
               for j in range(len(chessboard[i])):
                   # If an enemy piece is found, the legality of "capturing" the king is evaluated via the functions for checking the legality of any individual move.
                   if(piece == "bk"):
                       if(kingmove("K" + kingsqure, chessboard)):
                           return True
                   elif(piece == "bq"):
                       if(queenmove("Q" + kingsquare, chessboard):
                           return True
                   elif(piece == "br"):
                       if(rookmove("R" + kingsquare, chessboard):
                           return True
                   elif(piece == "bn"):
                       if(knightmove("N" + kingsquare, chessboard):
                           return True
                   elif(piece == "bb"):
                       if(bishopmove("B" + kingsquare, chessboard):
                           return True
                   elif(piece == "bp"):
                       if(pawnmove((squaremapping[i][j])[0] + kingsquare, chessboard):
                           return True
                   else:
                       return False
       else:
           for i in range(len(chessboard)):
               for j in range(len(chessboard[i])):
                   if(piece == "bk"):
                      kingsqure = squaremapping[i][j]
          for i in range(len(chessboard)):
               for j in range(len(chessboard[i])):
                   if(piece == "wk"):
                       if(kingmove("K" + kingsqure, chessboard)):
                           return True
                   elif(piece == "wq"):
                       if(queenmove("Q" + kingsquare, chessboard):
                           return True
                   elif(piece == "wr"):
                       if(rookmove("R" + kingsquare, chessboard):
                           return True
                   elif(piece == "wn"):
                       if(knightmove("N" + kingsquare, chessboard):
                           return True
                   elif(piece == "wb"):
                       if(bishopmove("B" + kingsquare, chessboard):
                           return True
                   elif(piece == "wp"):
                       if(pawnmove((squaremapping[i][j])[0] + kingsquare, chessboard):
                           return True
                   else:
                       return False

def checkmovelegal(move, chessboard, white):
    # TODO check if a move is legal in a given position. Moves must have already been validated through checkmovevalid as there is no internal error-handling.
    # Unfinished lmao.
   
   updatedboard = chessboard
   # Stores the square that the king in question is located on.
   kingsquare = ""
    
   # Listing of white and black pieces for use in evaluatecheck
   whitepieces = ["wk", "wq", "wr", "wn", "wb", "wp"]
   blackpieces = ["bk", "bq", "br", "bn", "bb", "bp"]
   
    
    # TODO Evaluate if a given move of the specificed piece in the given position is legal. Separated out for readability and ease of evaluating check to assess legality of other moves. Does not handle check considerations.
    
   if(move[0] == "K"):
        if(kingmove(move, chessboard) and evaluatecheck(updatedboard)):
            return True
        else:
            return False
   elif(move[0] == "Q"):
        if(queenmove(move, chessboard) and evaluatecheck(updatedboard)):
            return True
        else:
            return False
   elif(move[0] == "R"):
        if(rookmove(move, chessboard) and evaluatecheck(updatedboard)):
            return True
        else:
            return False
   elif(move[0] == "B"):
        if(bishopmove(move, chessboard) and evaluatecheck(updatedboard)):
            return True
        else:
            return False
   elif(move[0] == "N"):
        if(knightmove(move, chessboard) and evaluatecheck(updatedboard)):
            return True
        else:
            return False
   elif(move[0] in ["a", "b", "c", "d", "e", "f", "g", "h"]):
        if(pawnmove(move, chessboard) and evaluatecheck(updatedboard)):
            return True
        else:
            return False
   else:
        return False

   
       
def executemove(move, chessboard):
    # TODO alter a given chessboard based on a provided move.
    return
    
def renderboard (chessboard):
    # TODO: Create a png of a chessboard from an array in the format defined below.
    # Borked because of switch to 2D array.
    from PIL import Image
    
    # Importing / Creating Images
    # The base image on which everything else is built.
    builder = Image.new('RGB', (1000,1000))
    # Board + Pieces
    board = Image.open("Chessboard.png")
    wp = Image.open("WP.png")
    bp = Image.open("BP.png")
    wk = Image.open("WK.png")
    bk = Image.open("BK.png")
    wq = Image.open("WQ.png")
    bq = Image.open("BQ.png")
    wr = Image.open("WR.png")
    br = Image.open("BR.png")
    wn = Image.open("WN.png")
    bn = Image.open("BN.png")
    wb = Image.open("WB.png")
    bb = Image.open("BB.png")
    
    # Adding the base board to the builder image.
    builder.paste(board)
    
    # Dictionary because python doesn't have switch statements :(
    # Serves to map different pieces stored in chessboard to their respective images for the for loop below.
    fakeswitch = {
        "wp": wp,
        "bp": bp,
        "wk": wk,
        "bk": bk,
        "wq": wq,
        "bq": bq,
        "wr": wr,
        "br": br,
        "wn": wn,
        "bn": bn,
        "wb": wb,
        "bb": bb
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
                # Third argument tells PIL to use the transparency on the image as its own mask when pasting it onto the board.
                builder.paste(fakeswitch.get(piece), ((125*(j)),(125*(i)),(125*(j+1)),(125*(i+1))), mask = fakeswitch.get(piece))
        # Saving the final image as a PNG
        builder.save("test", format="PNG")
        return

# Array with each position representing one square on the chessboard.
# Snakes from left to right going from A to H and from top to bottom from 8 to 1.
# Pieces are designated with w / b indicating white or black and then a letter representing the piece.
chessboard = [ 
["br", "bn", "bb", "bq", "bk", "bb", "bn", "br",],
["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp",] ,
["", "", "", "", "", "", "", "", ],
["", "", "", "", "", "", "", "", ],
["", "", "", "", "", "", "", "", ],
["", "", "", "", "", "", "", "", ],
["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp",],
["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr",]
]


# Tracks whether castling is possible for white and black, kingside and queenside (in that order).
castling = [True, True, True, True]

# Tracks whether white or black is in check.
inCheck = [False, False]

# Tracks whether the game has ended, whether through a resignation, an accepted draw, or a checkmate.
game = True
# Tracks whether the entered move is impossible.
impossiblemove = True

# Taking move inputs.

checkmovelegal("Na5", chessboard, True)

while(game):
    while(impossiblemove):
        move = input("Enter a move: ")
        if(checkmovevalid(move)):
            print('valid')
        else:
            print('invalid')
    

    
