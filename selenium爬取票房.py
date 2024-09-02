import csv
import re
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from yz_solve import yz_solve
from fontTools.ttLib import TTFont
from parseFont import identify_word
from encodeStr import convert_html


def save_font():
    try:
        font_link = re.findall(r'//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/\w+\.woff', html_source)[0]
    except IndexError:
        raise '未找到字体'
    # print('link:', font_link)
    font_name = font_link.split('/')[-1]
    # print('name:', font_name)
    if os.path.exists('fonts/'+font_name):
        print(f'{font_name}字体已存在,跳过保存')
        return font_name
    font_link = 'https:' + font_link
    font_file=requests.get(font_link).content
    with open('fonts/'+font_name, 'wb') as f:
        f.write(font_file)
    font=TTFont('fonts/'+font_name)
    font.saveXML('./xml/'+font_name[:-5]+'.xml')
    font.save('./ttf/'+font_name[:-5]+'.ttf')
    return font_name

if __name__ == '__main__':

    service=Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.maoyan.com/board/1")
    # driver.get("https://tfz.maoyan.com/yamaha/verify?requestCode=17e3a5cbd930024606daa0a6eb8878d5lgvoi&redirectURL=https%3A%2F%2Fwww.maoyan.com%2Fboard%2F1#/")
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    driver.implicitly_wait(10)
    driver.maximize_window()
    while True:
        html_source=driver.page_source
        if '猫眼验证中心' in html_source:
            iframe=driver.find_element(By.CSS_SELECTOR,'#tcaptcha_iframe')
            driver.switch_to.frame(iframe)
            yz_solve.main(driver)
            time.sleep(5)
            print(driver.current_url)
            print(len(driver.window_handles))
        else:
            print('验证通过')
            op=input()
            if op=='1':
                break
            else:
                driver.refresh()

    html_source=driver.page_source
    font_name=save_font()
    dict_list=identify_word('./ttf/'+font_name[:-5]+'.ttf')

    box_offices=[]
    elem_box_offices=driver.find_elements(By.CSS_SELECTOR, '.stonefont')
    for i,item in enumerate(elem_box_offices):
        cur_box_office=convert_html(item.text)
        for code in dict_list:
            cur_box_office = cur_box_office.replace(code, dict_list[code])
        if i%2==0:
            box_offices.append([cur_box_office])
        else:
            box_offices[int(i/2)].append(cur_box_office)
    print('票房:',box_offices)

    js='''
        for(let i=0;i<5;++i)
        {
            document.documentElement.scrollTop=document.documentElement.scrollHeight*i/5;
            await new Promise(resolve => setTimeout(resolve, 1000));
        }
    '''
    driver.execute_script(js)
    imgs=[]
    elem_imgs=driver.find_elements(By.CSS_SELECTOR, '.board-img')
    for item in elem_imgs:
        imgs.append(item.get_attribute('src'))
    print('图片:',imgs)

    titles=[]
    elem_titles=driver.find_elements(By.CSS_SELECTOR, '.movie-item-info a')
    for item in elem_titles:
        titles.append(item.text)
    print('标题:',titles)

    actors=[]
    elem_actors=driver.find_elements(By.CSS_SELECTOR, '.movie-item-info .star')
    for item in elem_actors:
        actors.append(item.text)
    actors=list(map(lambda x:x.split('主演：')[-1],actors))
    print('主演:',actors)

    times=[]
    elem_times=driver.find_elements(By.CSS_SELECTOR, '.movie-item-info .releasetime')
    for item in elem_times:
        times.append(item.text)
    times=list(map(lambda x:x[-10:],times))
    print('时间:',times)
    with open('info.csv',mode='w',encoding='utf-8',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(['电影','实时票房','总票房','图片','主演','时间'])
        for i in range(len(titles)):
            writer.writerow([titles[i],box_offices[i][0],box_offices[i][1],imgs[i],actors[i],times[i]])
    input('输入任意键退出')
    driver.quit()


