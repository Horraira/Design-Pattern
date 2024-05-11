import tkinter as tk
from tkinter import messagebox
import json
import re


def create_window(title, is_root=False, width=0, height=0):
    window = tk.Tk() if is_root else tk.Toplevel(root)
    window.title(title)
    window.configure(bg="#3498db")
    window.resizable(False, False)

    if width and height:
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x_coordinate = int((screen_width - width) / 2)
        y_coordinate = int((screen_height - height) / 2)
        window.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

    return window


def read_user_info_file():
    try:
        with open("user_info.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found.")
        return None
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Error decoding JSON.")
        return None


def check_credentials(username, password, user_info, user_type):
    try:
        for user in user_info[user_type]:
            if user["username"] == username and user["password"] == password:
                return True
        return False
    except KeyError:
        messagebox.showerror("Error", "Invalid data format.")
        return False


def validate_password(password):
    try:
        return re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&# ()])[A-Za-z\d@$!%*?&# ()]{8,}$", password)
    except re.error:
        messagebox.showerror("Error", "Invalid regex pattern.")
        return False


def admin_login():
    try:
        admin_window = create_window("Administrator", width=700, height=400)
        admin_details_label = tk.Label(admin_window, text="Enter Administrator Details:", font=("Roboto", 16),
                                       bg="#3498db", fg="white")
        admin_details_label.pack(pady=20)
        username_label = tk.Label(admin_window, text="Username:", font=("Roboto", 12), bg="#3498db", fg="white")
        username_label.pack(padx=10, pady=5)
        username_entry = tk.Entry(admin_window, font=("Roboto", 12))
        username_entry.pack(pady=5, padx=10)
        password_label = tk.Label(admin_window, text="Password:", font=("Roboto", 12), bg="#3498db", fg="white")
        password_label.pack(pady=10, padx=5)
        password_entry = tk.Entry(admin_window, font=("Roboto", 12), show="*")
        password_entry.pack(pady=5, padx=10)
        error_label = tk.Label(admin_window, text="", font=("Roboto", 10), bg="#3498db", fg="red")
        error_label.pack()
        login_button = tk.Button(admin_window, text="Login", font=("Roboto", 12, "bold"), bg="#2ecc71", fg="white",
                                 width=15,
                                 command=lambda: switch_to_admin_panel(admin_window) if check_credentials(
                                     username_entry.get(), password_entry.get(), user_info,
                                     "administrators") else error_label.config(text="Invalid credentials"))
        login_button.pack(pady=25)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def switch_to_admin_panel(admin_window):
    try:
        admin_window.destroy()
        admin_panel = create_window("Administrator Panel", width=700, height=700)
        enter_user_details_label = tk.Label(admin_panel, text="Enter User Details:", font=("Roboto", 16), bg="#3498db",
                                            fg="white")
        enter_user_details_label.pack(pady=20)
        new_username_label = tk.Label(admin_panel, text="Username:", font=("Roboto", 12), bg="#3498db", fg="white")
        new_username_label.pack(padx=10, pady=5)
        new_username_entry = tk.Entry(admin_panel, font=("Roboto", 12))
        new_username_entry.pack(pady=5, padx=10)
        new_password_label = tk.Label(admin_panel, text="Password:", font=("Roboto", 12), bg="#3498db", fg="white")
        new_password_label.pack(pady=10, padx=5)
        new_password_entry = tk.Entry(admin_panel, font=("Roboto", 12), show="*")
        new_password_entry.pack(pady=5, padx=10)
        action_label = tk.Label(admin_panel, text="What do you wish to do?", font=("Roboto", 16), bg="#3498db",
                                fg="white")
        action_label.pack(pady=20)
        selection = tk.IntVar()
        create_radio = tk.Radiobutton(admin_panel, text="Create User Account", font=("Roboto", 14), bg="#3498db",
                                      variable=selection, value=1, cursor='arrow')
        create_radio.pack(pady=5)
        remove_radio = tk.Radiobutton(admin_panel, text="Remove User Account", font=("Roboto", 14), bg="#3498db",
                                      variable=selection, value=2, cursor='arrow')
        remove_radio.pack(pady=5)
        error2_label = tk.Label(admin_panel, text="", font=("Roboto", 10), bg="#3498db", fg="red")
        submit_button_admin_panel = tk.Button(admin_panel, text="Submit", font=("Roboto", 14), bg="#2ecc71", fg="white",
                                              command=lambda: submit_action(new_username_entry.get(),
                                                                            new_password_entry.get(), selection,
                                                                            error2_label, success_label))
        submit_button_admin_panel.pack(pady=10)
        error2_label.pack()
        success_label = tk.Label(admin_panel, text="", font=("Roboto", 12), bg="#3498db", fg="green")
        success_label.pack()
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to start the game
def start_game(player1_username, player1_password, player2_username,
               player2_password, error_label, player_login_window):
    try:
        if (not player1_username or
                not player1_password or
                not player2_username or
                not player2_password):
            error_label.config(text="Error: Please fill in all fields", fg="red")
            return
        if (check_credentials(player1_username, player1_password, user_info, "players") and
                check_credentials(player2_username, player2_password, user_info, "players")):
            switch_to_connect4_board(player1_username, player2_username, player_login_window)
        else:
            error_label.config(text="One or more of the players' credentials are invalid", fg="red")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def switch_to_player_login():
    try:
        player_login_window = create_window("Login For Connect 4 Game", width=700, height=600)
        login_label = tk.Label(player_login_window, text="Login to the Connect 4 Game",
                               font=("Roboto", 16), bg="#3498db", fg="white")
        login_label.pack(pady=20)
        player1_label = tk.Label(player_login_window, text="Player 1:", font=("Roboto", 14),
                                 bg="#3498db", fg="white")
        player1_label.pack(pady=10)
        player1_username_label = tk.Label(player_login_window, text="Username:",
                                          font=("Roboto", 12), bg="#3498db", fg="white")
        player1_username_label.pack(pady=5)
        player1_username_entry = tk.Entry(player_login_window, font=("Roboto", 12))
        player1_username_entry.pack(pady=5)
        player1_password_label = tk.Label(player_login_window, text="Password:",
                                          font=("Roboto", 12), bg="#3498db", fg="white")
        player1_password_label.pack(pady=10)
        player1_password_entry = tk.Entry(player_login_window, font=("Roboto", 12), show="*")
        player1_password_entry.pack(pady=5)
        player2_label = tk.Label(player_login_window, text="Player 2:", font=("Roboto", 14),
                                 bg="#3498db", fg="white")
        player2_label.pack(pady=10)
        player2_username_label = tk.Label(player_login_window, text="Username:",
                                          font=("Roboto", 12, "bold"), bg="#3498db", fg="white")
        player2_username_label.pack(pady=5)
        player2_username_entry = tk.Entry(player_login_window, font=("Roboto", 12))
        player2_username_entry.pack(pady=5)
        player2_password_label = tk.Label(player_login_window, text="Password:",
                                          font=("Roboto", 12, "bold"), bg="#3498db", fg="white")
        player2_password_label.pack(pady=10)
        player2_password_entry = tk.Entry(player_login_window, font=("Roboto", 12), show="*")
        player2_password_entry.pack(pady=5)
        start_button = tk.Button(player_login_window, text="Start", font=("Roboto", 12, "bold"),
                                 bg="#2ecc71", fg="white",
                                 width=15, command=lambda: start_game(player1_username_entry.get(),
                                                                      player1_password_entry.get(),
                                                                      player2_username_entry.get(),
                                                                      player2_password_entry.get(),
                                                                      error_label, player_login_window))
        start_button.pack(pady=25)
        error_label = tk.Label(player_login_window, text="", font=("Roboto", 10), bg="#3498db", fg="red")
        error_label.pack()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def on_submit():
    try:
        if selection.get() == 1:
            admin_login()
        elif selection.get() == 2:
            switch_to_player_login()
    except Exception as e:
        messagebox.showerror("Error", str(e))


