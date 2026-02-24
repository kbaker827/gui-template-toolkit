#!/usr/bin/env python3
"""
Common reusable tkinter widgets
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog


class LogWidget(scrolledtext.ScrolledText):
    """Scrolled text widget for logging"""
    
    def __init__(self, parent, height=10, **kwargs):
        super().__init__(
            parent,
            wrap=tk.WORD,
            font=('Consolas', 9),
            height=height,
            **kwargs
        )
        
    def log(self, message, tag=None):
        """Add log message"""
        import datetime
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.insert(tk.END, f"[{timestamp}] {message}\n")
        self.see(tk.END)
        
    def clear(self):
        """Clear log"""
        self.delete(1.0, tk.END)


class FileBrowseWidget(ttk.Frame):
    """File/directory browse widget"""
    
    def __init__(self, parent, label="Path:", mode='file', **kwargs):
        super().__init__(parent, **kwargs)
        
        self.mode = mode
        self.path_var = tk.StringVar()
        
        ttk.Label(self, text=label).pack(side=tk.LEFT)
        ttk.Entry(self, textvariable=self.path_var, width=40).pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=5
        )
        ttk.Button(self, text="Browse...", command=self.browse).pack(side=tk.LEFT)
        
    def browse(self):
        """Open browse dialog"""
        if self.mode == 'file':
            path = filedialog.askopenfilename()
        elif self.mode == 'directory':
            path = filedialog.askdirectory()
        else:
            path = filedialog.asksaveasfilename()
            
        if path:
            self.path_var.set(path)
            
    def get(self):
        """Get current path"""
        return self.path_var.get()


class StatusBar(ttk.Frame):
    """Status bar widget"""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, relief=tk.SUNKEN, **kwargs)
        
        self.label = ttk.Label(self, text="Ready")
        self.label.pack(side=tk.LEFT, padx=5)
        
    def set(self, message):
        """Update status"""
        self.label.config(text=message)


if __name__ == '__main__':
    # Demo
    root = tk.Tk()
    root.geometry("600x400")
    
    log = LogWidget(root, height=10)
    log.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    log.log("Application started")
    log.log("Processing item 1...")
    log.log("Complete!")
    
    root.mainloop()
