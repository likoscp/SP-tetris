class Observer:
    def update(self, score):
        pass

class ScoreObserver(Observer):
    def update(self, score):
        print(f"Score updated: {score}")
