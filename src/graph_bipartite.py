from typing import List, Dict

def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Check if a graph is bipartite using breadth-first search.
    
    A bipartite graph is a graph whose vertices can be divided into two 
    independent sets such that every edge connects a vertex in one set 
    to a vertex in the other set.
    
    Args:
        graph (List[List[int]]): Adjacency list representation of the graph
                                 where graph[i] contains neighbors of vertex i
    
    Returns:
        bool: True if the graph is bipartite, False otherwise
    
    Raises:
        ValueError: If the graph is empty or contains invalid vertices
    """
    # Handle empty graph
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Initialize color array (0: uncolored, 1: first color, -1: second color)
    colors = [0] * len(graph)
    
    # Check each unvisited vertex
    for start in range(len(graph)):
        # Skip already colored vertices
        if colors[start] != 0:
            continue
        
        # Use BFS to color the graph
        colors[start] = 1
        queue = [start]
        
        while queue:
            current = queue.pop(0)
            
            # Check neighbors
            for neighbor in graph[current]:
                # Validate neighbor index
                if neighbor < 0 or neighbor >= len(graph):
                    raise ValueError(f"Invalid vertex index: {neighbor}")
                
                # If neighbor is uncolored, color it opposite of current
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[current]
                    queue.append(neighbor)
                
                # If neighbor has same color as current, graph is not bipartite
                elif colors[neighbor] == colors[current]:
                    return False
    
    return True