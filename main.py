import tkinter as tk
from gui.app_window import AppWindow

def main():
    root = tk.Tk()
    root.title("URL Endpoint Verifier")
    window = AppWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()