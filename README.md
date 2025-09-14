# Argos Translate GUI

A modern graphical user interface for [Argos Translate](https://github.com/argosopentech/argos-translate), providing an easy-to-use interface for offline neural machine translation.

![Argos Translate GUI](https://img.shields.io/badge/Argos%20Translate-GUI-blue)
![Python](https://img.shields.io/badge/Python-3.11%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

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

## Installation

### Prerequisites
- Python 3.11 or higher (recommended for full compatibility)
- Tkinter (usually included with Python)
- Argos Translate (optional - GUI works in demo mode without it)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd argos-translate-gui
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   
   # On Windows:
   .venv\Scripts\activate
   
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the GUI:**
   ```bash
   # On Windows:
   launch_gui.bat
   
   # Or directly:
   python argos_translate_gui_safe.py
   ```

### Full Installation with Argos Translate

For full functionality, install Argos Translate:

```bash
pip install argostranslate
```

**Note:** If you encounter compatibility issues with Python 3.13+, the GUI will automatically run in demo mode.

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

## System Requirements

- **Python:** 3.11 or higher (3.11 recommended for full compatibility)
- **Memory:** 4GB RAM minimum, 8GB recommended
- **Storage:** 2GB free space for language packages
- **GPU:** Optional CUDA support for faster translations
- **OS:** Windows, macOS, or Linux

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

## Troubleshooting

### Common Issues

1. **"No languages available":**
   - Install language packages in the Package Management tab
   - Update the package index first

2. **Translation fails:**
   - Check that both source and target languages are installed
   - Verify the language package is properly installed
   - Try updating the package index

3. **GUI won't start:**
   - Ensure Python 3.11+ is installed
   - Check that Tkinter is available: `python -c "import tkinter"`
   - Try running in demo mode: `python argos_translate_gui_safe.py`

4. **Slow translations:**
   - Enable CUDA support in Settings if you have a compatible GPU
   - Ensure you have sufficient RAM available
   - Close other applications to free up resources

5. **Python 3.13+ compatibility issues:**
   - The GUI automatically runs in demo mode
   - For full functionality, use Python 3.11
   - See `setup_python311.py` for help setting up Python 3.11

### Debug Mode

Enable debug mode in the Settings tab to get detailed logging information for troubleshooting.

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

---

**Made with ❤️ for the open-source translation community**
