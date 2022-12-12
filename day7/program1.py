class Tree:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
        self.files = []
        self.size = 0

    def add_node(self, node):
        node.parent = self
        self.children.append(node)

    def add_file(self, name, size):
        self.size += size
        self.files.append((name, size))

    def get_total_size(self):
        total = self.size
        for child in self.children:
            total += child.get_total_size()
        return total

    def get_folder(self, name):
        for child in self.children:
            if child.name == name:
                return child

    def get_folders(self):
        return set(map(lambda child: child.name, self.children))

    def get_files(self):
        if self.files:
            filanames, _ = zip(*self.files)
            return filanames
        return []

    def get_sizes(self):
        sizes = [self.get_total_size()]
        for child in self.children:
            sizes.extend(child.get_sizes())
        return sizes

    def __str__(self):
        return f"Dir {name}"


filename = "input"
root = Tree("/")

node = root
with open(filename, "r") as input:
    while line := input.readline():
        if line.startswith("$ "):
            command = line[2:-1]
            if command.startswith("cd"):
                _, dir = command.split(" ")
                if dir == "/":
                    node = root
                elif dir == "..":
                    node = node.parent
                else:
                    if folder := node.get_folder(dir):
                        node = folder
                    else:
                        raise ValueError(f"invalid folder name {dir}")
            elif command.startswith("ls"):
                files = []
                while True:
                    line = input.readline()
                    if line == "" or line.startswith("$"):
                        input.seek(input.tell() - len(line))
                        break
                    files.append(line[:-1])
                for file in files:
                    if file.startswith("dir "):
                        name = file[4:]
                        if name not in node.get_folders():
                            new_node = Tree(file[4:])
                            node.add_node(new_node)
                    else:
                        size, name = file.split(" ")
                        if name not in node.get_files():
                            node.add_file(name, int(size))
                        else:
                            raise ValueError(f"Duplicated file {name}")
            else:
                raise ValueError(f"Invalid command '{command}'")
        else:
            raise ValueError(f"Invalid command '{line}'")

sizes = root.get_sizes()
MAX_SIZE = 100000
print(sum(filter(lambda x: x <= MAX_SIZE, sizes)))
