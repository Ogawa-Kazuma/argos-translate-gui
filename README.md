# Argos Translate GUI

A modern graphical user interface for [Argos Translate](https://github.com/argosopentech/argos-translate), providing an easy-to-use interface for offline neural machine translation.

![Argos Translate GUI](https://img.shields.io/badge/Argos%20Translate-GUI-blue)
![Python](https://img.shields.io/badge/Python-3.11%2B-green)
![Windows](https://img.shields.io/badge/Windows-10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🪟 Windows Build

This project is optimized for Windows 10/11 with easy installation and setup. The GUI provides a native Windows experience with batch file launchers and PowerShell support.

## Features

### 🔄 Translation Interface
- **Intuitive Language Selection**: Choose source and target languages from installed packages
- **Real-time Translation**: Fast translation with progress indication
- **Text Management**: Large text areas with scroll support for long documents
- **Language Swapping**: Quick button to swap source and target languages
- **Copy to Clipboard**: One-click copying of translated text

### 📦 Package Management
- **Package Browser**: View all available language packages in a table format
- **One-Click Installation**: Install language packages with a single click
- **Package Status**: See which packages are installed vs available
- **Update Index**: Refresh the package index to get latest packages
- **Progress Tracking**: Visual progress indicators for long operations
- **Uninstall Support**: Remove packages you no longer need

### ⚙️ Settings & Configuration
- **Device Configuration**: Choose between CPU, CUDA, or auto device selection
- **Debug Mode**: Enable debug logging for troubleshooting
- **Package Directory**: Configure where language packages are stored
- **System Information**: View current configuration and system details

### 🛡️ Compatibility Features
- **Safe Mode**: Gracefully handles compatibility issues with different Python versions
- **Demo Mode**: Works even when Argos Translate is not fully available
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Fallback Support**: Demo translations for testing the interface

## Screenshots

### Translation Tab
- Clean, modern interface for text translation
- Language selection with swap functionality
- Large text areas for comfortable editing

### Package Management Tab
- Table view of all available packages
- Install/uninstall buttons with status indicators
- Progress bars for long operations

### Settings Tab
- Device configuration options
- Package directory management
- System information display

## 🚀 Windows Installation

### Prerequisites for Windows
- **Windows 10/11** (64-bit recommended)
- **Python 3.11 or higher** (recommended for full compatibility)
- **Git for Windows** (for cloning the repository)
- **PowerShell** (included with Windows)

### 🪟 Windows Quick Start

#### Method 1: One-Click Installation (Recommended)
1. **Download the repository:**
   ```powershell
   git clone https://github.com/Ogawa-Kazuma/argos-translate-gui.git
   cd argos-translate-gui
   ```

2. **Run the setup script:**
   ```powershell
   python scripts\setup_python311.py
   ```

3. **Launch the GUI:**
   ```powershell
   run_gui.bat
   ```

#### Method 2: Manual Installation
1. **Clone the repository:**
   ```powershell
   git clone https://github.com/Ogawa-Kazuma/argos-translate-gui.git
   cd argos-translate-gui
   ```

2. **Create a virtual environment:**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Run the GUI:**
   ```powershell
   # Option 1: Batch file (easiest)
   run_gui.bat
   
   # Option 2: Python launcher
   python run_gui.py
   
   # Option 3: Direct execution
   python src\argos_translate_gui_safe.py
   ```

### 🔧 Windows-Specific Features

#### Batch File Launchers
- **`run_gui.bat`** - Main launcher from project root
- **`scripts\launch_gui.bat`** - Launcher from scripts directory
- **Double-click to run** - No command line needed

#### PowerShell Support
- **Full PowerShell compatibility** - All commands work in PowerShell
- **PowerShell ISE support** - Can be run from PowerShell ISE
- **Windows Terminal support** - Works with Windows Terminal

#### Windows Integration
- **Native Windows look and feel** - Uses Windows-native Tkinter styling
- **Windows file associations** - Can be associated with .py files
- **Windows Start Menu** - Can be added to Start Menu shortcuts
- **Windows Taskbar** - Proper taskbar integration

### 📦 Full Installation with Argos Translate (Windows)

For complete functionality on Windows:

```powershell
# Activate virtual environment
.venv\Scripts\activate

# Install Argos Translate
pip install argostranslate

# Run with full functionality
python run_gui.py
```

**Note:** If you encounter Python 3.13+ compatibility issues, the GUI automatically runs in demo mode with full interface functionality.

## Usage

### First Time Setup

1. **Install Language Packages:**
   - Go to the "Package Management" tab
   - Click "Update Package Index" to refresh available packages
   - Select a language package (e.g., "translate-en_es" for English to Spanish)
   - Click "Install Selected" to download and install the package

2. **Configure Settings (Optional):**
   - Go to the "Settings" tab
   - Adjust device type if you have CUDA support
   - Configure package directory if needed
   - Click "Save Settings"

### Translating Text

1. **Select Languages:**
   - Choose source language from the "From" dropdown
   - Choose target language from the "To" dropdown
   - Use the ⇄ button to quickly swap languages

2. **Enter Text:**
   - Type or paste text in the "Input Text" area
   - The text area supports multi-line text and long documents

3. **Translate:**
   - Click the "Translate" button
   - Wait for the translation to complete
   - View the result in the "Translated Text" area

4. **Copy Result:**
   - Click "Copy Translation" to copy the result to clipboard

### Managing Packages

- **View Packages:** All available packages are listed in the Package Management tab
- **Install Packages:** Select a package and click "Install Selected"
- **Uninstall Packages:** Select an installed package and click "Uninstall Selected"
- **Update Index:** Click "Update Package Index" to refresh the package list

## Supported Languages

The GUI supports all languages available in Argos Translate, including:

- **European Languages:** English, Spanish, French, German, Italian, Portuguese, Russian, Polish, Czech, Dutch, Swedish, Danish, Finnish, Norwegian, Greek, Hungarian, Romanian, Bulgarian, Croatian, Slovak, Slovenian, Estonian, Latvian, Lithuanian
- **Asian Languages:** Chinese (Simplified & Traditional), Japanese, Korean, Hindi, Thai, Vietnamese, Indonesian, Malay, Filipino
- **Middle Eastern Languages:** Arabic, Hebrew, Persian, Turkish
- **Other Languages:** Esperanto, Irish, Ukrainian, and more

## 💻 Windows System Requirements

### Minimum Requirements
- **OS:** Windows 10 (Build 1903) or Windows 11
- **Architecture:** 64-bit (x64) recommended
- **Python:** 3.11 or higher (3.11 recommended for full compatibility)
- **Memory:** 4GB RAM minimum, 8GB recommended
- **Storage:** 2GB free space for language packages
- **Display:** 1024x768 minimum resolution

### Recommended Requirements
- **OS:** Windows 11 (latest version)
- **Architecture:** 64-bit (x64)
- **Python:** 3.11.8 (latest stable)
- **Memory:** 8GB RAM or more
- **Storage:** 5GB free space (for multiple language packages)
- **GPU:** NVIDIA GPU with CUDA support (optional, for faster translations)
- **Display:** 1920x1080 or higher

### Windows-Specific Requirements
- **PowerShell 5.1+** (included with Windows 10/11)
- **Git for Windows** (for cloning the repository)
- **Microsoft Visual C++ Redistributable** (usually included with Python)
- **Windows Defender** (may need to allow Python scripts)

## Project Structure

```
argos-translate-gui/
├── argos_translate_gui_safe.py    # Main GUI application (safe version)
├── argos_translate_gui.py         # Original GUI application
├── launch_gui.py                  # Python launcher script
├── launch_gui.bat                 # Windows batch launcher
├── test_gui.py                    # Test script
├── setup_python311.py             # Python 3.11 setup helper
├── requirements.txt               # Python dependencies
├── README.md                      # This file
├── README_GUI.md                  # Detailed GUI documentation
├── LICENSE                        # License file
└── .gitignore                     # Git ignore file
```

## Development

### Running Tests

```bash
python test_gui.py
```

### Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Test your changes: `python test_gui.py`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

### Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to functions and classes
- Keep functions small and focused

## 🔧 Windows Troubleshooting

### Common Windows Issues

1. **"No languages available":**
   - Install language packages in the Package Management tab
   - Update the package index first
   - Check Windows Defender isn't blocking downloads

2. **Translation fails:**
   - Check that both source and target languages are installed
   - Verify the language package is properly installed
   - Try updating the package index
   - Run as Administrator if permission issues occur

3. **GUI won't start:**
   - Ensure Python 3.11+ is installed and added to PATH
   - Check that Tkinter is available: `python -c "import tkinter"`
   - Try running in demo mode: `python src\argos_translate_gui_safe.py`
   - Check Windows Defender isn't blocking the script

4. **Batch file won't run:**
   - Right-click `run_gui.bat` → "Run as administrator"
   - Check that Python is in your system PATH
   - Try running from PowerShell: `.\run_gui.bat`

5. **PowerShell execution policy error:**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

6. **Python 3.13+ compatibility issues:**
   - The GUI automatically runs in demo mode
   - For full functionality, use Python 3.11
   - Run `python scripts\setup_python311.py` for help

7. **Windows Defender blocking:**
   - Add the project folder to Windows Defender exclusions
   - Allow Python scripts in Windows Defender settings

8. **Virtual environment issues:**
   ```powershell
   # Recreate virtual environment
   Remove-Item -Recurse -Force .venv
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Windows-Specific Debug Mode

Enable debug mode in the Settings tab to get detailed logging information for troubleshooting. On Windows, logs are displayed in the console window.

### Windows Performance Tips

- **Enable CUDA support** in Settings if you have a compatible NVIDIA GPU
- **Close unnecessary applications** to free up RAM
- **Use SSD storage** for better package loading performance
- **Run as Administrator** if you encounter permission issues

## Technical Details

- **GUI Framework:** Tkinter with ttk styling for modern appearance
- **Threading:** Translation operations run in background threads to prevent GUI freezing
- **Package Management:** Full integration with Argos Translate package system
- **Configuration:** Persistent settings with environment variable support
- **Error Handling:** Comprehensive error handling with user-friendly messages
- **Compatibility:** Safe fallback mode for different Python versions

## Related Projects

- [Argos Translate](https://github.com/argosopentech/argos-translate) - Core translation library
- [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) - Web API and server
- [Argos Translate GUI (Official)](https://github.com/argosopentech/argos-translate-gui) - Official GUI

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Argos Open Technologies](https://www.argosopentech.com/) for the amazing Argos Translate library
- The open-source community for continuous improvements and feedback
- Contributors who help make this project better

## Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section above
- Review the [detailed GUI documentation](README_GUI.md)

## 🪟 Windows Build Information

### Windows Build Status
- ✅ **Windows 10/11 Compatible** - Tested on Windows 10 Build 19045 and Windows 11
- ✅ **PowerShell Support** - Full PowerShell 5.1+ compatibility
- ✅ **Batch File Launchers** - Native Windows batch file support
- ✅ **Windows Defender Compatible** - Works with Windows Defender (may need exclusions)
- ✅ **Windows Terminal Support** - Compatible with Windows Terminal and PowerShell ISE

### Windows Installation Methods
1. **Git Clone + Batch File** (Recommended for developers)
2. **Direct Download + Setup Script** (Recommended for end users)
3. **Manual Installation** (For advanced users)

### Windows-Specific Files
- `run_gui.bat` - Main Windows batch launcher
- `scripts\launch_gui.bat` - Alternative batch launcher
- `scripts\setup_python311.py` - Windows Python 3.11 setup helper
- `TEST_RESULTS.md` - Windows test results and validation

### Windows Development
- **IDE Support**: Works with Visual Studio Code, PyCharm, and other Windows IDEs
- **Debugging**: Full debugging support in Windows development environments
- **Testing**: Comprehensive test suite with Windows-specific test cases

---

**Made with ❤️ for the open-source translation community**

**Optimized for Windows 10/11** 🪟
