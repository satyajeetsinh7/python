import tkinter as tk

# Function to increment counter
def increment():
    global count
    count += 1
    label.config(text=f"Count: {count}")

# Initialize count
count = 0

# Create main window
root = tk.Tk()
root.title("Counter App")
root.geometry("300x200")

# Create label to display count
label = tk.Label(root, text="Count: 0", font=("Arial", 24))
label.pack(pady=20)

# Create increment button
button = tk.Button(root, text="Increment", command=increment, font=("Arial", 16))
button.pack(pady=10)

# Start GUI event loop
root.mainloop()
