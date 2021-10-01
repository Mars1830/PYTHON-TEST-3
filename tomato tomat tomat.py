
class Tomato:
    states = ['green', 'yellow', 'red']

    def __init__(self, index: int):
        self.index = index
        self.state = Tomato.states[0]

    def grow(self):
        state_idx = Tomato.states.index(self.state)
        if state_idx < len(Tomato.states) - 1:
            self.state = Tomato.states[state_idx + 1]

    def is_ripe(self) -> bool:
        return Tomato.states.index(self.state) == len(Tomato.states) - 1


class TomatoBush:

    def __init__(self, tomatoes_number: int):
        self.tomatoes = [Tomato(i) for i in range(1, tomatoes_number + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return len(list(filter(lambda t: not t.is_ripe(), self.tomatoes))) == 0

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    @staticmethod
    def knowledge_base():
        print('Knowledge base')

    def __init__(self, name: str, plant: TomatoBush):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('Not all tomatoes are ripe')


if __name__ == '__main__':
    Gardener.knowledge_base()

    bush = TomatoBush(8)
    bob = Gardener('Bob', bush)
    bob.work()
    bob.harvest()
    bob.work()
    bob.harvest()
