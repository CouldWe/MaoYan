from PIL import ImageFont, Image, ImageDraw
from io import BytesIO
import ddddocr
from fontTools.ttLib import TTFont
def font_to_img(_code, filename):
    """将字体画成图片"""
    img_size = 1024
    img = Image.new('1', (img_size, img_size), 255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(filename, int(img_size * 0.7))
    txt = chr(_code)
    # 使用 textbbox 计算文本尺寸
    bbox = draw.textbbox((0, 0), txt, font=font)
    x, y = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font, fill=0)
    return img


def identify_word(_ttf_path):
    """识别ttf字体结果"""
    font = TTFont(_ttf_path)
    ocr = ddddocr.DdddOcr(beta=True)
    dict_list = {}
    for cmap_code, glyph_name in font.getBestCmap().items():
        bytes_io = BytesIO()
        pil = font_to_img(cmap_code, _ttf_path)
        pil.save(bytes_io, format="PNG")
        word = ocr.classification(bytes_io.getvalue())  # 识别字体
        dict_list['&#x'+glyph_name[3:].lower()+";"]=word
        # with open(f"./img/{cmap_code}_{glyph_name}.png", "wb") as f:
        #     f.write(bytes_io.getvalue())
    del dict_list['&#x;']
    # print(dict_list)
    return dict_list


if __name__ == '__main__':

    identify_word("./ttf/20a70494.ttf")

    # woff_path = "./fonts/20a70494.woff"
    # ttf_path = './ttf/20a70494.ttf'

    # 将woff转换为ttf
    # font=TTFont(woff_path)
    # font.save(ttf_path)

    # decompress(woff2_path, ttf_path)
    # 将woff2文件转成ttf文件

    # print(_font.getGlyphNames())
    # print(font.getBestCmap())

    # xml_path = './woff/704224.xml'
    # _font.saveXML(xml_path)