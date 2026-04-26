import pygame
from src.model import MazeGame
from src.utils import parse_map, split_multiple_maps, parse_args
from src.agents import RandomAgent, BFSAgent, IterativeDFSAgent, Player
from src.view import Visualizer


if __name__ == "__main__":
    print("\n=== OUTPUT ====\n")

    args = parse_args()
    if args.agent == "player" or args.agent == "random":
        args.gui = True


    with open(args.input, 'r') as file:
        raw_input = file.read().replace('\n', ' ')

    maps_strings = split_multiple_maps(raw_input)
    
    parsed_maps = [parse_map(s) for s in maps_strings]

    if args.gui:
        pygame.init()
        view = Visualizer(agent_name=args.agent)

    for metadata in parsed_maps:
        map_height = metadata["height"]
        map_width = metadata["width"]
        start = metadata["start"]
        goal = metadata["goal"]
        game_map = metadata["map"]

        game = MazeGame(map=game_map,
                        height=map_height,
                        width=map_width,
                        start=start,
                        goal=goal)

        # aquí hay que solo poner el tema de
        if args.agent == "bfs":
            agent = BFSAgent(game=game)
        elif args.agent == "dfs":
            agent = IterativeDFSAgent(game=game)
        elif args.agent == "player":
            player = Player(game=game)
        else:
            agent = RandomAgent(game=game)

        if args.gui:
            running = True
            while running:
                view.draw(game_map, map_height, map_width, game.get_current_position())

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                        if args.agent == "player":
                            if event.key == pygame.K_UP:
                                action = player.go_up()
                            elif event.key == pygame.K_DOWN:
                                action = player.go_down()
                            elif event.key == pygame.K_RIGHT:
                                action = player.go_right()
                            elif event.key == pygame.K_LEFT:
                                action = player.go_left()
                            else:
                                action = game.get_current_position()

                            game.set_current_position(action)
                        else:
                            if event.key == pygame.K_SPACE:
                                action = agent.get_action()
                                if action:
                                    game.set_current_position(action)
                                else:
                                    print("No hay más acciones válidas")
        else:
            n_moves = len(agent.get_optimal_path())
            print(n_moves) if n_moves else print("No hay solución")
    pygame.quit() if args.gui else 42
    print("\n===============")
