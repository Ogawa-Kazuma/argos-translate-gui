#!/usr/bin/env python3
"""
Argos Translate GUI - Safe Version
A modern graphical user interface for Argos Translate with compatibility handling
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import threading
import queue
import sys
import os
from typing import List, Optional, Dict, Any
import json
from pathlib import Path

# Add the virtual environment to the path
venv_path = Path(__file__).parent / ".venv" / "Lib" / "site-packages"
if venv_path.exists():
    sys.path.insert(0, str(venv_path))

# Try to import Argos Translate with error handling
ARGOS_AVAILABLE = False
translate = None
package = None
settings = None

try:
    import argostranslate.translate as translate
    import argostranslate.package as package
    import argostranslate.settings as settings
    ARGOS_AVAILABLE = True
    print("Argos Translate imported successfully")
except ImportError as e:
    print(f"Warning: Argos Translate not available: {e}")
    print("GUI will run in demo mode")
except Exception as e:
    print(f"Warning: Error importing Argos Translate: {e}")
    print("GUI will run in demo mode")


class ArgosTranslateGUI:
    """Main GUI application for Argos Translate"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Argos Translate - Offline Translation")
        self.root.geometry("1000x700")
        self.root.minsize(800, 600)
        
        # Configure style
        self.setup_styles()
        
        # Initialize variables
        self.languages: List = []
        self.available_packages = []
        self.installed_packages = []
        self.argos_available = ARGOS_AVAILABLE
        
        # Create GUI elements
        self.create_widgets()
        
        # Load initial data
        if self.argos_available:
            self.load_languages()
            self.load_packages()
        else:
            self.show_demo_mode()
        
        # Message queue for thread communication
        self.message_queue = queue.Queue()
        self.check_queue()
    
    def setup_styles(self):
        """Configure the application styles"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
        style.configure('Heading.TLabel', font=('Arial', 12, 'bold'))
        style.configure('Status.TLabel', font=('Arial', 10))
        style.configure('Warning.TLabel', font=('Arial', 10), foreground='orange')
        style.configure('Error.TLabel', font=('Arial', 10), foreground='red')
        
        # Configure buttons
        style.configure('Action.TButton', font=('Arial', 10, 'bold'))
        style.configure('Primary.TButton', font=('Arial', 10, 'bold'))
    
    def create_widgets(self):
        """Create the main GUI widgets"""
        # Create main notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Translation tab
        self.create_translation_tab()
        
        # Package management tab
        self.create_package_tab()
        
        # Settings tab
        self.create_settings_tab()
        
        # Status bar
        self.create_status_bar()
    
    def create_translation_tab(self):
        """Create the translation interface tab"""
        self.translation_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.translation_frame, text="Translation")
        
        # Title
        title_label = ttk.Label(
            self.translation_frame, 
            text="Argos Translate", 
            style='Title.TLabel'
        )
        title_label.pack(pady=(10, 20))
        
        # Language selection frame
        lang_frame = ttk.LabelFrame(self.translation_frame, text="Language Selection", padding=10)
        lang_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # From language
        from_frame = ttk.Frame(lang_frame)
        from_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(from_frame, text="From:", style='Heading.TLabel').pack(side=tk.LEFT)
        self.from_lang_var = tk.StringVar()
        self.from_combo = ttk.Combobox(
            from_frame, 
            textvariable=self.from_lang_var,
            state='readonly',
            width=30
        )
        self.from_combo.pack(side=tk.LEFT, padx=(10, 0))
        
        # Swap button
        swap_btn = ttk.Button(
            from_frame, 
            text="⇄", 
            command=self.swap_languages,
            width=3
        )
        swap_btn.pack(side=tk.LEFT, padx=10)
        
        # To language
        to_frame = ttk.Frame(lang_frame)
        to_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(to_frame, text="To:", style='Heading.TLabel').pack(side=tk.LEFT)
        self.to_lang_var = tk.StringVar()
        self.to_combo = ttk.Combobox(
            to_frame, 
            textvariable=self.to_lang_var,
            state='readonly',
            width=30
        )
        self.to_combo.pack(side=tk.LEFT, padx=(10, 0))
        
        # Text input frame
        text_frame = ttk.LabelFrame(self.translation_frame, text="Text Translation", padding=10)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Input text
        ttk.Label(text_frame, text="Input Text:", style='Heading.TLabel').pack(anchor=tk.W)
        self.input_text = scrolledtext.ScrolledText(
            text_frame, 
            height=8, 
            wrap=tk.WORD,
            font=('Arial', 11)
        )
        self.input_text.pack(fill=tk.BOTH, expand=True, pady=(5, 10))
        
        # Translate button
        translate_btn = ttk.Button(
            text_frame, 
            text="Translate", 
            command=self.translate_text,
            style='Primary.TButton'
        )
        translate_btn.pack(pady=5)
        
        # Output text
        ttk.Label(text_frame, text="Translated Text:", style='Heading.TLabel').pack(anchor=tk.W, pady=(10, 0))
        self.output_text = scrolledtext.ScrolledText(
            text_frame, 
            height=8, 
            wrap=tk.WORD,
            font=('Arial', 11),
            state=tk.DISABLED
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Copy button
        copy_btn = ttk.Button(
            text_frame, 
            text="Copy Translation", 
            command=self.copy_translation
        )
        copy_btn.pack(pady=5)
    
    def create_package_tab(self):
        """Create the package management tab"""
        self.package_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.package_frame, text="Package Management")
        
        # Title
        title_label = ttk.Label(
            self.package_frame, 
            text="Language Package Management", 
            style='Title.TLabel'
        )
        title_label.pack(pady=(10, 20))
        
        # Control buttons frame
        control_frame = ttk.Frame(self.package_frame)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Update packages button
        update_btn = ttk.Button(
            control_frame, 
            text="Update Package Index", 
            command=self.update_package_index,
            style='Action.TButton'
        )
        update_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Refresh button
        refresh_btn = ttk.Button(
            control_frame, 
            text="Refresh", 
            command=self.load_packages
        )
        refresh_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(
            control_frame, 
            variable=self.progress_var,
            mode='indeterminate'
        )
        self.progress_bar.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Package list frame
        list_frame = ttk.LabelFrame(self.package_frame, text="Available Packages", padding=10)
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Treeview for packages
        columns = ('Package', 'From', 'To', 'Version', 'Status')
        self.package_tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=15)
        
        # Configure columns
        self.package_tree.heading('Package', text='Package Name')
        self.package_tree.heading('From', text='From Language')
        self.package_tree.heading('To', text='To Language')
        self.package_tree.heading('Version', text='Version')
        self.package_tree.heading('Status', text='Status')
        
        self.package_tree.column('Package', width=200)
        self.package_tree.column('From', width=120)
        self.package_tree.column('To', width=120)
        self.package_tree.column('Version', width=80)
        self.package_tree.column('Status', width=100)
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.package_tree.yview)
        self.package_tree.configure(yscrollcommand=scrollbar.set)
        
        self.package_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Package action buttons
        action_frame = ttk.Frame(self.package_frame)
        action_frame.pack(fill=tk.X, padx=10, pady=5)
        
        install_btn = ttk.Button(
            action_frame, 
            text="Install Selected", 
            command=self.install_selected_package,
            style='Action.TButton'
        )
        install_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        uninstall_btn = ttk.Button(
            action_frame, 
            text="Uninstall Selected", 
            command=self.uninstall_selected_package
        )
        uninstall_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Bind selection event
        self.package_tree.bind('<<TreeviewSelect>>', self.on_package_select)
    
    def create_settings_tab(self):
        """Create the settings tab"""
        self.settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_frame, text="Settings")
        
        # Title
        title_label = ttk.Label(
            self.settings_frame, 
            text="Settings", 
            style='Title.TLabel'
        )
        title_label.pack(pady=(10, 20))
        
        # Settings frame
        settings_frame = ttk.LabelFrame(self.settings_frame, text="Configuration", padding=20)
        settings_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Device type setting
        device_frame = ttk.Frame(settings_frame)
        device_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(device_frame, text="Device Type:", style='Heading.TLabel').pack(side=tk.LEFT)
        self.device_var = tk.StringVar(value='cpu')
        if self.argos_available and settings:
            self.device_var.set(settings.device)
        
        device_combo = ttk.Combobox(
            device_frame, 
            textvariable=self.device_var,
            values=['cpu', 'cuda', 'auto'],
            state='readonly',
            width=15
        )
        device_combo.pack(side=tk.LEFT, padx=(10, 0))
        
        # Debug mode
        debug_frame = ttk.Frame(settings_frame)
        debug_frame.pack(fill=tk.X, pady=10)
        
        self.debug_var = tk.BooleanVar(value=False)
        if self.argos_available and settings:
            self.debug_var.set(settings.debug)
        
        debug_check = ttk.Checkbutton(
            debug_frame, 
            text="Enable Debug Mode", 
            variable=self.debug_var
        )
        debug_check.pack(side=tk.LEFT)
        
        # Package directory
        pkg_frame = ttk.Frame(settings_frame)
        pkg_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(pkg_frame, text="Package Directory:", style='Heading.TLabel').pack(anchor=tk.W)
        pkg_path_frame = ttk.Frame(pkg_frame)
        pkg_path_frame.pack(fill=tk.X, pady=5)
        
        default_pkg_dir = str(Path.home() / ".local" / "share" / "argos-translate" / "packages")
        self.pkg_dir_var = tk.StringVar(value=default_pkg_dir)
        if self.argos_available and settings:
            self.pkg_dir_var.set(str(settings.package_data_dir))
        
        pkg_dir_entry = ttk.Entry(pkg_path_frame, textvariable=self.pkg_dir_var, width=50)
        pkg_dir_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        browse_btn = ttk.Button(
            pkg_path_frame, 
            text="Browse", 
            command=self.browse_package_directory
        )
        browse_btn.pack(side=tk.LEFT, padx=(10, 0))
        
        # Save settings button
        save_btn = ttk.Button(
            settings_frame, 
            text="Save Settings", 
            command=self.save_settings,
            style='Action.TButton'
        )
        save_btn.pack(pady=20)
        
        # Info frame
        info_frame = ttk.LabelFrame(self.settings_frame, text="System Information", padding=20)
        info_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Display system info
        if self.argos_available and settings:
            info_text = f"""
