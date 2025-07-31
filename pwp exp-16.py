import tkinter as tk

# Function to display typed text
def display_text():
    typed_text = entry.get()
    label_output.config(text=f"You typed: {typed_text}")

# Create main window
root = tk.Tk()
root.title("Text Input App")
root.geometry("350x200")

# Input field
entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=10)

# Button to display text
button = tk.Button(root, text="Display Text", command=display_text, font=("Arial", 12))
button.pack(pady=5)

# Label to show output
label_output = tk.Label(root, text="", font=("Arial", 14), fg="blue")
label_output.pack(pady=10)

# Start GUI loop
root.mainloop()
