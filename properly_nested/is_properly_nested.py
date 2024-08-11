def is_properly_nested(S):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for char in S:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or bracket_pairs[char] != stack.pop():
                return False

    return len(stack) == 0

def test(func):
    legals = ['(()[[]][])',
              '[[]{}{{}}]',
              '{[]{[][]}}',
              '()((){[]})',
              '{([][]{})}',
              '[[]([])]{}',
              '(([]{[]}))',
              '[]{[[]{}]}',
              '{[[]]{}}()',
              '{{}}[{()}]']
    illegal = ['}}))[{)({]',
               '{)({([)){}',
               '{{}[((]}}]',
               '[){{{{{)}(',
               '{}[[}]}(]{',
               '}[]]{[})[{',
               '][[([}[)()',
               '[)(]){]}(]',
               '(]}}[)})]]',
               '[)((])]{(}']
    for s in legals:
        assert func(s), s
    for s in illegal:
        assert not func(s), s

# הרצת הבדיקה
test(is_properly_nested)
print("All tests passed successfully!")

