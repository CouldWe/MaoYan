# -*- coding:utf-8 -*-
import re
from fontTools.ttLib import TTFont
import os
import requests
def save_font(html_source):
    try:
        font_link = re.findall(r'//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/\w+\.woff', html_source)[0]
    except IndexError:
        raise '未找到字体'
    # print('link:', font_link)
    font_name = font_link.split('/')[-1][:-5]
    # print('name:', font_name)
    if os.path.exists('fonts/'+font_name+'.woff'):
        print(f'{font_name}字体已存在,跳过保存')
        return font_name
    font_link = 'https:' + font_link
    font_file=requests.get(font_link).content
    with open('fonts/'+font_name+'.woff', 'wb') as f:
        f.write(font_file)
    font=TTFont('fonts/'+font_name+'.woff')
    font.saveXML('./xml/'+font_name+'.xml')
    font.save('./ttf/'+font_name+'.ttf')
    return font_name