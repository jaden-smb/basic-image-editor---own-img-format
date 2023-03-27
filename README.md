# Image Processing App

This is a simple image processing app that allows users to load, display, modify, and save image files. The app is built using Python and the following libraries:

`NumPy`
`tkinter`
`PIL (Python Imaging Library)`
`matplotlib`

The app uses a class called ImageFormat to store image data in a single object. The ImageFormat class has the following attributes:


`width (integer):`the width of the image in pixels
`height (integer):`the height of the image in pixels
`encoding_type (string):`the encoding type of the image (either "color" or "grayscale")
`pixel_values (NumPy array):`a 2D NumPy array that contains the pixel values of the image

The app has the following functions:

`load_image():`allows the user to select an image file and returns an ImageFormat object that contains the image data
`show_image(image_format):`displays the image in a new window using tkinter
`save_image(image_format):`allows the user to save the image to a file in the format created by us (MFG)
`display_histogram(image_format):`displays the histogram of the image using matplotlib
`brightness_change(image_format):`allows the user to change the brightness of the image by adding a constant value to each pixel
`contrast_around_mean(image_format):`allows the user to change the contrast of the image by multiplying each pixel value by a constant value
`histogram_equalization(image_format):`performs histogram equalization on the image
`gamma_correction(image_format):`performs gamma correction on the image by raising each pixel value to a power

The main function of the app displays a menu that allows the user to select the different functions. The user can select an option by entering the corresponding number. The main function uses a while loop to keep displaying the menu until the user chooses to exit.

# How to Run the script

1. To run the app, follow these steps:
2. Clone the repository to your local machine.
3. Open a terminal window and navigate to the directory where the repository is cloned.
4. Install the required libraries by running the following command:

`pip3 install numpy tkinter pillow matplotlib`

5. Run the app by running the following command:

`python3 image-editor-mgf.py`

6. Follow the instructions in the app to load, display, modify, and save image files.

Note: The app has been tested on Python 3.7.3 and may not work on earlier versions of Python.

# Example Usage

Here is an example usage of the app:

1. Load an image by selecting "Load image" from the menu and selecting an image file.
2. Display the image by selecting "Show image" from the menu.
3. Change the brightness of the image by selecting "Brightness change" from the menu and entering a value for k (e.g., 50).
4. Display the histogram of the image by selecting "Display histogram" from the menu.
5. Perform histogram equalization on the image by selecting "Histogram equalization" from the menu.
6. Display the histogram of the processed image by selecting "Display histogram" from the menu again.
7. Save the processed image by selecting "Save image" from the menu and entering a file name.
