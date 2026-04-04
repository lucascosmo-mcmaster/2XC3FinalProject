import csv
from dataclasses import dataclass
from final_project_part1 import DirectedWeightedGraph
from search_algs import a_star, dijkstra
import math
import time
import matplotlib.pyplot as plt
import numpy as np

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
        connections[s][d] = getDist(s, d)

heuristic = {}
for s in stations:
    for d in stations:
        if s not in heuristic:
            heuristic[s] = {}
        heuristic[s][d] = getDist(s, d)

#add nodes
G = DirectedWeightedGraph()
for node in stations.keys():
    G.add_node(node)

#add edges
for n1 in connections.keys():
    for n2 in connections[n1].keys():
        G.add_edge(n1, n2, connections[n1][n2])

# experiment setup

#list all possible trips
#run both experiments on each; track times(y) vs: lines(x), transfers(x), dist(x)
    
all_trips = []
for s in stations.keys():
    for d in stations.keys():
        if s != d:
            all_trips.append((s, d))

time_diffs = []
lens = []
count = 0
for s, d in all_trips:
    start = time.perf_counter()
    a_star_results = a_star(G, s, d, heuristic[s])
    end = time.perf_counter()
    a_time = (end - start)
    
    start = time.perf_counter()
    dijkstra_results = dijkstra(G, s, d)
    end = time.perf_counter()
    d_time = end - start
    time_diffs.append(a_time - d_time)
    if (len(a_star_results[1]) != len(dijkstra_results[1])):
        print("Path lenght mismatch on ", s , " to ", d)
        break
    else:
        lens.append(len(a_star_results[1]))

plt.plot(lens, time_diffs)
plt.legend()
plt.xlabel('Path Length (Number of Nodes)', fontsize=12, fontweight='bold')
plt.ylabel('Runtime difference (Seconds)', fontsize=12, fontweight='bold')
plt.title('Performance Comparison: Dijkstra vs A*', pad=15)
plt.savefig('Dijkstra_vs_A*_length.png', dpi=300)
plt.show()



