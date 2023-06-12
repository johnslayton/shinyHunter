from PIL import Image
import requests
import io
import shutil # save img locally
import urllib.request
from io import BytesIO

# couldn't figure out how to do it with requests, can't read bytes properly?
# url = "https://img.pokemondb.net/sprites/ruby-sapphire/normal/deoxys-normal.png"
# url2 = "https://img.pokemondb.net/sprites/ruby-sapphire/shiny/deoxys-normal.png"

generation = {  3 : "ruby-sapphire",
                4 : "diamond-pearl",
                5 : "black-white"
              }

def getSprite(gen, pName, type):
    url = "https://img.pokemondb.net/sprites/" + generation[gen] + "/" + type + "/" + pName + ".png"
    file_name = "images/" + type + "/" + pName + ".png" 

    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
            # shutil.copyfileobj(res.raw, f)
    else:
        print('Image Couldn\'t be retrieved')


# getSprite(3, "rayquaza", "normal")
# getSprite(3, "rayquaza", "shiny")
