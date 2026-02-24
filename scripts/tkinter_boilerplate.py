#!/usr/bin/env python3
"""
Full tkinter GUI application template
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import platform


class Application:
    """Main application class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Application Name")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        
        # Platform-specific tweaks
        if platform.system() == 'Windows':
            self.root.tk.call('tk', 'scaling', 1.5)
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = ttk.Label(
            main_frame, 
            text="Application Title",
            font=('Segoe UI', 14, 'bold')
        )
        header.pack(anchor=tk.W, pady=(0, 10))
        
        # Content area
        content = ttk.Frame(main_frame)
        content.pack(fill=tk.BOTH, expand=True)
        
        # Add your widgets here
        ttk.Label(content, text="Your content here").pack()
        
        # Buttons
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(
            btn_frame, 
            text="Action",
            command=self.on_action
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            btn_frame,
            text="Exit",
            command=self.root.quit
        ).pack(side=tk.RIGHT, padx=5)
        
    def on_action(self):
        """Handle action button"""
        messagebox.showinfo("Action", "Button clicked!")


def main():
    """Main entry point"""
    root = tk.Tk()
    
    # DPI awareness on Windows
    if platform.system() == 'Windows':
        try:
            from ctypes import windll
            windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
    
    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()
