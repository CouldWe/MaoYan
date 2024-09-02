import re


def convert_to_unicode(match):
    # 获取匹配到的字符
    char = match.group(0)
    # 将字符转换为 &#x 开头的 Unicode 编码
    return f'&#x{ord(char):x};'

# 假设 html_source 是你从网页中获取的 HTML 源代码
# with open('html_source.txt', 'r',encoding='utf-8') as f:
#     html_source = f.read()
# 定义一个正则表达式来匹配非中文、非ASCII、非常见符号的字符
def convert_html(html_source):
    pattern = re.compile(r'[^\x00-\x7F\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')
    # 替换所有匹配到的字符为 Unicode 编码
    encoded_html_source = pattern.sub(convert_to_unicode, html_source)
    # print(encoded_html_source)
    return encoded_html_source