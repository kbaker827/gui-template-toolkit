#!/usr/bin/env python3
"""
Progress bar dialog with threading support
"""

import tkinter as tk
from tkinter import ttk
import threading


class ProgressDialog:
    """Progress dialog with determinate progress bar"""
    
    def __init__(self, parent, title="Progress", maximum=100):
        self.parent = parent
        self.maximum = maximum
        
        self.window = tk.Toplevel(parent)
        self.window.title(title)
        self.window.geometry("400x120")
        self.window.resizable(False, False)
        self.window.transient(parent)
        self.window.grab_set()
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup dialog UI"""
        frame = ttk.Frame(self.window, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)
        
        self.label = ttk.Label(frame, text="Processing...")
        self.label.pack(anchor=tk.W)
        
        self.progress_var = tk.DoubleVar(value=0)
        self.progress = ttk.Progressbar(
            frame,
            variable=self.progress_var,
            maximum=self.maximum,
            mode='determinate'
        )
        self.progress.pack(fill=tk.X, pady=(10, 0))
        
        self.percent_label = ttk.Label(frame, text="0%")
        self.percent_label.pack(anchor=tk.E)
        
    def update(self, value, message=None):
        """Update progress"""
        self.progress_var.set(value)
        percent = int((value / self.maximum) * 100)
        self.percent_label.config(text=f"{percent}%")
        if message:
            self.label.config(text=message)
        self.window.update()
        
    def close(self):
        """Close the dialog"""
        self.window.destroy()


class AppWithProgress:
    """Example application with progress"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Progress Example")
        self.root.geometry("400x200")
        
        ttk.Button(
            self.root,
            text="Start Long Task",
            command=self.start_task
        ).pack(pady=20)
        
    def start_task(self):
        """Start long-running task in thread"""
        self.progress = ProgressDialog(self.root, "Processing", 100)
        
        thread = threading.Thread(target=self.long_task)
        thread.start()
        
    def long_task(self):
        """Simulate long task"""
        import time
        for i in range(101):
            time.sleep(0.05)
            # Update from main thread
            self.root.after(0, lambda v=i: self.progress.update(v, f"Step {v}"))
            
        self.root.after(0, self.progress.close)


if __name__ == '__main__':
    root = tk.Tk()
    app = AppWithProgress(root)
    root.mainloop()
