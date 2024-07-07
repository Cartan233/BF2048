import pygame
import sys
from pygame.locals import *
from game_2048 import new_game, move_left, move_right, move_up, move_down, add_new_tile, get_current_state

# Initialize Pygame
pygame.init()

# Constants
TILE_SIZE = 100
TILE_MARGIN = 20
BOARD_SIZE = 4
SCREEN_SIZE = BOARD_SIZE * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}

# Set up the display
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption('2048')

def draw_tile(value, x, y):
    font = pygame.font.Font(None, 40)
    text = font.render(str(value), True, (0, 0, 0)) if value > 0 else None
    color = TILE_COLORS[value]
    rect = pygame.Rect(x * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN, y * (TILE_SIZE + TILE_MARGIN) + TILE_MARGIN, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, color, rect)
    if text:
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

def draw_board(board):
    screen.fill(BACKGROUND_COLOR)
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            draw_tile(board[y][x], x, y)
    pygame.display.update()

def main():
    board = new_game(BOARD_SIZE)
    draw_board(board)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # print(f"Key pressed: {pygame.key.name(event.key)}")  # This will print the name of the key pressed.
                    running = False
                elif event.key in (K_UP, K_w):
                    # print(f"Key pressed: {pygame.key.name(event.key)}")  # This will print the name of the key pressed.
                    # print("Before move:", board)
                    board = move_up(board)
                    # print("After move:", board)
                elif event.key in (K_DOWN, K_s):
                    # print(f"Key pressed: {pygame.key.name(event.key)}")  # This will print the name of the key pressed.
                    # print("Before move:", board)
                    board = move_down(board)
                    # print("After move:", board)
                elif event.key in (K_LEFT, K_a):
                    # print(f"Key pressed: {pygame.key.name(event.key)}")  # This will print the name of the key pressed.
                    # print("Before move:", board)
                    board = move_left(board)
                    # print("After move:", board)
                elif event.key in (K_RIGHT, K_d):
                    # print(f"Key pressed: {pygame.key.name(event.key)}")  # This will print the name of the key pressed.
                    # print("Before move:", board)
                    board = move_right(board)
                    # print("After move:", board)
                else:
                    print("Invalid key pressed. Please use arrow keys or WASD.")
                    continue # Wait for another key input

                add_new_tile(board)
                draw_board(board)
                state = get_current_state(board)
                if state == 'WON' or state == 'LOST':
                    print(state)
                    pygame.time.wait(2000)
                    running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()