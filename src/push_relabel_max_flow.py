from typing import List, Dict, Optional

class PushRelabelMaxFlow:
    """
    Implements the Push-Relabel algorithm for computing maximum flow in a graph.
    
    This implementation uses the generic push-relabel method with the highest-label 
    selection rule to find the maximum flow between a source and sink node.
    
    Attributes:
        num_vertices (int): Number of vertices in the graph
        graph (List[List[int]]): Adjacency matrix representing the flow network
        flow (List[List[int]]): Flow matrix tracking current flow between vertices
        height (List[int]): Height (or level) of each vertex
        excess_flow (List[int]): Excess flow at each vertex
    """
    
    def __init__(self, num_vertices: int):
        """
        Initialize the push-relabel max flow algorithm.
        
        Args:
            num_vertices (int): Number of vertices in the graph
        """
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]
        self.flow = [[0] * num_vertices for _ in range(num_vertices)]
        self.height = [0] * num_vertices
        self.excess_flow = [0] * num_vertices
    
    def add_edge(self, u: int, v: int, capacity: int):
        """
        Add an edge to the graph with a given capacity.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
            capacity (int): Edge capacity
        
        Raises:
            ValueError: If vertices are out of range
        """
        if not (0 <= u < self.num_vertices and 0 <= v < self.num_vertices):
            raise ValueError("Vertex indices out of range")
        
        self.graph[u][v] = capacity
    
    def push(self, u: int, v: int):
        """
        Push flow from vertex u to vertex v.
        
        Args:
            u (int): Source vertex
            v (int): Destination vertex
        """
        # Determine the amount of flow that can be pushed
        delta = min(
            self.excess_flow[u], 
            self.graph[u][v] - self.flow[u][v]
        )
        
        # Update flow
        self.flow[u][v] += delta
        self.flow[v][u] -= delta
        
        # Update excess flow
        self.excess_flow[u] -= delta
        self.excess_flow[v] += delta
    
    def relabel(self, u: int):
        """
        Relabel vertex u by updating its height.
        
        Args:
            u (int): Vertex to relabel
        """
        # Find the minimum height of adjacent vertices with residual capacity
        min_height = float('inf')
        for v in range(self.num_vertices):
            if self.graph[u][v] > self.flow[u][v]:
                min_height = min(min_height, self.height[v])
        
        # Update height
        self.height[u] = min_height + 1
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow from source to sink.
        
        Args:
            source (int): Source vertex index
            sink (int): Sink vertex index
        
        Returns:
            int: Maximum flow value
        
        Raises:
            ValueError: If source or sink are out of range
        """
        # Validate source and sink
        if not (0 <= source < self.num_vertices and 0 <= sink < self.num_vertices):
            raise ValueError("Source or sink vertex index out of range")
        
        if source == sink:
            return 0
        
        # Initialize height and excess flow
        self.height[source] = self.num_vertices
        
        # Initial push from source to its neighbors
        for v in range(self.num_vertices):
            if self.graph[source][v] > 0:
                self.flow[source][v] = self.graph[source][v]
                self.flow[v][source] = -self.graph[source][v]
                self.excess_flow[v] = self.graph[source][v]
                self.excess_flow[source] -= self.graph[source][v]
        
        # Discharge vertices with excess flow
        while True:
            # Find a vertex with excess flow that is not the source or sink
            active_vertex = None
            for u in range(self.num_vertices):
                if u != source and u != sink and self.excess_flow[u] > 0:
                    active_vertex = u
                    break
            
            # If no active vertex, we're done
            if active_vertex is None:
                break
            
            # Try to push excess flow
            push_possible = False
            for v in range(self.num_vertices):
                # Push if there's residual capacity and height conditions are met
                if (self.graph[active_vertex][v] > self.flow[active_vertex][v] and 
                    self.height[active_vertex] > self.height[v]):
                    self.push(active_vertex, v)
                    push_possible = True
                    break
            
            # If no push is possible, relabel the vertex
            if not push_possible:
                self.relabel(active_vertex)
        
        # Return the maximum flow to the sink
        return sum(self.flow[sink])