#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install requests beautifulsoup4')


# In[29]:


import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# # Define the website URL
# url = "https://arbml.github.io/ARBML/Interfaces/Website/ArabicTextDetection/index.html"

# # Define the folder path containing the images
# image_folder = "C:/Users/muath/Downloads/OnePage_alqare"

# # Initialize the Chrome WebDriver
# driver = webdriver.Chrome()

# # Navigate to the website
# driver.get(url)

# # Wait for the page to load (you may need to adjust the sleep time depending on the website's loading time)
# time.sleep(5)

# # Initialize an empty string to store the output of all images
# output_string = ""

# # Function to process an individual image and append the result to the output string
# def process_image(image_path):
#     # Declare output_string as a global variable to be able to modify it inside the function
#     global output_string
#     try:
#         # Find the upload input element by ID and send the image file path
#         upload_input = driver.find_element(By.ID, "preview")
#         upload_input.send_keys(image_path)

#         # Wait for the file to be uploaded and the result to appear (you may need to adjust the sleep time)
#         time.sleep(10)

#         # Find the output text element
#         output_text_element = driver.find_element(By.ID, "output-text")

#         # Get the resulting text
#         resulting_text = output_text_element.text

#         # Append the resulting text to the output string
#         output_string += resulting_text + "\n"

#         print(f"Image '{image_path}' processed.")
#     except Exception as e:
#         print(f"Error processing image '{image_path}': {e}")
#         # Uncomment the following line to raise the exception and see the full traceback
#         # raise

# # Loop through all image files in the folder and process them
# for filename in os.listdir(image_folder):
#     if filename.lower().endswith((".png", ".jpg", ".jpeg")):
#         image_path = os.path.join(image_folder, filename)
#         process_image(image_path)

# # Close the browser
# driver.quit()

# # Create the output file and write the whole string to it
# output_file = os.path.join(image_folder, "output2.txt")
# with open(output_file, "w", encoding="utf-8") as file:
#     file.write(output_string)

# print(f"All images processed. Result written to '{output_file}'")



