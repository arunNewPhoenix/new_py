import random

# Constants for game elements
RABBIT = 'r'
RABBIT_HOLE = 'O'
CARROT = 'c'
STONE = '-'

# Function to generate a random game map
def generate_map(size, num_carrots, num_holes):
    # Initialize an empty grid filled with spaces
    grid = [[' ' for _ in range(size)] for _ in range(size)]
    
    # Place rabbit
    rabbit_x, rabbit_y = random.randint(0, size - 1), random.randint(0, size - 1)
    grid[rabbit_x][rabbit_y] = RABBIT
    
    # Place rabbit holes
    rabbit_holes = []
    for _ in range(num_holes):
        hole_x, hole_y = random.randint(0, size - 1), random.randint(0, size - 1)
        while grid[hole_x][hole_y] != ' ':
            hole_x, hole_y = random.randint(0, size - 1), random.randint(0, size - 1)
        grid[hole_x][hole_y] = RABBIT_HOLE
        rabbit_holes.append((hole_x, hole_y))
    
    # Place carrots
    for _ in range(num_carrots):
        carrot_x, carrot_y = random.randint(0, size - 1), random.randint(0, size - 1)
        while grid[carrot_x][carrot_y] != ' ':
            carrot_x, carrot_y = random.randint(0, size - 1), random.randint(0, size - 1)
        grid[carrot_x][carrot_y] = CARROT
    
    # Place stones in vacant locations
    for x in range(size):
        for y in range(size):
            if grid[x][y] == ' ' and (x, y) not in rabbit_holes:
                grid[x][y] = STONE
    
    return grid, rabbit_x, rabbit_y, rabbit_holes


# Function to display the game map
def display_map(grid):
    for row in grid:
        print(' '.join(row))

# Function to check if the rabbit can move to a given position
def can_move(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid) and grid[x][y] != STONE

# Main game loop
def main():
    size = int(input("Enter the size of the game map: "))
    num_carrots = int(input("Enter the number of carrots: "))
    num_holes = int(input("Enter the number of rabbit holes: "))
    
    grid, rabbit_x, rabbit_y, rabbit_holes = generate_map(size, num_carrots, num_holes)
    carrots_collected = 0
    
    while True:
        # Display the game map
        display_map(grid)
        
        # Check if the game is won
        if carrots_collected > 0 and grid[rabbit_x][rabbit_y] == RABBIT_HOLE:
            print("Congratulations! You won the game!")
            break
        
        move = input("Enter move (a/d/w/s/j/p/q for quit): ").lower()
        
        if move == 'q':
            print("Game Over! You quit the game.")
            break
        
        new_x, new_y = rabbit_x, rabbit_y
        
        # Handle movement and actions
        if move == 'a':
            new_y -= 1
        elif move == 'd':
            new_y += 1
        elif move == 'w':
            new_x -= 1
        elif move == 's':
            new_x += 1
        elif move == 'j':
            # Jump over rabbit hole
            if grid[new_x][new_y] == RABBIT_HOLE:
                if rabbit_x < new_x:
                    new_x += 1
                elif rabbit_x > new_x:
                    new_x -= 1
                elif rabbit_y < new_y:
                    new_y += 1
                else:
                    new_y -= 1
        elif move == 'p':
            # Pick up carrot
            if grid[new_x][new_y] == CARROT:
                grid[new_x][new_y] = ' '
                carrots_collected += 1
                print("Carrot picked up!")
        
        # Check if the new position is valid
        if can_move(grid, new_x, new_y):
            grid[rabbit_x][rabbit_y] = ' '
            grid[new_x][new_y] = RABBIT
            rabbit_x, rabbit_y = new_x, new_y
        else:
            print("Invalid move! Try again.")

if __name__ == "__main__":
    main()

  