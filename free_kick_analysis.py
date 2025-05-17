import json
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from fpdf import FPDF

# Load JSON
try:
    with open("simulated_kicks_1000.json", "r") as file:
        dataset = json.load(file)
except FileNotFoundError:
    print("Error: File 'simulated_kicks.json' not found.")
    exit()
except json.JSONDecodeError:
    print("Error: File 'simulated_kicks.json' does not contain valid JSON.")
    exit()

# Convert JSON to DataFrame
df = pd.DataFrame(dataset)

# Validate required columns
required_columns = ["kick", "result", "distance", "angle", "height", "velocity"]
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    print(f"Error: The following columns are missing in the JSON: {', '.join(missing_columns)}")
    exit()

# Calculate cumulative success rate
df = df.sort_values(by="kick")  # Sort by kick number
df["cumulative_success"] = df["result"].expanding().mean() * 100  # Cumulative rate in %

# Identify optimal ranges for each variable based on successful kicks
success_data = df[df["result"] == 1]
distance_range = (success_data["distance"].min(), success_data["distance"].max())
angle_range = (success_data["angle"].min(), success_data["angle"].max())
height_range = (success_data["height"].min(), success_data["height"].max())
velocity_range = (success_data["velocity"].min(), success_data["velocity"].max())

# Create performance evolution graph
plt.figure(figsize=(12, 10))  # Adjust graph size
plt.plot(df["kick"], df["cumulative_success"], color="blue", label="Cumulative Success Rate")

# Add trend line
model = LinearRegression()
kicks = df["kick"].values.reshape(-1, 1)
success = df["cumulative_success"].values
model.fit(kicks, success)
trend = model.predict(kicks)
plt.plot(df["kick"], trend, color="red", linestyle="--", label="Trend Line")

# Configure graph
plt.title("Athlete Performance Evolution", fontsize=16)
plt.xlabel("Kick Number", fontsize=12)
plt.ylabel("Cumulative Success Rate (%)", fontsize=12)
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# Calculate percentage improvement from start to end
improvement = success[-1] - success[0]
report = f"""
=== Performance Evolution Report ===

Summary:
- Start: Success rate of {success[0]:.2f}%.
- End: Success rate of {success[-1]:.2f}%.
- Improvement over time: {improvement:.2f}%. 

Insights:
- The athlete is {"improving" if improvement > 0 else "maintaining" if improvement == 0 else "regressing"} their performance with training.

Optimal Variable Ranges:
1. Distance: Between {distance_range[0]:.1f} and {distance_range[1]:.1f} meters.
2. Angle: Between {angle_range[0]:.1f}° and {angle_range[1]:.1f}°.
3. Height: Between {height_range[0]:.1f}m and {height_range[1]:.1f}m.
4. Velocity: Between {velocity_range[0]:.1f}m/s and {velocity_range[1]:.1f}m/s.

Recommendations:
- Focus on optimal ranges to maximize performance.
- Continue monitoring results for continuous training adjustments.
"""

# Save graph as image in project root
plt.tight_layout()
plt.savefig("performance_graph.png", dpi=300)  # Save in project root

# Create PDF with graph and report
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Insert graph in PDF
pdf.image("performance_graph.png", x=10, y=10, w=190)

# Add report below graph
pdf.ln(150)  # Adjust text position below graph
pdf.set_font("Arial", size=10)
pdf.multi_cell(0, 10, report)

# Save final PDF in project root
pdf.output("performance_report.pdf")

# Display final message
print("PDF generated successfully. You can access the file 'performance_report.pdf' in your project root.")
