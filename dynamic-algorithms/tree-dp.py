# find the maximum sum of node values in a tree where no two selected nodes are a parent and child

class Node:
    def _init__(self, val):
        self.val = val  # int value of node
        self.C = []  # list of child nodes
        self.f = -1  # max value of subtree
        self.g = -1  # max value of subtree without root


def F(root):
    if root.f != -1:
        return root.f

    f1 = root.value
    for u in root.C:
        f1 += G(u)

    f2 = G(root)
    root.f = max(f1, f2)
    return root.f


def G(root):
    if root.g != -1:
        return root.g

    g = 0
    for u in root.C:
        g += F(u)

    root.g = g
    return root.g
