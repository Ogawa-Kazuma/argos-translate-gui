#!/usr/bin/env python3
"""
Setup script to help install Python 3.11 and create a new virtual environment
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Check current Python version"""
    print(f"Current Python version: {sys.version}")
    return sys.version_info

def install_python311():
    """Instructions for installing Python 3.11"""
    print("\n" + "="*60)
    print("PYTHON 3.11 INSTALLATION INSTRUCTIONS")
    print("="*60)
    print("""
To install Python 3.11 on Windows:

1. Go to https://www.python.org/downloads/release/python-3118/
2. Download "Windows installer (64-bit)" for Python 3.11.8
3. Run the installer and make sure to:
   - Check "Add Python to PATH"
   - Check "Install for all users" (optional)
   - Click "Install Now"

Alternative method using winget:
1. Open PowerShell as Administrator
2. Run: winget install Python.Python.3.11

After installation, restart your terminal and run this script again.
""")

def create_venv_python311():
    """Create a new virtual environment with Python 3.11"""
    try:
        print("\nCreating new virtual environment with Python 3.11...")
        
        # Remove old venv if it exists
        venv_path = Path(".venv311")
        if venv_path.exists():
            import shutil
            shutil.rmtree(venv_path)
            print("Removed old virtual environment")
        
        # Create new venv with Python 3.11
        result = subprocess.run([
            "py", "-3.11", "-m", "venv", ".venv311"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Virtual environment created successfully")
            return True
        else:
            print(f"✗ Failed to create virtual environment: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error creating virtual environment: {e}")
        return False

def install_argostranslate():
    """Install Argos Translate in the new virtual environment"""
    try:
        print("\nInstalling Argos Translate...")
        
        # Activate venv and install
        if os.name == 'nt':  # Windows
            pip_path = ".venv311\\Scripts\\pip.exe"
        else:  # Unix-like
            pip_path = ".venv311/bin/pip"
        
        result = subprocess.run([
            pip_path, "install", "argostranslate"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✓ Argos Translate installed successfully")
            return True
        else:
            print(f"✗ Failed to install Argos Translate: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error installing Argos Translate: {e}")
        return False

def create_launcher():
    """Create a launcher script for Python 3.11"""
    launcher_content = '''@echo off
cd /d "%~dp0"
.venv311\\Scripts\\python.exe argos_translate_gui_safe.py
pause
'''
    
    with open("launch_gui_311.bat", "w") as f:
        f.write(launcher_content)
    
    print("✓ Created launch_gui_311.bat")

def main():
    """Main setup function"""
    print("Argos Translate GUI Setup for Python 3.11")
    print("="*50)
    
    # Check current Python version
    current_version = check_python_version()
    
    if current_version.major == 3 and current_version.minor == 11:
        print("✓ Python 3.11 is already available!")
        
        # Try to create venv
        if create_venv_python311():
            if install_argostranslate():
                create_launcher()
                print("\n" + "="*50)
                print("SETUP COMPLETE!")
                print("="*50)
                print("You can now run the GUI with:")
                print("  launch_gui_311.bat")
                print("or")
                print("  .venv311\\Scripts\\python.exe argos_translate_gui_safe.py")
            else:
                print("\nSetup failed at Argos Translate installation")
        else:
            print("\nSetup failed at virtual environment creation")
    else:
        print(f"Current Python version is {current_version.major}.{current_version.minor}")
        print("Python 3.11 is required for compatibility with CTranslate2")
        install_python311()

if __name__ == "__main__":
    main()
    input("\nPress Enter to exit...")
