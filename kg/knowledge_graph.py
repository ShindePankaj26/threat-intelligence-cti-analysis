class CTIKnowledgeGraph:
    """
    Simple CTI Knowledge Graph
    """

    def __init__(self):
        self.nodes = []
        self.edges = []

        print("CTI Knowledge Graph Initialized")

    def add_entity(self, entity):
        self.nodes.append(entity)

    def add_relation(self, source, target, relation):
        self.edges.append({
            "source": source,
            "target": target,
            "relation": relation
        })

    def build_graph(self, entities, relations):
        """
        Build simple graph
        """

        for key, values in entities.items():
            for value in values:
                self.add_entity({
                    "type": key,
                    "value": value
                })

        for relation in relations:
            self.edges.append(relation)

    def display_graph(self):
        """
        Print graph data
        """

        print("\n=== Knowledge Graph Nodes ===")
        for node in self.nodes:
            print(node)

        print("\n=== Knowledge Graph Relations ===")
        for edge in self.edges:
            print(edge)
