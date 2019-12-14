class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.childs = []
        self.orbit_count = 0


def parse_input(data):
    root = None
    node_map = dict()
    for line in data:
        line_split = line.split(")")
        parent = line_split[0].strip()
        node_str = line_split[1].strip()
        if parent in node_map:
            parent_node = node_map[parent]
        else:
            parent_node = Node(parent, None)
            node_map[parent] = parent_node
        if parent == "COM":
            root = parent_node
        if node_str not in node_map:
            node = Node(node_str, parent_node)
            node_map[node_str] = node
            parent_node.childs.append(node)
        else:
            node_map[node_str].parent = parent_node
            parent_node.childs.append(node_map[node_str])
    return root, node_map


def calculate_depths(root_node):
    total_orbits = 0
    node_list = root_node.childs.copy()
    while node_list:
        current_node = node_list.pop()
        current_node.orbit_count = current_node.parent.orbit_count + 1
        total_orbits += current_node.orbit_count
        node_list.extend(current_node.childs)
    return total_orbits


def puzzle1(root):
    total_orbits = calculate_depths(root)
    print("Orbits: ", total_orbits)


def find_ancestors(node):
    node_ancestors = [node]
    current_ancestor = node
    while True:
        current_ancestor = current_ancestor.parent
        node_ancestors.append(current_ancestor)
        if not current_ancestor.parent:
            break
    return node_ancestors


def find_common_ancestor(node1, node2):
    ancestors1 = find_ancestors(node1)
    ancestors2 = find_ancestors(node2)
    ancestors1.reverse()
    ancestors2.reverse()
    common_ancestor = None
    for i in range(len(ancestors1)):
        if ancestors1[i] == ancestors2[i]:
            common_ancestor = ancestors1[i]
        else:
            break
    return common_ancestor


def find_distance(node1, node2):
    common_ancestor = find_common_ancestor(node1, node2)
    path1 = node1.orbit_count - common_ancestor.orbit_count
    path2 = node2.orbit_count - common_ancestor.orbit_count
    return path1 + path2


def puzzle2(root_node, node_map):
    node1 = node_map["YOU"].parent
    node2 = node_map["SAN"].parent
    distance = find_distance(node1, node2)
    print("Distance: ", distance)


def main():
    with open("input/input_day6.txt") as f:
        data = f.readlines()
    root, node_map = parse_input(data)
    puzzle1(root)
    puzzle2(root, node_map)


if __name__ == "__main__":
    main()
