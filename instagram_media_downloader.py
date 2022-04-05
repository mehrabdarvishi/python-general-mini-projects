from selenium import webdriver
from csv import DictReader
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import urllib.request
import os
from datetime import datetime

url = "https://www.instagram.com/p/Cb8nNhWoen0/"

next_button_class_name = "coreSpriteRightChevron"
media_section_class_name = "_97aPb"
image_objects_class_name = "FFVAD"

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)

def get_cookies(file):
    with open(file) as f:
        return list(DictReader(f))

cookies = get_cookies('cookies.csv')

for cookie in cookies:
    driver.add_cookie(cookie)

driver.get(url)


media_sources = []
while True:
	media_section = driver.find_element(By.CLASS_NAME, media_section_class_name)
	image_objects = media_section.find_elements(By.CLASS_NAME, image_objects_class_name)

	for obj in image_objects:
		media_source = obj.get_attribute('src')
		if media_source not in media_sources:
			media_sources.append(media_source)

	next_button = driver.find_elements(By.CLASS_NAME, next_button_class_name)
	if len(next_button) != 0:
		next_button[0].click()
	else:
		break

dir_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
os.makedirs(f"./media/{dir_name}")
for i, media_source in enumerate(media_sources):
	urllib.request.urlretrieve(media_source, f'./media/{dir_name}/{i+1}.jpg')