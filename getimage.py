import sys
import io
from PIL import Image
import base64

from selenium import webdriver
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


searchURL = "https://images.google.com/search?q="
keywords = sys.argv[1]
fullSearchURL = searchURL + keywords

# Get a new scraper browser
browser = webdriver.Chrome(dir_path + "/chromedriver")

# Go to this URL
browser.get(fullSearchURL)

# Find the "I Agree" button and click it
i_agree_button_xpath = "/html/body/div[3]/div[3]/span/div/div/div[3]/button[2]"
browser.find_element_by_xpath(i_agree_button_xpath).click()

images_button_xpath = "/html/body/div[8]/div/div[4]/div/div[1]/div/div[1]/div/div[2]/a"
browser.find_element_by_xpath(images_button_xpath).click()

browser.find_element_by_xpath("//*[@id='islrg']/div[1]/div[1]").click()

images_on_page = browser.find_elements_by_css_selector("img")
images_urls = []
for image in images_on_page:
    image_base64 = image.get_attribute("src")
    try:
        image_base64 = image_base64.split("base64,")[1]
    except IndexError:
        continue
    except AttributeError:
        continue

    imgdata = base64.b64decode(image_base64)
    im = Image.open(io.BytesIO(imgdata))
    width, height = im.size
    if width > 100:
        images_urls.append(image.get_attribute("src"))

print(images_urls[5])

# Do we want to quit the browser when finished?
browser.quit()

