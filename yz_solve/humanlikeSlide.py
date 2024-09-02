import pyautogui
import random
import time
def simulate_human_slider(x, y, distance):
    # 移动到滑块起始位置
    pyautogui.moveTo(x, y, duration=0.5)
    pyautogui.mouseDown()

    # 主要滑动，加入轻微的y轴移动
    pyautogui.moveRel(distance * 0.7, random.uniform(-5, 5), duration=0.5)

    # 模拟人类行为的微调，包括x和y轴
    for i in [30,12,1]:
        x_adjustment = random.uniform(-1*i, i)/100
        y_adjustment = random.uniform(-7, 7)
        pyautogui.moveTo(x+(1+x_adjustment)*distance, y+y_adjustment, duration=random.uniform(0.15,0.25))
        time.sleep(random.uniform(0.06,0.11))

    # 最终调整到目标位置，轻微修正y轴位置
    # final_x_adjustment = distance * 0.1
    # final_y_adjustment = random.uniform(-2, 2)
    # pyautogui.moveRel(final_x_adjustment, final_y_adjustment, duration=0.2)

    # 松开鼠标
    time.sleep(0.5)
    pyautogui.mouseUp()

# 使用示例
# simulate_human_slider(500, 500, 200)