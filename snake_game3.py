import curses
import random
import time

# Initialize the game window
def setup_window():
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)  # (height, width, start_y, start_x)
    win.keypad(True)
    curses.noecho()
    curses.curs_set(False)
    win.border(0)
    return win

# Main function for the snake game
def snake_game():
    while True:  # Loop to allow restart
        win = setup_window()

        # Snake initial position and body
        snake = [[10, 15], [10, 14], [10, 13]]  # (y, x) coordinates
        food = [random.randint(1, 18), random.randint(1, 58)]
        win.addch(food[0], food[1], '*')  # Food symbol

        key = curses.KEY_RIGHT  # Initial movement direction
        score = 0
        speed = 100  # Initial speed

        while True:
            win.addstr(0, 2, f" Score: {score}  Level: {score//5 + 1} ")  # Display score & level
            win.border(0)

            # Detect collision with food
            if snake[0] == food:
                score += 1
                speed = max(30, 100 - (score * 2))  # Increase speed with score
                food = [random.randint(1, 18), random.randint(1, 58)]
                win.addch(food[0], food[1], '*')  # New food
            else:
                snake.pop()  # Remove last segment

            # Get user input for movement
            new_key = win.getch()
            key = key if new_key == -1 else new_key

            # Change snake direction
            if key == curses.KEY_UP and snake[1] != [snake[0][0] - 1, snake[0][1]]:
                new_head = [snake[0][0] - 1, snake[0][1]]
            elif key == curses.KEY_DOWN and snake[1] != [snake[0][0] + 1, snake[0][1]]:
                new_head = [snake[0][0] + 1, snake[0][1]]
            elif key == curses.KEY_LEFT and snake[1] != [snake[0][0], snake[0][1] - 1]:
                new_head = [snake[0][0], snake[0][1] - 1]
            elif key == curses.KEY_RIGHT and snake[1] != [snake[0][0], snake[0][1] + 1]:
                new_head = [snake[0][0], snake[0][1] + 1]
            else:
                new_head = snake[0]  # Keep moving in the same direction

            # Check for collisions (Wall or Self)
            if new_head in snake or new_head[0] in [0, 19] or new_head[1] in [0, 59]:
                break  # Game over

            # Move the snake
            snake.insert(0, new_head)
            win.addch(snake[0][0], snake[0][1], '#')  # Snake body
            win.addch(snake[-1][0], snake[-1][1], ' ')  # Remove tail
            win.timeout(speed)  # Adjust speed dynamically

        curses.endwin()
        print(f"Game Over! Your final score was: {score}")

        # Restart option
        restart = input("Do you want to play again? (y/n): ").strip().lower()
        if restart != 'y':
            break  # Exit game loop

# Run the game
snake_game()