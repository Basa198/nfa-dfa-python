from nfa import NFA
from dfa import DFA


# dfa for multiples of 3
def mul3_delta(state, symbol):
    if symbol == "0":
        if state == 0:
            return 0
        elif state == 1:
            return 2
        elif state == 2:
            return 1
        else:
            return -1
    elif symbol == "1":
        if state == 0:
            return 1
        elif state == 1:
            return 0
        elif state == 2:
            return 2
        else:
            return -1
    else:
        return -1


# NFA: fourth from last symbol has to be 1
def delta_nfa(state, symbol):
    if symbol == "0":
        if state == 10:
            return set([10])
        elif state == 0:
            return set([1])
        elif state == 1:
            return set([2])
        elif state == 2:
            return set([3])
        else:
            return set()
    elif symbol == "1":
        if state == 10:
            return set([10, 0])
        elif state == 0:
            return set([1])
        elif state == 1:
            return set([2])
        elif state == 2:
            return set([3])
        else:
            return set()
    else:
        return set()


def delta_eps(state, symbol):
    if symbol == "":
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


mul3_dfa = DFA({"0", "1"}, 0, {0}, mul3_delta)
assert mul3_dfa.check("") == True
assert mul3_dfa.check("1") == False
assert mul3_dfa.check("0000") == True
assert mul3_dfa.check("101") == False
assert mul3_dfa.check("1001") == True
assert mul3_dfa.check("1111") == True

mul3_nfa = mul3_dfa.toNFA()
assert mul3_nfa.check("") == True
assert mul3_nfa.check("1") == False
assert mul3_nfa.check("0000") == True
assert mul3_nfa.check("101") == False
assert mul3_nfa.check("1001") == True
assert mul3_nfa.check("1111") == True

mul3_dfa = mul3_nfa.toDFA()
assert mul3_nfa.check("") == True
assert mul3_nfa.check("1") == False
assert mul3_nfa.check("0000") == True
assert mul3_nfa.check("101") == False
assert mul3_nfa.check("1001") == True
assert mul3_nfa.check("1111") == True

mul3_nfa = mul3_dfa.toNFA()
assert mul3_nfa.check("") == True
assert mul3_nfa.check("1") == False
assert mul3_nfa.check("0000") == True
assert mul3_nfa.check("101") == False
assert mul3_nfa.check("1001") == True
assert mul3_nfa.check("1111") == True


nfa = NFA({"0", "1"}, 10, {3}, delta_nfa)
assert nfa.check("") == False
assert nfa.check("0000") == False
assert nfa.check("1000") == True
assert nfa.check("10001") == False
assert nfa.check("11111") == True
assert nfa.check("10111") == False
assert nfa.check("000000001000") == True
assert nfa.check("10010010") == False
assert nfa.check("111") == False

dfa = nfa.toDFA()
assert dfa.check("") == False
assert dfa.check("0000") == False
assert dfa.check("1000") == True
assert dfa.check("10001") == False
assert dfa.check("11111") == True
assert dfa.check("10111") == False
assert dfa.check("000000001000") == True
assert dfa.check("10010010") == False
assert dfa.check("111") == False

nfa = dfa.toNFA()
assert nfa.check("") == False
assert nfa.check("0000") == False
assert nfa.check("1000") == True
assert nfa.check("10001") == False
assert nfa.check("11111") == True
assert nfa.check("10111") == False
assert nfa.check("000000001000") == True
assert nfa.check("10010010") == False
assert nfa.check("111") == False

dfa = nfa.toDFA()
assert dfa.check("") == False
assert dfa.check("0000") == False
assert dfa.check("1000") == True
assert dfa.check("10001") == False
assert dfa.check("11111") == True
assert dfa.check("10111") == False
assert dfa.check("000000001000") == True
assert dfa.check("10010010") == False
assert dfa.check("111") == False


nfa = NFA({"0", "1"}, 0, {1, 3}, delta_eps)
assert nfa.check("") == True
assert nfa.check("1") == True
assert nfa.check("0") == True
assert nfa.check("10") == False
assert nfa.check("1001") == True
assert nfa.check("100") == True
assert nfa.check("111000") == False
assert nfa.check("11001101") == False
assert nfa.check("1001") == True
assert nfa.check("1111000") == True
assert nfa.check("010101") == False
assert nfa.check("111111") == True
assert nfa.check("111110") == False

dfa = nfa.toDFA()
assert dfa.check("") == True
assert dfa.check("1") == True
assert dfa.check("0") == True
assert dfa.check("10") == False
assert dfa.check("1001") == True
assert dfa.check("100") == True
assert dfa.check("111000") == False
assert dfa.check("11001101") == False
assert dfa.check("1001") == True
assert dfa.check("1111000") == True
assert dfa.check("010101") == False
assert dfa.check("111111") == True
assert dfa.check("111110") == False

nfa = dfa.toNFA()
assert nfa.check("") == True
assert nfa.check("1") == True
assert nfa.check("0") == True
assert nfa.check("10") == False
assert nfa.check("1001") == True
assert nfa.check("100") == True
assert nfa.check("111000") == False
assert nfa.check("11001101") == False
assert nfa.check("1001") == True
assert nfa.check("1111000") == True
assert nfa.check("010101") == False
assert nfa.check("111111") == True
assert nfa.check("111110") == False

dfa = nfa.toDFA()
assert dfa.check("") == True
assert dfa.check("1") == True
assert dfa.check("0") == True
assert dfa.check("10") == False
assert dfa.check("1001") == True
assert dfa.check("100") == True
assert dfa.check("111000") == False
assert dfa.check("11001101") == False
assert dfa.check("1001") == True
assert dfa.check("1111000") == True
assert dfa.check("010101") == False
assert dfa.check("111111") == True
assert dfa.check("111110") == False

print("All tests pass")