from min_heap import MinHeap, Element
from final_project_part1 import DirectedWeightedGraph

def getPath(n, pred):
    path = [n]
    current = n
    while current in pred:
        path.append(pred[current])
        current = pred[current]
    path.reverse()
    return path

def a_star(G: DirectedWeightedGraph, s, d, h):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(s, 0 + h[s])
    dist[s] = 0

    #Meat of the algorithm
    while not Q.is_empty(): 
        current_element = Q.extract_min() #grab next
        current_node = current_element.value
        if current_node == d:
            return (pred, getPath(d, pred))
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]: #found a shorter path to neighbour
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour) + h[neighbour]) # add h to queue determination
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    
    




    