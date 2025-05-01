# ACE Controller Teaching Kit

This repository serves as a comprehensive teaching kit for building end-to-end digital human pipelines using the ACE Controller and NVIDIA-pipecat. It provides hands-on examples, tutorials, and best practices for developing digital human applications. 

## Who is this for?
This is for academic use, and as such is geared more towards understanding the nvidia-pipecat library and the development around digital human pipelines.

## Prerequisites

- Python 3.12 (required)
- [uv](https://github.com/astral-sh/uv) package manager
- You will need an NVIDIA_API_KEY (free) by making an account on the [NVIDIA API Catalog](build.nvidia.com)
  - We recommend to create a `.env` file and store it as `NVIDIA_API_KEY=your_key_here`
  - This setup allows the notebooks to run on ANY device. For local deployment options, explore the [NVIDIA ACE Controller documentation](https://docs.nvidia.com/ace/ace-controller-microservice/1.0/index.html)

## Overview

The teaching kit focuses on:
- Integration with ACE Controller for digital human development
- NVIDIA-pipecat for agent pipeline development
- End-to-end digital human pipeline implementation
- Best practices and patterns for digital human design

## Development Environment Setup

1. Clone this repository:
```bash
git clone https://github.com/your-username/ace-controller-nb.git
cd ace-controller-nb
```

3. Create and activate a virtual environment with Python 3.12:
```bash
# On macOS/Linux
uv venv --python python3.12 .venv
# Or: uv venv --python /usr/local/bin/python3.12 .venv

# On Windows PowerShell
uv venv --python python3.12 .venv 
.\.venv\Scripts\activate

# On Windows Command Prompt
uv venv --python python3.12 .venv
.venv\Scripts\activate.bat

# Verify correct Python version in venv
source .venv/bin/activate
```

4. Install required packages:
```bash
# Install dependencies
uv pip install -e .
```

5. Register the Jupyter kernel:
```bash
uv run ipython kernel install --user --name=nv-pipecat-env
```

6. Start JupyterLab:
```bash
uv run jupyter lab
```

## Running Notebooks Locally

To run the notebooks in this repository:

1. Make sure you've completed the development environment setup above
2. Start JupyterLab using `uv run jupyter lab`
3. When opening a notebook, select the "nv-pipecat-env" kernel from the kernel selector:

![Select nv-pipecat-env kernel](docs/images/kernel.png)

> **Important**: Make sure "nv-pipecat-env" is selected as shown in the image above. If you see "Python 3" or another kernel name, click the kernel name in the top-right to change it.

4. The notebooks will run in your Python 3.12 environment with all the required dependencies

## Troubleshooting

### Common Issues

1. Wrong Python Version
```
Error: Failed to build nvidia-pipecat-notebooks
```
Solution: Ensure you're using Python 3.12.x exactly. Other versions are not supported.

3. Kernel Not Found
```
Kernel 'nv-pipecat-env' not found
```
Solution: Re-run the kernel installation:
```bash
uv run ipython kernel install --user --name=nv-pipecat-env
```

4. Permission Issues (Linux/macOS)
```
error: failed to copy file... Permission denied
```
Solution: Don't use sudo. Instead, ensure your user owns the directory:
```bash
chown -R $USER:$USER .
```

### Still Having Issues?

1. Clean your environment and start fresh:
```bash
# Remove existing environment
rm -rf .venv  # (Unix/macOS)
rmdir /s /q .venv  # (Windows)

# Create new environment
uv venv .venv
# Activate and install as shown above
```

2. Check your pip and uv are up to date:
```bash
pip install --upgrade pip
pip install --upgrade uv
```

## Repository Structure

- `notebooks/`: Jupyter notebooks containing tutorials and examples
- `src/`: Source code for reusable components and utilities

## Environment Management

This project uses a `.gitignore` file to exclude:
- Virtual environment directories (`.venv/`, `.env/`)
- Python cache files (`__pycache__/`)
- Jupyter notebook checkpoints
- Environment variable files
- IDE-specific files
- OS-specific files

Make sure to create your own `.env` file for any environment-specific configurations.

## Getting Started

1. Clone this repository
2. Set up your development environment as described above
3. Explore the notebooks in the `notebooks/` directory
4. Follow the tutorials to build your first digital human pipeline

## Contributing

Contributions are welcome as this is currently under development!