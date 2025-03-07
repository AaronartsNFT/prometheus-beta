import pytest
from src.graph_bipartite import is_bipartite

def test_bipartite_graph():
    """Test a simple bipartite graph"""
    graph = [[1,3], [0,2], [1,3], [0,2]]
    assert is_bipartite(graph) == True

def test_non_bipartite_graph():
    """Test a graph that is not bipartite"""
    graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
    assert is_bipartite(graph) == False

def test_disconnected_bipartite_graph():
    """Test a disconnected bipartite graph"""
    graph = [[1], [0,2,3], [1], [1]]
    assert is_bipartite(graph) == True

def test_disconnected_non_bipartite_graph():
    """Test a disconnected non-bipartite graph"""
    graph = [[1,2], [0,2], [0,1]]
    assert is_bipartite(graph) == False

def test_single_vertex_graph():
    """Test a graph with a single vertex"""
    graph = [[]]
    assert is_bipartite(graph) == True

def test_two_vertex_graph():
    """Test a graph with two vertices connected"""
    graph = [[1], [0]]
    assert is_bipartite(graph) == True

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        is_bipartite([])

def test_invalid_vertex_index():
    """Test that an invalid vertex index raises a ValueError"""
    with pytest.raises(ValueError):
        is_bipartite([[1], [2]])  # Vertex 2 does not exist