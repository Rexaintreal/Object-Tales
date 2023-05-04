import customtkinter 
import tkinter 
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import numpy as np
import os
import gpt_2_simple as gpt2

class MyFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

class MyTabView(customtkinter.CTkTabview):

    def generate(self):
        # Load YOLO
        net = cv2.dnn.readNet("OpenCV Files/yolov3.weights", "OpenCV Files/yolov3.cfg")

        # Load classes
        classes = []
        with open("OpenCV Files/coco.names", "r") as f:
            classes = [line.strip() for line in f.readlines()]

        # Load image
        image = cv2.imread(img_path)

        # Preprocess image
        blob = cv2.dnn.blobFromImage(image, 1/255, (320, 320), (0, 0, 0), swapRB=True, crop=False)

        # Set input and run forward pass
        net.setInput(blob)
        output_layers_names = net.getUnconnectedOutLayersNames()
        layer_outputs = net.forward(output_layers_names)

        # Initialize lists for bounding boxes and labels
        boxes = []
        labels = []

        # Loop over each output layer
        for output in layer_outputs:
            # Loop over each detection
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # Filter out weak detections
                if confidence > 0.5:
                    # Scale the bounding box coordinates
                    width, height = image.shape[1], image.shape[0]
                    center_x, center_y, bbox_width, bbox_height = detection[:4] * np.array([width, height, width, height])
                    x = int(center_x - bbox_width/2)
                    y = int(center_y - bbox_height/2)

                    # Add bounding box coordinates and label to their respective lists
                    boxes.append([x, y, int(bbox_width), int(bbox_height)])
                    labels.append(str(classes[class_id]))

        # Concatenate labels into a single string
        prompt = "This image contains " + ", ".join(labels) + ". Once upon a time, "

        # Generate story with GPT-2
        model_name = "124M"
        gpt2.download_gpt2(model_name=model_name)  # Change to your desired GPT-2 model size
        sess = gpt2.start_tf_sess()
        gpt2.load_gpt2(sess, model_name=model_name)
        story = gpt2.generate(sess, prefix=prompt, length=500, temperature=0.7, return_as_list=True)[0]

        # Print or save story
        if 1 == 1:
            self.label.configure(text=story)

    def OpenPic(self):
        global img_path
        img_path = filedialog.askopenfilename(
            title="Open an Image File",
            filetypes=(("Image Files", "*.jpg"), ("all files", "*.*"))
        )
        new_img = ImageTk.PhotoImage(Image.open(img_path))
        if img_path:
            self.picture.configure(image=new_img)

        
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        Buttons= '#445878'
        Background= '#2E2E2E'
        Borders= '#444444'
        self.add("Picture")
        self.add("Story")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = MyFrame(master=self.tab("Story"), width=920, height=550)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20)
        self.label = customtkinter.CTkLabel(master=self.my_frame,font=("",20),text="Your Story Will Appear Here")
        self.label.grid(row=1, column=1, padx=20,pady=20)
        img = ImageTk.PhotoImage(Image.open("Images/Untitled.png"))
        self.picture=customtkinter.CTkLabel(master=self.tab("Picture"),image=img,text="")
        self.picture.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        self.button1=customtkinter.CTkButton(master=self.tab("Picture"),text="Open Picture",
                                             font=("",20),command=self.OpenPic,fg_color=Buttons)
        self.button1.place(relx=0.5,rely=0.96,anchor=tkinter.CENTER)
        self.button2=customtkinter.CTkButton(master=self.tab("Story"),text="Generate Story",
                                             font=("",20),command=self.generate,fg_color=Buttons)
        self.button2.place(relx=0.5,rely=0.96,anchor=tkinter.CENTER)

       
class App(customtkinter.CTk):


    def __init__(self):
        super().__init__()
        Buttons= '#445878'
        Background= '#2E2E2E'
        Borders= '#444444'
        self.geometry("1024x720")
        self.title("ObjectTales")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color=Borders)
        self.tab_view = MyTabView(master=self)
        self.tab_view.configure(fg_color=Background)
        self.tab_view=MyTabView(master=self,width=1366,height=768)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)

app = App()
app.mainloop()
        

    