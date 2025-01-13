class Solution:
    def isNumber(self, s: str) -> bool:
        state = 0
        finals = {2, 3, 7, 8}
        transition = [
            {'blank': 0, 'sign': 1, 'digit': 2, 'dot': 4},
            {'digit': 2, 'dot': 4},
            {'digit': 2, 'dot': 3, 'exp': 5, 'blank': 8},
            {'digit': 3, 'exp': 5, 'blank': 8},
            {'digit': 3},
            {'sign': 6, 'digit': 7},
            {'digit': 7},
            {'digit': 7, 'blank': 8},
            {'blank': 8}
        ]

        def char_type(c):
            if c in '0123456789':
                return 'digit'
            elif c in ' \t\n':
                return 'blank'
            elif c in '+-':
                return 'sign'
            elif c in 'eE':
                return 'exp'
            elif c == '.':
                return 'dot'
            else:
                return None

        for char in s:
            typ = char_type(char)
            if typ not in transition[state]:
                return False
            state = transition[state][typ]

        return state in finals