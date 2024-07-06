from copy import deepcopy
from typing import Optional
from collections import deque

adj_list = [[2,4],[1,3],[2,4],[1,3]]

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        clones = {node: Node(node.val)}  # Maps original nodes to their clones
        queue = deque([node])  # BFS queue initialized with the start node
        
        while queue:
            # get node from queue
            current = queue.popleft()
            
            for neighbor in current.neighbors:
                if neighbor not in clones:  # If neighbor hasn't been cloned
                    clones[neighbor] = Node(neighbor.val)  # Clone and add to map
                    queue.append(neighbor)  # Enqueue for subsequent processing
                # add clone as neighbor node to the current node
                clones[current].neighbors.append(clones[neighbor])  # Link clone to its neighbors
        
        for k,v in clones.items():
            print(f'k:{k.val}, v:{v.val}')
        return clones[node]


# write driver here, send in first node of global adj_list
if __name__ == "__main__":
    # Adjacency list
    adj_list = [[2,4],[1,3],[2,4],[1,3]]

    # Create nodes for each entry in the adjacency list
    nodes = [Node(i + 1) for i in range(len(adj_list))]

    # Connect nodes as per the adjacency list
    for i, node in enumerate(nodes):
        node.neighbors = [nodes[j - 1] for j in adj_list[i]]

    # Solution instance
    solution = Solution()
    cloned_graph = solution.cloneGraph(nodes[0])  # Passing the first node to clone the graph

    # Function to print the graph to verify cloning
    def print_graph(node, visited=set()):
        if node in visited:
            return
        visited.add(node)
        print(f'Node {node.val}:', ' -> '.join(str(neighbor.val) for neighbor in node.neighbors))
        for neighbor in node.neighbors:
            print_graph(neighbor, visited)

    # Print original and cloned graph for comparison
    print("Original graph:")
    print_graph(nodes[0])

    print("\nCloned graph:")
    print_graph(cloned_graph)
    