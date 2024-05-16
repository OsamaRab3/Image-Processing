from tkinter import filedialog, messagebox
import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

class RegionSplitMergeApp:
    def __init__(self, root):
        self.root = root
        self.image = None
        self.page()
    
    def page(self):
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
            "Hough Circle Transform": self.apply_hough_circle_transform,
            "Region Split and Merge": self.apply_region_split_merge_segmentation,
            "Thresholding Segmentation":self.apply_thresholding_segmentation,
            "Opening Filter": self.apply_opening_filter,
            "Closing Filter": self.apply_closing_filter,
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
            
    def region_growing(self,image, seed):
           
        height, width = image.shape[:2]
        visited = set()
        stack = [seed]
        region_pixels = set()

        while stack:
            x, y = stack.pop()
            if (x, y) not in visited:
                visited.add((x, y))
                region_pixels.add((x, y))
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < width and 0 <= ny < height:
                            if abs(int(image[y, x]) - int(image[ny, nx])) < 20:
                                stack.append((nx, ny))

        return region_pixels
      
    def apply_region_split_merge_segmentation(self):
        if self.image is not None:
            gray_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_BGR2GRAY)
            seed_point = (0, 0)  # Choose a seed point (you may need to adjust this)
            segmented_image = np.zeros_like(gray_image)
            for seed in [seed_point]:
                region_pixels = self.region_growing(gray_image, seed)
                for pixel in region_pixels:
                    segmented_image[pixel[1], pixel[0]] = 255

            pil_image = Image.fromarray(segmented_image)
            photo = ImageTk.PhotoImage(pil_image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
            messagebox.showerror("Error", "Please load an image first.")
            
    def apply_thresholding_segmentation(self):
        if self.image is not None:
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_BGR2GRAY)

            # Apply thresholding segmentation with a fixed threshold value
            _, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

            # Convert the thresholded image back to a PIL Image
            pil_image = Image.fromarray(thresholded_image)

            # Convert the PIL Image to a Tkinter PhotoImage
            photo = ImageTk.PhotoImage(pil_image)

            # Configure the image label to display the new image
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
            messagebox.showerror("Error", "Please load an image first.")


    def apply_opening_filter(self):
        if self.image is not None:
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_BGR2GRAY)

            # Create a kernel for the opening operation (a square of size 5x5)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

            # Apply the opening operation
            opened_image = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel)

            # Convert the opened image back to a PIL Image
            pil_image = Image.fromarray(opened_image)

            # Convert the PIL Image to a Tkinter PhotoImage
            photo = ImageTk.PhotoImage(pil_image)

            # Configure the image label to display the new image
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
            messagebox.showerror("Error", "Please load an image first.")
    def apply_closing_filter(self):
        if self.image is not None:
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(np.array(self.image), cv2.COLOR_BGR2GRAY)

            # Create a kernel for the closing operation (a square of size 5x5)
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

            # Apply the closing operation
            closed_image = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)

            # Convert the closed image back to a PIL Image
            pil_image = Image.fromarray(closed_image)

            # Convert the PIL Image to a Tkinter PhotoImage
            photo = ImageTk.PhotoImage(pil_image)

            # Configure the image label to display the new image
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
            messagebox.showerror("Error", "Please load an image first.")
   
    def apply_hough_circle_transform(self):
        if self.image is not None:
            # Convert the image to a NumPy array
            image_array = np.array(self.image)
    
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    
            # Apply Gaussian blur to reduce noise
            blurred_image = cv2.GaussianBlur(gray_image, (9, 9), 2)
    
            # Detect circles using Hough Circle Transform
            circles = cv2.HoughCircles(
                blurred_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0
            )
    
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0, :]:
                    # Draw the outer circle
                    cv2.circle(image_array, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    # Draw the center of the circle
                    cv2.circle(image_array, (i[0], i[1]), 2, (0, 0, 255), 3)
    
                # Convert the image with detected circles back to a PIL Image
                pil_image = Image.fromarray(image_array)
    
                # Convert the PIL Image to a Tkinter PhotoImage
                photo = ImageTk.PhotoImage(pil_image)
    
                # Configure the image label to display the new image
                self.image_label.configure(image=photo)
                self.image_label.image = photo  # Keep a reference
            else:
                messagebox.showinfo("Info", "No circles detected.")
        else:
            messagebox.showerror("Error", "Please load an image first.")

          


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    root.title("Region Split and Merge")
    app = RegionSplitMergeApp(root)
    
    root.mainloop()
