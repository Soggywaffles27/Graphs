class Graph():
    def __init__(self, verts, edges):
        self.edges = edges
        self.verts = verts
    def add_vert(self, v):
        self.verts.append(w)
    def add_edge(self, v, w):
        self.verts.append((v, w))
    def adj(self, v):
        out = []
        for i in self.edges:
            if v in i:
                out.append(i)
        return out
    def max_degree(self):
        max_e = 0
        for v in self.verts:
            max_e = max(max_e, len(self.adj(v)))
        return max_e

G = Graph(["A", "B","C", "D","E", "F"], [("A", "B"),("A", "C"),("C", "D")])
print(G.max_degree())