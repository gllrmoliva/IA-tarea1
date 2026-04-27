from collections import deque
import argparse


def split_multiple_maps(large_data_string):
    """Divide un string largo con multiples mapas en varios cortos con información
    sobre un solo mapa."""
    tokens = deque(large_data_string.split())
    all_maps = []

    while tokens:
        try:
            if len(tokens) < 6:  # minimo 6 params
                break

            h = int(tokens[0])  # esto para contar tokens por mapa
            w = int(tokens[1])

            # total de un bloque 6(dimension, start, goal) + (h * w)
            total_elements = 6 + (h * w)

            if len(tokens) < total_elements:
                raise ValueError("ERROR: one map is incomplete")

            current_map_tokens = []
            for _ in range(total_elements):
                current_map_tokens.append(tokens.popleft())

            all_maps.append(" ".join(current_map_tokens))

        except ValueError as e:
            print(f"ERROR: {e}")
            break

    return all_maps


def parse_map(data_string):
    """Parsea un string con información sobre un solo mapa"""

    tokens = data_string.split()
    if len(tokens) < 6:
        raise ValueError("ERROR: string is incomplete")

    # parse info values
    height = int(tokens[0])
    width = int(tokens[1])
    start_row = int(tokens[2])
    start_col = int(tokens[3])
    goal_row = int(tokens[4])
    goal_col = int(tokens[5])

    # parse map
    map_data = tokens[6:]
    if len(map_data) < (height * width):
        raise ValueError("ERROR: unexpected map values")

    # create grid with all numbers
    grid = []
    for i in range(height):
        row = [int(x) for x in map_data[i * width:(i + 1) * width]]
        grid.append(row)

    return {
        "height": height,
        "width": width,
        "start": (start_row, start_col),
        "goal": (goal_row, goal_col),
        "map": grid
    }


def parse_args():
    """
    Parseo de argumentos para main
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("--agent", type=str, default="random",
                        choices=["player", "random", "bfs", "dfs"],
                        help="agente a ejecutar")

    parser.add_argument("--input", type=str,
                        help="archivo .txt con el mapa")

    parser.add_argument("--gui", action="store_true",
                        help="visualización gráfica")

    return parser.parse_args()
