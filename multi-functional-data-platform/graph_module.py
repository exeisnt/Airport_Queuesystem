# --- Graph Module ---
def create_dag(edges):
    """Creates a Directed Acyclic Graph (DAG) from given edges."""
    graph = nx.DiGraph()
    graph.add_edges_from(edges)
    if not nx.is_directed_acyclic_graph(graph):
        raise ValueError("The graph contains cycles.")
    return graph
