# Elmely Energy Monitor

## Developer Setup Guide

Document version: 1.0
Last updated: 2026-07-01

---

# Prerequisites

Install the following software:

- Git
- Python 3.14.x
- Visual Studio Code

---

# Clone / Open Project

Open the project folder in Visual Studio Code.

Example:

C:\Users\son\iCloudDrive\ElmelyEnergyMonitor

---

# Create Virtual Environment

From the project root:

```powershell
python -m venv .venv
```

---

# Activate Virtual Environment

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

The prompt should change to:

```text
(.venv) PS C:\...\ElmelyEnergyMonitor>
```

---

# Install Dependencies

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install required packages:

```powershell
pip install PySide6 pyqtgraph pandas requests openpyxl reportlab
```

---

# Verify Installation

Check Python:

```powershell
python --version
```

Check pip:

```powershell
pip --version
```

Check Git:

```powershell
git --version
```

---

# Running the Application

From the project root:

```powershell
python src\elmely\main.py
```

---

# Git Workflow

Initialize repository:

```powershell
git init
```

Rename default branch:

```powershell
git branch -M main
```

Check repository status:

```powershell
git status
```

Stage changes:

```powershell
git add .
```

Create commit:

```powershell
git commit -m "Description of changes"
```

View history:

```powershell
git log --oneline
```

---

# Useful Git Commands

Current branch:

```powershell
git branch
```

Create new branch:

```powershell
git checkout -b feature/feature-name
```

Switch branch:

```powershell
git checkout main
```

---

# VS Code

Recommended extensions:

- Python (Microsoft)
- Pylance (Microsoft)
- GitLens (optional)
- Material Icon Theme (optional)
- Error Lens (optional)

---

# Recommended Project Structure

ElmelyEnergyMonitor/

    docs/
    src/
    assets/
    config/
    data/
    logs/
    scripts/
    tests/

    .gitignore
    README.md

---

# Notes

Always activate the virtual environment before working.

Use small Git commits.

Keep documentation updated.

Developer Mode is intended for diagnostics and testing.