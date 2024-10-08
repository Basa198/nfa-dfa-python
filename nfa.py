from collections.abc import Callable


class NFA:
    initial_state: int
    accepting_states: set[int]
    delta: Callable[[int, str], set[int]]

    def __init__(
        self,
        initial_state: int,
        accepting_states: set[int],
        delta: Callable[[int, str], set[int]],
    ):
        self.accepting_states = accepting_states
        self.delta = delta
        self.initial_state = initial_state

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

    def _nfa_transition(
        self, delta: Callable[[int, str], set[int]], states: set[int], symbol: str
    ):
        # Only the first time this is called. Only state is the init state
        if len(states) == 1:
            states = self.epsilon_closure(states)
        new_states = set()
        for state in states:
            new_states.update(delta(state, symbol))
        return self.epsilon_closure(new_states)

    def toDFA(self):
        from dfa import DFA

        dfa = DFA(self.initial_state, self.accepting_states, self.delta)
        dfa._transition = self._nfa_transition
        return dfa
