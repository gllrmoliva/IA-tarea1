import random


class MazeGame:

    def __init__(self, map, height, width, start: tuple, goal: tuple):
        """"""
        self.map = map
        self.height = height
        self.width = width
        self.start = start
        self.current_position = start
        self.goal = goal
        self.terminated = False

    def reset(self, ):
        self.current_position = self.start
        self.terminated = False

    def action(self, action):
        self.current_position = action

        if self.current_position == self.goal:
            self.terminated = True

        return self.terminated

    def is_goal(self, state):
        return self.goal == state

    def set_current_position(self, position):
        self.current_position = position

    def get_current_map(self, ):
        return self.map

    def get_possible_actions(self, position = None):
        possible_actions = []

        if position == None:
            position = self.current_position


        step =  self.map[position[0]][position[1]]

        if 0 <= position[0] - step:
            possible_actions.append((position[0] - step,
                                     position[1]))

        if position[0] + step < self.height:
            possible_actions.append((position[0] + step,
                                     position[1]))

        if 0 <= position[1] - step:
           possible_actions.append((position[0],
                                     position[1] - step))

        if position[1] + step < self.width:
            possible_actions.append((position[0],
                                     position[1] + step))

        return possible_actions

    def get_start(self, ):
        return self.start

    def get_current_position(self, ):
        return self.current_position

    def get_current_step(self, ):
        position = self.current_position
        return self.map[position[0]][position[1]]

    def print_game(self, ):
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.current_position:
                    print("X", end="")
                elif (i, j) == self.goal:
                    print("G", end="")
                else:
                    print(self.map[i][j], end="")
            print("")


if __name__ == "__main__":
    height = 5
    width = 5
    test_start = (0, 0)
    test_goal = (1, 3)
    test_map = [[3, 4, 1, 3, 1],
                [3, 3, 3, 0, 2],
                [3, 1, 2, 2, 3],
                [4, 2, 3, 3, 3],
                [4, 1, 4, 3, 2]]


    # test_map, test_start, test_goal = generate_random_game(5, 5)

    test_game = MazeGame(map=test_map,
                          height= height,
                          width = width,
                          start=test_start, 
                          goal=test_goal)

    test_game.print_game()
    while not test_game.terminated:
        input()
        action = random.choice(test_game.get_possible_actions())
        test_game.action(action)

        test_game.print_game()
