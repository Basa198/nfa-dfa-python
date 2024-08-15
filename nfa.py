from collections.abc import Callable


class NFA:
    symbols: set[str]
    initial_state: int
    accepting_states: set[int]
    delta: Callable[[int, str], set[int]]

    def __init__(
        self,
        symbols: set[str],
        initial_state: int,
        accepting_states: set[int],
        delta: Callable[[int, str], set[int]],
    ):
        self.symbols = symbols
        self.accepting_states = accepting_states
        self.delta = delta
        self.initial_state = initial_state

    def print(self):
        print(
            f"NFA: Symbols: {self.symbols}, initial states: {self.initial_state}, accepting: {self.accepting_states}, delta: {self.delta}"
        )

    def epsilon_closure(self, states: set[int]):
        """Returns a list of states reachable through epsilon transitions."""
        q = list(states)
        res = states.copy()
        while len(q) > 0:
            cur_state = q.pop(0)
            new_states = self.delta(cur_state, "")
            for i in new_states:
                if i not in res:
                    q.append(i)
                    res.add(i)
        return res

    def check(self, input):
        last_states = self.run(input)
        return len(set.intersection(last_states, self.accepting_states)) > 0

    def run(self, input):
        cur_states = set([self.initial_state])
        for c in input:
            cur_states = self.epsilon_closure(cur_states)
            res = set()
            for i in cur_states:
                res.update(self.delta(i, c))
            cur_states = res
        return self.epsilon_closure(cur_states)

    def toDFA(self):
        from dfa import DFA

        def delta_wrapper(state, symbol):
            # state MIGHT an iterable
            # it's not iterable on the first iteration in DFA.run() when the input is initial state
            # it's iterable on subsequent iterations in DFA.run()
            if not hasattr(state, "__iter__"):
                state = self.epsilon_closure({state})

            new_state = set()
            for i in state:
                new_state.update(self.delta(i, symbol))
            return self.epsilon_closure(new_state)

        return DFA(
            self.symbols, self.initial_state, self.accepting_states, delta_wrapper
        )