def submit_action(username, password, selection, error_label, success_label):
    try:
        if not username or not password:
            error_label.config(text="Error: Please fill in all fields", fg="red")
            return

        if selection.get() == 1:  # Create User Account
            if not validate_password(password):
                error_label.config(text=("Error: Password must be at least:\n"
                                         "8 characters long\n"
                                         "Contain at least one lowercase and uppercase letter\n"
                                         "One digit and one special character (@$!%*?&# ())."), fg="red")
                return

        if selection.get() == 1:  # Create User Account
            for player in user_info["players"]:
                if player["username"] == username:
                    error_label.config(text=f"Error: User '{username}' already exists", fg="red")
                    return
            user_info["players"].append({"username": username, "password": password})
            with open("user_info.txt", "w") as file:
                json.dump(user_info, file, indent=4)
            success_label.config(text="User account created successfully", fg="green")
        elif selection.get() == 2:  # Remove User Account
            for player in user_info["players"]:
                if player["username"] == username:
                    user_info["players"].remove(player)
                    with open("user_info.txt", "w") as file:
                        json.dump(user_info, file, indent=4)
                    success_label.config(text="User account removed successfully", fg="green")
                    return
            error_label.config(text=f"Error: User '{username}' not found", fg="red")
        else:
            error_label.config(text="Error: Please select an action", fg="red")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Function to intercept window closing event
