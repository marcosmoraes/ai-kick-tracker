import json
import random

# Function to generate a simulated dataset
def generate_kicks(qty=1000):
    kicks = []
    for i in range(1, qty + 1):
        kick = {
            "kick": i,
            "distance": round(random.uniform(10, 30), 1),  # Distance in meters
            "angle": round(random.uniform(20, 60), 1),    # Angle in degrees
            "height": round(random.uniform(0.5, 3.0), 1),  # Height in meters
            "velocity": round(random.uniform(10, 40), 1), # Velocity in m/s
            "result": random.choice([0, 1])             # Result (0 or 1)
        }
        kicks.append(kick)
    return kicks

# Generate 1000 simulated kicks
dataset = generate_kicks(1000)

# Save to JSON file
with open("simulated_kicks_1000.json", "w") as file:
    json.dump(dataset, file, indent=4)

print("Dataset generated successfully!")
