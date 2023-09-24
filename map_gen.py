import random

class CellularAutomataMap:
    """
    A class to generate maps using cellular automata.
    
    Attributes:
        width (int): The width of the map.
        height (int): The height of the map.
        fill_probability (float): The initial probability of a cell being filled.
        iterations (int): The number of cellular automata iterations.
        randomize_initial_map (bool): Whether to randomize the initial map completely.
    """

    def __init__(self, width, height, fill_probability, iterations, randomize_initial_map=False):
        """
        Initializes the CellularAutomataMap instance.

        Args:
            width (int): The width of the map.
            height (int): The height of the map.
            fill_probability (float): The initial probability of a cell being filled.
            iterations (int): The number of cellular automata iterations.
            randomize_initial_map (bool): Whether to randomize the initial map completely.
        """
        self.width = width
        self.height = height
        self.map = [[False for _ in range(height)] for _ in range(width)]

        # Initialize the map with random cells or completely randomize it
        if randomize_initial_map:
            for x in range(width):
                for y in range(height):
                    self.map[x][y] = random.random() < 0.5
        else:
            for x in range(width):
                for y in range(height):
                    self.map[x][y] = random.random() < fill_probability

        # Perform cellular automata iterations
        for _ in range(iterations):
            new_map = [[False for _ in range(height)] for _ in range(width)]

            for x in range(width):
                for y in range(height):
                    neighbors = self.count_alive_neighbors(x, y)

                    # Apply cellular automata rules with some randomness
                    random_factor = random.uniform(0.2, 0.8)
                    if self.map[x][y]:
                        new_map[x][y] = neighbors >= 4
                    else:
                        new_map[x][y] = neighbors >= 5 and random.random() < random_factor

            # Update the map
            self.map = new_map

    def count_alive_neighbors(self, x, y):
        """
        Counts the number of alive (filled) neighbors for a cell.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            int: The count of alive neighbors.
        """
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbor_x = x + i
                neighbor_y = y + j

                if i == 0 and j == 0:
                    continue  # Skip the current cell
                if (
                    neighbor_x < 0
                    or neighbor_x >= self.width
                    or neighbor_y < 0
                    or neighbor_y >= self.height
                ):
                    # Out of bounds cells are considered as filled
                    count += 1
                elif self.map[neighbor_x][neighbor_y]:
                    count += 1
        return count

    def get_map(self):
        """
        Gets the generated map.

        Returns:
            list[list[bool]]: The generated map.
        """
        return self.map

def print_map(map):
    """
    Prints the generated map.

    Args:
        map (list[list[bool]]): The generated map.
    """
    for y in range(len(map[0])):
        for x in range(len(map)):
            print("#" if map[x][y] else ".", end="")
        print()

if __name__ == "__main__":
    width = 50
    height = 25
    fill_probability = 0.45
    iterations = 5
    randomize_initial_map = True  # Set to True to randomize the initial map completely

    cellular_automata_map = CellularAutomataMap(
        width, height, fill_probability, iterations, randomize_initial_map
    )
    map = cellular_automata_map.get_map()

    print_map(map)