Argos Translate Version: {getattr(settings, '__version__', 'Unknown')}
Package Directory: {settings.package_data_dir}
Cache Directory: {settings.cache_dir}
Device Type: {settings.device}
Debug Mode: {settings.debug}
Model Provider: {settings.model_provider.name if hasattr(settings.model_provider, 'name') else settings.model_provider}
            """.strip()
        else:
            info_text = f"""
Argos Translate: Not Available (Demo Mode)
Python Version: {sys.version}
GUI Framework: Tkinter
Status: Running in compatibility mode
            """.strip()
        
        info_label = ttk.Label(info_frame, text=info_text, font=('Courier', 9))
        info_label.pack(anchor=tk.W)
    
    def create_status_bar(self):
        """Create the status bar"""
        self.status_frame = ttk.Frame(self.root)
        self.status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        
        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(
            self.status_frame, 
            textvariable=self.status_var, 
            style='Status.TLabel'
        )
        status_label.pack(side=tk.LEFT, padx=10, pady=5)
        
        # Language count
        self.lang_count_var = tk.StringVar()
        lang_count_label = ttk.Label(
            self.status_frame, 
            textvariable=self.lang_count_var, 
            style='Status.TLabel'
        )
        lang_count_label.pack(side=tk.RIGHT, padx=10, pady=5)
    
    def show_demo_mode(self):
        """Show demo mode when Argos Translate is not available"""
        # Add demo languages
        demo_languages = [
            ("English", "en"),
            ("Spanish", "es"),
            ("French", "fr"),
            ("German", "de"),
            ("Italian", "it"),
            ("Portuguese", "pt"),
            ("Russian", "ru"),
            ("Chinese", "zh"),
            ("Japanese", "ja"),
            ("Korean", "ko")
        ]
        
        lang_names = [f"{name} ({code})" for name, code in demo_languages]
        self.from_combo['values'] = lang_names
        self.to_combo['values'] = lang_names
        
        # Set default languages
        if lang_names:
            self.from_lang_var.set(lang_names[0])  # English
            if len(lang_names) > 1:
                self.to_lang_var.set(lang_names[1])  # Spanish
        
        self.update_language_count()
        self.status_var.set("Demo Mode - Argos Translate not available")
        
        # Add demo packages
        demo_packages = [
            ("translate-en_es", "English", "Spanish", "1.0", "Available"),
            ("translate-en_fr", "English", "French", "1.0", "Available"),
            ("translate-en_de", "English", "German", "1.0", "Available"),
            ("translate-es_en", "Spanish", "English", "1.0", "Available"),
            ("translate-fr_en", "French", "English", "1.0", "Available"),
        ]
        
        for pkg_data in demo_packages:
            self.package_tree.insert('', 'end', values=pkg_data)
    
    def load_languages(self):
        """Load available languages"""
        if not self.argos_available:
            return
        
        try:
            self.status_var.set("Loading languages...")
            self.languages = translate.get_installed_languages()
            
            # Update language comboboxes
            lang_names = [f"{lang.name} ({lang.code})" for lang in self.languages]
            self.from_combo['values'] = lang_names
            self.to_combo['values'] = lang_names
            
            # Set default languages if available
            if self.languages:
                # Try to set English as default from language
                en_lang = next((lang for lang in self.languages if lang.code == 'en'), None)
                if en_lang:
                    self.from_lang_var.set(f"{en_lang.name} ({en_lang.code})")
                
                # Set first non-English language as default to language
                other_lang = next((lang for lang in self.languages if lang.code != 'en'), None)
                if other_lang:
                    self.to_lang_var.set(f"{other_lang.name} ({other_lang.code})")
            
            self.update_language_count()
            self.status_var.set("Languages loaded successfully")
            
        except Exception as e:
            self.status_var.set(f"Error loading languages: {str(e)}")
            messagebox.showerror("Error", f"Failed to load languages: {str(e)}")
    
    def load_packages(self):
        """Load available and installed packages"""
        if not self.argos_available:
            return
        
        try:
            self.status_var.set("Loading packages...")
            
            # Get installed packages
            self.installed_packages = package.get_installed_packages()
            installed_codes = {f"{pkg.from_code}-{pkg.to_code}" for pkg in self.installed_packages}
            
            # Get available packages
            try:
                self.available_packages = package.get_available_packages()
            except:
                # If no package index, update it first
                self.update_package_index()
                self.available_packages = package.get_available_packages()
            
            # Update package tree
            self.update_package_tree(installed_codes)
            
            self.status_var.set("Packages loaded successfully")
            
        except Exception as e:
            self.status_var.set(f"Error loading packages: {str(e)}")
            messagebox.showerror("Error", f"Failed to load packages: {str(e)}")
    
    def update_package_tree(self, installed_codes: set):
        """Update the package tree view"""
        # Clear existing items
        for item in self.package_tree.get_children():
            self.package_tree.delete(item)
        
        # Add packages to tree
        for pkg in self.available_packages:
            package_id = f"{pkg.from_code}-{pkg.to_code}"
            status = "Installed" if package_id in installed_codes else "Available"
            
            self.package_tree.insert('', 'end', values=(
                pkg.code,
                pkg.from_name,
                pkg.to_name,
                pkg.package_version,
                status
            ))
    
    def update_language_count(self):
        """Update the language count in status bar"""
        if self.argos_available:
            count = len(self.languages)
        else:
            count = 10  # Demo mode
        self.lang_count_var.set(f"Languages: {count}")
    
    def swap_languages(self):
        """Swap the from and to languages"""
        from_lang = self.from_lang_var.get()
        to_lang = self.to_lang_var.get()
        self.from_lang_var.set(to_lang)
        self.to_lang_var.set(from_lang)
    
    def translate_text(self):
        """Translate the input text"""
        try:
            # Get input text
            input_text = self.input_text.get("1.0", tk.END).strip()
            if not input_text:
                messagebox.showwarning("Warning", "Please enter text to translate")
                return
            
            # Get language codes
            from_lang_str = self.from_lang_var.get()
            to_lang_str = self.to_lang_var.get()
            
            if not from_lang_str or not to_lang_str:
                messagebox.showwarning("Warning", "Please select both source and target languages")
                return
            
            # Extract language codes
            from_code = from_lang_str.split('(')[-1].rstrip(')')
            to_code = to_lang_str.split('(')[-1].rstrip(')')
            
            # Check if languages are the same
            if from_code == to_code:
                self.output_text.config(state=tk.NORMAL)
                self.output_text.delete("1.0", tk.END)
                self.output_text.insert("1.0", input_text)
                self.output_text.config(state=tk.DISABLED)
                return
            
            if not self.argos_available:
                # Demo mode translation
                self.demo_translate(input_text, from_code, to_code)
                return
            
            # Perform translation
            self.status_var.set("Translating...")
            self.root.update()
            
            # Run translation in thread to prevent GUI freezing
            thread = threading.Thread(target=self._translate_thread, args=(input_text, from_code, to_code))
            thread.daemon = True
            thread.start()
            
        except Exception as e:
            self.status_var.set(f"Translation error: {str(e)}")
            messagebox.showerror("Error", f"Translation failed: {str(e)}")
    
    def demo_translate(self, text: str, from_code: str, to_code: str):
        """Demo translation for when Argos Translate is not available"""
        # Simple demo translations
        demo_translations = {
            ("en", "es"): "¡Hola! Este es un modo de demostración.",
            ("en", "fr"): "Bonjour! Ceci est un mode de démonstration.",
            ("en", "de"): "Hallo! Dies ist ein Demo-Modus.",
            ("en", "it"): "Ciao! Questa è una modalità demo.",
            ("en", "pt"): "Olá! Este é um modo de demonstração.",
            ("en", "ru"): "Привет! Это демонстрационный режим.",
            ("en", "zh"): "你好！这是演示模式。",
            ("en", "ja"): "こんにちは！これはデモモードです。",
            ("en", "ko"): "안녕하세요! 이것은 데모 모드입니다.",
        }
        
        # Reverse translations
        reverse_translations = {v: k for k, v in demo_translations.items()}
        demo_translations.update(reverse_translations)
        
        # Default demo response
        demo_text = f"[Demo Mode] Translation from {from_code} to {to_code}: {text}"
        
        # Check for specific demo translation
        translation_key = (from_code, to_code)
        if translation_key in demo_translations:
            demo_text = demo_translations[translation_key]
        
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", demo_text)
        self.output_text.config(state=tk.DISABLED)
        self.status_var.set("Demo translation completed")
    
    def _translate_thread(self, text: str, from_code: str, to_code: str):
        """Translation thread function"""
        try:
            # Perform translation
            translated_text = translate.translate(text, from_code, to_code)
            
            # Queue the result for GUI update
            self.message_queue.put(('translation_result', translated_text))
            
        except Exception as e:
            self.message_queue.put(('translation_error', str(e)))
    
    def copy_translation(self):
        """Copy the translated text to clipboard"""
        try:
            translated_text = self.output_text.get("1.0", tk.END).strip()
            if translated_text:
                self.root.clipboard_clear()
                self.root.clipboard_append(translated_text)
                self.status_var.set("Translation copied to clipboard")
            else:
                messagebox.showwarning("Warning", "No translation to copy")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy text: {str(e)}")
    
    def update_package_index(self):
        """Update the package index"""
        if not self.argos_available:
            messagebox.showinfo("Demo Mode", "Package management is not available in demo mode")
            return
        
        def update_thread():
            try:
                self.message_queue.put(('status', 'Updating package index...'))
                self.progress_bar.start()
                
                package.update_package_index()
                
                self.message_queue.put(('status', 'Package index updated successfully'))
                self.message_queue.put(('refresh_packages', None))
                
            except Exception as e:
                self.message_queue.put(('error', f'Failed to update package index: {str(e)}'))
            finally:
                self.progress_bar.stop()
        
        thread = threading.Thread(target=update_thread)
        thread.daemon = True
        thread.start()
    
    def on_package_select(self, event):
        """Handle package selection"""
        selection = self.package_tree.selection()
        if selection:
            item = self.package_tree.item(selection[0])
            values = item['values']
            if values:
                self.status_var.set(f"Selected: {values[0]} ({values[1]} → {values[2]})")
    
    def install_selected_package(self):
        """Install the selected package"""
        if not self.argos_available:
            messagebox.showinfo("Demo Mode", "Package installation is not available in demo mode")
            return
        
        selection = self.package_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a package to install")
            return
        
        item = self.package_tree.item(selection[0])
        values = item['values']
        if values and values[4] == "Installed":
            messagebox.showinfo("Info", "Package is already installed")
            return
        
        # Find the package
        package_name = values[0]
        pkg = next((p for p in self.available_packages if p.code == package_name), None)
        
        if pkg:
            def install_thread():
                try:
                    self.message_queue.put(('status', f'Installing {package_name}...'))
                    self.progress_bar.start()
                    
                    pkg.install()
                    
                    self.message_queue.put(('status', f'Package {package_name} installed successfully'))
                    self.message_queue.put(('refresh_packages', None))
                    self.message_queue.put(('refresh_languages', None))
                    
                except Exception as e:
                    self.message_queue.put(('error', f'Failed to install package: {str(e)}'))
                finally:
                    self.progress_bar.stop()
            
            thread = threading.Thread(target=install_thread)
            thread.daemon = True
            thread.start()
    
    def uninstall_selected_package(self):
        """Uninstall the selected package"""
        if not self.argos_available:
            messagebox.showinfo("Demo Mode", "Package management is not available in demo mode")
            return
        
        selection = self.package_tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a package to uninstall")
            return
        
        item = self.package_tree.item(selection[0])
        values = item['values']
        if values and values[4] != "Installed":
            messagebox.showinfo("Info", "Package is not installed")
            return
        
        # Confirm uninstall
        package_name = values[0]
        if messagebox.askyesno("Confirm", f"Are you sure you want to uninstall {package_name}?"):
            def uninstall_thread():
                try:
                    self.message_queue.put(('status', f'Uninstalling {package_name}...'))
                    self.progress_bar.start()
                    
                    # Find and uninstall the package
                    pkg = next((p for p in self.installed_packages if p.code == package_name), None)
                    if pkg:
                        package.uninstall_package(pkg)
                    
                    self.message_queue.put(('status', f'Package {package_name} uninstalled successfully'))
                    self.message_queue.put(('refresh_packages', None))
                    self.message_queue.put(('refresh_languages', None))
                    
                except Exception as e:
                    self.message_queue.put(('error', f'Failed to uninstall package: {str(e)}'))
                finally:
                    self.progress_bar.stop()
            
            thread = threading.Thread(target=uninstall_thread)
            thread.daemon = True
            thread.start()
    
    def browse_package_directory(self):
        """Browse for package directory"""
        directory = filedialog.askdirectory(
            title="Select Package Directory",
            initialdir=self.pkg_dir_var.get()
        )
        if directory:
            self.pkg_dir_var.set(directory)
    
    def save_settings(self):
        """Save settings"""
        try:
            if self.argos_available and settings:
                # Update device setting
                os.environ['ARGOS_DEVICE_TYPE'] = self.device_var.get()
                settings.device = self.device_var.get()
                
                # Update debug setting
                os.environ['ARGOS_DEBUG'] = '1' if self.debug_var.get() else '0'
                settings.debug = self.debug_var.get()
                
                # Update package directory
                new_pkg_dir = self.pkg_dir_var.get()
                if new_pkg_dir != str(settings.package_data_dir):
                    os.environ['ARGOS_PACKAGES_DIR'] = new_pkg_dir
                    settings.package_data_dir = Path(new_pkg_dir)
                    settings.package_dirs = [settings.package_data_dir]
            
            messagebox.showinfo("Success", "Settings saved successfully")
            self.status_var.set("Settings saved")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {str(e)}")
    
    def check_queue(self):
        """Check for messages from worker threads"""
        try:
            while True:
                message_type, data = self.message_queue.get_nowait()
                
                if message_type == 'translation_result':
                    self.output_text.config(state=tk.NORMAL)
                    self.output_text.delete("1.0", tk.END)
                    self.output_text.insert("1.0", data)
                    self.output_text.config(state=tk.DISABLED)
                    self.status_var.set("Translation completed")
                
                elif message_type == 'translation_error':
                    self.status_var.set(f"Translation error: {data}")
                    messagebox.showerror("Translation Error", data)
                
                elif message_type == 'status':
                    self.status_var.set(data)
                
                elif message_type == 'error':
                    self.status_var.set(f"Error: {data}")
                    messagebox.showerror("Error", data)
                
                elif message_type == 'refresh_packages':
                    self.load_packages()
                
                elif message_type == 'refresh_languages':
                    self.load_languages()
                
        except queue.Empty:
            pass
        
        # Schedule next check
        self.root.after(100, self.check_queue)


def main():
    """Main function to run the GUI"""
    root = tk.Tk()
    app = ArgosTranslateGUI(root)
    
    # Center the window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # Start the GUI
    root.mainloop()


if __name__ == "__main__":
    main()
