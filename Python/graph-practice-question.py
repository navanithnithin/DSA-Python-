class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graphDict = {}
        for start, end in edges:
            if start in self.graphDict:
                self.graphDict[start].append(end)
            else:
                self.graphDict[start] = [end]
        print(self.graphDict)

    def getPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graphDict:
            return []
        paths = []
        for node in self.graphDict[start]:
            if node not in path:
                newPath = self.getPath(node, end, path)
                for p in newPath:
                    paths.append(p)
        return paths

    def shortestPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graphDict:
            return None
        shortPath = None
        for node in self.graphDict[start]:
            if node not in path:
                sp = self.shortestPath(node, end, path)
                if sp:
                    if shortPath is None or len(sp) < len(shortPath):
                        shortPath = sp
        return shortPath


if __name__ == "__main__":
    routes1 = [
        ("Mumbai", "Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bengaluru"),
        ("Pune", "Hyderabad"),
        ("Pune", "Mysuru"),
        ("Hyderabad", "Bengaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bengaluru"),
        ("Chennai", "Bengaluru"),
    ]
    routes2 = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    # routGrap1 = Graph(routes1)
    routGrap2 = Graph(routes2)
    start = "Mumbai"
    end = "New York"
    print(f"All paths between: {start} and {end}: ", routGrap2.getPath(start, end))
    print(
        f"Shortest path between {start} and {end}: ", routGrap2.shortestPath(start, end)
    )
