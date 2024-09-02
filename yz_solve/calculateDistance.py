import ddddocr
def get_distance():
    ocr = ddddocr.DdddOcr(beta=True)
    with open('yz_solve/img/bg.png',mode='rb') as f:
        bg_bytes=f.read()
    with open('yz_solve/img/slide.png',mode='rb') as f:
        slide_bytes=f.read()
    result=ocr.slide_match(slide_bytes,bg_bytes,simple_target=True)
    print('result:',result)
    return (result['target'][0]+result['target'][2])/2