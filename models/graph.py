# models/graph.py

class GraphModel:
    def __init__(self):
        pass

    def generate_graph(self, objects, relations):
        graph = {}

        # Add objects as nodes in the graph
        for obj in objects:
            graph[obj] = {"relations": []}

        # Add relations as edges in the graph
        for relation in relations:
            obj1, obj2, rel = relation
            if obj1 in graph and obj2 in graph:
                graph[obj1]["relations"].append((obj2, rel))
                graph[obj2]["relations"].append((obj1, rel))

        return graph
