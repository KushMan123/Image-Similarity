import os
import requests
import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    driver = selenium.webdriver.Chrome("./scripts/chromedriver")

    path = os.path.join(os.getcwd(), "..", "AnimalData")
    
    for animal in os.listdir(path):
        if os.path.isdir(os.path.join(path, animal)):
            continue

        name = animal.split(".")[0]

        dirpath = os.path.join(path, "animalImages", name)
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
        else:
            if os.listdir(dirpath):
                continue

        driver.get(f"https://unsplash.com/s/photos/{name}")

        imgs = driver.find_element(by=By.CLASS_NAME, value="mItv1").find_elements(by=By.CLASS_NAME, value="YVj9w")
        
        
        print(f"Fetching images for {name}")
        for index, img in enumerate([i.get_attribute("src") for i in imgs][1:8]):
            r = requests.get(img)
            print(f"Fetching image {index}")
            with open(os.path.join(dirpath, f"{name}{index}.jpeg"), "wb") as f:
                f.write(r.content)        

if __name__ == "__main__":
    main()