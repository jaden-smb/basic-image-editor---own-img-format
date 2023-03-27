import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

# Class to store image data in a single object
class ImageFormat:
    def __init__(self, width, height, encoding_type, pixel_values):
        self.width = width
        self.height = height
        self.encoding_type = encoding_type
        self.pixel_values = pixel_values

# Function to load image from file
def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        # Convert image to grayscale if it is in color
        if image.mode == "RGB":
            encoding_type = "color"
        else:
            encoding_type = "grayscale"
        # Convert image to numpy array and return it along with image dimensions and encoding type
        pixel_values = np.array(image)
        return ImageFormat(image.width, image.height, encoding_type, pixel_values)

# Function to display image in a window using tkinter
def show_image(image_format):
    image = Image.fromarray(image_format.pixel_values)
    # Convert image to RGB if it is in grayscale
    if image_format.encoding_type == "color":
        image = image.convert("RGB")
    else:
        image = image.convert("L")
    image.show()

# Function to save image to file using PIL
def save_image(image_format):
    # Save the image in the format created by us (MFG)
    file_path = filedialog.asksaveasfilename(defaultextension=".mfg", filetypes=[("MFG Files", "*.mfg")])
    
    with open(file_path, 'wb') as f:
        # Write the image dimensions
        f.write(image_format.width.to_bytes(4, byteorder='little'))
        f.write(image_format.height.to_bytes(4, byteorder='little'))
        # Write the encoding type
        if image_format.encoding_type == "color":
            f.write(b'color')
        else:
            f.write(b'grayscale')
        # Write the pixel values
        f.write(image_format.pixel_values.tobytes())

# Function to display histogram of image using matplotlib
def display_histogram(image_format):
    # Create a figure with two subplots and display the histogram of original and processed image
    fig, axs = plt.subplots(1, 2, figsize=(10,5))
    # Flatten the image to a 1D array and display the histogram
    axs[0].hist(image_format.pixel_values.flatten(), bins=256, range=(0, 255), color='r')
    axs[0].set_title('Original Image')
    # Flatten the image to a 1D array and display the histogram (after processing)
    axs[1].hist(image_format.pixel_values.flatten(), bins=256, range=(0, 255), color='g')
    axs[1].set_title('Processed Image')
    plt.show()

# Function to change the brightness of image by adding a constant value to each pixel
def brightness_change(image_format):
    k = int(input("Enter value of k (-255 to 255): "))
    # Add the constant value to each pixel and clip the values to lie between 0 and 255
    image_format.pixel_values = np.clip(image_format.pixel_values.astype(int) + k, 0, 255).astype(np.uint8)

# Function to change the contrast of image by multiplying each pixel value by a constant value
def contrast_around_mean(image_format):
    k = float(input("Enter value of k (0 to 2): "))
    mean_intensity = np.mean(image_format.pixel_values)
    # Multiply each pixel value by the constant value and clip the values to lie between 0 and 255
    image_format.pixel_values = np.clip((image_format.pixel_values - mean_intensity) * k + mean_intensity, 0, 255).astype(np.uint8)

# Function to perform histogram equalization on image
def histogram_equalization(image_format):
    # If image is in color, convert it to grayscale and perform histogram equalization
    if image_format.encoding_type == "grayscale":
        # Calculate the histogram of the image and calculate the cumulative distribution function
        hist, bins = np.histogram(image_format.pixel_values.flatten(), 256, [0,256])
        cdf = hist.cumsum()
        # Normalize the cumulative distribution function and map the pixel values to the new values
        cdf_normalized = cdf * hist.max() / cdf.max()
        # Interpolate the pixel values to the new values and clip the values to lie between 0 and 255
        image_format.pixel_values = np.interp(image_format.pixel_values.flatten(), bins[:-1], cdf_normalized).reshape(image_format.height, image_format.width).astype(np.uint8)

# Function to perform gamma correction on image by raising each pixel value to a power
def gamma_correction(image_format):
    gamma = float(input("Enter value of gamma (0.1 to 10): "))
    # Raise each pixel value to the power and clip the values to lie between 0 and 255
    image_format.pixel_values = np.clip((image_format.pixel_values / 255) ** gamma * 255, 0, 255).astype(np.uint8)

# Main function to display menu and call functions
if __name__ == "__main__":
    image_format = None
    while True:
        print("Menu:")
        print("1. Load image")
        print("2. Show image")
        print("3. Save image")
        print("4. Display histogram")
        print("5. Brightness change")
        print("6. Contrast around mean")
        print("7. Histogram equalization")
        print("8. Gamma correction")
        print("9. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            image_format = load_image()
        elif choice == "2":
            if image_format:
                show_image(image_format)
            else:
                print("Please load an image first.")
        elif choice == "3":
            if image_format:
                save_image(image_format)
            else:
                print("Please load an image first.")
        elif choice == "4":
            if image_format:
                display_histogram(image_format)
            else:
                print("Please load an image first.")
        elif choice == "5":
            if image_format:
                brightness_change(image_format)
            else:
                print("Please load an image first.")
        elif choice == "6":
            if image_format:
                contrast_around_mean(image_format)
            else:
                print("Please load an image first.")
        elif choice == "7":
            if image_format:
                histogram_equalization(image_format)
            else:
                print("Please load an image first.")
        elif choice == "8":
            if image_format:
                gamma_correction(image_format)
            else:
                print("Please load an image first.")
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")
