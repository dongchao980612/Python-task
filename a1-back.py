# DO NOT modify or add any import statements
from support import *

# Name:
# Student Number:
# Favorite Tree:
# -----------------------------------------------------------------------------

# Define your classes and functions here

def num_hours() -> float:
    """
    Returns the number of hours spent on this assignment.

    Returns:
        float: Number of hours spent on the assignment
    """
    return 10.0

def create_empty_board(board_size: int) -> list[list[str]]:
    """
    Generates an empty board with a specified number of rows.

    Args:
        board_size (int): The size of the square board

    Returns:
        list[list[str]]: A 2D list representing the empty board
    """
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(EMPTY)
        board.append(row)
    return board

def display_board(board: list[list[str]]) -> None:
    """
    Prints the given game state to the screen in a visually appealing format.

    Args:
        board (list[list[str]]): The board to display
    """
    if not board:
        return

    # Print column headers
    print("  ", end="")
    for col in range(len(board[0])):
        print(f"{col + 1}  ", end="")
    print()

    # Print rows with row numbers
    for row_idx, row in enumerate(board):
        print(f"{row_idx + 1} ", end="")
        for cell in row:
            print(f"{cell}  ", end="")
        print()
        if row_idx < len(board) - 1:
            print()

def add_piece(board: list[list[str]], piece: str, pos: tuple[int, int]) -> bool:
    """
    Adds the specified piece to the board at the given location if valid to do so.

    Args:
        board (list[list[str]]): The game board
        piece (str): The piece to add
        pos (tuple[int, int]): Position as (row, column) 1-indexed

    Returns:
        bool: True if piece was successfully added, False otherwise
    """
    row, col = pos
    # Convert to 0-indexed
    row -= 1
    col -= 1

    # Check if position is empty
    if board[row][col] != EMPTY:
        print(INVALID_PLACEMENT_MESSAGE)
        return False

    # Place the piece
    board[row][col] = piece
    return True

def move_piece(board: list[list[str]], piece: str, current_pos: tuple[int, int], target_pos: tuple[int, int]) -> bool:
    """
    Moves the specified piece from current_pos to target_pos within board.

    Args:
        board (list[list[str]]): The game board
        piece (str): The piece to move
        current_pos (tuple[int, int]): Current position (row, col) 1-indexed
        target_pos (tuple[int, int]): Target position (row, col) 1-indexed

    Returns:
        bool: True if piece was successfully moved, False otherwise
    """
    curr_row, curr_col = current_pos
    target_row, target_col = target_pos

    # Convert to 0-indexed
    curr_row -= 1
    curr_col -= 1
    target_row -= 1
    target_col -= 1

    # Check if current position contains the piece
    if board[curr_row][curr_col] != piece:
        print(INVALID_MOVEMENT_MESSAGE)
        return False

    # Check if target position is empty
    if board[target_row][target_col] != EMPTY:
        print(INVALID_MOVEMENT_MESSAGE)
        return False

    # Check if target position is adjacent (including diagonal)
    row_diff = abs(target_row - curr_row)
    col_diff = abs(target_col - curr_col)

    if row_diff > 1 or col_diff > 1 or (row_diff == 0 and col_diff == 0):
        print(INVALID_MOVEMENT_MESSAGE)
        return False

    # Move the piece
    board[curr_row][curr_col] = EMPTY
    board[target_row][target_col] = piece
    return True

def check_input(command: str) -> bool:
    """
    Returns True if the given command is of a valid format.

    Args:
        command (str): The command to check

    Returns:
        bool: True if command is valid format, False otherwise
    """
    if not command:
        return False

    command = command.lower()

    # Check for help command
    if command == "h":
        return True

    # Check for quit command
    if command == "q":
        return True

    # Check for place command (p + 2 digits)
    if len(command) == 3 and command[0] == "p":
        if command[1].isdigit() and command[2].isdigit():
            row = int(command[1])
            col = int(command[2])
            if 1 <= row <= 5 and 1 <= col <= 5:
                return True

    # Check for move command (m + 4 digits)
    if len(command) == 5 and command[0] == "m":
        if all(c.isdigit() for c in command[1:]):
            from_row = int(command[1])
            from_col = int(command[2])
            to_row = int(command[3])
            to_col = int(command[4])
            if (1 <= from_row <= 5 and 1 <= from_col <= 5 and
                1 <= to_row <= 5 and 1 <= to_col <= 5):
                return True

    return False


def get_command() -> str:
    """
    Repeatedly prompts the user until they enter a valid command.

    Returns:
        str: The first valid command entered by the user (lowercase)
    """
    while True:
        command = input(ENTER_COMMAND_PROMPT)
        if check_input(command):
            return command.lower()
        else:
            print(INVALID_FORMAT_MESSAGE)

