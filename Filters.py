import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib import pyplot as plt

class imag_processing:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processing")
        self.image = None 
        self.main_page()
        
    def main_page(self):
        self.load_image_button = Button(
                self.root,
                text="Load Image",
                font=("Arial", 10, "bold"),
                command=self.load_image,
        )
        self.load_image_button.place(x=10,y=10)
        
        self.image_label = Label(self.root)
        self.image_label.pack()
        operations = {
            "LPF": self.apply_lpf,
            "HPF": self.apply_hpf,
            "Mean Filter": self.apply_mean_filter,
            "Median Filter": self.apply_median_filter
        }

        y_offset=50
        for operation_name, operation_func in operations.items():
            button = Button(
                self.root,
                text=operation_name,
                font=("Arial", 10, "bold"),
                command=operation_func,
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

    def apply_lpf(self):
        # Load the image
        if self.image is not None:
            image_np = np.array(self.image)

            # Apply Gaussian blur as a low-pass filter
            blurred_image = cv2.GaussianBlur(image_np, (5, 5), 0)

            # plt.figure(figsize=(12, 12))

            # plt.subplot(1, 2, 2)
            plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
            plt.title('Lowpass Filtered Image')
            plt.axis('off')
            plt.show()
        else:
            print("Please load an image first.")
            
    def apply_hpf(self):
        if self.image is not None:
            # Convert the image to a numpy array
            image_np = np.array(self.image)

            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur to the grayscale image with a large kernel size
            blurred_image = cv2.GaussianBlur(gray_image, (25, 25), 0)

            # Subtract the blurred image from the grayscale image to obtain the high-pass filtered image
            hpf_image = cv2.subtract(gray_image, blurred_image)

            plt.imshow(hpf_image, cmap='gray')
            plt.title('High Pass Filtered Image')
            plt.axis('off')
            plt.show()
        else:
            print("Please load an image first.")
            
    def apply_mean_filter(self):
        if self.image is not None:
            # Convert the image to a numpy array
            image_np = np.array(self.image)

            # Apply a mean filter to the image
            mean_filtered_image = cv2.blur(image_np, (5, 5))

            # Display the mean filtered image
            plt.imshow(cv2.cvtColor(mean_filtered_image, cv2.COLOR_BGR2RGB))
            plt.title('Mean Filtered Image')
            plt.axis('off')
            plt.show()
        else:
            print("Please load an image first.")

    def apply_median_filter(self):
        if self.image is not None:
            # Convert the image to a numpy array
            image_np = np.array(self.image)

            # Apply a median filter to the image
            median_filtered_image = cv2.medianBlur(image_np, 5)

            # Display the median filtered image

            plt.imshow(cv2.cvtColor(median_filtered_image, cv2.COLOR_BGR2RGB))
            plt.title('Median Filtered Image')
            plt.axis('off')
            plt.show()
        else:
            print("Please load an image first.")
