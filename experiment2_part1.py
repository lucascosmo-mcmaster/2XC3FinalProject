import matplotlib.pyplot as plt
import csv
from final_project_part1 import create_random_complete_graph, dijkstra, total_dist, dijkstra_approx, bellman_ford_approx

num_nodes = list(range(1, 300, 20)) #different numbers of nodes for testing
source = 0
trials = 30
k = 1

dijkstra_totals = {}
bellman_totals = {}
exact_total_sum = {}

for n in num_nodes:
    dijkstra_totals[n] = 0
    bellman_totals[n] = 0
    exact_total_sum[n] = 0

for n in num_nodes:
    for t in range(trials):
        G = create_random_complete_graph(n, 50) #create a new random graph for each trial
        
        exact_dist = dijkstra(G, source) #calculate the exact distances using Dijkstra's algorithm
        exact_total = total_dist(exact_dist) #calculate the total distance from the source to all other nodes
        exact_total_sum[n] += exact_total

        dijkstra_approx_dist = dijkstra_approx(G, source, k) #calculate the approximate distances using Dijkstra's algorithm
        bellman_ford_approx_dist = bellman_ford_approx(G, source, k) #calculate the approximate distances using Bellman-Ford's algorithm
        dijkstra_totals[n] += total_dist(dijkstra_approx_dist) #add the total distance for this trial to the corresponding number of nodes
        bellman_totals[n] += total_dist(bellman_ford_approx_dist) #add the total distance for this trial to the corresponding number of nodes

dijkstra_avg = []
bellman_avg = []
exact_avg = []

for n in num_nodes:
    dijkstra_avg.append(dijkstra_totals[n] / trials)
    bellman_avg.append(bellman_totals[n] / trials)
    exact_avg.append(exact_total_sum[n] / trials)

#save the results to a CSV file
with open("csv/experiment2_part1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["num_nodes", "dijkstra_approx_avg", "bellman_ford_approx_avg", "exact_avg"])
    for i, n in enumerate(num_nodes):
        writer.writerow([n, dijkstra_avg[i], bellman_avg[i], exact_avg[i]])

#plot the results
plt.figure()
plt.plot(num_nodes, dijkstra_avg, label="Dijkstra's Approximation")
plt.plot(num_nodes, bellman_avg, label="Bellman-Ford's Approximation")
plt.plot(num_nodes, exact_avg, label="Exact Distance")
plt.xlabel("Number of Nodes")
plt.ylabel("Total Distance")
plt.legend()
plt.savefig("graphs/experiment2_part1.png")
plt.show()