import pyautogui

#Keep running this script until the image looks like this: https://github.com/xacvwe/DeBomberOCR/blob/main/letters.png

im1 = pyautogui.screenshot(region=(540,390,50,30))
im1.save(r"./savedimage.png")
