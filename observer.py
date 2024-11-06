class Observer:
    def update(self, score):
        pass

class ScoreObserver(Observer):
    def update(self, score):
        print(f"Score updated: {score}")
class GameObserver:
    def update(self, is_game_over):
        print(f"Game Over: {is_game_over}")
