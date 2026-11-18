Vision Starter
Objective
This project demonstrates a reproducible Computer Vision (CV) development environment using Python, Poetry, virtual environments, and project automation.

The objective is to ensure that any developer can recreate the exact development environment and run the project successfully on a clean machine.

Prerequisites
Python 3.15.2 (or Python 3.11+)
Poetry
Git
Python Version Management
Commands Used
pyenv install 3.15.2
pyenv local 3.15.2
python --version
Python Version File
.python-version

3.15.2
This ensures the project uses a consistent Python version across different machines.

Create Virtual Environment
python -m venv .venv
Activate the virtual environment:

Windows PowerShell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
Verification
python --version
Expected:

Python 3.15.2
Install Poetry
pip install poetry
Verify installation:

poetry --version
Install Dependencies
Install all dependencies from the lock file:

poetry install
This recreates the project environment on any clean machine.

Generate Lock File
poetry lock
This creates:

poetry.lock
which stores exact package versions.

Generate requirements.txt
Install export plugin:

poetry self add poetry-plugin-export
Generate requirements file:

poetry export --without-hashes -f requirements.txt -o requirements.txt
Project Dependencies
Runtime Dependencies
numpy
opencv-python
matplotlib
Development Dependencies
pytest
ruff
black
Project Structure
vision-starter/
│
├── src/
│   └── vision_starter/
│       ├── __init__.py
│       └── main.py
│
├── tests/
│   └── test_sample.py
│
├── .venv/
├── .python-version
├── pyproject.toml
├── poetry.lock
├── requirements.txt
├── Makefile
└── README.md
Source Code Example
main.py
from pathlib import Path

PROJECT_ROOT = Path.cwd()

def main():
    print("Vision Starter Project")
    print(f"Project Root: {PROJECT_ROOT}")

if __name__ == "__main__":
    main()
Why pathlib?
The project avoids hardcoded paths and uses Python's pathlib module.

Example:

from pathlib import Path

project_root = Path.cwd()
image_path = project_root / "images" / "sample.jpg"
This works across Windows, Linux, and macOS.

Testing
Test File
def test_addition():
    assert 2 + 2 == 4
Run tests:

poetry run pytest
Expected:

1 passed
Makefile Commands
Install Dependencies
make install
Executes:

poetry install
Run Linter
make lint
Executes:

poetry run ruff check .
Run Tests
make test
Executes:

poetry run pytest
Run Application
make run
Executes:

poetry run python src/vision_starter/main.py
Running the Application
python src\vision_starter\main.py
Expected Output:

Vision Starter Project
Project Root: C:\Users\username\vision-starter
Reproducibility
The following files make the project reproducible:

File	Purpose
.python-version	Python version control
pyproject.toml	Project metadata and dependencies
poetry.lock	Exact dependency versions
requirements.txt	Dependency export
Makefile	Common automation commands
Using these files, any developer can recreate the environment by running:

poetry install
or

make install
Acceptance Criteria Coverage
✅ Python 3.11+ configured
✅ Virtual environment created
✅ Valid pyproject.toml
✅ Version constrained dependencies
✅ At least three dependencies
✅ .python-version added
✅ requirements.txt generated
✅ Makefile created
✅ Uses pathlib instead of hardcoded paths
✅ Reproducible environment setup