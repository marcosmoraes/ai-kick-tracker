# Architecture

## Overview
This project implements a free kick analysis system using machine learning to predict and analyze free kick trajectories.

## Components

### Data Generation
- `generate_dataset.py`: Generates synthetic free kick data for training and testing
- Output: `simulated_kicks_1000.json`

### Analysis
- `free_kick_analysis.py`: Main analysis module for processing and visualizing free kick data
- Outputs:
  - `grafico.png`: Visualization of kick trajectories
  - `performance_report.pdf`: Detailed analysis report

## Data Flow
1. Data Generation
   - Synthetic data is generated with various parameters
   - Data is stored in JSON format

2. Analysis
   - Data is loaded and processed
   - Trajectories are analyzed
   - Results are visualized and reported

## Dependencies
- Python 3.x
- Required packages (to be listed) 