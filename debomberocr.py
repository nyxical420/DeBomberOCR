# DeBomber OCR made by Xavee#7951
import pyautogui
from PIL import Image
from pytesseract import *
import keyboard
import random

# DeBomber OCR Settings
triggerkey   = "delete"
stopkey      = "escape"
clearlistkey = "end"
sscoords     = 540, 390, 50, 30
textfile     = "jklm_allwords.txt"
typespeed    = 0.01
ocrpath      = "C:\\path\\Tesseract-OCR\\tesseract.exe"
ocrconfig    = "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8.5"
ocrlang      = "eng"

# Debomber OCR Settings Help
# triggerkey   - You can choose any trigger key to trigger DeBomberOCR and type words for you, key names is on this link https://github.com/xacvwe/DeBomberOCR/blob/main/triggerkeys.txt
# stopkey      - Stops DeBomberOCR. You can change this stop key if you want with the link above.
# clearlistkey - Clears the usedwords list.
# sscoords     - Screenshots the bomb's letter prompt and converts it into a word containing those letters. it should look something like this: https://github.com/xacvwe/DeBomberOCR/blob/main/letters.png
# textfile     - Where the OCR grabbs words containing the letters from sscoords.
# typespeed    - Changes the typespeed, for faster epic dejavu thing use 0.00000000001 if you want but you might get banned
# ocrpath      - Path for tesseract.exe, and also to make the OCR work.
# ocrconfig    - Keep this config put if you don't know what it does to the script.
# ocrlang      - Needs tesseract traineddata for france language.

pytesseract.tesseract_cmd = ocrpath
print("DeBomberOCR is now running.")
usedwords = []

while True:
    a = keyboard.read_key()
    
    if a == stopkey:
        exit()
    
    if a == clearlistkey:
        usedwords.clear()
        print("Cleared usedwords list.")

    if a == triggerkey:
        scltr = pyautogui.screenshot(region=(sscoords))
        scltr.save(r"./letters.png")
        ltrimg = Image.open("letters.png")
        ltrstr = pytesseract.image_to_string(ltrimg, config=ocrconfig, lang=ocrlang)
        n = ltrstr.split()
        pltrs = ''.join(str(x) for x in n)

        print('Letters: ' + pltrs)
        x = open(textfile, "r")
        words = [w for w in x.read().split() if pltrs in w]

        try:
            a = random.choice(words)
        except:
            print("Cannot choose from an empty sequence (IndexError)")
        
        used = [w for w in usedwords if a in w]

        if used:
            print("Word is already used!")
        
        if not used:
            print(f"Typing Word: {a}")
            pyautogui.write(a, typespeed)
            pyautogui.press('enter')
