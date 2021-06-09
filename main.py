import os
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


searchURL = "https://images.google.com/searchbyimage?image_url="
imageURL = sys.argv[1]
# imageURL = "https://assets.weforum.org/article/image/large_pYZGZE6sRzFmW3Gp9N0dWv7NguNhdFu95Rhr0SvyhkU.jpg"
fullSearchURL = searchURL + imageURL

# Get a new scraper browser
browser = webdriver.Chrome(dir_path + "/chromedriver")

# Go to this URL
browser.get(fullSearchURL)

# Find the "I Agree" button and click it
i_agree_button_xpath = "/html/body/div[3]/div[3]/span/div/div/div[3]/button[2]"
browser.find_element_by_xpath(i_agree_button_xpath).click()

# Find the found keyword for the image
keyword_xpath = "/html/body/div[8]/div/div[9]/div[1]/div/div[2]/div[1]/div/div[2]/a"
keyword_element = browser.find_element_by_xpath(keyword_xpath)
print(keyword_element.get_attribute("innerHTML"))

# Do we want to quit the browser when finished?
browser.quit()

