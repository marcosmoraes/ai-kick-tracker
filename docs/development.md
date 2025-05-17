# Development Guide

## Setup

1. Clone the repository
```bash
git clone https://github.com/marcosmoraes/ai-kick-tracker.git
cd ai-kick-tracker
```

2. Create and activate virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Development Workflow

1. Generate dataset
```bash
python generate_dataset.py
```

2. Run analysis
```bash
python free_kick_analysis.py
```

## Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions and classes

## Testing
- Write unit tests for new features
- Run tests before committing changes

## Contributing
1. Create a new branch for your feature
2. Make your changes
3. Run tests
4. Submit a pull request

## Common Issues and Solutions
(To be added as issues are encountered) 