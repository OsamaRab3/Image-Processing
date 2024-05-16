import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib import pyplot as plt

class imag_processing:
    def __init__(self, root):
        self.root = root
        self.image = None 

    def Page(self):
        self.load_image_button = Button(
                self.root,
                text="Load Image",
                font=("Arial", 10, "bold"),
                command=self.load_image
        )
        self.load_image_button.place(x=10, y=10)

        self.image_label = Label(self.root)
        self.image_label.pack()
        operations = {
            "LPF": self.apply_lpf,
            "HPF": self.apply_hpf,
            "Mean Filter": self.apply_mean_filter,
            "Median Filter": self.apply_median_filter,
        }

        y_offset = 50
        for operation_name, operation_func in operations.items():
            button = Button(
                self.root,
                text=operation_name,
                font=("Arial", 10, "bold"),
                command=operation_func
            )
            button.place(x=10, y=y_offset)
            y_offset += 30

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image = Image.open(file_path)
            photo = ImageTk.PhotoImage(self.image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
            print("No file selected.")
