# Usage

Epsilon transitions are supported by all `NFA`s and those `DFA`s that were converted from an `NFA`.

## Run Tests

```Bash
$ python3 test.py
```

## DFA

### `DFA` class:

```Python
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
        self.delta = delta
        self._transition = _transition
```

### `DFA` methods:

```Python
check(self, input: str) -> bool
run(self, input: str) -> set[int]
toNFA(self) -> NFA
```

### To run:

```Python
from dfa import DFA

dfa = DFA(initial_state, accepting_states_set, delta)
dfa.check(string)
```

## NFA

### `NFA` class:

```Python
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
```

### `NFA` methods:

```Python
epsilon_closure(self, states: set[int]) -> set[int]
check(self, input: str) -> bool
run(self, input: str) -> set[int]
toDFA(self) -> NFA
_nfa_transition( # used internally by toDFA
        self, delta: Callable[[int, str], set[int]], states: set[int], symbol: str
    ) -> set[int]
```

### To run:

```Python
from nfa import NFA

nfa = NFA(initial_state, accepting_states_set, delta)
nfa.check(string)
```

## Conversion between `NFA` and `DFA`

```Python
from nfa import NFA
from dfa import DFA

nfa = NFA(initial_state, accepting_states_set, delta)
dfa = DFA(initial_state, accepting_states_set, delta)

nfa_from_dfa = nfa.toDFA()
dfa_from_nfa = dfa.toNFA()
```

## `delta` example

```Python
def delta_eps(state, symbol):
    if symbol == "": # epsilon transition
        if state == 0:
            return {1, 3}
        else:
            return {}
    elif symbol == "0":
        if state == 1:
            return {2}
        elif state == 2:
            return {1}
        elif state == 3 or state == 4:
            return {state}
        else:
            return {}
    elif symbol == "1":
        if state == 1 or state == 2:
            return {state}
        elif state == 3:
            return {4}
        elif state == 4:
            return {3}
        else:
            return {}
    else:
        return {}
```
