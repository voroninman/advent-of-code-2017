import re
from typing import NamedTuple, List, Iterator

parse_re = re.compile(r'^(\w+) \((\d+)\)(?: -> ((?:(?:\w+)(?:, )?)+))?$')

Node = NamedTuple('Node', [('value', str), ('weight', int), ('leaves', List[str])])


def parse_line(line: str) -> Node:
    node, weight, leaves = re.search(parse_re, line).groups()
    return Node(**{
        'value': node,
        'weight': int(weight),
        'leaves': leaves.split(', ') if leaves else [],
    })


def parse_input() -> Iterator[Node]:
    with open('input') as f:
        for line in f:
            yield parse_line(line)


nodes = {node.value: node for node in parse_input()}


def trace_root(given_node: Node = None) -> Node:
    if not given_node:
        given_node = nodes[list(nodes.keys())[0]]
    for a_node_value, a_node in nodes.items():
        if given_node.value in a_node.leaves:
            return trace_root(a_node)
    return given_node


def trace_weight_error(node: Node) -> int:
    children_weights = []
    for leaf in node.leaves:
        leaf_node = nodes[leaf]
        children_weights.append(trace_weight_error(leaf_node))

    if len(set(children_weights)) > 1:
        err_nodes_with_weight = []
        for an_err_node_value in node.leaves:
            an_err_node = nodes[an_err_node_value]
            err_nodes_with_weight.append(
                (an_err_node, trace_weight_error(an_err_node)))
        a_correct_node_with_weight, *_, err_node_with_weight \
            = sorted(err_nodes_with_weight, key=lambda v: v[1])
        raise ValueError('Node {} with weight {} should have {} weight'
                         .format(err_node_with_weight[0].value,
                                 err_node_with_weight[0].weight,
                                 err_node_with_weight[0].weight -
                                 err_node_with_weight[1] +
                                 a_correct_node_with_weight[1]))

    total_weight = node.weight + sum(children_weights)
    return total_weight


root_node = trace_root()
print('The root node is: {}'.format(root_node.value))
try:
    trace_weight_error(root_node)
except ValueError as e:
    print('Error found: {}'.format(e))
