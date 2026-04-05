from london_graph import stations, connections, heuristic, G
from search_algs import a_star, dijkstra
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

time_diffs = []
transfers = []
count = 0
for s, d in all_trips:
    start = time.perf_counter()
    a_star_results = a_star(G, s, d, heuristic)
    end = time.perf_counter()
    a_time = (end - start)
    
    start = time.perf_counter()
    dijkstra_results = dijkstra(G, s, d)
    end = time.perf_counter()
    d_time = end - start
    diff = a_time - d_time

    time_diffs.append(1000 * diff)
    if (numTransfers(a_star_results[1]) != numTransfers(dijkstra_results[1])):
        print("Transfer count mismatch on ", s , " to ", d)
        break
    else:
        transfers.append(numTransfers(a_star_results[1]))


plt.scatter(transfers, time_diffs)
plt.xlabel('Transfers', fontsize=12, fontweight='bold')
plt.ylabel('Runtime difference (miliseconds)', fontsize=12, fontweight='bold')
plt.title('Performance Comparison: Dijkstra vs A*', pad=15)
plt.savefig('Dijkstra_vs_A_star_transfers.png', dpi=300)
plt.show()
