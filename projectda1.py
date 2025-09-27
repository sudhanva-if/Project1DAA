import time
import math
import matplotlib.pyplot as plt
import numpy as np

# n values #
n_values = [15, 16, 17, 18, 19, 20, 50, 100, 500, 1000, 2000, 4000, 8000, 16000, 32000]
exp_times = []
theo_values = []

# Measuring the experimental runtime with actual code #
for n in n_values:
    a = list(range(n))
    b = list(range(n))
    Sum = 0
    j = 2
    
    start = time.perf_counter()
    while j < n:
        k = j
        while k < n:
            Sum += a[j] * b[k]
            k = k * k
        j = 2 * j
    end = time.perf_counter()
    
    exp_times.append((end - start) * 1e3)  # Convert to milliseconds #
    theo_values.append(math.log2(n) * math.log2(math.log2(n)))  # Theoretical O(log n * log log n) #

# Compute averages and scaling factor #
avg_exp = np.mean(exp_times)
avg_theo = np.mean(theo_values)
scaling_factor = avg_exp / avg_theo
theo_scaled = [val * scaling_factor for val in theo_values]

# Print the averages and scaling #
print("\n=== Summary of Averages and Scaling ===")
print(f"Average Experimental Time (ms): {avg_exp:.6f}")
print(f"Average Theoretical Value     : {avg_theo:.6f}")
print(f"Scaling Factor (avg_exp/avg_theo): {scaling_factor:.6f}")

# Print table #
print("\n=== Detailed Table (Time in ms) ===")
print("n\tExperimental(ms)\tTheoretical\tScaled Theoretical(ms)")
for n, e, t, ts in zip(n_values, exp_times, theo_values, theo_scaled):
    print(f"{n}\t{e:.6f}\t\t{t:.6f}\t\t{ts:.6f}")

# Plot Experimental vs Scaled Theoretical Complexity #
plt.figure(figsize=(10,6))
plt.plot(n_values, exp_times, marker='o', label="Experimental Runtime (ms)")
plt.plot(n_values, theo_scaled, marker='s', label="Theoretical (scaled, ms)")
plt.xlabel("n")
plt.ylabel("Runtime (milliseconds) / Scaled Units")
plt.title("Experimental vs Theoretical Complexity (O(log n * log log n))")
plt.legend()
plt.grid(True)
plt.show()
