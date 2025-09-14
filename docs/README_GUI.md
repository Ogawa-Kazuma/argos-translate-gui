# Argos Translate GUI

A modern graphical user interface for Argos Translate, providing an easy-to-use interface for offline neural machine translation.

## Features

### Translation Tab
- **Language Selection**: Choose source and target languages from installed language packages
- **Text Translation**: Input text and get instant translations
- **Swap Languages**: Quick button to swap source and target languages
- **Copy Translation**: Copy translated text to clipboard
- **Real-time Translation**: Fast translation with progress indication

### Package Management Tab
- **Package Browser**: View all available language packages
- **Install/Uninstall**: Manage language packages with one-click installation
- **Package Status**: See which packages are installed vs available
- **Update Index**: Refresh the package index to get latest packages
- **Progress Tracking**: Visual progress indicators for long operations

### Settings Tab
- **Device Configuration**: Choose between CPU, CUDA, or auto device selection
- **Debug Mode**: Enable debug logging for troubleshooting
- **Package Directory**: Configure where language packages are stored
- **System Information**: View current configuration and system details

## Installation

1. Ensure Argos Translate is installed in your virtual environment:
   ```bash
   pip install argostranslate
   ```

2. Run the GUI using one of these methods:

   **Method 1: Python launcher**
   ```bash
   python launch_gui.py
   ```

   **Method 2: Batch file (Windows)**
   ```bash
   launch_gui.bat
   ```

   **Method 3: Direct execution**
   ```bash
   python argos_translate_gui.py
   ```

## Usage

### First Time Setup

1. **Install Language Packages**: 
   - Go to the "Package Management" tab
   - Click "Update Package Index" to refresh available packages
   - Select a language package (e.g., "translate-en_es" for English to Spanish)
   - Click "Install Selected" to download and install the package

2. **Configure Settings** (Optional):
   - Go to the "Settings" tab
   - Adjust device type if you have CUDA support
   - Configure package directory if needed
   - Click "Save Settings"

### Translating Text

1. **Select Languages**:
   - Choose source language from the "From" dropdown
   - Choose target language from the "To" dropdown
   - Use the ⇄ button to quickly swap languages

2. **Enter Text**:
   - Type or paste text in the "Input Text" area
   - The text area supports multi-line text

3. **Translate**:
   - Click the "Translate" button
   - Wait for the translation to complete
   - View the result in the "Translated Text" area

4. **Copy Result**:
   - Click "Copy Translation" to copy the result to clipboard

### Managing Packages

- **View Packages**: All available packages are listed in the Package Management tab
- **Install Packages**: Select a package and click "Install Selected"
- **Uninstall Packages**: Select an installed package and click "Uninstall Selected"
- **Update Index**: Click "Update Package Index" to refresh the package list

## Supported Languages

The GUI supports all languages available in Argos Translate, including:
- Arabic, Chinese, English, French, German, Japanese, Spanish
- And many more (30+ languages total)

## System Requirements

- Python 3.5 or higher
- Argos Translate installed
- Tkinter (usually included with Python)
- Sufficient disk space for language packages (varies by package, typically 100MB-1GB per language pair)

## Troubleshooting

### Common Issues

1. **"No languages available"**:
   - Install language packages in the Package Management tab
   - Update the package index first

2. **Translation fails**:
   - Check that both source and target languages are installed
   - Verify the language package is properly installed
   - Try updating the package index

3. **GUI won't start**:
   - Ensure Argos Translate is installed: `pip install argostranslate`
   - Check that Tkinter is available: `python -c "import tkinter"`

4. **Slow translations**:
   - Enable CUDA support in Settings if you have a compatible GPU
   - Ensure you have sufficient RAM available

### Debug Mode

Enable debug mode in the Settings tab to get detailed logging information for troubleshooting.

## Technical Details

- **GUI Framework**: Tkinter with ttk styling
- **Threading**: Translation operations run in background threads to prevent GUI freezing
- **Package Management**: Full integration with Argos Translate package system
- **Configuration**: Persistent settings with environment variable support

## License

This GUI follows the same license as Argos Translate (MIT License or Creative Commons CC0).
