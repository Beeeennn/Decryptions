import pygame
import sys

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().replace('\n', '').replace(' ', '')

def display_grid(screen, grid, cell_size, font, selected_row):
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            text = font.render(char, True, (0, 0, 0))
            x, y = col_idx * cell_size, row_idx * cell_size
            if row_idx == selected_row:
                pygame.draw.rect(screen, (220, 220, 220), (x, y, cell_size, cell_size))
            screen.blit(text, (x, y))

def save_grid_to_file(grid, file_path):
    with open(file_path, 'w') as file:
        for row in grid:
            file.write(''.join(row) + '\n')

def main():
    # Initialize Pygame
    pygame.init()
    screen_width = 1200
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Cipher Grid")

    # Load and process the text
    input_file_path = 'codedmsg.txt'  # Replace with your file path
    output_file_path = 'output.txt'  # File where the grid will be saved
    text = read_file(input_file_path)
    columns = int(560/7)  # Adjust as needed
    grid = [list(text[i:i+columns]) for i in range(0, len(text), columns)]

    cell_size = 15  # Adjust as needed
    font = pygame.font.SysFont(None, 24)
    selected_row = None

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                selected_row = y // cell_size
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and selected_row is not None and selected_row > 0:
                    grid[selected_row], grid[selected_row - 1] = grid[selected_row - 1], grid[selected_row]
                    selected_row -= 1
                elif event.key == pygame.K_DOWN and selected_row is not None and selected_row < len(grid) - 1:
                    grid[selected_row], grid[selected_row + 1] = grid[selected_row + 1], grid[selected_row]
                    selected_row += 1
                elif event.key == pygame.K_s:
                    save_grid_to_file(grid, output_file_path)
                    print("Grid saved to", output_file_path)

        screen.fill((255, 255, 255))
        display_grid(screen, grid, cell_size, font, selected_row)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()