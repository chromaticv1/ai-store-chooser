import sys
import os

# Add src to python path so internal imports in src/app.py work
sys.path.append(os.path.abspath("src"))

# Import the actual application code from src/app.py
# We use src.app to avoid importing this file (app.py) recursively
import src.app
