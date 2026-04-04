import matplotlib.pyplot as plt
import time
import csv
from final_project_part1 import create_random_negative_graph, mystery

num_nodes = list(range(1, 200, 20))
p = 0.5
trials = 50
times = []

#run experiments for each number of nodes and average the execution time over multiple trials
for n in num_nodes:
    total_time = 0
    
    for t in range(trials):
        G = create_random_negative_graph(n, p)
        
        start = time.time()
        mystery(G)
        end = time.time()
        
        total_time += (end - start)
    
    avg_time = total_time / trials
    times.append(avg_time)

#save the results to a CSV file
with open("csv/mystery_experiment_part1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["n", "time"])
    for n, t in zip(num_nodes, times):
        writer.writerow([n, t])

#plot the results
plt.figure()
plt.plot(num_nodes, times)
plt.xlabel("Number of Nodes")
plt.ylabel("Run Time")
plt.savefig("graphs/mystery_experiment_part1.png")
plt.show()

#plot the results on a log-log plot
plt.figure()
plt.loglog(num_nodes, times)
plt.xlabel("log(n)")
plt.ylabel("log(time)")
plt.savefig("graphs/mystery_loglog.png")
plt.show()