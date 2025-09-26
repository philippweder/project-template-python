# Python Project Template for Academic Research

This repository template is specifically designed for scientific computing projects in Python. It provides a complete, production-ready structure that ensures reproducibility, portability, and maintainability of your research code.

## 🎯 When to Use This Template

Use this template when you need to:
- Develop a reusable Python package for your research
- Run reproducible experiments with configuration management
- Share your code with supervisors, peers, or the research community
- Maintain clean separation between core algorithms and experimental scripts
- Ensure your project works consistently across different environments

## 📁 Project Structure

```
your-project-name/
├── package-name/           # Your main Python package
│   ├── __init__.py        # Package initialization
│   ├── core/              # Core algorithms and models
│   │   └── __init__.py
│   ├── utils/             # Utility functions and helpers
│   │   └── some_utils.py
│   └── data/              # Small datasets and static files
│       └── some_data.txt
├── scripts/               # Experiment and analysis scripts
│   ├── experiments/       # Main experimental runs
│   │   ├── main.py       # Entry point for experiments
│   │   ├── conf/         # Configuration files (Hydra)
│   │   │   └── config.yaml
│   │   └── outputs/      # Experiment results (auto-generated)
│   └── sandbox/          # Development and testing scripts
│       └── dev.py
├── tests/                # Unit tests for your package
│   └── test_module1.py
├── requirements.txt      # Python dependencies
├── setup.py             # Package installation configuration
├── README.md            # This file
└── LICENSE              # License information
```

### Directory Explanations

- **`package-name/`**: Your main Python package. Rename this to match your project name (e.g., `neural_networks`, `data_analysis`, `optimization_toolkit`)
- **`core/`**: Contains your main algorithms, models, and core functionality
- **`utils/`**: Helper functions, data processing utilities, visualization tools
- **`data/`**: Small datasets, configuration files, or reference data (< 10MB). Store large datasets elsewhere
- **`scripts/experiments/`**: Your main experimental scripts using Hydra for configuration management
- **`scripts/sandbox/`**: Quick testing, prototyping, and development scripts
- **`tests/`**: Unit tests to ensure your code works correctly

Of course, the structure may be adapted to the specific needs of the project.

## 📋 Prerequisites

Before you start, ensure you have:
- **Python 3.8 or higher** (check with `python --version`)
- **Git** for version control
- **Basic command line knowledge**
- A **text editor or IDE** (VS Code, PyCharm, etc.)

## 🚀 Getting Started

### Step 1: Create Your Project from This Template

1. **Click "Use this template"** at the top of this repository page
2. **Name your repository** (e.g., `sentiment-analysis-toolkit`, `optimization-algorithms`)
3. **Choose visibility** (public for open research, private for confidential work)
4. **Clone your new repository**:
   ```bash
   git clone https://github.com/your-username/your-project-name.git
   cd your-project-name
   ```

### Step 2: Set Up Your Development Environment

1. **Create and activate a virtual environment**:
   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate it (macOS/Linux)
   source .venv/bin/activate
   
   # Activate it (Windows)
   .venv\Scripts\activate
   ```

2. **Customize your project configuration**:
   - **Rename the package directory**: Change `package-name/` to your actual package name (e.g., `ml_toolkit/`)
   - **Edit `setup.py`**: Update the placeholder values:
     ```python
     name='your_actual_package_name',    # Match your renamed directory
     version='0.1.0',
     author='Your Full Name',
     author_email='your.email@university.edu',
     description='Brief description of your research project',
     url='https://github.com/your-username/your-project-name',
     ```

3. **Install dependencies and your package**:
   ```bash
   # Install required packages
   pip install -r requirements.txt
   
   # Install your package in development mode
   pip install -e .
   ```
   
   The `-e` flag installs in "editable" mode, so changes to your code are immediately available.

4. **Verify installation**:
   ```python
   # Test that you can import your package
   python -c "import your_package_name; print('Success!')"
   ```

### Step 3: Start Developing

1. **Add your core algorithms** in `your_package_name/core/`
2. **Add utility functions** in `your_package_name/utils/`
3. **Create experiments** in `scripts/experiments/`
4. **Write tests** in `tests/` (run with `pytest`)
5. **Update `requirements.txt`** when you add new dependencies:
   ```bash
   pip freeze > requirements.txt
   ```

## ⚙️ Configuration Management with Hydra

This template uses [Hydra](https://hydra.cc/) for experiment configuration management, which is essential for reproducible research.

### Understanding the Configuration System

- **Configuration files** are stored in `scripts/experiments/conf/`
- **Default config**: `config.yaml` contains your base experiment settings
- **Override parameters** from command line without editing files
- **Automatic logging** and output directory management

### Example: Running Experiments
Here's an example of how `hydra` can be used to run and configure experiments from the command line.
The parameter names here are just for illustration though.

```bash
cd scripts/experiments

# Run with default configuration
python main.py

# Override specific parameters
python main.py learning_rate=0.001 batch_size=64

# Use a different config file
python main.py --config-name=experiment_2

# Combine multiple overrides
python main.py model=resnet data.augment=true optimizer.lr=0.01
```

### Output Management

Hydra automatically creates timestamped output directories:
```
scripts/experiments/outputs/
└── 2025-09-26/
    └── 17-23-46/
        ├── main.log        # Automatic logging
        ├── .hydra/         # Configuration snapshots
        └── your_results/   # Your experiment outputs
```

## 📤 Sharing Your Project

```bash
# Clone and setup
git clone https://github.com/your-username/your-project-name.git
cd your-project-name

# Create environment and install
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e .

# Run experiments
cd scripts/experiments
python main.py
```

## Testing
```bash
# Run tests regularly
pytest

# Check test coverage
pytest --cov=your_package_name

# Add tests for critical functions
def test_model_accuracy():
    model = YourModel()
    result = model.predict(test_data)
    assert result.accuracy > 0.8
```

## 🔧 Common Issues and Solutions

### Import Errors
```bash
# If you can't import your package
pip install -e .  # Reinstall in editable mode

# If tests can't find your package
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

### Environment Issues
```bash
# If packages conflict
pip freeze > old_requirements.txt
pip uninstall -r old_requirements.txt -y
pip install -r requirements.txt
```

### Hydra Configuration Issues
```bash
# If config files aren't found
cd scripts/experiments  # Make sure you're in the right directory
python main.py --help   # Check available configurations
```

## 📖 Additional Resources

- [Hydra Documentation](https://hydra.cc/) - Configuration management
- [pytest Documentation](https://docs.pytest.org/) - Testing framework
- [Python Packaging Guide](https://packaging.python.org/) - Package distribution
- [Git Tutorial](https://git-scm.com/docs/gittutorial) - Version control basics
- [PEP 8 Style Guide](https://pep8.org/) - Python coding standards

## 📄 License
This project is licensed under the [MIT License](LICENSE).