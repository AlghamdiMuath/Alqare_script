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
