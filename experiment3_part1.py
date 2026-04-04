import matplotlib.pyplot as plt
import csv
from final_project_part1 import create_random_sparse_graph, dijkstra, total_dist, dijkstra_approx, bellman_ford_approx

n = 100 #number of nodes
p = 0.25 #probability of an edge existing between two nodes
source = 0
trials = 100
k_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 50] #different number of max relaxations per node to test

dijkstra_totals = [0] * len(k_vals) #list to store the total distances for each k using Dijkstra's
bellman_totals = [0] * len(k_vals) #list to store the total distances for each k using Bellman-Ford's
exact_total_sum = 0

for t in range(trials):
    G = create_random_sparse_graph(n, p, 50) #create a new random graph for each trial
    
    exact_dist = dijkstra(G, source) #calculate the exact distances using Dijkstra's algorithm
    exact_total = total_dist(exact_dist) #calculate the total distance from the source to all other nodes
    exact_total_sum += exact_total

    for i, k in enumerate(k_vals):
        dijkstra_approx_dist = dijkstra_approx(G, source, k) #calculate the approximate distances using Dijkstra's algorithm
        bellman_ford_approx_dist = bellman_ford_approx(G, source, k) #calculate the approximate distances using Bellman-Ford's algorithm
        dijkstra_totals[i] += total_dist(dijkstra_approx_dist) #add the total distance for this trial to the corresponding k value
        bellman_totals[i] += total_dist(bellman_ford_approx_dist) #add the total distance for this trial to the corresponding k value

dijkstra_avg = [total / trials for total in dijkstra_totals] #calculate the average total distance for each k value using Dijkstra's approximation
bellman_avg = [total / trials for total in bellman_totals] #calculate the average total distance for each k value using Bellman-Ford's approximation
exact_avg = exact_total_sum / trials #calculate the average total distance for the exact distances

#save the results to a CSV file
with open("csv/experiment3_part1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["k", "dijkstra_approx_avg", "bellman_ford_approx_avg", "exact_avg"])
    for i in range(len(k_vals)):
        writer.writerow([k_vals[i], dijkstra_avg[i], bellman_avg[i], exact_avg])

#plot the results
plt.figure()
plt.plot(k_vals, dijkstra_avg, label="Dijkstra's Approximation")
plt.plot(k_vals, bellman_avg, label="Bellman-Ford's Approximation")
plt.plot(k_vals, [exact_avg]*len(k_vals), label="Exact Distance")
plt.xlabel("Maximum Relaxations per Node")
plt.ylabel("Total Distance")
plt.legend()
plt.savefig("graphs/experiment3_part1.png")
plt.show()