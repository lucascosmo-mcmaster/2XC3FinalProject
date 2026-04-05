from min_heap import MinHeap, Element
from undirected_weighted_graph import UndirectedWeightedGraph

def getPath(n, pred):
    path = [n]
    current = n
    while current in pred:
        path.append(pred[current])
        current = pred[current]
    path.reverse()
    return path


def a_star(G: UndirectedWeightedGraph, s, d, h):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    visited = set()
    Q = MinHeap([])

    #Initialize priority queue/heap and distances
    Q.insert(Element(s, h[s][d]))
    dist[s] = 0

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        if (current_node == d):
            return (pred, getPath(d, pred))
        visited.add(current_node)
        for neighbour in G.adj[current_node]:
            if (neighbour not in Q.map and neighbour not in visited):
                Q.insert(Element(neighbour, dist[current_node] + G.w(current_node, neighbour) + h[neighbour][d]))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
            elif dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour) + h[neighbour][d])
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    print("didnt find ", d, " in ", visited, "leaving from ", s)
    
    
def dijkstra(G, s, d): #for our comparisons we need a djikstra that only searches for one node 'd' 
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    visited = set()
    Q = MinHeap([])

    #Initialize priority queue/heap and distances
    Q.insert(Element(s, 0))
    dist[s] = 0

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        if (current_node == d):
            return (pred, getPath(d, pred))
        visited.add(current_node)
        for neighbour in G.adj[current_node]:
            if (neighbour not in Q.map and neighbour not in visited):
                Q.insert(Element(neighbour, dist[current_node] + G.w(current_node, neighbour)))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
            elif dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return None


def a_star_visits(G: UndirectedWeightedGraph, s, d, h):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    visited = set()
    Q = MinHeap([])

    #Initialize priority queue/heap and distances
    Q.insert(Element(s, h[s][d]))
    dist[s] = 0

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        if (current_node == d):
            return (pred, getPath(d, pred), len(visited))
        visited.add(current_node)
        for neighbour in G.adj[current_node]:
            if (neighbour not in Q.map and neighbour not in visited):
                Q.insert(Element(neighbour, dist[current_node] + G.w(current_node, neighbour) + h[neighbour][d]))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
            elif dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour) + h[neighbour][d])
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    print("didnt find ", d, " in ", visited, "leaving from ", s)
    
    
def dijkstra_visits(G, s, d): #for our comparisons we need a djikstra that only searches for one node 'd' 
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    visited = set()
    Q = MinHeap([])

    #Initialize priority queue/heap and distances
    Q.insert(Element(s, 0))
    dist[s] = 0

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        if (current_node == d):
            return (pred, getPath(d, pred), len(visited))
        visited.add(current_node)
        for neighbour in G.adj[current_node]:
            if (neighbour not in Q.map and neighbour not in visited):
                Q.insert(Element(neighbour, dist[current_node] + G.w(current_node, neighbour)))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
            elif dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return None