class Vertex:
    def __init__(self, value):
        self.value = value
        self.adj_list = []
    
    def add_edge(self, vertex):
        self.adj_list.append(vertex)
    
    def delete_edge(self, vertex):
        self.adj_list.remove(vertex)

class Graph:
    def __init__(self):
        self.vertices = []
    
    def add_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)
        self.vertices.append(vertex)
    
    def add_edge(self, v1, v2):
        if v2 in v1.adj_list:
            raise Exception('Edge already created!')
        v1.add_edge(v2)
    
    def is_adjacent(self, v1, v2):
        return v2 in v1.adj_list

    def is_empty(self):
        return len(self.vertices) == 0

    def delete_edge(self, v1, v2):
        if self.is_adjacent(v1, v2):
            v1.delete_edge(v2)
    
    def delete_vertex(self, vertex):
        self.vertices.remove(vertex)
        for v in self.vertices:
            self.delete_edge(v, vertex)
    
    def get_vertex_by_value(self, value):
        for v in self.vertices:
            if v.value == value:
                return v
        return None