from pose_controller import PoseController
from game import Game

def main():
    controller = PoseController()
    game = Game()

    game.run(controller)

    controller.release()

if __name__ == "__main__":
    main()