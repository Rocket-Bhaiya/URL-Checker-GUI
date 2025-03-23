import tkinter as tk
from tkinter import ttk, messagebox
from core.endpoint_checker import check_endpoint

class AppWindow:
    def __init__(self, master):
        self.master = master
        
        # Create the GUI elements
        self.url_label = tk.Label(master, text="Enter URL:")
        self.url_entry = tk.Entry(master, width=50)
        self.check_button = tk.Button(master, text="Check Endpoint", command=self.check_url)
        self.result_label = tk.Label(master, text="Result:")
        self.result_text = tk.Text(master, width=50, height=10, state="disabled")
        
        # Place the elements on the grid
        self.url_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)
        self.check_button.grid(row=1, column=0, columnspan=2, pady=10)
        self.result_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        self.result_text.grid(row=2, column=1, padx=10, pady=10)
        
    def check_url(self):
        url = self.url_entry.get()
        try:
            success, status_code, hash_value = check_endpoint(url)
            
            # Enable text widget for editing
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, tk.END)
            
            # Display results
            if success:
                self.result_text.insert(tk.END, f"URL is valid\nStatus Code: {status_code}\nHash Value: {hash_value}")
            else:
                self.result_text.insert(tk.END, f"Failed to connect to URL\nError: {hash_value}")
            
            # Disable text widget after updating
            self.result_text.config(state="disabled")
            
        except Exception as e:
            messagebox.showerror("Error", str(e))