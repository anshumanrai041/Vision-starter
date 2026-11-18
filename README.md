# 🚀 Vision Starter

A reproducible Computer Vision (CV) project template built using Python, Poetry, virtual environments, and modern software engineering practices.

---

## 🎯 Objective

This project demonstrates a reproducible Computer Vision (CV) development environment using Python, Poetry, virtual environments, and project automation.

The objective is to ensure that any developer can recreate the exact development environment and run the project successfully on a clean machine.

---

## 📋 Prerequisites

- Python 3.15.2 (or Python 3.11+)
- Poetry
- Git

---

## 🐍 Python Version Management

### Commands Used

```bash
pyenv install 3.15.2
pyenv local 3.15.2
python --version
```

### Python Version File

`.python-version`

```text
3.15.2
```

This ensures the project uses a consistent Python version across different machines.

---

## 🏗️ Create Virtual Environment

```powershell
python -m venv .venv
```

### Activate Environment (Windows)

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### Verify

```powershell
python --version
```

Expected:

```text
Python 3.15.2
```

---

## 📦 Install Poetry

```powershell
pip install poetry
```

Verify:

```powershell
poetry --version
```

---

## 📥 Install Dependencies

```powershell
poetry install
```

This recreates the project environment on any clean machine.

---

## 🔒 Generate Lock File

```powershell
poetry lock
```

This creates:

```text
poetry.lock
```

which stores exact dependency versions.

---

## 📄 Generate requirements.txt

Install export plugin:

```powershell
poetry self add poetry-plugin-export
```

Generate requirements file:

```powershell
poetry export --without-hashes -f requirements.txt -o requirements.txt
```

---

## 📚 Dependencies

### Runtime Dependencies

- numpy
- opencv-python
- matplotlib

### Development Dependencies

- pytest
- ruff
- black

---

## 📂 Project Structure

```text
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
├── .python-version
├── pyproject.toml
├── poetry.lock
├── requirements.txt
├── Makefile
├── README.md
└── .gitignore
```

---

## 💻 Source Code Example

### main.py

```python
from pathlib import Path

PROJECT_ROOT = Path.cwd()

def main():
    print("Vision Starter Project")
    print(f"Project Root: {PROJECT_ROOT}")

if __name__ == "__main__":
    main()
```

---

## 📁 Why pathlib?

The project avoids hardcoded paths and uses Python's `pathlib` module.

Example:

```python
from pathlib import Path

project_root = Path.cwd()

image_path = project_root / "images" / "sample.jpg"
```

Benefits:

- Cross-platform compatibility
- No hardcoded paths
- Easier maintenance

---

## ✅ Testing

Example test:

```python
def test_addition():
    assert 2 + 2 == 4
```

Run tests:

```powershell
poetry run pytest
```

Expected:

```text
1 passed
```

---

## ⚙️ Makefile Commands

| Command | Purpose |
|----------|---------|
| make install | Install dependencies |
| make lint | Run Ruff linter |
| make test | Run Pytest |
| make run | Run application |

---

## ▶️ Running the Application

```powershell
python src\vision_starter\main.py
```

Expected output:

```text
Vision Starter Project
Project Root: C:\Users\username\vision-starter
```

---

## 🔄 Reproducibility

The following files make the project reproducible:

| File | Purpose |
|--------|---------|
| `.python-version` | Python version control |
| `pyproject.toml` | Project metadata and dependencies |
| `poetry.lock` | Exact dependency versions |
| `requirements.txt` | Dependency export |
| `Makefile` | Automation commands |

Any developer can recreate the environment using:

```powershell
poetry install
```

or

```bash
make install
```

---

## 🎓 Learning Outcomes

This project demonstrates:

- Virtual Environment Creation
- Python Version Management
- Poetry Dependency Management
- Dependency Locking
- Automated Testing
- Linting
- Git & GitHub Workflow
- Reproducible Computer Vision Development

---

## 👨‍💻 Author

**Anshuman Rai**

GitHub: https://github.com/anshumanrai041