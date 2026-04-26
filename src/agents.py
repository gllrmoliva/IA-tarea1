import random
from src.model import MazeGame
from collections import deque
from src.utils import parse_map
from pprint import pprint


class Node:
    def __init__(self, position, parent=None, ):
        self.position = position
        self.parent = parent

class Player:
    def __init__(self, game: MazeGame):
        self.game = game

    def go_up(self, ):
        posible_actions = self.game.get_possible_actions()
        pos = self.game.get_current_position()

        action = (pos[0] - 1 * self.game.get_current_step(), pos[1])
        
        if action in posible_actions:
            return action
        else:
            return pos

    def go_down(self, ):
        posible_actions = self.game.get_possible_actions()
        pos = self.game.get_current_position()

        action = (pos[0] + 1 * self.game.get_current_step(), pos[1])
        
        if action in posible_actions:
            return action
        else:
            return pos

    def go_left(self, ):
        posible_actions = self.game.get_possible_actions()
        pos = self.game.get_current_position()

        action = (pos[0], pos[1] - 1 * self.game.get_current_step())
        
        if action in posible_actions:
            return action
        else:
            return pos

    def go_right(self, ):
        posible_actions = self.game.get_possible_actions()
        pos = self.game.get_current_position()

        action = (pos[0], pos[1] + 1 * self.game.get_current_step())

        if action in posible_actions:
            return action
        else:
            return pos


class Agent:
    def __init__(self, game: MazeGame):
        self.game = game
        self.number_moves = 0

    def get_action(self,):
        pass

    def get_number_moves(self, ):
        return self.number_moves


class RandomAgent(Agent):
    def __init__(self, game: MazeGame):
        super().__init__(game)

    def get_action(self,):
        action = random.choice(self.game.get_possible_actions())
        self.number_moves += 1
        return action


class BFSAgent(Agent):
    def __init__(self, game):
        super().__init__(game)
        # precompute the path
        self.found_path = self.get_optimal_path()

    def get_action(self, ):
        if self.found_path:
            self.number_moves += 1
            return self.found_path.pop(0)
        else:
            return None

    def get_optimal_path(self, ):
        queue = deque()
        visited = set()
        traversal_order = []

        # surfing BFS until reach goal
        current_node = Node(position = self.game.get_start())
        queue.append(current_node)
        visited.add(current_node.position)

        while not self.game.is_goal(current_node.position):
            # esto nose si está bien
            if not queue:
                return []
            current_node = queue.popleft()
            traversal_order.append(current_node)

            for neighbor_position in self.game.get_possible_actions(position = current_node.position):
                if neighbor_position not in visited:
                    queue.append(Node(position = neighbor_position, parent = current_node))
                    visited.add(neighbor_position)
        # Go bottom up on tree
        path = []

        while current_node.parent != None:
            path.append(current_node.position)
            current_node = current_node.parent

        return list(reversed(path))


class IterativeDFSAgent(Agent):
    def __init__(self, game):
        super().__init__(game)
        self.found_path = self.get_optimal_path()

    def get_action(self):
        if self.found_path:
            self.number_moves += 1
            return self.found_path.pop(0)
        return None

    def get_optimal_path(self):
        depth = 0
        start = self.game.get_start()
        
        while True:
            result, was_cutoff = self._dls(start, depth, [start])
            
            if result:
                result.pop(0) # eliminar raíz
                return result
            
            # no resultado y no recortes de profundidad, no solución
            if not was_cutoff:
                return []
            
            depth += 1

    def _dls(self, node, depth, path):
        if self.game.is_goal(node):
            return path, False # encontrado, no importa el cutoff
        
        if depth == 0:
            # límite no sabemos si hay una solución más abajo.
            return [], True

        any_cutoff = False
        
        for neighbor_position in self.game.get_possible_actions(position=node):
            if neighbor_position not in path:
                result, cutoff_occurred = self._dls(neighbor_position, depth - 1, path + [neighbor_position])
                
                if result:
                    return result, False
                
                if cutoff_occurred:
                    any_cutoff = True
                    
        # no hay camino en esta rama
        return [], any_cutoff


if __name__ == "__main__":
    raw_input = """
    5 5
    0 0
    1 3
    3 4 1 3 1
    3 3 3 0 2
    3 1 2 2 3
    4 2 3 3 3
    4 1 4 3 2
    """
    metadata = parse_map(raw_input)
    height = metadata["height"]
    width = metadata["width"]
    test_start = metadata["start"]
    test_goal = metadata["goal"]
    test_map = metadata["map"]
    pprint(metadata)


    test_game = MazeGame(map=test_map,
                          height= height,
                          width = width,
                          start=test_start, 
                          goal=test_goal)

    test_game.reset()
    DFS_agent = IterativeDFSAgent(game = test_game)

    test_game.reset()
    BFS_agent = BFSAgent(game = test_game)

    print("==== Iterative DFS =====")
    print("RUTA: ", DFS_agent._get_optimal_path(), "\n")

    print("==== BFS =====")
    print("RUTA: ", BFS_agent._get_optimal_path())
