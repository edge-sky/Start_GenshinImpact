import os

from PIL import ImageGrab
from collections import defaultdict


def get_screen_color():
    # 屏幕截图
    img = ImageGrab.grab()
    screen_width, screen_height = img.size

    # 初始化颜色计数器
    color_counter = defaultdict(int)

    # 遍历屏幕上的每个像素，计算颜色计数
    for x in range(screen_width):
        for y in range(screen_height):
            color = img.getpixel((x, y))
            color_counter[color] += 1

    # 获取颜色计数最多的颜色
    most_common_color, max_count = max(color_counter.items(), key=lambda x: x[1])

    # 计算百分比
    percent_same = max_count / (screen_width * screen_height) * 100

    return percent_same, most_common_color


def start_genshin_impact(percent_same, most_common_color):
    if percent_same > 60 and most_common_color >= (240, 240, 240):
        return 1
    return 0


if __name__ == "__main__":
    flag = True
    while flag:
        if start_genshin_impact(*get_screen_color()):
            os.system('start "" "C:\PersonalApp\Genshin Impact\Genshin Impact Game\YuanShen.exe"')
            print("start genshin impact")
            flag = False
        else:
            print("not start genshin impact")
