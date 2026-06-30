import tkinter as tk
from tkinter import messagebox


# 1. Functions for Sidebar Navigation (Buttons ke kaam)
def show_home():
    clear_frame()
    label = tk.Label(
        content_frame,
        text="Welcome to Your Mini Portal!",
        font=("Arial", 24, "bold"),
        bg="white",
    )
    label.pack(pady=50)
    sub_label = tk.Label(
        content_frame,
        text="Click any option from the left menu to start.",
        font=("Arial", 14),
        bg="white",
        fg="gray",
    )
    sub_label.pack()


def show_calculator():
    clear_frame()
    tk.Label(
        content_frame,
        text="Simple 10+10 Calculator",
        font=("Arial", 18, "bold"),
        bg="white",
    ).pack(pady=10)

    # Input Boxes
    num1_entry = tk.Entry(content_frame, font=("Arial", 14), bd=2, width=10)
    num1_entry.pack(pady=5)
    num2_entry = tk.Entry(content_frame, font=("Arial", 14), bd=2, width=10)
    num2_entry.pack(pady=5)

    # Calculation logic
    def do_sum():
        try:
            res = float(num1_entry.get()) + float(num2_entry.get())
            result_label.config(text=f"Answer: {res}")
        except:
            messagebox.showerror("Error", "Please enter valid numbers!")

    tk.Button(
        content_frame,
        text="Calculate Total",
        command=do_sum,
        bg="#4CAF50",
        fg="white",
    ).pack(pady=10)
    result_label = tk.Label(
        content_frame, text="Answer: 0", font=("Arial", 14, "bold"), bg="white"
    )
    result_label.pack(pady=5)


def show_notes():
    clear_frame()
    tk.Label(
        content_frame,
        text="Quick Notepad",
        font=("Arial", 18, "bold"),
        bg="white",
    ).pack(pady=10)

    # Text Area for typing notes
    text_area = tk.Text(content_frame, width=40, height=8, font=("Arial", 12))
    text_area.pack(pady=10)

    def save_note():
        messagebox.showinfo("Success", "Your note has been saved successfully!")

    tk.Button(
        content_frame, text="Save Note", command=save_note, bg="#008CBA", fg="white"
    ).pack()


def clear_frame():
    # Yeh function purani screen ka data saaf karta hai taake naya page khul sake
    for widget in content_frame.winfo_children():
        widget.destroy()


# 2. Main Window Design (Portal ki Base)
root = tk.Tk()
root.title("My First Python Mini Portal")
root.geometry("600x400")

# Left Sidebar Frame (Menu Box)
sidebar = tk.Frame(root, bg="#333333", width=150, height=400)
sidebar.pack(side="left", fill="y")

# Right Content Frame (Main Display Box)
content_frame = tk.Frame(root, bg="white", width=450, height=400)
content_frame.pack(side="right", expand=True, fill="both")

# 3. Sidebar Menu Buttons
btn_home = tk.Button(
    sidebar,
    text="Home",
    command=show_home,
    bg="#555555",
    fg="white",
    width=15,
    bd=0,
    pady=10,
)
btn_home.pack(pady=10)

btn_calc = tk.Button(
    sidebar,
    text="Calculator",
    command=show_calculator,
    bg="#555555",
    fg="white",
    width=15,
    bd=0,
    pady=10,
)
btn_calc.pack(pady=10)

btn_notes = tk.Button(
    sidebar,
    text="Notes",
    command=show_notes,
    bg="#555555",
    fg="white",
    width=15,
    bd=0,
    pady=10,
)
btn_notes.pack(pady=10)

# Default screen to show on startup
show_home()

# Start the application
root.mainloop()