def on_closing():
    if messagebox.askokcancel("Quit", "Please select one of the options to quit or restart the game."):
        pass  # Do nothing


def switch_to_connect4_board(player1_username,
                             player2_username, player_login_window):
    try:
        connect4_window = create_window("Connect 4 Game",
                                        width=700, height=700)
        player_login_window.destroy()
        # connect4_window.overrideredirect(True)

        # Create the Connect 4 board screen using a Canvas
        connect4_board = tk.Canvas(connect4_window,
                                   bg="#a08c64",
                                   width=700, height=700)
        connect4_board.pack()

        # Draw the circles for the Connect 4 board
        board_height = 6
        board_width = 7
        circle_radius = 40
        disc_color = "#d7d7d7"
        board = [[None] * board_width for _ in range(board_height)]

        # Calculate the distance between circles
        x_distance = 700 // board_width
        y_distance = 700 // board_height

        # Variable to keep track of whose turn it is (Player 1 starts)
        current_player = 1

        for i in range(board_height):
            for j in range(board_width):
                # Calculate the center of each circle
                x_center = (j * x_distance) + (x_distance // 2)
                y_center = (i * y_distance) + (y_distance // 2)
                # Draw the circle
                circle = connect4_board.create_oval(x_center - circle_radius,
                                                    y_center - circle_radius,
                                                    x_center + circle_radius, y_center + circle_radius,
                                                    fill=disc_color)
                # Store the circle in the board
                board[i][j] = circle

        def check_circle_occupancy(circle):
            if connect4_board.itemcget(circle, "fill") != "red" and connect4_board.itemcget(circle, "fill") != "yellow":
                return False
            return True

        def check_win_conditions(board, player):
            # Check horizontal
            for row in board:
                for i in range(len(row) - 3):
                    if all(connect4_board.itemcget(circle, "fill") == player for circle in row[i:i + 4]):
                        return True

            # Check vertical
            for j in range(len(board[0])):
                for i in range(len(board) - 3):
                    if all(connect4_board.itemcget(board[i + k][j], "fill") == player for k in range(4)):
                        return True

            # Check diagonals
            for i in range(len(board) - 3):
                for j in range(len(board[0]) - 3):
                    if all(connect4_board.itemcget(board[i + k][j + k], "fill") == player for k in range(4)):
                        return True
                    if all(connect4_board.itemcget(board[i + k][j + 3 - k], "fill") == player for k in range(4)):
                        return True

            return False

        def close_windows(*windows):
            for window in windows:
                window.destroy()

        def show_winner(player):
            winner_dialog = create_window("Winner", width=300, height=250)
            winner_dialog.protocol("WM_DELETE_WINDOW", on_closing)  # Intercept window closing event
            winner_dialog.grab_set()
            winner_label = tk.Label(winner_dialog, text=f"{player} wins!", font=("Roboto", 16),
                                    bg="#3498db", fg="white")
            winner_label.pack(pady=20)
            play_again_button = tk.Button(winner_dialog, text="Reset", font=("Roboto", 12),
                                          bg="#2ecc71", fg="white", command=lambda: reset_board(winner_dialog))
            play_again_button.pack(pady=10)
            exit_button = tk.Button(winner_dialog, text="Exit", font=("Roboto", 12),
                                    bg="#e74c3c", fg="white",
                                    command=lambda: close_windows(winner_dialog, connect4_window))
            exit_button.pack(pady=10)

        def check_draw_condition():
            # Check if all circles are occupied
            for grids in board:
                for disc in grids:
                    if not check_circle_occupancy(disc):
                        return False
            return True

        def show_draw_message():
            draw_dialog = create_window("Draw", width=300, height=250)
            draw_dialog.protocol("WM_DELETE_WINDOW", on_closing)
            draw_dialog.grab_set()
            draw_label = tk.Label(draw_dialog, text="It's a draw!", font=("Roboto", 16),
                                  bg="#3498db", fg="white")
            draw_label.pack(pady=20)
            play_again_button = tk.Button(draw_dialog, text="Reset", font=("Roboto", 12),
                                          bg="#2ecc71", fg="white", command=lambda: reset_board(draw_dialog))
            play_again_button.pack(pady=10)
            exit_button = tk.Button(draw_dialog, text="Exit", font=("Roboto", 12),
                                    bg="#e74c3c", fg="white",
                                    command=lambda: close_windows(draw_dialog, connect4_window))
            exit_button.pack(pady=10)

        def reset_board(dialog):
            for grids in board:
                for disc in grids:
                    connect4_board.itemconfig(disc, fill=disc_color)
            nonlocal current_player
            current_player = 1
            dialog.destroy()

        def on_circle_hover(event):
            nonlocal current_player
            # Get the circle item under the mouse pointer
            circle = connect4_board.find_withtag("current")[0]
            # Change the color of the circle based on the current player
            if not check_circle_occupancy(circle):
                if current_player == 1:
                    connect4_board.itemconfig(circle, fill="#ffcccc")  # Light shade of red for Player 1
                else:
                    connect4_board.itemconfig(circle, fill="#ffff99")  # Light shade of yellow for Player 2

        def on_circle_leave(event):
            # Get the circle item under the mouse pointer
            circle = connect4_board.find_withtag("current")[0]
            # Change the color of the circle back to its original color
            if not check_circle_occupancy(circle):
                connect4_board.itemconfig(circle, fill=disc_color)

        def on_circle_click(event):
            nonlocal current_player
            # Get the circle item under the mouse pointer
            circle = connect4_board.find_withtag("current")[0]
            # Get the column index of the clicked circle
            try:
                column = board[0].index(circle)
            except ValueError:
                return  # Do nothing

            # Check from bottom to top in the column to find the lowest available position
            row = len(board) - 1
            while row >= 0:
                if not check_circle_occupancy(board[row][column]):
                    # Change the color of the circle based on the current player
                    if current_player == 1:
                        connect4_board.itemconfig(board[row][column], fill="red")  # Red for Player 1
                        if check_win_conditions(board, "red"):
                            show_winner(player1_username)
                        elif check_draw_condition():
                            show_draw_message()
                        else:
                            current_player = 2  # Switch to Player 2's turn
                    else:
                        connect4_board.itemconfig(board[row][column], fill="yellow")  # Yellow for Player 2
                        if check_win_conditions(board, "yellow"):
                            show_winner(player2_username)
                        elif check_draw_condition():
                            show_draw_message()
                        else:
                            current_player = 1  # Switch to Player 1's turn
                    break
                row -= 1

        # Bind the events to the circles
        for row in board:
            for circle in row:
                connect4_board.tag_bind(circle, "<Enter>", on_circle_hover)
                connect4_board.tag_bind(circle, "<Leave>", on_circle_leave)
                connect4_board.tag_bind(circle, "<Button-1>", on_circle_click)
    except Exception as e:
        messagebox.showerror("Error", str(e))


try:
    # Create the main window
    root = create_window("Connect 4 Game", is_root=True, width=700, height=400)

    user_info = read_user_info_file()

    # Create a header label
    header_label = tk.Label(root, text="Connect 4 Game", font=("Roboto", 24), bg="#3498db", fg="white")
    header_label.pack(pady=20)

    # Create a label for the selection prompt
    prompt_label = tk.Label(root, text="Select how you wish to enter:", font=("Roboto", 16), bg="#3498db", fg="white")
    prompt_label.pack()

    # Radio button selection variable
    selection = tk.IntVar()

    # Create radio buttons for Administrator and Player
    admin_radio = tk.Radiobutton(root, text="Administrator", font=("Roboto", 14), bg="#3498db", variable=selection,
                                 value=1)
    admin_radio.pack(pady=5)

    player_radio = tk.Radiobutton(root, text="Player", font=("Roboto", 14), bg="#3498db", variable=selection, value=2)
    player_radio.pack(pady=5)

    # Create submit button
    submit_button = tk.Button(root, text="Submit", font=("Roboto", 14), command=on_submit, bg="#2ecc71", fg="white")
    submit_button.pack(pady=10)

    # Run the Tkinter event loop
    root.mainloop()
except Exception as e:
    messagebox.showerror("Error", str(e))
