import re
from numpy import tri
import pyautogui
from PIL import Image
from pytesseract import *
import keyboard
import random
pyautogui.FAILSAFE = False

# DeBomber OCR Settings
triggerkey   = "delete"
stopkey      = "escape"
clearlistkey = "end"
sscoords     = 540, 395, 47, 22
textfile     = "jklm_allwords.txt"
typespeed    = 0.01
ocrpath      = "C:\\path\\to\\Tesseract-OCR\\tesseract.exe"
ocrconfig    = "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 8.6"
ocrlang      = "eng"

# Debomber OCR Settings Help
# triggerkey   - You can choose any trigger key to trigger DeBomberOCR and type words for you, key names is on this link https://github.com/xacvwe/DeBomberOCR/blob/main/triggerkeys.txt
# stopkey      - Stops DeBomberOCR. You can change this stop key if you want with the link above.
# clearlistkey - Clears the usedwords list.
# sscoords     - Screenshots the bomb's letter prompt and converts it into a word containing those letters. it should look something like this: https://github.com/xacvwe/DeBomberOCR/blob/main/letters.png
# textfile     - Where the OCR grabbs words containing the letters from sscoords.
# typespeed    - Changes the typespeed, for faster epic dejavu thing use 0.00000000001 if you want but you might get banned
# ocrpath      - Path for tesseract.exe, and also to make DeBomberOCR work.
# ocrconfig    - Keep this config put if you don't know what it does to the script.
# ocrlang      - Needs tesseract traineddata for france language.


pytesseract.tesseract_cmd = ocrpath
print("DeBomberOCR is now running.")
usedwords = []
bonus = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"]



while True:
    a = keyboard.read_key()
    
    if a == stopkey:
        exit()
    
    if a == clearlistkey:
        usedwords.clear()
        print("Cleared usedwords list.")

    if a == triggerkey:
        reqltr = random.choice(bonus)
        print(reqltr)
        scltr = pyautogui.screenshot(region=(sscoords))
        scltr.save(r"./letters.png")
        ltrimg = Image.open("letters.png")
        ltrstr = pytesseract.image_to_string(ltrimg, config=ocrconfig, lang=ocrlang)
        n = ltrstr.split()
        pltrs = ''.join(str(x) for x in n)

        print('Letters: ' + pltrs)
        x = open(textfile, "r")
        words = [w for w in x.read().split() if pltrs in w]
        while True:
            try:
                a = random.choice(words)
            except:
                print("Cannot choose from an empty sequence (IndexError)")

            if reqltr in a:
                print(f"Word Accepted: {a}")
                break
            
            if a == triggerkey:
                continue

            if reqltr not in a:
                print(f"Word Declined: {a}")
                continue

        used = [w for w in usedwords if a in w]

        if used:
            print("Word is already used!")

        if not used:
            print(f"Typing Word: {a}")
            pyautogui.write(a, typespeed)
            pyautogui.press('enter')
            result = "".join(dict.fromkeys(a))
            for letter in result:
                letters = [w for w in bonus if letter in w]
                if letters:
                    bonus.remove(letter)
                if not letters:
                    print(f"Letter '{letter}' not in list")
            
            if bonus == []:
                print("Gained +1 Life!")
                fillbonus = "ABCDEFGHIJKLMNOPQRSTUV"
                for bonusfill in fillbonus:
                    bonus.append(bonusfill)
            print("Bonus Letters Left" + ''.join(str(x) for x in bonus))
