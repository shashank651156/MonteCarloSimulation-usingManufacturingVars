import random
import matplotlib.pyplot as plt

def simulate_production_cycle():
    raw_material_time = random.uniform(1, 3)
    cutting_time = random.uniform(2, 5)
    assembly_time = random.uniform(1, 2)
    quality_control_time = random.uniform(0.5, 1)
    packaging_time = random.uniform(1, 2)

    total_time = (raw_material_time + cutting_time + assembly_time + 
                  quality_control_time + packaging_time)

    if random.random() < 0.1:  # Machine downtime
        total_time *= 1.2
    if random.random() > 0.8:  # Worker efficiency
        total_time *= 1.1
    if random.random() > 0.9:  # Material quality affects quality control time
        quality_control_time *= 1.5

    return total_time

# Run the simulation 1000 times
simulation_results = [simulate_production_cycle() for _ in range(1000)]

# Plotting
plt.figure(figsize=(6, 3))  # Adjusted size to how to asdd 
plt.hist(simulation_results, bins=30, density=True, color='skyblue', alpha=0.7)
plt.axvline(10, color='r', label='Target Production Time (10 hours)')  # Target time at 10 hours
plt.title('Distribution of Production Times with Target Time')
plt.xlabel('Production Time (hours)')
plt.ylabel('Density')
plt.legend()
plt.show()

# Print some results
print(f"Percentage of production cycles meeting the target time: {sum(t <= 10 for t in simulation_results) / len(simulation_results) * 100:.2f}%")

"""
Features of Configurable Target Production Time:
Adaptability: Allows the simulation to be easily adjusted for different products or production conditions without altering the core code structure. This adaptability makes the simulation tool more robust and useful across various contexts.
Precision in Benchmarking: By setting a configurable target time, the company can tailor the benchmark to specific production goals or industry standards, providing a more accurate measure of performance.
Dynamic Strategy Implementation: Enables the company to dynamically alter production targets in response to changes in operational strategy or external market pressures, ensuring that the simulation remains relevant over time.
Use Case:
Scenario: A widget manufacturing company is looking to optimize its production lines to meet varying demand cycles throughout the year. During peak seasons, the company aims to reduce production time to meet increased demand, whereas, in off-peak times, the focus shifts towards cost optimization and efficiency.
Application: The company integrates the Monte Carlo simulation with a user interface that allows managers to input a target production time based on current business objectives. The simulation outputs help managers understand the likelihood of meeting these targets under current conditions and identify where adjustments are needed. This strategic use of configurable targets helps the company remain agile and responsive to market conditions, enhancing its competitive edge.
This approach ensures that the simulation not only provides generic insights but also delivers tailored, actionable information that directly supports the company's operational goals.
"""
