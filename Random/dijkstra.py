from collections import deque, namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost):
    return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(sum(([edge.start, edge.end] for edge in self.edges), []))

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))
        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, "Such source node doesn't exist"
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {vertex: None for vertex in self.vertices}
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return list(path)


def cost_setup(l, m):
    for i in range(len(l)):
        out = l[i][:2]
        if "p" in l[i][3] and "p" in m:
            cost = int(l[i][2]) / 500
        elif "t" in l[i][3] and "t" in m:
            cost = (int(l[i][2]) / 100)
        elif "c" in l[i][3] and "c" in m:
            cost = (int(l[i][2]) / 80)
        elif "f" in l[i][3] and "f" in m:
            cost = (int(l[i][2]) / 5)
        else:
            cost = inf
        l[i] = (l[i][0], l[i][1], cost)
    return l


if __name__ == '__main__':
    methods = "fctp"
    graph = Graph(cost_setup([('dublin', 'cork', 200, 'fct'),
                              ('cork', 'dublin', 200, 'fct'),
                              ('cork', 'corkAirport', 20, 'fc'),
                              ('corkAirport', 'cork', 25, 'fc'),
                              ('dublin', 'dublinAirport', 10, 'fc'),
                              ('dublinAirport', 'dublin', 20, 'fc'),
                              ('dublinAirport', 'corkAirport', 225, 'p'),
                              ('corkAirport', 'dublinAirport', 225, 'p')], methods))
    print(graph.dijkstra("cork", "dublin"))
