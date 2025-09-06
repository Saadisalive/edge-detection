import cv2
import numpy as np
from matplotlib import pyplot as plt

def diaplay_image(title, image):
    """Utility fnction to display an image"""
    plt.figure(figsize=(8, 8))
    if len(image.shape) == 2:  # grayscale image
        plt.show(image, cmap='gray')
    else:
        plt.show(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    """Interactive activity for edge detection and filtering"""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    diaplay_image("Original Image", gray_image)

    print("select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian smoothing")
    print("5. Median filtering")
    print("6. Exit")

    while True:
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
            diaplay_image("Sobel Edge Detection", combined_sobel)
        elif choice == '2':
            print("Adjust the thresholds for Canny (default 100 and 200)")
            lower_thresh = int(input("Enter lower threshold: "))
            upper_thresh = int(input("Enter upper threshold: "))
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            diaplay_image("Canny Edge Detection", edges)
        
        elif choice == '3':
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            diaplay_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))

        elif choice == '4':
            print("Adjust the kernel size for Gaussian smoothing (must be odd, default 5)")
            kernrl_size = int(input("Enter kernel size(oddnumber): "))
            blurred = cv2.GaussianBlur(image, (kernrl_size, kernrl_size), 0) 
            diaplay_image("Gaussian Smoothing", blurred)

        elif choice == '5':
            print("Adjust the kernel size for Median filtering (must be odd, default 5)")
            kernrl_size = int(input("Enter kernel size(oddnumber): "))
            median_filtered = cv2.medianBlur(image, kernrl_size)
            diaplay_image("Median Filtering", median_filtered)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

interactive_edge_detection("fire-dragon-menacing-black-body-uqp2uj30eoedyoob.jpg")