"""
Генерация дерева и вывод его в виде древовидной структуры с помощью символов.
Также вычисляется наибольшая глубина дерева.

Переменные:
- tree: корень сгенерированного дерева
- depth: глубина дерева
- prefix: префикс для отступов при печати узлов
- is_tail: указывает, является ли узел последним у дочерних узлов своего родителя
"""

import random


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)


def generate_random_tree(depth):
    if depth == 0:
        return None
    root = TreeNode(random.randint(1, 100))
    num_children = random.randint(0, 3)
    for _ in range(num_children):
        root.children.append(generate_random_tree(depth - 1))
    return root


def print_tree(root, prefix='', is_tail=True):
    if root is None:
        return
    print(prefix + ('└── ' if is_tail else '├── ') + str(root.value))
    prefix += '    ' if is_tail else '│   '
    children_count = len(root.children)
    for i, child in enumerate(root.children):
        is_last_child = (i == children_count - 1)
        print_tree(child, prefix, is_last_child)


def max_depth(root):
    if root is None:
        return 0
    if not root.children:
        return 1
    return 1 + max(max_depth(child) for child in root.children)


def main():
    depth = random.randint(1, 20)
    tree = generate_random_tree(depth)
    print("Сгенерированное дерево:")
    print_tree(tree)
    print("Наибольшая глубина дерева:", max_depth(tree))


if __name__ == "__main__":
    main()
