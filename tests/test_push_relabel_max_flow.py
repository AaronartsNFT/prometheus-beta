import pytest
from src.push_relabel_max_flow import PushRelabelMaxFlow

def test_simple_max_flow():
    """
    Test a simple flow network with a known max flow.
    """
    # Create a simple graph: 0 (source) -> 1 -> 2 (sink)
    max_flow_solver = PushRelabelMaxFlow(3)
    max_flow_solver.add_edge(0, 1, 10)  # source to intermediate
    max_flow_solver.add_edge(1, 2, 10)  # intermediate to sink
    
    assert max_flow_solver.max_flow(0, 2) == 10

def test_complex_max_flow():
    """
    Test a more complex flow network with multiple paths.
    """
    # More complex graph with multiple paths
    max_flow_solver = PushRelabelMaxFlow(4)
    max_flow_solver.add_edge(0, 1, 3)
    max_flow_solver.add_edge(0, 2, 2)
    max_flow_solver.add_edge(1, 2, 1)
    max_flow_solver.add_edge(1, 3, 3)
    max_flow_solver.add_edge(2, 3, 4)
    
    assert max_flow_solver.max_flow(0, 3) == 5

def test_no_flow_between_same_vertex():
    """
    Test that no flow is returned when source and sink are the same.
    """
    max_flow_solver = PushRelabelMaxFlow(3)
    max_flow_solver.add_edge(0, 1, 10)
    
    assert max_flow_solver.max_flow(1, 1) == 0

def test_zero_capacity_graph():
    """
    Test a graph with no capacity.
    """
    max_flow_solver = PushRelabelMaxFlow(3)
    assert max_flow_solver.max_flow(0, 2) == 0

def test_invalid_vertex_index():
    """
    Test error handling for invalid vertex indices.
    """
    max_flow_solver = PushRelabelMaxFlow(3)
    
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(-1, 2)
    
    with pytest.raises(ValueError):
        max_flow_solver.max_flow(0, 3)

def test_add_edge_invalid_vertex():
    """
    Test error handling when adding an edge with invalid vertices.
    """
    max_flow_solver = PushRelabelMaxFlow(3)
    
    with pytest.raises(ValueError):
        max_flow_solver.add_edge(-1, 1, 10)
    
    with pytest.raises(ValueError):
        max_flow_solver.add_edge(0, 3, 10)