from tkinter import *
from tkinter import ttk

class LoadingWindow:
    def __init__(self, parent):
        self.parent = parent
        self.loading_window = Toplevel(parent)
        self.loading_window.title("Loading...")
        self.loading_window.geometry("300x100")
        self.loading_window.resizable(False, False)
        
        
        ## Add label
        self.label = Label(self.loading_window, text="Loading, please wait...")
        self.label.pack(pady=10)
        
        ## Add progress bar
        self.progressbar = ttk.Progressbar(self.loading_window, orient="horizontal", length=200, mode="determinate")
        self.progressbar.pack(pady=10)
        
        self.loading_window.grab_set()  
        parent.update()  # Update the main window's interface so the loading window is visible
    
    def destroy(self):
        self.loading_window.grab_release()
        self.loading_window.destroy()

    def set_progress(self, value): ## Set the progress bar value from 0 to 100
        self.progressbar['value'] = value

