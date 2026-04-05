from london_graph import stations, connections, heuristic, G
from search_algs import a_star_visits, dijkstra_visits
import time
import matplotlib.pyplot as plt


all_trips = []
for s in stations.keys():
    for d in stations.keys():
        if s != d:
            all_trips.append((s, d))

def numTransfers(path):
    if (len(path) < 3):
        return 0
    first = path[0]
    second = path[1]
    line = connections[first][second]["line"]
    count = 0
    current = second
    for next in path[2:]:
        if line != connections[current][next]["line"]:
            count += 1
        current = next
    return count


a_num_seen = []
d_num_seen = []
path_length = []
count = 0
for s, d in all_trips:
    start = time.perf_counter()
    a_star_results = a_star_visits(G, s, d, heuristic)
    end = time.perf_counter()
    a_time = (end - start)
    
    start = time.perf_counter()
    dijkstra_results = dijkstra_visits(G, s, d)
    end = time.perf_counter()
    d_time = end - start
    diff = a_time - d_time
    path_length.append(len(a_star_results[1]))
    a_num_seen.append(a_star_results[2])
    d_num_seen.append(dijkstra_results[2])

plt.scatter(path_length, a_num_seen)
plt.scatter(path_length, d_num_seen)
plt.xlabel('Path length (nodes)', fontsize=12, fontweight='bold')
plt.ylabel('Total nodes visited', fontsize=12, fontweight='bold')
plt.title('Performance Comparison: Dijkstra vs A*', pad=15)
plt.savefig('Dijkstra_vs_A_star_visited.png', dpi=300)
plt.show()
