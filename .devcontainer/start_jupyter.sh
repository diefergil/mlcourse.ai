#!/bin/bash

# MLCourse.ai Jupyter Lab Startup Script
# This script starts Jupyter Lab with the correct configuration for the devcontainer

echo "🚀 Starting Jupyter Lab for MLCourse.ai..."
echo "📍 Make sure you're in the Poetry virtual environment"

# Ensure Poetry is in PATH
export PATH="$HOME/.local/bin:$PATH"

# Check if Poetry is available
if ! command -v poetry &> /dev/null; then
    echo "❌ Poetry not found. Please ensure Poetry is installed and in your PATH."
    exit 1
fi

# Check if we're in a Poetry project
if [ ! -f "pyproject.toml" ]; then
    echo "❌ pyproject.toml not found. Please run this script from the project root."
    exit 1
fi

# Start Jupyter Lab
echo "🔧 Starting Jupyter Lab..."
echo "📝 Access it at: http://localhost:8888"
echo "🛑 Press Ctrl+C to stop"
echo ""

poetry run jupyter lab \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --allow-root \
    --ServerApp.token='' \
    --ServerApp.password='' \
    --ServerApp.allow_origin='*' \
    --ServerApp.disable_check_xsrf=True 