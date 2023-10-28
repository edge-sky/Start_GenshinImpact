## Start_Genshin_Impact/启动原神

**Use the PIL library to display screenshots and calculate the percentage of the most colors on the screen, and start a specific software when the specific color ratio reaches a certain value** 

Percent _ same represents the percentage of the same color at most, most _ common _ color represents the same color at most, in RGB values, where the range is ( 240, 240, 240 ) to ( 255, 255, 255 )
```python
def start_genshin_impact(percent_same, most_common_color):
    if percent_same > 80 and most_common_color >= (240, 240, 240):
        return 1
    return 0
```

After meeting the conditions, use the os library cmd to start the specified application. Note : when there is a space on the path, you need to add "" before the path

```python
if start_genshin_impact(*get_screen_color()):
    os.system('start "" "C:\PersonalApp\Genshin Impact\Genshin Impact Game\YuanShen.exe"')
    print("start genshin impact")
    flag = False
else:
    print("not start genshin impact")
```

**Known Issue**: Cannot seamlessly start applications that require administrator privileges, CPU usage is slightly higher, and can not be used normally after trying to package with PyInstaller



## Start_Genshin_Impact/启动原神

**使用PIL库进行显示画面截图并计算最多颜色所占屏幕的百分比，当特定颜色占比达到一定值时启动特定软件（这里白色启动原神/doge）**

percent_same表示最多相同颜色所占的百分比，most_common_color表示最多相同的颜色，以RGB数值表示，这里表示的范围为(240, 240, 240)到(255, 255, 255)
```python
def start_genshin_impact(percent_same, most_common_color):
    if percent_same > 80 and most_common_color >= (240, 240, 240):
        return 1
    return 0
```

满足条件后使用os库cmd启动指定应用，注意：路径上有空格时需要在路径前加上 ""

```python
if start_genshin_impact(*get_screen_color()):
    os.system('start "" "C:\PersonalApp\Genshin Impact\Genshin Impact Game\YuanShen.exe"')
    print("start genshin impact")
    flag = False
else:
    print("not start genshin impact")
```

**已知问题**：不能无缝启动需要管理员权限的应用，CPU占用略高，尝试使用PyInstaller打包后无法正常使用