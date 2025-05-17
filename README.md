# AI Kick Tracker

A performance analysis tool for tracking and analyzing free kick performance in soccer. This project processes simulated free kick data to generate performance insights, visualizations, and recommendations for athletes.

## Features

1. **Data Processing**
   - Loads and processes free kick data from JSON format
   - Validates required data fields (kick number, result, distance, angle, height, velocity)
   - Calculates cumulative success rate

2. **Performance Analysis**
   - Tracks success rate evolution over time
   - Identifies optimal ranges for key variables:
     - Distance (meters)
     - Angle (degrees)
     - Height (meters)
     - Velocity (m/s)
   - Generates trend analysis using linear regression

3. **Visualization**
   - Creates performance evolution graphs
   - Includes trend line for performance analysis
   - Saves high-resolution visualization (300 DPI)

4. **Report Generation**
   - Generates comprehensive PDF reports including:
     - Performance summary (initial and final success rates)
     - Improvement metrics
     - Optimal variable ranges
     - Training recommendations

## Project Structure

```
ai-kick-tracker/
├── free_kick_analysis.py     # Main analysis script
├── generate_dataset.py       # Dataset generation script
├── simulated_kicks_1000.json # Sample dataset
├── performance_graph.png     # Generated performance graph
└── performance_report.pdf    # Generated performance report
```

## Requirements

Install the required dependencies:

```bash
pip install pandas scikit-learn matplotlib fpdf
```

## Usage

1. **Generate Sample Dataset**
   ```bash
   python generate_dataset.py
   ```
   This will create a simulated dataset of 1000 free kicks.

2. **Run Analysis**
   ```bash
   python free_kick_analysis.py
   ```
   This will:
   - Process the free kick data
   - Generate performance visualizations
   - Create a PDF report with insights

## Output

The analysis generates two main outputs:
1. `performance_graph.png`: A visualization of the athlete's performance evolution
2. `performance_report.pdf`: A detailed report containing:
   - Performance metrics
   - Success rate analysis
   - Optimal variable ranges
   - Training recommendations

## Data Format

The input JSON file should contain an array of free kick attempts with the following structure:
```json
{
    "kick": number,       // Kick number
    "distance": number,   // Distance in meters
    "angle": number,      // Angle in degrees
    "height": number,     // Height in meters
    "velocity": number,   // Velocity in m/s
    "result": number      // Result (1 for success, 0 for failure)
}
```

## Contributing

Feel free to submit issues and enhancement requests.
