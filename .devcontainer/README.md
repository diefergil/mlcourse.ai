# MLCourse.ai Development Container

This devcontainer configuration provides a complete development environment for the MLCourse.ai project with Python, Poetry, and all necessary extensions pre-installed.

## What's Included

### Base Environment

- **Python 3.11** (compatible with project requirements: >=3.9,<3.12)
- **Poetry** for dependency management
- **Zsh** with Oh My Zsh for enhanced terminal experience
- **Git** latest version

### VS Code Extensions

- **Python Development**: Python, Pylance, Black formatter, Pylint, isort
- **Jupyter**: Full Jupyter notebook support with cell tags and slideshow
- **Code Quality**: Ruff linter, YAML/JSON/Markdown support
- **AI Assistance**: GitHub Copilot and Copilot Chat (if available)

### Pre-configured Settings

- Python interpreter automatically set to Poetry virtual environment
- Black formatting enabled
- Pylint linting enabled
- Jupyter kernels configured to use project environment

## How to Use

### Option 1: GitHub Codespaces

1. Go to your repository on GitHub
2. Click the green "Code" button
3. Select "Codespaces" tab
4. Click "Create codespace on main"

### Option 2: Local Development with VS Code

1. Install [VS Code](https://code.visualstudio.com/) and the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
2. Clone this repository
3. Open the repository in VS Code
4. When prompted, click "Reopen in Container" or use Command Palette: "Dev Containers: Reopen in Container"

## What Happens During Setup

1. **Container Creation**: Downloads and sets up Python 3.11 base image
2. **Poetry Installation**: Installs Poetry package manager
3. **Environment Setup**: Creates virtual environment and installs all dependencies from `pyproject.toml`
4. **Extension Installation**: Installs all VS Code extensions for Python development

## Available Ports

The following ports are automatically forwarded:

- **8888**: Jupyter Lab/Notebook server
- **8000**: Development server (for web apps)
- **5000**: Flask/FastAPI applications

## Working with the Environment

### Running Jupyter

```bash
poetry run jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

### Installing New Dependencies

```bash
poetry add package-name
```

### Running Scripts

```bash
poetry run python your_script.py
```

### Activating the Shell

```bash
poetry shell
```

## Troubleshooting

### Poetry Not Found

If Poetry commands don't work, ensure the PATH is set correctly:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Virtual Environment Issues

To recreate the virtual environment:

```bash
poetry env remove python
poetry install
```

### Extension Issues

If VS Code extensions aren't working properly, reload the window:

- Command Palette → "Developer: Reload Window"

## Project Structure

This devcontainer is specifically configured for the MLCourse.ai project structure:

- Data science and machine learning libraries (scikit-learn, pandas, numpy, etc.)
- Jupyter notebook support
- Visualization libraries (matplotlib, seaborn, plotly)
- Pre-commit hooks and code quality tools

## Performance Tips

- The virtual environment is mounted as a volume for faster rebuilds
- Dependencies are cached between container rebuilds
- Use the integrated terminal for best performance with Poetry commands
