from collections.abc import Callable


class DFA:
    symbols: set[str]
    initial_state: int
    accepting_states: set[int]
    delta: Callable[[int, str], int] | Callable[[set[int], str], set[int]]

    def __init__(
        self,
        symbols: set[str],
        initial_state: int,
        accepting_states: set[int],
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

    def check(self, input):
        s = self.run(input)
        # s is iterable if the current dfa was converted from an nfa
        if hasattr(s, "__iter__"):
            return len(set.intersection(s, self.accepting_states)) > 0
        else:
            return s in self.accepting_states

    def run(self, input):
        if input == "":
            s = self.delta(self.initial_state, "")
            if s == -1:
                return self.initial_state
            else:
                return s
        cur_state = self.initial_state
        for c in input:
            cur_state = self.delta(cur_state, c)
            if cur_state == -1:
                return -1
        return cur_state

    def toNFA(self):
        from nfa import NFA

        def delta_wrapper(state: int, symbol: str) -> set[int]:
            s = self.delta(state, symbol) # returns either a set or an int
            if hasattr(s, "__iter__"):
                return s
            else:
                return {s}

        return NFA(
            self.symbols, self.initial_state, self.accepting_states, delta_wrapper
        )
