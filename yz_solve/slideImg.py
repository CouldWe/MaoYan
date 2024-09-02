import pyautogui
import random
import time
def move_slide(offset_x, offset_y, left):
    """
    执行滑块的移动
    :param offset_x: 滑块的x轴坐标
    :param offset_y: 滑块的y轴坐标
    :param left: 需要移动的距离
    :return:
    """

    # 移动到滑块的位置
    # duration为持续时间
    # random.uniform(参数1，参数2) 返回参数1和参数2之间的任意值
    pyautogui.moveTo(
        offset_x,
        offset_y,
        duration=0.1 + random.uniform(0, 0.1 + random.randint(1, 100) / 100))

    # 按下鼠标 准备开始滑动
    pyautogui.mouseDown()
    # random.randint(参数1, 参数2) 函数返回参数1和参数2之间的任意整数
    offset_y += random.randint(9, 19)
    pyautogui.moveTo(
        offset_x + int(left * random.randint(15, 25) / 20),
        offset_y,
        duration=0.28)

    offset_y += random.randint(-9, 0)
    pyautogui.moveTo(
        offset_x + int(left * random.randint(18, 22) / 20),
        offset_y,
        duration=random.randint(19, 31) / 100)

    offset_y += random.randint(0, 8)
    pyautogui.moveTo(
        offset_x + int(left * random.randint(19, 21) / 20),
        offset_y,
        duration=random.randint(20, 40) / 100)

    offset_y += random.randint(-3, 3)
    pyautogui.moveTo(
        left + offset_x + random.randint(-3, 3),
        offset_y,
        duration=0.5 + random.randint(-10, 10) / 100)

    offset_y += random.randint(-2, 2)
    pyautogui.moveTo(
        left + offset_x + random.randint(-2, 2),
        offset_y,
        duration=0.5 + random.randint(-3, 3) / 100)

    # 释放鼠标
    pyautogui.mouseUp()
    time.sleep(3)
    # 173