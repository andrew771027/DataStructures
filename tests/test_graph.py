from src.graph import dfs_recursive, dfs_iterative, bfs_traverse

def test_graph_dfs_recursive_traverse(capfd):
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    dfs_recursive(graph, 'A')
    out, err = capfd.readouterr()
    assert out == "A B D E F C "

def test_graph_dfs_iterative_traverse(capfd):
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    dfs_iterative(graph, "A")
    out, err = capfd.readouterr()
    assert out == "A B D E F C "

def test_graph_bfs_traverse(capfd):
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    bfs_traverse(graph, "A")
    out, err = capfd.readouterr()
    assert out == "A B C D E F "