#!/usr/bin/env python3
"""
Verification script for MLCourse.ai development environment.
Run this script to verify that all dependencies are properly installed.
"""

import importlib.util
import subprocess
import sys


def check_python_version():
    """Check if Python version meets requirements."""
    version = sys.version_info
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")

    if version.major == 3 and 9 <= version.minor < 12:
        print("✓ Python version is compatible with project requirements")
        return True
    else:
        print("✗ Python version not compatible. Requires Python >=3.9,<3.12")
        return False


def check_poetry():
    """Check if Poetry is installed and accessible."""
    try:
        result = subprocess.run(
            ["poetry", "--version"], capture_output=True, text=True, check=True
        )
        print(f"✓ Poetry installed: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Poetry not found or not accessible")
        return False


def check_virtual_env():
    """Check if we're in a Poetry virtual environment."""
    try:
        result = subprocess.run(
            ["poetry", "env", "info", "--path"],
            capture_output=True,
            text=True,
            check=True,
        )
        venv_path = result.stdout.strip()
        print(f"✓ Virtual environment: {venv_path}")

        # Check if current Python is from the virtual environment
        if venv_path in sys.executable:
            print("✓ Running in Poetry virtual environment")
            return True
        else:
            print("⚠ Not running in Poetry virtual environment")
            print(f"  Current Python: {sys.executable}")
            print(f"  Expected: {venv_path}/bin/python")
            return False
    except subprocess.CalledProcessError:
        print("✗ Could not get virtual environment info")
        return False


def check_key_packages():
    """Check if key packages are installed."""
    key_packages = [
        "numpy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "jupyter",
        "plotly",
        "scipy",
        "statsmodels",
    ]

    missing_packages = []

    for package in key_packages:
        spec = importlib.util.find_spec(package)
        if spec is not None:
            print(f"✓ {package} is installed")
        else:
            print(f"✗ {package} is missing")
            missing_packages.append(package)

    return len(missing_packages) == 0


def check_jupyter():
    """Check if Jupyter is properly configured."""
    try:
        result = subprocess.run(
            ["jupyter", "--version"], capture_output=True, text=True, check=True
        )
        print("✓ Jupyter is installed:")
        for line in result.stdout.strip().split("\n"):
            print(f"  {line}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Jupyter not found or not accessible")
        return False


def main():
    """Run all verification checks."""
    print("🔍 Verifying MLCourse.ai Development Environment")
    print("=" * 50)

    checks = [
        ("Python Version", check_python_version),
        ("Poetry Installation", check_poetry),
        ("Virtual Environment", check_virtual_env),
        ("Key Packages", check_key_packages),
        ("Jupyter", check_jupyter),
    ]

    results = []

    for check_name, check_func in checks:
        print(f"\n📋 {check_name}:")
        try:
            result = check_func()
            results.append(result)
        except Exception as e:
            print(f"✗ Error during {check_name}: {e}")
            results.append(False)

    print("\n" + "=" * 50)
    print("📊 Summary:")

    passed = sum(results)
    total = len(results)

    if passed == total:
        print(f"🎉 All checks passed! ({passed}/{total})")
        print("Your development environment is ready to use.")
    else:
        print(f"⚠ {passed}/{total} checks passed.")
        print("Some issues need to be resolved before proceeding.")

        if not results[1]:  # Poetry check failed
            print("\n💡 To fix Poetry issues:")
            print('   export PATH="$HOME/.local/bin:$PATH"')
            print("   poetry install")

        if not results[3]:  # Package check failed
            print("\n💡 To install missing packages:")
            print("   poetry install")

    print("\n🚀 To start Jupyter Lab:")
    print(
        "   poetry run jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root"
    )


if __name__ == "__main__":
    main()
