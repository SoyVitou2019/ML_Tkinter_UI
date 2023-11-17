import tkinter as Tk
from tkinter import ttk

def Edit_Image():
    edit_root = Tk.Tk()
    frame = Tk.Frame(edit_root, bg='gray')
    edit_root.geometry("500x300")
    edit_root.title("Customize Image")
    frame.pack()
    edit_root.mainloop()
    
def create_progress_bar(root):
    global progress_bar, loading_label
    def update_progress():
        value = progress_var.get()
        if value <= 100:
            progress_var.set(value + 1)
            progress_bar["value"] = value
            root.after(30, update_progress)
            if value >=100:
                loading_label.destroy()

    # Create a progress bar variable
    progress_var = Tk.DoubleVar()

    loading_label = Tk.Label(root, text="Loading ...", fg='#3498DB' , font=("Helvetica", 12))
    loading_label.pack(pady=5)
    # Create a progress bar widget
    progress_bar = ttk.Progressbar(root, variable=progress_var, orient="horizontal", length=200, mode="determinate", style="text.Horizontal.TProgressbar")
    progress_bar.pack(pady=5)
    # Start the progress
    update_progress()
    
    
def show_message(root, result, calculate_score, btn_browse, Edit_btn):
    global label_frame, label_text1, label_text2
    select_class = list(result.keys())[0]
    non_abusive = ["Nice emoji", "Non Abuse"]
    accurate = calculate_score(top_class=result, non_Abuse=non_abusive)
    pick_type = ""
    color = ""
    status = ""
    if select_class in non_abusive:
        pick_type = "Non Abusive Image"
        status = "Non-Abusive"
        color = "green"
    else:
        pick_type = "Abusive Image"
        status = "Abusive"
        color = "red"
    label_text1 = Tk.Label(root, text=f"{pick_type} : {round(accurate[pick_type] * 100, 2)}% ", font=("Helvetica", 12))
    label_text2 = Tk.Label(root, text=f"Status : {status} ", fg=color , font=("Helvetica", 12))
    label_text1.pack()
    label_text2.pack()
    btn_browse.grid(row=2, column=0, columnspan="2", padx=10, pady=10)
    Edit_btn.grid(row=2, column=4, columnspan="2", padx=10, pady=10)