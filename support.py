EMPTY = "\U000025CB"
PLAYER_1_PIECE ='\U000025CD' 
PLAYER_2_PIECE ='\U000025CF'

BOARD_SIZE = 5
NUM_PLAYER_PIECES = 4
WIN_LENGTH = NUM_PLAYER_PIECES

HELP_COMMAND = "h"
QUIT_COMMAND = "q"
PLACE_COMMAND = "p"
MOVE_COMMAND = "m"

PLAYER_1_DISPLAY = "Player 1"
PLAYER_2_DISPLAY = "Player 2"
WELCOME_MESSAGE = "Welcome to Teeko!"
INVALID_FORMAT_MESSAGE = "Invalid command. Enter 'h' for valid command format or 'q' to quit"
ENTER_COMMAND_PROMPT = "Please enter your command (h to see valid command): "
MOVE_MESSAGE = "'s turn to move"
PLACE_MESSAGE = "'s pieces to place: "
MUST_PLACE_MESSAGE = "First, you have to place all your pieces on the board!"
ALREADY_PLACED_MESSAGE = "You have already placed all your pieces on the board!"
INVALID_PLACEMENT_MESSAGE = "That position is not valid!"
INVALID_MOVEMENT_MESSAGE = "That movement is not valid!"
HELP_MESSAGE = """Valid Commands: 
    pXY   - Place a piece at row X, column Y (e.g., p34 places a piece at row 3, column 4)
    mXYUV - Move a piece from position (X,Y) to (U,V) (e.g., m3425 moves from 3,4 to 2,5)
    h     - Show this help message
    q     - Quit the game"""
VICTORY_MESSAGE = " wins!"
AGAIN_PROMPT = "Would you like to play again? (y/n): "

def turn_message(num_pieces: int) -> str:
    """
    Returns the appropriate prompting message based on remaining pieces.

    Args:
        num_pieces (int): The number of pieces the current player has left to 
                          place.

    Returns:
        str: A message prompting the player to place or move a piece.
    """
    if num_pieces:
        message = PLACE_MESSAGE + str(num_pieces)
    else:
        message = MOVE_MESSAGE
    return message
