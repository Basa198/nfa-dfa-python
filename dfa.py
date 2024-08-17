from collections.abc import Callable


def _transition(delta: Callable[[int, str], set[int]], states: set[int], symbol: str):
    new_states = set()
    for state in states:
        new_states.update(delta(state, symbol))
    return new_states


class DFA:
    _transition: Callable[[Callable[[int, str], set[int]], set[int], str], set[int]]
    initial_state: int
    accepting_states: set[int]
    delta: Callable[[int, str], set[int]]

    def __init__(
        self,
        initial_state: int,
        accepting_states: set[int],
        delta: Callable[[int, str], set[int]],
    ):
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.delta = delta  # return -1 for unknown transition

        self._transition = _transition

    def check(self, input):
        s = self.run(input)
        return len(set.intersection(s, self.accepting_states)) > 0

    def run(self, input):
        cur_state = set([self.initial_state])
        if input == "":
            cur_state = self._transition(self.delta, cur_state, "")
            if len(cur_state) == 0:
                return set([self.initial_state])
            else:
                return cur_state
        for c in input:
            cur_state = self._transition(self.delta, cur_state, c)
        return cur_state

    def toNFA(self):
        from nfa import NFA

        return NFA(self.initial_state, self.accepting_states, self.delta)
