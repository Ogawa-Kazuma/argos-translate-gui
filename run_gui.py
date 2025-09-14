#!/usr/bin/env python3
"""
Main launcher for Argos Translate GUI
This script can be run from the project root directory
"""

import sys
import os
from pathlib import Path

# Add the virtual environment to the path
venv_path = Path(__file__).parent / ".venv" / "Lib" / "site-packages"
if venv_path.exists():
    sys.path.insert(0, str(venv_path))

# Add src directory to path
src_path = Path(__file__).parent / "src"
if src_path.exists():
    sys.path.insert(0, str(src_path))

# Import and run the GUI
try:
    from argos_translate_gui_safe import main
    main()
except ImportError as e:
    print(f"Error: {e}")
    print("Please ensure Argos Translate is installed in the virtual environment")
    print("You can install it with: pip install argostranslate")
    input("Press Enter to exit...")
except Exception as e:
    print(f"Unexpected error: {e}")
    input("Press Enter to exit...")
