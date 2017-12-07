import re

parse_re = re.compile(r'^(\w+) \((\d+)\)(?: -> ((?:(?:\w+)(?:, )?)+))?$')


def parse_line(line):
    node, weight, leafs = re.search(parse_re, line).groups()
    node, weight, leafs = node, int(weight), leafs.split(', ') if leafs else []
    return node, weight, leafs


with open('test_input') as f:
    for line in f:
        print(parse_line(line.strip()))
