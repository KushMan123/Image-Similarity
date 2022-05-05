import requests
from bs4 import BeautifulSoup

import os

def main():
    cwd = os.getcwd()
    dpath = os.path.join(cwd, "..", "AnimalData")
    descriptions = {}
    for animal in os.listdir(dpath):
        name = animal.split(".")[0]

        res = requests.get(f"https://animals.net/{name}/")
        if not res.status_code == 200:
            print("Error", name)
            continue
        
        soup = BeautifulSoup(res.content, "html.parser")
        div = soup.find("div", attrs={"class": "td-post-content td-pb-padding-side"})

        desc = " ".join([a.text for a in div.find_all("p")[2:4]])
        descriptions[name] = desc
    
    with open(os.path.join(dpath, "description.json"), "w") as f:
        import json
        json.dump(descriptions, f, indent=4)

if __name__ == "__main__":
    main()