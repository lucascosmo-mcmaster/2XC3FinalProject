from london_graph import stations, connections, heuristic, G
from search_algs import a_star, dijkstra
import time
import matplotlib.pyplot as plt


all_trips = []
for s in stations.keys():
    for d in stations.keys():
        if s != d:
            all_trips.append((s, d))


large_paths = []
time_diffs = []
path_lengths = []
for s, d in all_trips:
    start = time.perf_counter()
    a_star_results = a_star(G, s, d, heuristic)
    end = time.perf_counter()
    a_time = (end - start)
    
    start = time.perf_counter()
    dijkstra_results = dijkstra(G, s, d)
    end = time.perf_counter()
    d_time = end - start
    diff = 1000*(a_time - d_time)

    time_diffs.append(diff)
    if (len(a_star_results[1]) != len(dijkstra_results[1])):
        print("Path lenght mismatch on ", s , " to ", d)
        break
    else:
        path_lengths.append(len(a_star_results[1]))
    if len(a_star_results[1]) > 20:
        large_paths.append((s,d))
    
time_diffs = []
path_lengths = []
for s, d in large_paths:
    start = time.perf_counter()
    a_star_results = a_star(G, s, d, heuristic)
    end = time.perf_counter()
    a_time = (end - start)
    
    start = time.perf_counter()
    dijkstra_results = dijkstra(G, s, d)
    end = time.perf_counter()
    d_time = end - start
    diff = 1000*(a_time - d_time)

    time_diffs.append(diff)
    path_lengths.append(len(a_star_results[1]))

plt.scatter(path_lengths, time_diffs)
plt.xlabel('Path length (nodes)', fontsize=12, fontweight='bold')
plt.ylabel('Runtime difference (miliseconds)', fontsize=12, fontweight='bold')
plt.title('Performance Comparison: Dijkstra vs A*', pad=15)
plt.savefig('Dijkstra_vs_A_star_largepaths.png', dpi=300)
plt.show()
