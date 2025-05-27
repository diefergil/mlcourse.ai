#!/bin/bash

# Install Jupyter Kernel for MLCourse.ai Poetry Environment
# Run this script if Jupyter can't find the correct Python kernel

echo "🔧 Installing Jupyter kernel for MLCourse.ai Poetry environment..."

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Check if Poetry is available
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry not found. Please ensure Poetry is installed and in your PATH."
    exit 1
fi

# Get the virtual environment Python path
VENV_PYTHON=$(poetry env info --path)/bin/python

echo "📍 Virtual environment Python: $VENV_PYTHON"

# Install the kernel
echo "🚀 Installing IPython kernel..."
poetry run python -m ipykernel install --user --name=mlcourse-ai --display-name="MLCourse.ai (Poetry)"

# List available kernels
echo "✅ Available Jupyter kernels:"
poetry run jupyter kernelspec list

echo ""
echo "🎉 Kernel installation complete!"
echo "💡 In Jupyter, select 'MLCourse.ai (Poetry)' as your kernel"
echo "🔍 Kernel path: $VENV_PYTHON" 