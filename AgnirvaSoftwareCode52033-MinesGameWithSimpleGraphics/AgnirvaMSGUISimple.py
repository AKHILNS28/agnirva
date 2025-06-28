import tkinter as tk
import random

def Agnirva_create_board(Agnirva_size, Agnirva_num_mines):
    """Create the game board with mines placed randomly.(Commented by Agnirva.com)"""
    Agnirva_board = [[0 for _ in range(Agnirva_size)] for _ in range(Agnirva_size)]  # Initialize board with zeros (Commented by Agnirva.com)
    Agnirva_mine_positions = set()

    while len(Agnirva_mine_positions) < Agnirva_num_mines:
        Agnirva_row = random.randint(0, Agnirva_size - 1)  # Random row for mine placement (Commented by Agnirva.com)
        Agnirva_col = random.randint(0, Agnirva_size - 1)  # Random column for mine placement (Commented by Agnirva.com)
        Agnirva_mine_positions.add((Agnirva_row, Agnirva_col))  # Add mine position to set (Commented by Agnirva.com)

    for Agnirva_row, Agnirva_col in Agnirva_mine_positions:
        Agnirva_board[Agnirva_row][Agnirva_col] = 'M'  # Place mine on the board (Commented by Agnirva.com)
        for Agnirva_r in range(max(0, Agnirva_row - 1), min(Agnirva_size, Agnirva_row + 2)):
            for Agnirva_c in range(max(0, Agnirva_col - 1), min(Agnirva_size, Agnirva_col + 2)):
                if Agnirva_board[Agnirva_r][Agnirva_c] != 'M':
                    Agnirva_board[Agnirva_r][Agnirva_c] += 1  # Increment adjacent cell counters (Commented by Agnirva.com)

    return Agnirva_board, Agnirva_mine_positions

def Agnirva_reveal_cell(Agnirva_board, Agnirva_buttons, Agnirva_revealed, Agnirva_row, Agnirva_col):
    """Reveal a cell and handle recursive revealing if no adjacent mines.(Commented by Agnirva.com)"""
    if Agnirva_revealed[Agnirva_row][Agnirva_col]:  # Skip already revealed cells (Commented by Agnirva.com)
        return

    Agnirva_revealed[Agnirva_row][Agnirva_col] = True  # Mark the cell as revealed (Commented by Agnirva.com)
    if Agnirva_board[Agnirva_row][Agnirva_col] == 'M':
        Agnirva_buttons[Agnirva_row][Agnirva_col].config(text='M', bg='red', state='disabled')  # Display mine hit (Commented by Agnirva.com)
        Agnirva_end_game(False, Agnirva_buttons)  # End game due to mine hit (Commented by Agnirva.com)
        return

    Agnirva_buttons[Agnirva_row][Agnirva_col].config(text=str(Agnirva_board[Agnirva_row][Agnirva_col]) if Agnirva_board[Agnirva_row][Agnirva_col] > 0 else '', state='disabled')  # Show cell value (Commented by Agnirva.com)

    if Agnirva_board[Agnirva_row][Agnirva_col] == 0:  # If no adjacent mines, reveal surrounding cells (Commented by Agnirva.com)
        for Agnirva_r in range(max(0, Agnirva_row - 1), min(len(Agnirva_board), Agnirva_row + 2)):
            for Agnirva_c in range(max(0, Agnirva_col - 1), min(len(Agnirva_board), Agnirva_col + 2)):
                if not Agnirva_revealed[Agnirva_r][Agnirva_c]:
                    Agnirva_reveal_cell(Agnirva_board, Agnirva_buttons, Agnirva_revealed, Agnirva_r, Agnirva_c)  # Recursive reveal (Commented by Agnirva.com)

