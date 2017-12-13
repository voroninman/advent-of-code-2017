from collections import defaultdict
from operator import lt, le, eq, ne, ge, gt, add, sub

import sys

f_map = {
    '>': gt,
    '<': lt,
    '>=': ge,
    '<=': le,
    '!=': ne,
    '==': eq,
    'inc': add,
    'dec': sub,
}

max_ = -sys.maxsize
memory = defaultdict(int)

with open('input') as f:
    for line in f:
        params = line.strip().split(' ')
        reg, f_arg0, f, f_arg1, cond_arg0, cond_f, cond_arg1 = \
            params[0], memory[params[0]], f_map[params[1]], int(params[2]), \
            memory[params[4]], f_map[params[5]], int(params[6])

        if cond_f(cond_arg0, cond_arg1):
            memory[reg] = f(f_arg0, f_arg1)
            max_ = max(memory[reg], max_)

print(max(memory.values()), max_)
