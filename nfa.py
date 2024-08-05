from collections.abc import Callable


class NFA:
    symbols: list[str]
    initial_states: list[int]
    accepting_states: list[int]
    delta: Callable[[int, str], list[int]]

    def __init__(
        self,
        symbols: list[str],
        initial_state: int,
        accepting_states: list[int],
        delta: Callable[[int, str], list[int]],
    ):
        self.symbols = symbols
        self.accepting_states = accepting_states
        self.delta = delta
        self.initial_states = self.epsilon_closure([initial_state])

    def print(self):
        print(
            f"NFA: Symbols: {self.symbols}, initial states: {self.initial_states}, accepting: {self.accepting_states}, delta: {self.delta}"
        )

    def epsilon_closure(self, states: list[int]):
        """Returns a list of states reachable through epsilon transitions."""
        q = states.copy()
        while len(q) > 0:
            cur_state = q.pop(0)
            new_states = self.delta(cur_state, "")
            for i in new_states:
                if i not in states:
                    q.append(i)
                    states.append(i)
        return states

    def check(self, input):
        last_states = self.run(input)
        union = [*last_states, *self.accepting_states]
        return len(set(union)) != len(union)

    def run(self, input):
        cur_states = self.initial_states
        for c in input:
            res = []
            for i in cur_states:
                new_states = self.delta(i, c)
                for j in new_states:
                    if j not in res:
                        res.append(j)
            cur_states = self.epsilon_closure(res)
        return cur_states
