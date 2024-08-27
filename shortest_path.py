import heapq

class Graph:
  def __init__(self):
      self.vertices = {}

  def add_vertex(self, vertex):
      if vertex not in self.vertices:
          self.vertices[vertex] = {}

  def add_edge(self, source, destination, weight):
      if source in self.vertices and destination in self.vertices:
          self.vertices[source][destination] = weight
          self.vertices[destination][source] = weight  # For undirected graph

  def get_neighbors(self, vertex):
      if vertex in self.vertices:
          return self.vertices[vertex]
      else:
          return {}
  
  def dijkstra(self,start,end):
    distances = {vertex: float('inf') for vertex in self.vertices}
    distances[start] = 0
    pq = [(0,start)]
    
    while pq:
      current_distance, current_vertex = heapq.heappop(pq)
      if current_distance > distances[current_vertex]:
        continue
      for neighbor, weight in self.vertices[current_vertex].items():
        distance = current_distance + weight
        print(distance)
        print(weight)
        print(neighbor)
        if distance < distances[neighbor]:
          distances[neighbor] = distance
          heapq.heappush(pq,(distance,neighbor))
    return distances[end]

# Example usage:
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_edge('A', 'B', 5)
graph.add_edge('D', 'B', 13)
graph.add_edge('E', 'B', 8)
graph.add_edge('F', 'B', 6)
graph.add_edge('D', 'C', 6)
graph.add_edge('E', 'A', 12)
graph.add_edge('F', 'C', 21)
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 3)
graph.add_edge('A', 'C', 10)
distances = graph.dijkstra("F","A")
print("Shortest distance from Vertex 'A' to 'C':",distances)
print(graph.vertices)