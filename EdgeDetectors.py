import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from matplotlib import pyplot as plt


class edge_detector():
    def __init__(self,root):
        self.root=root
        self.Page()
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
            "Roberts Edge Detector": self.apply_roberts_edge_detector,
            "Sobel Edge Detector": self.apply_sobel_edge_detector,
            "Prewitt Edge Detector": self.apply_prewitt_edge_detector,
            "Erosion": self.apply_erosion,
            "Dilation": self.apply_dilation
           
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

    def apply_roberts_edge_detector(self):
        if self.image is not None:
            # Apply the Roberts filter
            roberts_image = cv2.Canny(np.array(self.image), 100, 200)

            # Convert the Roberts edge detected image to a PIL Image
            pil_image = Image.fromarray(roberts_image.astype(np.uint8))

            # Convert the PIL Image to a Tkinter PhotoImage
            photo = ImageTk.PhotoImage(pil_image)

            # Configure the image label to display the new image
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
             print("Please load an image first.")
             
    def apply_prewitt_edge_detector(self):
          if self.image is not None:
              # Convert the image to grayscale
              gray_image = np.array(self.image.convert('L'))

              # Apply the Prewitt filter
              prewitt_x = cv2.filter2D(gray_image, -1, np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]]))
              prewitt_y = cv2.filter2D(gray_image, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]))
              prewitt_image = np.sqrt(prewitt_x**2 + prewitt_y**2)

              # Convert the Prewitt edge detected image to a PIL Image
              pil_image = Image.fromarray(prewitt_image.astype(np.uint8))

              # Convert the PIL Image to a Tkinter PhotoImage
              photo = ImageTk.PhotoImage(pil_image)

              # Configure the image label to display the new image
              self.image_label.configure(image=photo)
              self.image_label.image = photo  # Keep a reference
          else:
               print("Please load an image first.")

    def apply_sobel_edge_detector(self):
        if self.image is not None:
            # Convert the image to grayscale
            gray_image = np.array(self.image.convert('L'))

            # Apply the Sobel filter
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            sobel_image = np.sqrt(sobel_x**2 + sobel_y**2)

            # Convert the Sobel edge detected image to a PIL Image
            pil_image = Image.fromarray(sobel_image.astype(np.uint8))

            # Convert the PIL Image to a Tkinter PhotoImage
            photo = ImageTk.PhotoImage(pil_image)

            # Configure the image label to display the new image
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
            print("Please load an image first.")
    def apply_erosion(self):
         if self.image is not None:
             # Convert the image to a numpy array
             image_np = np.array(self.image)

             # Define the kernel for erosion
             kernel = np.ones((5, 5), np.uint8)

             # Apply erosion to the image
             eroded_image = cv2.erode(image_np, kernel, iterations=1)

             # Convert the eroded image back to a PIL Image
             pil_image = Image.fromarray(eroded_image)

             # Convert the PIL Image to a Tkinter PhotoImage
             photo = ImageTk.PhotoImage(pil_image)

             # Configure the image label to display the new image
             self.image_label.configure(image=photo)
             self.image_label.image = photo  # Keep a reference
         else:
             print("Please load an image first.")
    def apply_dilation(self):
        if self.image is not None:
            # Convert the image to a numpy array
            image_np = np.array(self.image)

            # Define the kernel for dilation
            kernel = np.ones((5, 5), np.uint8)

            # Apply dilation to the image
            dilated_image = cv2.dilate(image_np, kernel, iterations=1)

            # Convert the dilated image back to a PIL Image
            pil_image = Image.fromarray(dilated_image)

            # Convert the PIL Image to a Tkinter PhotoImage
            photo = ImageTk.PhotoImage(pil_image)

            # Configure the image label to display the new image
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
            print("Please load an image first.")



if __name__=="__main__":
    root = Tk()
    root.geometry("800x600")
    root.title("Edge")
    edg=edge_detector(root)
 
    
    root.mainloop()
