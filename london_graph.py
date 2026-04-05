import csv
from undirected_weighted_graph import UndirectedWeightedGraph
import math


stations = {}
with open('london_stations.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        stations[row['id']] = (float(row['longitude']), float(row['latitude']))

def getDist(s, d):
    a = stations[s][0] - stations[d][0]
    b = stations[s][1] - stations[d][1]
    c = math.sqrt(a ** 2 + b ** 2)
    return c

connections = {}
with open('london_connections.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        s = row['station1']
        d = row['station2']
        if s not in connections:
            connections[s] = {}
        if d not in connections:
            connections[d] = {}
        connections[s][d] = {"dist": getDist(s, d), "line": row["line"]}
        connections[d][s] = {"dist": getDist(d, s), "line": row["line"]}

heuristic = {}
for s in stations:
    for d in stations:
        if s not in heuristic:
            heuristic[s] = {}
        heuristic[s][d] = getDist(s, d)

#add nodes
G = UndirectedWeightedGraph()
for node in stations.keys():
    G.add_node(node)

#add edges
for n1 in connections.keys():
    for n2 in connections[n1].keys():
        G.add_edge(n1, n2, connections[n1][n2]["dist"])