def Agnirva_end_game(Agnirva_won, Agnirva_buttons):
    """Handle the end of the game, displaying a message and disabling all buttons.(Commented by Agnirva.com)"""
    for Agnirva_row in Agnirva_buttons:
        for Agnirva_btn in Agnirva_row:
            Agnirva_btn.config(state='disabled')  # Disable all buttons (Commented by Agnirva.com)
    if Agnirva_won:
        print("Congratulations! You cleared the board.")  # Display win message (Commented by Agnirva.com)
    else:
        print("BOOM! You hit a mine! Game over.")  # Display game-over message (Commented by Agnirva.com)

def Agnirva_check_win(Agnirva_board, Agnirva_revealed, Agnirva_mine_positions):
    """Check if the player has won by revealing all non-mine cells.(Commented by Agnirva.com)"""
    Agnirva_size = len(Agnirva_board)
    return all(Agnirva_revealed[Agnirva_r][Agnirva_c] or (Agnirva_r, Agnirva_c) in Agnirva_mine_positions for Agnirva_r in range(Agnirva_size) for Agnirva_c in range(Agnirva_size))  # Verify win condition (Commented by Agnirva.com)

def Agnirva_on_cell_click(Agnirva_board, Agnirva_buttons, Agnirva_revealed, Agnirva_row, Agnirva_col, Agnirva_mine_positions):
    """Handle cell click events.(Commented by Agnirva.com)"""
    if Agnirva_revealed[Agnirva_row][Agnirva_col]:  # Ignore clicks on revealed cells (Commented by Agnirva.com)
        return

    Agnirva_reveal_cell(Agnirva_board, Agnirva_buttons, Agnirva_revealed, Agnirva_row, Agnirva_col)  # Reveal clicked cell (Commented by Agnirva.com)
    if Agnirva_check_win(Agnirva_board, Agnirva_revealed, Agnirva_mine_positions):
        Agnirva_end_game(True, Agnirva_buttons)  # End game with win message (Commented by Agnirva.com)

def Agnirva_create_gui(Agnirva_size, Agnirva_board, Agnirva_mine_positions):
    """Create the Minesweeper GUI.(Commented by Agnirva.com)"""
    Agnirva_root = tk.Tk()
    Agnirva_root.title("Minesweeper")  # Set window title (Commented by Agnirva.com)

    Agnirva_buttons = [[None for _ in range(Agnirva_size)] for _ in range(Agnirva_size)]  # Initialize button grid (Commented by Agnirva.com)
    Agnirva_revealed = [[False for _ in range(Agnirva_size)] for _ in range(Agnirva_size)]  # Track revealed cells (Commented by Agnirva.com)

    for Agnirva_row in range(Agnirva_size):
        for Agnirva_col in range(Agnirva_size):
            Agnirva_btn = tk.Button(Agnirva_root, text="", width=3, height=1,
                            command=lambda Agnirva_r=Agnirva_row, Agnirva_c=Agnirva_col: Agnirva_on_cell_click(Agnirva_board, Agnirva_buttons, Agnirva_revealed, Agnirva_r, Agnirva_c, Agnirva_mine_positions))  # Create button with click handler (Commented by Agnirva.com)
            Agnirva_btn.grid(row=Agnirva_row, column=Agnirva_col)  # Place button on grid (Commented by Agnirva.com)
            Agnirva_buttons[Agnirva_row][Agnirva_col] = Agnirva_btn  # Store button reference (Commented by Agnirva.com)

    Agnirva_root.mainloop()  # Start GUI loop (Commented by Agnirva.com)

def Agnirva_main():
    Agnirva_size = 8  # Board size (Commented by Agnirva.com)
    Agnirva_num_mines = 10  # Number of mines (Commented by Agnirva.com)
    Agnirva_board, Agnirva_mine_positions = Agnirva_create_board(Agnirva_size, Agnirva_num_mines)  # Create board and mine positions (Commented by Agnirva.com)
    Agnirva_create_gui(Agnirva_size, Agnirva_board, Agnirva_mine_positions)  # Launch GUI (Commented by Agnirva.com)

if __name__ == "__main__":
    Agnirva_main()
