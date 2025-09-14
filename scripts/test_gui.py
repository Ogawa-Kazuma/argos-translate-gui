#!/usr/bin/env python3
"""
Test script for Argos Translate GUI
"""

import sys
import os
from pathlib import Path

# Add the virtual environment to the path
venv_path = Path(__file__).parent.parent / ".venv" / "Lib" / "site-packages"
if venv_path.exists():
    sys.path.insert(0, str(venv_path))

# Add src directory to path
src_path = Path(__file__).parent.parent / "src"
if src_path.exists():
    sys.path.insert(0, str(src_path))

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import tkinter as tk
        print("✓ Tkinter imported successfully")
    except ImportError as e:
        print(f"✗ Tkinter import failed: {e}")
        return False
    
    try:
        import argostranslate.translate as translate
        print("✓ Argos Translate imported successfully")
    except ImportError as e:
        print(f"✗ Argos Translate import failed: {e}")
        return False
    
    try:
        import argostranslate.package as package
        print("✓ Argos Translate package module imported successfully")
    except ImportError as e:
        print(f"✗ Argos Translate package import failed: {e}")
        return False
    
    try:
        import argostranslate.settings as settings
        print("✓ Argos Translate settings imported successfully")
    except ImportError as e:
        print(f"✗ Argos Translate settings import failed: {e}")
        return False
    
    return True

def test_argos_functionality():
    """Test basic Argos Translate functionality"""
    print("\nTesting Argos Translate functionality...")
    
    try:
        import argostranslate.translate as translate
        import argostranslate.package as package
        
        # Test getting installed languages
        languages = translate.get_installed_languages()
        print(f"✓ Found {len(languages)} installed languages")
        
        if languages:
            for lang in languages[:3]:  # Show first 3 languages
                print(f"  - {lang.name} ({lang.code})")
        
        # Test getting available packages
        try:
            packages = package.get_available_packages()
            print(f"✓ Found {len(packages)} available packages")
        except:
            print("! No package index available (this is normal for first run)")
        
        # Test getting installed packages
        installed = package.get_installed_packages()
        print(f"✓ Found {len(installed)} installed packages")
        
        return True
        
    except Exception as e:
        print(f"✗ Argos Translate functionality test failed: {e}")
        return False

def test_gui_creation():
    """Test that the GUI can be created"""
    print("\nTesting GUI creation...")
    
    try:
        import tkinter as tk
        from argos_translate_gui import ArgosTranslateGUI
        
        # Create a test root window
        root = tk.Tk()
        root.withdraw()  # Hide the window
        
        # Create the GUI
        app = ArgosTranslateGUI(root)
        print("✓ GUI created successfully")
        
        # Clean up
        root.destroy()
        return True
        
    except Exception as e:
        print(f"✗ GUI creation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Argos Translate GUI Test Suite")
    print("=" * 40)
    
    tests = [
        test_imports,
        test_argos_functionality,
        test_gui_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 40)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed! The GUI should work correctly.")
    else:
        print("✗ Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
