from collections.abc import Callable
from nfa import NFA


class DFA:
    symbols: list[str]
    initial_state: int
    accepting_states: list[int]
    delta: Callable[[int, str], int]

    def __init__(
        self,
        symbols: list[str],
        initial_state: int,
        accepting_states: list[int],
        delta: Callable[[int, str], int],
    ):
        self.symbols = symbols
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.delta = delta  # return -1 for unknown transition

    def print(self):
        print(
            f"DFA: Symbols: {self.symbols}, initial state: {self.initial_state}, accepting: {self.accepting_states}, delta: {self.delta}"
        )

    def run(self, input):
        cur_state = self.initial_state
        for c in input:
            cur_state = self.delta(cur_state, c)
            if cur_state == -1:
                return False
        return cur_state in self.accepting_states


def delta(state: int, input: str):
    if input == "a":
        if state == 1:
            return 2
        else:
            return state
    elif input == "b":
        if state == 0:
            return 1
        else:
            return state
    else:
        return -1


dfa = DFA(["a", "b"], 0, [0, 1], delta)

print(dfa.run("bbbb"))
