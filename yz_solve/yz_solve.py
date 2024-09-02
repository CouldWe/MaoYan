import base64
import time
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from yz_solve.calculateDistance import get_distance
from yz_solve.slideImg import move_slide
from yz_solve.humanlikeSlide import simulate_human_slider
def get_img_scale(bg,slide):

    bg_url=bg.get_attribute('src')
    bg_bytes=requests.get(url=bg_url).content
    with open('yz_solve/img/bg.png',mode='wb') as f:
        f.write(bg_bytes)
    slide_url = slide.get_attribute('src')
    slide_bytes = requests.get(url=slide_url).content
    with open('yz_solve/img/slide.png',mode='wb') as f:
        f.write(slide_bytes)

    with Image.open('yz_solve/img/bg.png') as f:
        scaling=round(bg.rect['width']/4*5/f.size[0],4)
        print('实际bg图片宽度:',f.size[0])
    print('浏览器中元素宽度:',bg.rect['width']/4*5)
    return scaling
def main(driver):
    # while True:

    time.sleep(2)
    slide=driver.find_element(By.CSS_SELECTOR,"#slideBlock")
    bg = driver.find_element(By.CSS_SELECTOR, "#slideBg")

    scale=get_img_scale(bg,slide)
    print('scale:',scale)
    distance=get_distance()*scale-73
    print('distance:',distance)
    simulate_human_slider(823,724,distance)
