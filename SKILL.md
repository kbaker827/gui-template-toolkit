---
name: gui-template-toolkit
description: GUI application templates and patterns for Python tkinter. Use when building desktop applications with tkinter - includes window setup, frames, widgets, threading, and common UI patterns. Extracted from 4+ GUI tools via Ralph Loop analysis.
---

# GUI Template Toolkit

**Reusable tkinter GUI patterns extracted from Ralph Loop analysis.**

## What It Provides

Ready-to-use GUI patterns including:
- ✅ Standard tkinter app structure
- ✅ Progress bars with threading
- ✅ Scrolled text logging
- ✅ Button actions and callbacks
- ✅ File dialogs and browsing
- ✅ Menu bars and toolbars
- ✅ Status bar updates

## Quick Start

### Basic GUI Template

```python
#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Application")
        self.root.geometry("800x600")
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add widgets here
        ttk.Label(main_frame, text="Hello World!").pack()
        
    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    app = MyApp(root)
    app.run()
```

### GUI with Progress Bar Template

```python
import tkinter as tk
from tkinter import ttk
import threading

class AppWithProgress:
    def __init__(self, root):
        self.root = root
        self.progress_var = tk.DoubleVar(value=0)
        
    def start_task(self):
        thread = threading.Thread(target=self.long_task)
        thread.start()
        
    def long_task(self):
        for i in range(101):
            self.progress_var.set(i)
            self.root.after(10, lambda: None)
```

## Scripts

- `scripts/tkinter_boilerplate.py` - Full app template
- `scripts/progress_dialog.py` - Progress bar with threading
- `widgets/common_widgets.py` - Reusable widget patterns

## Usage Examples

"Create a tkinter GUI with progress bar and log window"

→ Use this skill to generate the boilerplate instantly.

## Ralph Loop Origin

Extracted from GUI patterns in:
- sharepoint-orphan-finder
- adobe-sign-cache-reset
- And 2 more GUI tools...
