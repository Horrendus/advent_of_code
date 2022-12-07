class Directory:
    def __init__(self, name, parent):
        self.name: str = name
        self.parent: "Directory" = parent
        self.subdirs: dict[str, "Directory"] = {}
        self.files: list[tuple[str, int]] = []
        if self.parent:
            self.parent.subdirs[self.name] = self

    def size(self):
        file_sizes = sum([f[1] for f in self.files])
        subdir_sizes = sum(d.size() for d in self.subdirs.values())
        return file_sizes + subdir_sizes


def build_directory_tree(data):
    root = Directory("/", None)
    current_directory = root
    for d in data:
        if d[0] == "COMMAND":
            if d[1] == "cd":
                if d[2] == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.subdirs[d[2]]
            if d[1] == "ls":
                pass
        elif d[0] == "FILE":
            current_directory.files.append((d[1], d[2]))
        elif d[0] == "DIRECTORY":
            Directory(d[1], current_directory)

    return root


def depth_first_search(
    d: Directory, visited: list[Directory], sizes: dict[Directory, int]
):
    visited.add(d)
    sizes[d] = d.size()

    for subdir in d.subdirs.values():
        if subdir not in visited:
            depth_first_search(subdir, visited, sizes)


def get_directory_sizes(root: Directory):
    visited = set()
    sizes = {}
    depth_first_search(root, visited, sizes)
    return sizes


def puzzle(data):
    root = build_directory_tree(data)
    sizes = get_directory_sizes(root)
    return root, sizes


def puzzle1(sizes):
    directories_under_100000 = [size for name, size in sizes.items() if size <= 100000]
    print("Puzzle 1: ", sum(directories_under_100000))


def puzzle2(root, sizes):
    total_diskspace = 70000000
    required_space = 30000000
    unused_diskspace = total_diskspace - sizes[root]
    deleted_directory_size = sizes[root]
    for d, size in sizes.items():
        if d.name != "/":
            if (
                unused_diskspace + size >= required_space
                and size < deleted_directory_size
            ):
                deleted_directory_size = size
    print("Puzzle 2: ", deleted_directory_size)


def parse_line(line):
    if line[0] == "$":
        splitted_command = line[2:].split(" ")
        if len(splitted_command) == 2:
            return ("COMMAND", splitted_command[0], splitted_command[1])
        return ("COMMAND", splitted_command[0], None)
    elif line.startswith("dir"):
        return ("DIRECTORY", line[4:], None)
    else:
        splitted_file = line.split(" ")
        return ("FILE", splitted_file[1], int(splitted_file[0]))


def parse_input(data):
    lines = data.strip().split("\n")
    parsed = [parse_line(line) for line in lines]
    return parsed[1:]


def main():
    with open("input/input_day07.txt") as f:
        data = f.read()
    data = parse_input(data)
    root, sizes = puzzle(data)
    puzzle1(sizes)
    puzzle2(root, sizes)


if __name__ == "__main__":
    main()
