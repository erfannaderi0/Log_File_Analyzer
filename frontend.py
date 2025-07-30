# frontend.py
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
from main import log_parser  # ✅ import from your logic file

def browse_log_file():
    filepath = filedialog.askopenfilename(filetypes=[("Log files", "*.log *.txt")])
    log_file_var.set(filepath)

def browse_save_path():
    filename = f"log_summary_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"
    path = filedialog.asksaveasfilename(
        initialfile=filename,
        defaultextension=".xlsx",
        filetypes=[("Excel files", "*.xlsx")],
        title="Save summary report as..."
    )
    save_path_var.set(path)

def run_analysis():
    log_file = log_file_var.get()
    save_path = save_path_var.get()

    if not log_file or not save_path:
        messagebox.showerror("Error", "Please select both input and output files.")
        return

    try:
        log_parser(log_file, save_path)
        messagebox.showinfo("Success", f"Report saved to:\n{save_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Set up GUI
root = tk.Tk()
root.title("Log Analyzer")
root.geometry("500x300")

log_file_var = tk.StringVar()
save_path_var = tk.StringVar()

tk.Label(root, text="Select Log File:").pack(pady=5)
tk.Entry(root, textvariable=log_file_var, width=60).pack()
tk.Button(root, text="Browse...", command=browse_log_file).pack(pady=5)

tk.Label(root, text="Save Excel Report To:").pack(pady=5)
tk.Entry(root, textvariable=save_path_var, width=60).pack()
tk.Button(root, text="Browse...", command=browse_save_path).pack(pady=5)

tk.Button(root, text="Analyze Logs", command=run_analysis, bg="green", fg="white").pack(pady=10)

root.mainloop()
