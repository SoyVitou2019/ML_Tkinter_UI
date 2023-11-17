import tkinter as Tk
# from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
from assets.hybrid import XG_boosting_prediction
from components import Edit_Image, create_progress_bar, show_message
from model import calculate_score, destroy_widget


root = Tk.Tk()

frame = Tk.Frame(root, bg='#45aaf2')
root.geometry("800x600")
root.title("Abusive Detection")

main_title = Tk.Label(root, text="Abusive Detection", font=('Arial', 20))
main_title.pack(padx=20, pady=20)

# Button Initial
btn_browse = Tk.Button(frame, text='Select Image', bg='#1F618D', fg='#F1C40F', font=('Arial', 18))
Edit_btn = Tk.Button(frame, text='Edit', bg='#1F618D', fg='#F1C40F', font=('Arial', 18))

label_frame = None
label_text1 = None
label_text2 = None
progress_bar = None
loading_label = None




                  

def selectPic():
    global label_frame, label_text1, label_text2
    # Delete previous image label if it exists
    destroy_widget(label_frame)
    destroy_widget(label_text1)
    destroy_widget(label_text2)
    destroy_widget(progress_bar)
    
    filename = filedialog.askopenfilename(initialdir="/images", title="Select Image",
                                      filetypes=(("jpg images", "*.jpg"), ("All files", "*.*")))
    # Create a photoimage object of the image in the path
    if filename is not None:
        image1 = Image.open(filename)
        image1 = image1.resize((200, 200))
        test = ImageTk.PhotoImage(image1)
        # create border to image
        label_frame = Tk.Frame(root, bd=2, relief="solid")  # Create a frame for the image with border
        label_frame.pack(pady=10)
        label1 = Tk.Label(label_frame, image=test)  # Place the image inside the frame
        label1.image = test
        label1.pack()
        result = XG_boosting_prediction(cv2.imread(filename)) 
        create_progress_bar(root)
        def show_message():
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
        root.after(300*10, show_message)
    else:
        print("Null Image Input")



btn_browse.grid(row=2, column=0, columnspan="2", padx=10, pady=10)
Edit_btn.grid(row=2, column=4, columnspan="2", padx=10, pady=10)
btn_browse['command'] = selectPic
Edit_btn['command'] = Edit_Image

frame.pack()
root.mainloop()