def has_unbroken_line(board: list[list[str]], piece: str) -> bool:
    """
    Returns True if the board contains an unbroken line of the specified piece at least 4 long.

    Args:
        board (list[list[str]]): The game board
        piece (str): The piece to check for

    Returns:
        bool: True if unbroken line exists, False otherwise
    """
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    # Check horizontal lines
    for row in range(rows):
        count = 0
        for col in range(cols):
            if board[row][col] == piece:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0

    # Check vertical lines
    for col in range(cols):
        count = 0
        for row in range(rows):
            if board[row][col] == piece:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0

    # Check diagonal lines (top-left to bottom-right)
    # Start from each position in first row and first column
    for start_row in range(rows):
        count = 0
        row, col = start_row, 0
        while row < rows and col < cols:
            if board[row][col] == piece:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
            row += 1
            col += 1

    for start_col in range(1, cols):
        count = 0
        row, col = 0, start_col
        while row < rows and col < cols:
            if board[row][col] == piece:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
            row += 1
            col += 1

    # Check diagonal lines (top-right to bottom-left)
    # Start from each position in first row and last column
    for start_row in range(rows):
        count = 0
        row, col = start_row, cols - 1
        while row < rows and col >= 0:
            if board[row][col] == piece:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
            row += 1
            col -= 1

    for start_col in range(cols - 2, -1, -1):
        count = 0
        row, col = 0, start_col
        while row < rows and col >= 0:
            if board[row][col] == piece:
                count += 1
                if count >= 4:
                    return True
            else:
                count = 0
            row += 1
            col -= 1

    return False

def has_square(board: list[list[str]], piece: str) -> bool:
    """
    Returns True if the board contains a complete 2x2 square of the specified piece.

    Args:
        board (list[list[str]]): The game board
        piece (str): The piece to check for

    Returns:
        bool: True if 2x2 square exists, False otherwise
    """
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0

    # Check all possible 2x2 squares
    for row in range(rows - 1):
        for col in range(cols - 1):
            if (board[row][col] == piece and
                board[row][col + 1] == piece and
                board[row + 1][col] == piece and
                board[row + 1][col + 1] == piece):
                return True

    return False

def check_win(board: list[list[str]]) -> str:
    """
    Returns the piece of the player who has won, or empty string if no winner.

    Args:
        board (list[list[str]]): The game board

    Returns:
        str: The winning piece, or empty string if no winner
    """
    # Check Player 1 first (takes precedence)
    if has_unbroken_line(board, PLAYER_1_PIECE) or has_square(board, PLAYER_1_PIECE):
        return PLAYER_1_PIECE

    # Check Player 2
    if has_unbroken_line(board, PLAYER_2_PIECE) or has_square(board, PLAYER_2_PIECE):
        return PLAYER_2_PIECE

    # No winner
    return EMPTY

def play_game() -> None:
    """
    Coordinates gameplay of a single game of Teeko from start to finish.
    """
    # Initialize game state
    board = create_empty_board(BOARD_SIZE)
    player1_pieces_left = NUM_PLAYER_PIECES
    player2_pieces_left = NUM_PLAYER_PIECES
    current_player = 1

    print(WELCOME_MESSAGE)

    while True:
        # Display current board state
        print()
        display_board(board)
        print()

        # Determine current player info
        if current_player == 1:
            current_piece = PLAYER_1_PIECE
            current_display = PLAYER_1_DISPLAY
            pieces_left = player1_pieces_left
        else:
            current_piece = PLAYER_2_PIECE
            current_display = PLAYER_2_DISPLAY
            pieces_left = player2_pieces_left

        # Display turn message
        message = turn_message(pieces_left)
        print(current_display + message)

        # Get and process command
        command = get_command()

        if command == "h":
            print(HELP_MESSAGE)
            continue
        elif command == "q":
            break
        elif command[0] == "p":
            # Place piece command
            if pieces_left == 0:
                print(ALREADY_PLACED_MESSAGE)
                continue

            row = int(command[1])
            col = int(command[2])

            if add_piece(board, current_piece, (row, col)):
                if current_player == 1:
                    player1_pieces_left -= 1
                else:
                    player2_pieces_left -= 1

                # Check for win
                winner = check_win(board)
                if winner != EMPTY:
                    print()
                    display_board(board)
                    print()
                    print(current_display + VICTORY_MESSAGE)
                    break

                # Switch players
                current_player = 2 if current_player == 1 else 1
        elif command[0] == "m":
            # Move piece command
            if pieces_left > 0:
                print(MUST_PLACE_MESSAGE)
                continue

            from_row = int(command[1])
            from_col = int(command[2])
            to_row = int(command[3])
            to_col = int(command[4])

            if move_piece(board, current_piece, (from_row, from_col), (to_row, to_col)):
                # Check for win
                winner = check_win(board)
                if winner != EMPTY:
                    print()
                    display_board(board)
                    print()
                    print(current_display + VICTORY_MESSAGE)
                    break

                # Switch players
                current_player = 2 if current_player == 1 else 1

def main() -> None:
    """
    Main function that handles the game loop and replay functionality.
    """
    while True:
        play_game()

        # Ask if user wants to play again
        play_again = input(AGAIN_PROMPT)
        if play_again.lower() != "y":
            break

if __name__ == "__main__":
    main()