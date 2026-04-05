from london_graph import stations, connections, heuristic, G
from search_algs import a_star, dijkstra
import time
import matplotlib.pyplot as plt


same_line_trips = []
for s in stations.keys():
    for d in stations.keys():
        if s != d:
            if stations[s]['line'] == stations[d]['line']:
                same_line_trips.append((s, d))

time_diffs = []
index = []
count = 0
for s, d in same_line_trips:
    count += 1
    start = time.perf_counter()
    a_star_results = a_star(G, s, d, heuristic)
    end = time.perf_counter()
    a_time = (end - start)
    
    start = time.perf_counter()
    dijkstra_results = dijkstra(G, s, d)
    end = time.perf_counter()
    d_time = end - start
    diff = a_time - d_time

    time_diffs.append(diff)
    index.append(count)


plt.scatter(index, time_diffs)
plt.xlabel('Transfers', fontsize=12, fontweight='bold')
plt.ylabel('Runtime difference (Seconds)', fontsize=12, fontweight='bold')
plt.title('Performance Comparison: Dijkstra vs A*', pad=15)
plt.savefig('Dijkstra_vs_A_star_same_line.png', dpi=300)
plt.show()
