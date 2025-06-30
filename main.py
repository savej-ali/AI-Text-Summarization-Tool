import tkinter as tk
from tkinter import scrolledtext, messagebox
from summarizer import extract_summary 

def handle_summarization():
    raw_text = input_area.get("1.0", tk.END).strip()
    if len(raw_text) < 10:
        messagebox.showwarning("Notice", "Enter at least 10 characters.")
        return

    try:
        output = extract_summary(raw_text, summary_length=3)
        input_area.delete("1.0", tk.END)

        result_area.config(state=tk.NORMAL)
        result_area.delete("1.0", tk.END)
        result_area.insert(tk.END, output)
        result_area.config(state=tk.DISABLED)
    except Exception as err:
        messagebox.showerror("Error", f"Error during summarization:\n{err}")

# App Window
window = tk.Tk()
window.title("Smart Text Summarizer")
window.geometry("920x720")
window.configure(bg="#fcfcfc")

# Fonts and Themes
TITLE_FONT = ("Arial", 18, "bold")
LABEL_FONT = ("Arial", 11)
TEXT_FONT = ("Courier", 12)
COLOR_MAIN = "#1a73e8"
COLOR_HOVER = "#155ab6"

# Title Label
title_lbl = tk.Label(window, text="🔎 AI-Powered Summarization", font=TITLE_FONT, bg="#fcfcfc", fg="#333")
title_lbl.pack(pady=(25, 10))

# Input Label
lbl_input = tk.Label(window, text="Input Text:", font=LABEL_FONT, bg="#fcfcfc")
lbl_input.pack(anchor="w", padx=30)

# Input Box
input_area = scrolledtext.ScrolledText(window, height=13, width=105, wrap=tk.WORD,
                                       font=TEXT_FONT, bg="white", bd=1, relief=tk.SOLID)
input_area.pack(padx=30, pady=(5, 20))

# Hover Functions
def hover_in(event): summarize_button.config(bg=COLOR_HOVER)
def hover_out(event): summarize_button.config(bg=COLOR_MAIN)

# Summarize Button
summarize_button = tk.Button(window, text="Summarize", font=("Arial", 12, "bold"),
                             bg=COLOR_MAIN, fg="white", padx=20, pady=10,
                             relief=tk.FLAT, command=handle_summarization, cursor="hand2")
summarize_button.bind("<Enter>", hover_in)
summarize_button.bind("<Leave>", hover_out)
summarize_button.pack(pady=10)

# Output Label
lbl_output = tk.Label(window, text="Summary Output:", font=LABEL_FONT, bg="#fcfcfc")
lbl_output.pack(anchor="w", padx=30, pady=(15, 0))

# Output Box
result_area = scrolledtext.ScrolledText(window, height=9, width=105, wrap=tk.WORD,
                                        font=TEXT_FONT, bg="#eaeaea", bd=1, relief=tk.SOLID)
result_area.config(state=tk.DISABLED)
result_area.pack(padx=30, pady=(5, 15))

# Footer Label
footer_note = tk.Label(window, text="Developed by Savej Ali", font=("Arial", 10, "italic"),
                       bg="#fcfcfc", fg="#666")
footer_note.pack(side=tk.BOTTOM, pady=10)

# Launch
window.mainloop()
