from Main_page import *

class Filter(imag_processing):
    def __init__(self, root):
        self.root=root
        self.root.title("Image Processing")
        self.Page()

    def apply_lpf(self):
        if self.image is not None:
            image_np = np.array(self.image)
            # Apply Gaussian blur as a low-pass filter
            blurred_image = cv2.GaussianBlur(image_np, (5, 5), 0)

            # Convert the image back to PIL format
            pil_image = Image.fromarray(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))

            # Convert the PIL image to a Tkinter-compatible format
            photo = ImageTk.PhotoImage(pil_image)

            # Configure the image label to display the new image
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference to prevent garbage collection
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

            # Convert the high-pass filtered image to a PIL Image
            pil_image = Image.fromarray(hpf_image)

            # Convert the PIL Image to a Tkinter PhotoImage
            photo = ImageTk.PhotoImage(pil_image)

            # Configure the image label to display the new image
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
             print("Please load an image first.")
       
    def apply_mean_filter(self):
        if self.image is not None:
            # Convert the image to a numpy array
            image_np = np.array(self.image)    
            # Apply a mean filter to the image
            mean_filtered_image = cv2.blur(image_np, (5, 5))   
            # Convert the mean filtered image to a PIL Image
            pil_image = Image.fromarray(cv2.cvtColor(mean_filtered_image, cv2.COLOR_BGR2RGB))  
            # Convert the PIL Image to a Tkinter PhotoImage
            photo = ImageTk.PhotoImage(pil_image)  
            # Configure the image label to display the new image
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # Keep a reference
        else:
            print("Please load an image first.")

    def apply_median_filter(self):
        if self.image is not None:
            # Convert the image to a numpy array
            image_np = np.array(self.image)

            # Apply a median filter to the image
            median_filtered_image = cv2.medianBlur(image_np, 5)

            # Convert the median filtered image to a PIL Image
            pil_image = Image.fromarray(cv2.cvtColor(median_filtered_image, cv2.COLOR_BGR2RGB))

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
    Filter=Filter(root)
 
    
    root.mainloop()
